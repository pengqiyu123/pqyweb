(function (global) {
  'use strict';

  var GHR = global.GHR;

  /* ── 状态 ── */
  var state = {
    activeTab:    'stars',
    activeLang:   '',
    items:        [],
    fromCache:    false,
    totalCount:   0,
    loading:      false,
    error:        null,
    lastUpdated:  null
  };

  /* ── DOM 引用 ── */
  var $tabs, $langPills, $content, $statusLeft, $statusRight;
  var $searchWrap, $searchInput, $searchBtn;
  var $refreshBtn, $rateBadge, $lastUpdate, $autoRefresh;

  /* ── 自动刷新定时器 ── */
  var autoRefreshTimer = null;
  var countdownTimer   = null;

  /* ══════════════════════════════════════════
     初始化
     ══════════════════════════════════════════ */
  document.addEventListener('DOMContentLoaded', function () {
    $tabs         = document.getElementById('ghr-tabs');
    $langPills    = document.getElementById('ghr-lang-pills');
    $content      = document.getElementById('ghr-content');
    $statusLeft   = document.getElementById('ghr-status-left');
    $statusRight  = document.getElementById('ghr-status-right');
    $searchWrap   = document.getElementById('ghr-search-wrap');
    $searchInput  = document.getElementById('ghr-search-input');
    $searchBtn    = document.getElementById('ghr-search-btn');
    $refreshBtn   = document.getElementById('ghr-refresh-btn');
    $rateBadge    = document.getElementById('ghr-rate-badge');
    $lastUpdate   = document.getElementById('ghr-last-update');
    $autoRefresh  = document.getElementById('ghr-auto-refresh');

    renderTabs();
    renderLangPills();
    bindEvents();
    updateRateBadge();
    loadData();
  });

  /* ══════════════════════════════════════════
     渲染 Tab
     ══════════════════════════════════════════ */
  function renderTabs() {
    var html = '';
    GHR.TABS.forEach(function (tab) {
      var cls = 'ghr-tab' + (tab.id === state.activeTab ? ' active' : '');
      html += '<button class="' + cls + '" data-tab="' + tab.id + '" role="tab">'
            + '<i class="fas ' + tab.icon + '"></i> '
            + tab.label
            + '</button>';
    });
    $tabs.innerHTML = html;
  }

  /* ══════════════════════════════════════════
     渲染语言筛选
     ══════════════════════════════════════════ */
  function renderLangPills() {
    var html = '';
    GHR.LANGUAGES.forEach(function (lang) {
      var active = lang.id === state.activeLang;
      var cls = 'ghr-lang-pill' + (active ? ' active' : '');
      var dot = '';
      if (lang.id && GHR.LANG_COLORS[lang.id]) {
        dot = '<span class="ghr-lang-dot" style="background:' + GHR.LANG_COLORS[lang.id] + '"></span>';
      }
      html += '<button class="' + cls + '" data-lang="' + lang.id + '">' + dot + lang.label + '</button>';
    });
    $langPills.innerHTML = html;
  }

  /* ══════════════════════════════════════════
     事件绑定
     ══════════════════════════════════════════ */
  function bindEvents() {
    // Tab 点击
    $tabs.addEventListener('click', function (e) {
      var btn = e.target.closest('.ghr-tab');
      if (!btn || state.loading) return;
      switchTab(btn.getAttribute('data-tab'));
    });

    // 语言筛选点击
    $langPills.addEventListener('click', function (e) {
      var btn = e.target.closest('.ghr-lang-pill');
      if (!btn || state.loading) return;
      switchLang(btn.getAttribute('data-lang'));
    });

    // 刷新按钮
    $refreshBtn.addEventListener('click', function () {
      if (state.loading) return;
      clearCacheForCurrent();
      loadData();
    });

    // 搜索按钮
    $searchBtn.addEventListener('click', function () {
      if (state.loading) return;
      doSearch();
    });

    // 搜索回车
    $searchInput.addEventListener('keydown', function (e) {
      if (e.key === 'Enter') {
        e.preventDefault();
        if (!state.loading) doSearch();
      }
    });
  }

  /* ══════════════════════════════════════════
     Tab 切换
     ══════════════════════════════════════════ */
  function switchTab(tabId) {
    if (tabId === state.activeTab && tabId !== 'search') return;
    state.activeTab = tabId;

    // 更新 Tab 激活状态
    var tabs = $tabs.querySelectorAll('.ghr-tab');
    tabs.forEach(function (t) {
      t.classList.toggle('active', t.getAttribute('data-tab') === tabId);
    });

    // 显示/隐藏搜索框
    $searchWrap.classList.toggle('visible', tabId === 'search');

    // 加载数据
    if (tabId === 'search') {
      // 如果搜索框有内容就自动搜索
      if ($searchInput.value.trim()) {
        doSearch();
      } else {
        renderEmpty('search');
      }
      // 聚焦搜索框
      setTimeout(function () { $searchInput.focus(); }, 100);
    } else {
      loadData();
    }
  }

  /* ══════════════════════════════════════════
     语言切换
     ══════════════════════════════════════════ */
  function switchLang(langId) {
    if (langId === state.activeLang) return;
    state.activeLang = langId;

    // 更新 pill 激活状态
    var pills = $langPills.querySelectorAll('.ghr-lang-pill');
    pills.forEach(function (p) {
      p.classList.toggle('active', p.getAttribute('data-lang') === langId);
    });

    // 重新加载
    if (state.activeTab === 'search' && $searchInput.value.trim()) {
      doSearch();
    } else if (state.activeTab !== 'search') {
      loadData();
    }
  }

  /* ══════════════════════════════════════════
     搜索
     ══════════════════════════════════════════ */
  function doSearch() {
    var keyword = $searchInput.value.trim();
    if (!keyword) {
      renderEmpty('search');
      return;
    }
    state.error = null;
    setLoading(true);
    var url = GHR.buildSearchQuery(keyword, state.activeLang);
    GHR.fetchRepos(url).then(function (result) {
      state.items = result.items;
      state.fromCache = result.fromCache;
      state.totalCount = result.totalCount || result.items.length;
      state.lastUpdated = new Date();
      setLoading(false);
      renderTable();
      startAutoRefresh(GHR.CACHE_TTL);
    }).catch(function (err) {
      setLoading(false);
      state.error = err;
      renderError(err);
    });
  }

  /* ══════════════════════════════════════════
     数据加载
     ══════════════════════════════════════════ */
  function loadData() {
    var url = GHR.buildQuery(state.activeTab, state.activeLang);
    if (!url) return; // 搜索 tab 且无 URL

    state.error = null;
    setLoading(true);

    GHR.fetchRepos(url).then(function (result) {
      state.items = result.items;
      state.fromCache = result.fromCache;
      state.totalCount = result.totalCount || result.items.length;
      state.lastUpdated = new Date();
      setLoading(false);
      renderTable();
      updateRateBadge();
      startAutoRefresh(GHR.CACHE_TTL);
    }).catch(function (err) {
      setLoading(false);
      state.error = err;
      renderError(err);
      updateRateBadge();
    });
  }

  /* ══════════════════════════════════════════
     清除当前查询的缓存
     ══════════════════════════════════════════ */
  function clearCacheForCurrent() {
    GHR.cacheCleanup();
  }

  /* ══════════════════════════════════════════
     设置加载状态
     ══════════════════════════════════════════ */
  function setLoading(loading) {
    state.loading = loading;
    $refreshBtn.classList.toggle('ghr-btn-loading', loading);
    if (loading) {
      $content.innerHTML =
        '<div class="ghr-loading">'
        + '<div class="ghr-loading-spinner"></div>'
        + '<div class="ghr-loading-text">正在加载 GitHub 数据...</div>'
        + '</div>';
      clearTimers();
    }
  }

  /* ══════════════════════════════════════════
     渲染表格
     ══════════════════════════════════════════ */
  function renderTable() {
    var items = state.items;
    if (!items || items.length === 0) {
      renderEmpty(state.activeTab);
      return;
    }

    var html = '<div class="ghr-table-wrap"><table class="ghr-table">';
    html += '<thead><tr>'
          + '<th class="ghr-col-rank">#</th>'
          + '<th>仓库</th>'
          + '<th>语言</th>'
          + '<th class="ghr-col-stars"><i class="fas fa-star ghr-stat-icon"></i>Stars</th>'
          + '<th class="ghr-col-forks"><i class="fas fa-code-branch ghr-stat-icon"></i>Forks</th>'
          + '</tr></thead>';
    html += '<tbody>';

    items.forEach(function (repo, i) {
      var rankCls = 'ghr-rank';
      if (i === 0) rankCls += ' gold';
      else if (i === 1) rankCls += ' silver';
      else if (i === 2) rankCls += ' bronze';

      var langHtml = '';
      if (repo.language) {
        var color = GHR.LANG_COLORS[repo.language.toLowerCase()] || '#888';
        langHtml = '<span class="ghr-lang-tag">'
                 + '<span class="ghr-lang-tag-dot" style="background:' + color + '"></span>'
                 + repo.language
                 + '</span>';
      }

      html += '<tr>'
            + '<td class="' + rankCls + '">' + (i + 1) + '</td>'
            + '<td>'
            +   '<div class="ghr-repo-cell">'
            +     '<img class="ghr-repo-avatar" src="' + escapeAttr(repo.avatar) + '" alt="" loading="lazy">'
            +     '<div class="ghr-repo-info">'
            +       '<a class="ghr-repo-name" href="' + escapeAttr(repo.url) + '" target="_blank" rel="noopener noreferrer">'
            +         escapeHtml(repo.name)
            +       '</a>'
            +       '<span class="ghr-repo-desc" title="' + escapeAttr(repo.description) + '">'
            +         escapeHtml(repo.description)
            +       '</span>'
            +     '</div>'
            +   '</div>'
            + '</td>'
            + '<td>' + langHtml + '</td>'
            + '<td class="ghr-stat ghr-stat-stars">'
            +   '<i class="fas fa-star ghr-stat-icon"></i>' + GHR.formatNumber(repo.stars)
            + '</td>'
            + '<td class="ghr-stat ghr-stat-forks">'
            +   '<i class="fas fa-code-branch ghr-stat-icon"></i>' + GHR.formatNumber(repo.forks)
            + '</td>'
            + '</tr>';
    });

    html += '</tbody></table></div>';
    $content.innerHTML = html;

    // 状态栏
    var cacheTag = state.fromCache ? '<span class="ghr-status-dot from-cache"></span> 来自缓存' : '<span class="ghr-status-dot"></span> 实时数据';
    $statusLeft.innerHTML = cacheTag;
    $statusRight.textContent = '共 ' + items.length + ' 条结果';
  }

  /* ══════════════════════════════════════════
     空状态
     ══════════════════════════════════════════ */
  function renderEmpty(tabId) {
    var icon = tabId === 'search' ? 'fa-search' : 'fa-inbox';
    var msg  = tabId === 'search' ? '输入关键词开始搜索 GitHub 仓库' : '暂无数据，请稍后再试';
    $content.innerHTML =
      '<div class="ghr-empty">'
      + '<div class="ghr-empty-icon"><i class="fas ' + icon + '"></i></div>'
      + '<div>' + msg + '</div>'
      + '</div>';
    $statusLeft.innerHTML = '';
    $statusRight.textContent = '';
  }

  /* ══════════════════════════════════════════
     错误状态
     ══════════════════════════════════════════ */
  function renderError(err) {
    var icon = 'fa-exclamation-triangle';
    var msg = err.message || '请求失败，请稍后重试';
    if (err.type === 'rate_limited') {
      icon = 'fa-clock';
    }
    $content.innerHTML =
      '<div class="ghr-error">'
      + '<div class="ghr-error-icon"><i class="fas ' + icon + '"></i></div>'
      + '<div>' + escapeHtml(msg) + '</div>'
      + '</div>';
    $statusLeft.innerHTML = '';
    $statusRight.textContent = '';
  }

  /* ══════════════════════════════════════════
     限流显示
     ══════════════════════════════════════════ */
  function updateRateBadge() {
    var rate = GHR.getRateLimit();
    var remaining = rate.remaining;
    $rateBadge.textContent = '剩余 ' + remaining + ' 次/小时';
    $rateBadge.classList.toggle('warning', remaining <= 10);
  }

  /* ══════════════════════════════════════════
     自动刷新 & 倒计时
     ══════════════════════════════════════════ */
  function startAutoRefresh(intervalMs) {
    clearTimers();

    // 更新上次刷新时间
    if (state.lastUpdated) {
      $lastUpdate.textContent = '上次更新: ' + formatTime(state.lastUpdated);
    }

    // 倒计时
    var target = Date.now() + intervalMs;
    countdownTimer = setInterval(function () {
      var left = Math.max(0, target - Date.now());
      var mins = Math.floor(left / 60000);
      var secs = Math.floor((left % 60000) / 1000);
      $autoRefresh.textContent = '缓存过期: ' + mins + '分' + secs + '秒后刷新';
    }, 1000);

    // 到期自动刷新
    autoRefreshTimer = setTimeout(function () {
      if (state.activeTab !== 'search') {
        loadData();
      }
    }, intervalMs);
  }

  function clearTimers() {
    if (autoRefreshTimer) { clearTimeout(autoRefreshTimer); autoRefreshTimer = null; }
    if (countdownTimer)   { clearInterval(countdownTimer);   countdownTimer = null; }
  }

  /* ══════════════════════════════════════════
     工具函数
     ══════════════════════════════════════════ */
  function escapeHtml(str) {
    if (!str) return '';
    return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  function escapeAttr(str) {
    if (!str) return '';
    return str.replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/'/g, '&#39;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }

  function formatTime(date) {
    var h = String(date.getHours()).padStart(2, '0');
    var m = String(date.getMinutes()).padStart(2, '0');
    var s = String(date.getSeconds()).padStart(2, '0');
    return h + ':' + m + ':' + s;
  }

})(window);
