(function (global) {
  'use strict';

  /* ── 语言列表 ── */
  var LANGUAGES = [
    { id: '',          label: 'All' },
    { id: 'python',    label: 'Python' },
    { id: 'javascript',label: 'JavaScript' },
    { id: 'typescript',label: 'TypeScript' },
    { id: 'go',        label: 'Go' },
    { id: 'rust',      label: 'Rust' },
    { id: 'java',      label: 'Java' },
    { id: 'cpp',       label: 'C++' }
  ];

  /* ── 语言 → 颜色映射 ── */
  var LANG_COLORS = {
    python:     '#3572A5',
    javascript: '#f1e05a',
    typescript: '#3178c6',
    go:         '#00ADD8',
    rust:       '#dea584',
    java:       '#b07219',
    cpp:        '#f34b7d',
    c:          '#555555',
    'c#':       '#178600',
    ruby:       '#701516',
    php:        '#4F5D95',
    swift:      '#F05138',
    kotlin:     '#A97BFF',
    dart:       '#00B4AB',
    shell:      '#89e051',
    html:       '#e34c26',
    css:        '#563d7c'
  };

  /* ── Tab 配置 ── */
  var TABS = [
    { id: 'stars',     label: '🔥 总星榜',     icon: 'fa-fire' },
    { id: 'trending',  label: '🚀 最近热门',   icon: 'fa-rocket' },
    { id: 'updated',   label: '📈 最近更新',   icon: 'fa-chart-line' },
    { id: 'search',     label: '🔍 搜索',       icon: 'fa-search' }
  ];

  /* ── 每页条数 ── */
  var PER_PAGE = 30;

  /* ── 缓存有效期（毫秒） ── */
  var CACHE_TTL = 30 * 60 * 1000; // 30 分钟

  /* ── 工具函数：获取 N 天前的 ISO 日期 ── */
  function daysAgo(n) {
    var d = new Date();
    d.setDate(d.getDate() - n);
    return d.toISOString().split('T')[0]; // "2026-06-11"
  }

  /* ── 工具函数：格式化数字 ── */
  function formatNumber(num) {
    if (num == null) return '0';
    if (num >= 1000000) return (num / 1000000).toFixed(1) + 'M';
    if (num >= 1000) return (num / 1000).toFixed(1) + 'K';
    return String(num);
  }

  /* ── 构建 GitHub Search API URL ── */
  function buildQuery(tabId, language) {
    var q = '';
    switch (tabId) {
      case 'stars':
        q = 'stars:>1000';
        break;
      case 'trending':
        q = 'stars:>100+created:>' + daysAgo(7);
        break;
      case 'updated':
        q = 'stars:>100+pushed:>' + daysAgo(7);
        break;
      case 'search':
        return null; // 搜索由用户输入决定
    }
    if (language) {
      q += '+language:' + language;
    }
    return 'https://api.github.com/search/repositories?q=' + encodeURIComponent(q)
      + '&sort=stars&order=desc&per_page=' + PER_PAGE;
  }

  function buildSearchQuery(keyword, language) {
    var q = keyword;
    if (language) {
      q += '+language:' + language;
    }
    return 'https://api.github.com/search/repositories?q=' + encodeURIComponent(q)
      + '&sort=stars&order=desc&per_page=' + PER_PAGE;
  }

  /* ── 导出 ── */
  global.GHR = global.GHR || {};
  global.GHR.LANGUAGES    = LANGUAGES;
  global.GHR.LANG_COLORS  = LANG_COLORS;
  global.GHR.TABS         = TABS;
  global.GHR.PER_PAGE     = PER_PAGE;
  global.GHR.CACHE_TTL    = CACHE_TTL;
  global.GHR.buildQuery   = buildQuery;
  global.GHR.buildSearchQuery = buildSearchQuery;
  global.GHR.formatNumber = formatNumber;
  global.GHR.daysAgo      = daysAgo;

})(window);
