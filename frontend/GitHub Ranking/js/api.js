(function (global) {
  'use strict';

  var GHR = global.GHR;
  var DATA_DIR = 'data/'; // 相对于 index.html 的路径

  /* ══════════════════════════════════════════
     加载本地 JSON（GitHub Actions 预生成的数据）
     ══════════════════════════════════════════ */
  function loadLocalJSON(filename) {
    return fetch(DATA_DIR + filename)
      .then(function (r) {
        if (!r.ok) throw { type: 'fetch_error', message: '无法加载 ' + filename };
        return r.json();
      });
  }

  /**
   * 加载指定 tab 的数据
   * stars / trending / updated → 读本地 JSON，客户端按语言筛选
   * search → 实时调 GitHub API（仅搜索用）
   */
  function loadTabData(tabId) {
    return loadLocalJSON(tabId + '.json').then(function (data) {
      return { items: data.items || [], totalCount: data.totalCount || 0 };
    });
  }

  /**
   * 加载语言分类数据
   */
  function loadLanguageData() {
    return loadLocalJSON('languages.json').then(function (data) {
      return data; // { python: {items, totalCount}, javascript: {...}, ... }
    });
  }

  /**
   * 加载元信息（上次更新时间等）
   */
  function loadMeta() {
    return loadLocalJSON('meta.json').then(function (data) {
      return data;
    });
  }

  /* ══════════════════════════════════════════
     搜索：仅此功能实时调 GitHub API（有缓存保护）
     ══════════════════════════════════════════ */
  var SEARCH_CACHE_PREFIX = 'ghr_search_';
  var SEARCH_CACHE_TTL   = 30 * 60 * 1000; // 30 分钟
  var RATE_KEY            = 'ghr_search_rate';
  var RATE_RESET_KEY      = 'ghr_search_reset';

  function searchCacheGet(url) {
    try {
      var raw = localStorage.getItem(SEARCH_CACHE_PREFIX + url);
      if (!raw) return null;
      var entry = JSON.parse(raw);
      if (Date.now() - entry.ts > SEARCH_CACHE_TTL) {
        localStorage.removeItem(SEARCH_CACHE_PREFIX + url);
        return null;
      }
      return entry.data;
    } catch (e) { return null; }
  }

  function searchCacheSet(url, data) {
    try {
      localStorage.setItem(SEARCH_CACHE_PREFIX + url,
        JSON.stringify({ data: data, ts: Date.now() }));
    } catch (e) { /* ignore */ }
  }

  function updateSearchRateLimit(response) {
    var remaining = response.headers.get('X-RateLimit-Remaining');
    var reset     = response.headers.get('X-RateLimit-Reset');
    if (remaining != null) localStorage.setItem(RATE_KEY, remaining);
    if (reset != null)     localStorage.setItem(RATE_RESET_KEY, reset);
  }

  function getSearchRateLimit() {
    var remaining = parseInt(localStorage.getItem(RATE_KEY), 10);
    var reset     = parseInt(localStorage.getItem(RATE_RESET_KEY), 10);
    if (isNaN(remaining)) remaining = 60;
    if (isNaN(reset)) return { remaining: remaining, resetAt: null };
    return { remaining: remaining, resetAt: new Date(reset * 1000) };
  }

  function searchRepos(keyword, language) {
    var q = keyword;
    if (language) q += '+language:' + language;
    var url = 'https://api.github.com/search/repositories?q=' + encodeURIComponent(q)
      + '&sort=stars&order=desc&per_page=' + GHR.PER_PAGE;

    // 检查缓存
    var cached = searchCacheGet(url);
    if (cached) {
      return Promise.resolve({ items: cached, fromCache: true });
    }

    // 检查限流
    var rate = getSearchRateLimit();
    if (rate.remaining <= 0 && rate.resetAt && rate.resetAt > new Date()) {
      var mins = Math.ceil((rate.resetAt - Date.now()) / 60000);
      return Promise.reject({
        type: 'rate_limited',
        message: 'GitHub API 搜索限流，请 ' + mins + ' 分钟后再试（每日数据榜不受影响）'
      });
    }

    return fetch(url)
      .then(function (response) {
        updateSearchRateLimit(response);
        if (!response.ok) {
          if (response.status === 403) {
            throw { type: 'rate_limited', message: 'GitHub API 搜索限流，请稍后再试' };
          }
          throw { type: 'http_error', message: 'HTTP ' + response.status };
        }
        return response.json();
      })
      .then(function (data) {
        var items = (data.items || []).map(function (repo) {
          return {
            id: repo.id, name: repo.full_name, url: repo.html_url,
            description: repo.description || '',
            stars: repo.stargazers_count || 0, forks: repo.forks_count || 0,
            language: repo.language || null,
            avatar: repo.owner ? repo.owner.avatar_url : '',
            owner: repo.owner ? repo.owner.login : '',
            created: repo.created_at, updated: repo.updated_at, pushed: repo.pushed_at
          };
        });
        searchCacheSet(url, items);
        return { items: items, fromCache: false, totalCount: data.total_count };
      });
  }

  /* ── 导出 ── */
  global.GHR = global.GHR || {};
  global.GHR.loadTabData     = loadTabData;
  global.GHR.loadLanguageData = loadLanguageData;
  global.GHR.loadMeta        = loadMeta;
  global.GHR.searchRepos     = searchRepos;
  global.GHR.getSearchRateLimit = getSearchRateLimit;

})(window);
