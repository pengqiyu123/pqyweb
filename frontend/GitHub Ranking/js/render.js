(function (global) {
  'use strict';

  var GHR = global.GHR;

  /* ── 应用状态 ── */
  var state = {
    activeTab:    'stars',
    activeLang:   '',
    allItems:     {},          // { stars: [...], trending: [...], updated: [...] }
    langItems:    null,        // { python: {items:[...], totalCount:N}, ... }  从 languages.json 加载
    meta:         null,        // { updatedAt, tabs, languages, perTabCount }
    filteredItems: [],         // 当前展示的条目（可能经过语言筛选）
    loading:      false,
    error:        null
  };

  /* ── DOM 引用 ── */
  var $tabs, $langPills, $content, $statusLeft, $statusRight;
  var $searchWrap, $searchInput, $searchBtn;
  var $refreshBtn, $rateBadge, $lastUpdate, $autoRefresh;

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
    loadAllData();
  });

  /* ══════════════════════════════════════════
     渲染 Tab
     ══════════════════════════════════════════ */
  function renderTabs() {
    var html = '';
    GHR.TABS.forEach(function (tab) {
      var cls = 'ghr-tab' + (tab.id === state.activeTab ? ' active' : '');
      html += '<button class="' + cls + '" data-tab="' + tab.id + '" role="tab">'
            + tab.label + '</button>';
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
    $tabs.addEventListener('click', function (e) {
      var btn = e.target.closest('.ghr-tab');
      if (!btn || state.loading) return;
      switchTab(btn.getAttribute('data-tab'));
    });

    $langPills.addEventListener('click', function (e) {
      var btn = e.target.closest('.ghr-lang-pill');
      if (!btn || state.loading) return;
      switchLang(btn.getAttribute('data-lang'));
    });

    // 刷新 = 重新加载本地数据（清除浏览器缓存）
    $refreshBtn.addEventListener('click', function () {
      if (state.loading) return;
      loadAllData(true);
    });

    $searchBtn.addEventListener('click', function () {
      if (state.loading) return;
      doSearch();
    });

    $searchInput.addEventListener('keydown', function (e) {
      if (e.key === 'Enter') {
        e.preventDefault();
        if (!state.loading) doSearch();
      }
    });
  }

  /* ══════════════════════════════════════════
     加载所有本地数据
     ══════════════════════════════════════════ */
  function loadAllData(bustCache) {
    state.loading = true;
    state.error = null;
    $content.innerHTML =
      '<div class="ghr-loading">'
      + '<div class="ghr-loading-spinner"></div>'
      + '<div class="ghr-loading-text">正在加载榜单数据...</div>'
      + '</div>';
    $refreshBtn.classList.add('ghr-btn-loading');

    var cacheBuster = bustCache ? '?t=' + Date.now() : '';

    Promise.all([
      GHR.loadTabData('stars').then(function (d) { state.allItems.stars = d.items; }),
      GHR.loadTabData('trending').then(function (d) { state.allItems.trending = d.items; }),
      GHR.loadTabData('updated').then(function (d) { state.allItems.updated = d.items; }),
      GHR.loadMeta().then(function (m) { state.meta = m; }).catch(function () { /* meta 可选 */ }),
      GHR.loadLanguageData().then(function (d) { state.langItems = d; }).catch(function () { /* 语言榜可选 */ })
    ]).then(function () {
      state.loading = false;
      $refreshBtn.classList.remove('ghr-btn-loading');
      renderCurrentView();
      updateFooter();
    }).catch(function (err) {
      state.loading = false;
      $refreshBtn.classList.remove('ghr-btn-loading');
      state.error = err;
      renderError(err);
    });
  }

  /* ══════════════════════════════════════════
     Tab 切换
     ══════════════════════════════════════════ */
  function switchTab(tabId) {
    if (tabId === state.activeTab && tabId !== 'search') return;
    state.activeTab = tabId;

    var tabs = $tabs.querySelectorAll('.ghr-tab');
    tabs.forEach(function (t) {
      t.classList.toggle('active', t.getAttribute('data-tab') === tabId);
    });

    $searchWrap.classList.toggle('visible', tabId === 'search');

    if (tabId === 'search') {
      if ($searchInput.value.trim()) {
        doSearch();
      } else {
        renderEmpty('search');
      }
      setTimeout(function () { $searchInput.focus(); }, 100);
    } else {
      renderCurrentView();
    }
  }

  /* ══════════════════════════════════════════
     语言切换
     ══════════════════════════════════════════ */
  function switchLang(langId) {
    if (langId === state.activeLang) return;
    state.activeLang = langId;

    var pills = $langPills.querySelectorAll('.ghr-lang-pill');
    pills.forEach(function (p) {
      p.classList.toggle('active', p.getAttribute('data-lang') === langId);
    });

    // 如果在搜索 tab，重新搜索
    if (state.activeTab === 'search' && $searchInput.value.trim()) {
      doSearch();
    } else {
      renderCurrentView();
    }
  }

  /* ══════════════════════════════════════════
     获取当前 Tab + 语言对应的条目
     ══════════════════════════════════════════ */
  function getFilteredItems() {
    var tabId = state.activeTab;
    var lang  = state.activeLang;

    // 如果选了特定语言，优先从语言分类数据取
    if (lang && state.langItems && state.langItems[lang]) {
      return state.langItems[lang].items || [];
    }

    // 否则取全语言 tab 数据
    return state.allItems[tabId] || [];
  }

  /* ══════════════════════════════════════════
     渲染当前视图
     ══════════════════════════════════════════ */
  function renderCurrentView() {
    if (state.activeTab === 'search') return;
    var items = getFilteredItems();
    state.filteredItems = items;
    renderTable(items, false);
  }

  /* ══════════════════════════════════════════
     搜索（唯一需要调 API 的功能）
     ══════════════════════════════════════════ */
  function doSearch() {
    var keyword = $searchInput.value.trim();
    if (!keyword) {
      renderEmpty('search');
      return;
    }
    state.loading = true;
    state.error = null;
    $content.innerHTML =
      '<div class="ghr-loading">'
      + '<div class="ghr-loading-spinner"></div>'
      + '<div class="ghr-loading-text">正在搜索...</div>'
      + '</div>';

    GHR.searchRepos(keyword, state.activeLang).then(function (result) {
      state.loading = false;
      state.filteredItems = result.items;
      renderTable(result.items, result.fromCache);
      updateSearchRateBadge();
    }).catch(function (err) {
      state.loading = false;
      state.error = err;
      renderError(err);
      updateSearchRateBadge();
    });
  }

  /* ══════════════════════════════════════════
     渲染表格
     ══════════════════════════════════════════ */
  function renderTable(items, fromCache) {
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
                 + escapeHtml(repo.language)
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
    if (state.activeTab === 'search') {
      var tag = fromCache
        ? '<span class="ghr-status-dot from-cache"></span> 来自搜索缓存'
        : '<span class="ghr-status-dot"></span> 实时搜索';
      $statusLeft.innerHTML = tag;
    } else {
      $statusLeft.innerHTML = '<span class="ghr-status-dot"></span> 本地数据（每日自动更新）';
    }
    $statusRight.textContent = '共 ' + items.length + ' 条结果';
  }

  /* ══════════════════════════════════════════
     空状态
     ══════════════════════════════════════════ */
  function renderEmpty(tabId) {
    var icon = tabId === 'search' ? 'fa-search' : 'fa-inbox';
    var msg  = tabId === 'search' ? '输入关键词开始搜索 GitHub 仓库' : '暂无数据，等待下次自动更新';
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
    var msg = err.message || '加载失败，请稍后重试';
    if (err.type === 'rate_limited') icon = 'fa-clock';
    $content.innerHTML =
      '<div class="ghr-error">'
      + '<div class="ghr-error-icon"><i class="fas ' + icon + '"></i></div>'
      + '<div>' + escapeHtml(msg) + '</div>'
      + '</div>';
    $statusLeft.innerHTML = '';
    $statusRight.textContent = '';
  }

  /* ══════════════════════════════════════════
     底部信息
     ══════════════════════════════════════════ */
  function updateFooter() {
    if (state.meta && state.meta.updatedAt) {
      var d = new Date(state.meta.updatedAt);
      $lastUpdate.textContent = '数据更新: ' + formatDate(d);
    } else {
      $lastUpdate.textContent = '数据更新: --';
    }
    $autoRefresh.textContent = '由 GitHub Actions 每日自动刷新';
    $rateBadge.textContent = '每日数据';
    $rateBadge.classList.remove('warning');
  }

  function updateSearchRateBadge() {
    var rate = GHR.getSearchRateLimit();
    $rateBadge.textContent = '搜索剩余 ' + rate.remaining + ' 次';
    $rateBadge.classList.toggle('warning', rate.remaining <= 10);
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

  function formatDate(d) {
    var y = d.getFullYear();
    var m = String(d.getMonth() + 1).padStart(2, '0');
    var day = String(d.getDate()).padStart(2, '0');
    var h = String(d.getHours()).padStart(2, '0');
    var min = String(d.getMinutes()).padStart(2, '0');
    return y + '-' + m + '-' + day + ' ' + h + ':' + min;
  }

})(window);
