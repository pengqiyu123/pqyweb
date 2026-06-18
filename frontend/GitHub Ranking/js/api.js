(function (global) {
  'use strict';

  var CACHE_PREFIX = 'ghr_cache_';
  var RATE_KEY     = 'ghr_rate_limit';
  var RATE_RESET_KEY = 'ghr_rate_reset';

  /* ── 缓存：读 ── */
  function cacheGet(url) {
    var key = CACHE_PREFIX + url;
    try {
      var raw = localStorage.getItem(key);
      if (!raw) return null;
      var entry = JSON.parse(raw);
      if (Date.now() - entry.ts > global.GHR.CACHE_TTL) {
        localStorage.removeItem(key);
        return null;
      }
      return entry.data;
    } catch (e) {
      return null;
    }
  }

  /* ── 缓存：写 ── */
  function cacheSet(url, data) {
    var key = CACHE_PREFIX + url;
    try {
      localStorage.setItem(key, JSON.stringify({ data: data, ts: Date.now() }));
    } catch (e) {
      // localStorage 满，清理旧条目
      cacheCleanup();
      try { localStorage.setItem(key, JSON.stringify({ data: data, ts: Date.now() })); } catch (e2) { /* ignore */ }
    }
  }

  /* ── 缓存：清理过期条目 ── */
  function cacheCleanup() {
    var now = Date.now();
    var keys = [];
    for (var i = 0; i < localStorage.length; i++) {
      var k = localStorage.key(i);
      if (k && k.indexOf(CACHE_PREFIX) === 0) keys.push(k);
    }
    keys.forEach(function (k) {
      try {
        var entry = JSON.parse(localStorage.getItem(k));
        if (now - entry.ts > global.GHR.CACHE_TTL) localStorage.removeItem(k);
      } catch (e) { /* ignore */ }
    });
  }

  /* ── 限流：从响应头获取剩余次数 ── */
  function updateRateLimit(response) {
    var remaining = response.headers.get('X-RateLimit-Remaining');
    var reset     = response.headers.get('X-RateLimit-Reset');
    if (remaining != null) {
      localStorage.setItem(RATE_KEY, remaining);
    }
    if (reset != null) {
      localStorage.setItem(RATE_RESET_KEY, reset);
    }
  }

  /* ── 限流：获取本地记录的剩余次数 ── */
  function getRateLimit() {
    var remaining = parseInt(localStorage.getItem(RATE_KEY), 10);
    var reset     = parseInt(localStorage.getItem(RATE_RESET_KEY), 10);
    if (isNaN(remaining)) remaining = 60;
    if (isNaN(reset)) return { remaining: remaining, resetAt: null };
    return { remaining: remaining, resetAt: new Date(reset * 1000) };
  }

  /* ── 核心请求：先缓存再 API ── */
  function fetchRepos(url) {
    // 1. 检查缓存
    var cached = cacheGet(url);
    if (cached) {
      return Promise.resolve({ items: cached, fromCache: true });
    }

    // 2. 检查限流
    var rate = getRateLimit();
    if (rate.remaining <= 0 && rate.resetAt && rate.resetAt > new Date()) {
      var mins = Math.ceil((rate.resetAt - Date.now()) / 60000);
      return Promise.reject({
        type: 'rate_limited',
        message: 'GitHub API 限流，请 ' + mins + ' 分钟后再试',
        resetAt: rate.resetAt
      });
    }

    // 3. 发起请求
    return fetch(url)
      .then(function (response) {
        updateRateLimit(response);
        if (!response.ok) {
          if (response.status === 403) {
            throw { type: 'rate_limited', message: 'GitHub API 限流，请稍后再试' };
          }
          throw { type: 'http_error', message: 'HTTP ' + response.status };
        }
        return response.json();
      })
      .then(function (data) {
        var items = (data.items || []).map(function (repo) {
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
        });
        // 写入缓存
        cacheSet(url, items);
        return { items: items, fromCache: false, totalCount: data.total_count };
      });
  }

  /* ── 导出 ── */
  global.GHR = global.GHR || {};
  global.GHR.fetchRepos  = fetchRepos;
  global.GHR.getRateLimit = getRateLimit;
  global.GHR.cacheGet     = cacheGet;
  global.GHR.cacheCleanup = cacheCleanup;

})(window);
