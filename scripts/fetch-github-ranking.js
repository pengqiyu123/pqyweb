#!/usr/bin/env node
/**
 * GitHub 排行榜数据抓取脚本
 * 由 GitHub Actions 每日定时调用，抓取数据写入 JSON 文件
 *
 * 用法: node scripts/fetch-github-ranking.js
 * 环境变量:
 *   GITHUB_TOKEN  — GitHub Personal Token (Actions 自动提供 GITHUB_TOKEN)
 *   OUTPUT_DIR    — 输出目录 (默认: frontend/GitHub Ranking/data)
 */

const fs = require('fs');
const path = require('path');

const OUTPUT_DIR = process.env.OUTPUT_DIR || path.join(__dirname, '..', 'frontend', 'GitHub Ranking', 'data');
const PER_PAGE = 30;
const LANGUAGES = ['python', 'javascript', 'typescript', 'go', 'rust', 'java', 'cpp'];

// 确保输出目录存在
if (!fs.existsSync(OUTPUT_DIR)) {
  fs.mkdirSync(OUTPUT_DIR, { recursive: true });
}

// 获取 Token（优先环境变量，用于 Actions）
const TOKEN = process.env.GITHUB_TOKEN || '';

function headers() {
  var h = {
    'Accept': 'application/vnd.github.v3+json',
    'User-Agent': 'pqyweb-ranking-bot'
  };
  if (TOKEN) h['Authorization'] = 'Bearer ' + TOKEN;
  return h;
}

/**
 * 分页抓取，合并所有页
 */
async function fetchAll(url) {
  var allItems = [];
  var page = 1;
  var totalCount = 0;

  while (true) {
    var fullUrl = url + '&per_page=' + PER_PAGE + '&page=' + page;
    console.log('  GET ' + fullUrl);

    var resp = await fetch(fullUrl, { headers: headers() });
    if (!resp.ok) {
      var text = await resp.text();
      throw new Error('HTTP ' + resp.status + ': ' + text.slice(0, 200));
    }

    var data = await resp.json();
    totalCount = data.total_count || 0;

    if (data.items && data.items.length > 0) {
      allItems = allItems.concat(data.items.map(normalizeRepo));
    }

    // 最多抓 3 页 (90 条)，避免消耗过多请求
    if (allItems.length >= 90 || !data.items || data.items.length < PER_PAGE) {
      break;
    }
    page++;

    // 等一秒避免触发二次限流
    await sleep(1000);
  }

  return { items: allItems, totalCount: totalCount };
}

function normalizeRepo(repo) {
  return {
    id:          repo.id,
    name:        repo.full_name,
    url:         repo.html_url,
    description: repo.description || '',
    stars:       repo.stargazers_count || 0,
    forks:       repo.forks_count || 0,
    language:    repo.language || null,
    avatar:      repo.owner ? repo.owner.avatar_url : '',
    owner:       repo.owner ? repo.owner.login : '',
    created:     repo.created_at,
    updated:     repo.updated_at,
    pushed:      repo.pushed_at
  };
}

function sleep(ms) {
  return new Promise(function (resolve) { setTimeout(resolve, ms); });
}

function daysAgo(n) {
  var d = new Date();
  d.setDate(d.getDate() - n);
  return d.toISOString().split('T')[0];
}

/**
 * 写入 JSON 文件
 */
function writeJSON(filename, data) {
  var filepath = path.join(OUTPUT_DIR, filename);
  fs.writeFileSync(filepath, JSON.stringify(data, null, 2), 'utf8');
  console.log('  ✓ ' + filename + ' (' + data.items.length + ' repos)');
}

/**
 * 主流程
 */
async function main() {
  console.log('=== GitHub Ranking Data Fetch ===');
  console.log('Time: ' + new Date().toISOString());
  console.log('Output: ' + OUTPUT_DIR);
  console.log('Token: ' + (TOKEN ? 'YES' : 'NO'));
  console.log('');

  var sevenDaysAgo = daysAgo(7);

  // ── 1. 总星榜（全语言，不分页，直接取前 100） ──
  console.log('[1/3] 总星榜 ...');
  var starsData = await fetchAll(
    'https://api.github.com/search/repositories?q=stars:>1000&sort=stars&order=desc'
  );
  writeJSON('stars.json', starsData);

  // ── 2. 最近热门（7天内创建的高星项目） ──
  console.log('[2/3] 最近热门 (created > ' + sevenDaysAgo + ') ...');
  var trendingData = await fetchAll(
    'https://api.github.com/search/repositories?q=stars:>50+created:>' + sevenDaysAgo + '&sort=stars&order=desc'
  );
  writeJSON('trending.json', trendingData);

  // ── 3. 最近更新（7天内推送的高星项目） ──
  console.log('[3/3] 最近更新 (pushed > ' + sevenDaysAgo + ') ...');
  var updatedData = await fetchAll(
    'https://api.github.com/search/repositories?q=stars:>100+pushed:>' + sevenDaysAgo + '&sort=stars&order=desc'
  );
  writeJSON('updated.json', updatedData);

  // ── 4. 每种语言的总星榜 ──
  console.log('[4/4] 语言分类榜 ...');
  var langAll = {};
  for (var i = 0; i < LANGUAGES.length; i++) {
    var lang = LANGUAGES[i];
    console.log('  ' + lang + ' ...');
    var langData = await fetchAll(
      'https://api.github.com/search/repositories?q=stars:>500+language:' + lang + '&sort=stars&order=desc'
    );
    langAll[lang] = langData;
    await sleep(500); // 语言间也等一下
  }
  writeJSON('languages.json', langAll);

  // ── 5. 写入元信息 ──
  var meta = {
    updatedAt: new Date().toISOString(),
    tabs: ['stars', 'trending', 'updated'],
    languages: LANGUAGES,
    perTabCount: {
      stars: starsData.items.length,
      trending: trendingData.items.length,
      updated: updatedData.items.length
    }
  };
  writeJSON('meta.json', meta);

  console.log('');
  console.log('=== Done! ' + new Date().toISOString() + ' ===');
}

main().catch(function (err) {
  console.error('ERROR: ' + err.message);
  process.exit(1);
});
