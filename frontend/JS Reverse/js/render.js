(function (global) {
  var state = global.JSReverseProgress.load();
  var currentLevel = null;
  var revealedHints = 0;
  var currentToolFilter = 'all';

  document.addEventListener('DOMContentLoaded', init);

  function init() {
    bindGlobalEvents();
    global.JSReverseTools.wire();
    restoreSession();
  }

  function bindGlobalEvents() {
    byId('jsr-reset-progress').addEventListener('click', onReset);
    byId('jsr-report-reset').addEventListener('click', onReset);
    byId('jsr-report-back').addEventListener('click', function () { renderHub(); focusTop(false); });
    byId('jsr-back-button').addEventListener('click', function () { renderHub(); focusTop(false); });
    byId('jsr-hint-button').addEventListener('click', revealHint);
    byId('jsr-validate-button').addEventListener('click', submitLevel);
    byId('jsr-open-tools').addEventListener('click', openTools);
    byId('jsr-close-tools').addEventListener('click', closeTools);
    document.querySelector('[data-close-tools="true"]').addEventListener('click', closeTools);
    Array.prototype.forEach.call(document.querySelectorAll('.jsr-tool-tab'), function (button) {
      button.addEventListener('click', function () {
        setToolFilter(button.getAttribute('data-tool-filter') || 'all');
      });
    });
  }

  function renderHub() {
    switchView('hub');
    renderSummary();
    renderCurrentMission();
    renderStageBoard();
    renderBadges();
    renderAchievements();
    renderTimeline();
    renderInvestigationBrief();
    byId('jsr-stage-note').textContent = getStageNote();
    if (Object.keys(state.completedLevels).length === global.JS_REVERSE_LEVELS.length) {
      renderReport();
    }
  }

  function renderSummary() {
    byId('jsr-total-stars').textContent = global.JSReverseProgress.getStars(state);
    byId('jsr-total-score').textContent = state.score;
    byId('jsr-clue-count').textContent = state.unlockedClues.length + ' / ' + global.JS_REVERSE_LEVELS.length;
    byId('jsr-story-progress').textContent = state.storyProgress + '%';
    byId('jsr-story-chip').textContent = state.storyProgress + '% 已归档';
    byId('jsr-case-summary').textContent = getCaseSummary();
    byId('jsr-current-objective').textContent = getGlobalObjective();
  }

  function renderCurrentMission() {
    var container = byId('jsr-current-mission');
    var nextLevel = getNextAvailableLevel();
    var completedCount = Object.keys(state.completedLevels).length;
    var currentArc = getStageArc(nextLevel ? nextLevel.group : '终极揭秘') || global.JS_REVERSE_STAGE_ARCS[0];
    container.innerHTML =
      '<div class="jsr-mission-card">' +
      '<span>当前分幕</span>' +
      '<strong>' + currentArc.title + '</strong>' +
      '<p>' + escapeHtml(currentArc.summary) + '</p>' +
      '</div>' +
      '<div class="jsr-mission-card">' +
      '<span>当前主线目标</span>' +
      '<strong>' + escapeHtml(nextLevel ? getPresentation(nextLevel.id).objective : '所有证据已归档，进入结案复盘。') + '</strong>' +
      '<p>已完成 ' + completedCount + ' / ' + global.JS_REVERSE_LEVELS.length + ' 份证据，下一步继续推进主控链路。</p>' +
      '</div>';
  }

  function renderStageBoard() {
    var board = byId('jsr-stage-board');
    board.innerHTML = '';

    global.JS_REVERSE_STAGE_ARCS.forEach(function (arc) {
      var levels = getLevelsByGroup(arc.group);
      var solved = levels.filter(function (level) {
        return global.JSReverseProgress.isCompleted(state, level.id);
      }).length;
      var section = document.createElement('section');
      section.className = 'jsr-stage-section';
      section.setAttribute('data-stage-id', arc.id);
      section.innerHTML =
        '<div class="jsr-stage-head">' +
        '<div>' +
        '<p class="jsr-section-tag">' + escapeHtml(arc.group) + '</p>' +
        '<h3>' + escapeHtml(arc.title) + '</h3>' +
        '</div>' +
        '<div class="jsr-stage-progress">' + solved + ' / ' + levels.length + '</div>' +
        '</div>' +
        '<p class="jsr-stage-summary">' + escapeHtml(arc.atmosphere) + '</p>' +
        '<div class="jsr-stage-grid"></div>';

      var grid = section.querySelector('.jsr-stage-grid');
      levels.forEach(function (level, index) {
        var absoluteIndex = global.JS_REVERSE_LEVELS.indexOf(level);
        var unlocked = absoluteIndex === 0 || global.JSReverseProgress.isCompleted(state, global.JS_REVERSE_LEVELS[absoluteIndex - 1].id);
        var card = document.createElement('article');
        var presentation = getPresentation(level.id);
        var cardState = getLevelState(level, unlocked);
        card.className = 'jsr-level-card ' + cardState;
        card.setAttribute('data-level-id', level.id);
        card.setAttribute('data-level-state', cardState);
        card.setAttribute('data-testid', 'level-card');
        card.innerHTML =
          '<div class="jsr-level-card-top">' +
          '<div class="jsr-card-id">证据#' + String(absoluteIndex + 1).padStart(2, '0') + '</div>' +
          '<span class="jsr-state-pill">' + getLevelStatusLabel(cardState) + '</span>' +
          '</div>' +
          '<h4>' + escapeHtml(level.title) + '</h4>' +
          '<p>' + escapeHtml(presentation.objective) + '</p>' +
          '<div class="jsr-card-meta"><span>' + escapeHtml(level.group) + '</span><span>' + getLevelStars(level.id) + '</span></div>' +
          (global.JSReverseProgress.isCompleted(state, level.id)
            ? '<div class="jsr-card-clue">' + escapeHtml(level.clueFragment) + '</div>'
            : '<div class="jsr-card-note">' + escapeHtml(presentation.action) + '</div>');

        if (unlocked) {
          card.addEventListener('click', function () {
            openLevel(level);
          });
        }
        grid.appendChild(card);
      });

      board.appendChild(section);
    });
  }

  function renderBadges() {
    var box = byId('jsr-badges');
    box.innerHTML = '';
    global.JS_REVERSE_BADGES.forEach(function (badge) {
      var unlocked = !!state.badges[badge.id];
      var node = document.createElement('div');
      node.className = 'jsr-badge' + (unlocked ? '' : ' locked');
      node.innerHTML = '<strong>' + badge.title + '</strong><p>' + badge.group + '</p>';
      box.appendChild(node);
    });
  }

  function renderAchievements() {
    var box = byId('jsr-achievements');
    box.innerHTML = '';
    global.JS_REVERSE_ACHIEVEMENTS.forEach(function (item) {
      var unlocked = !!state.achievements[item.id];
      var node = document.createElement('div');
      node.className = 'jsr-achievement' + (unlocked ? '' : ' locked');
      node.innerHTML = '<strong>' + item.title + '</strong><p>' + item.description + '</p>';
      box.appendChild(node);
    });
  }

  function renderTimeline() {
    var box = byId('jsr-timeline');
    box.innerHTML = '';
    renderTimelineInto(box);
  }

  function renderTimelineInto(box) {
    var unlockedCount = state.unlockedClues.length;
    global.JS_REVERSE_TIMELINE.forEach(function (text, index) {
      var item = document.createElement('div');
      item.className = 'jsr-timeline-item' + (unlockedCount >= (index + 1) * 4 || (index === 4 && unlockedCount === 18) ? ' active' : '');
      item.textContent = text;
      box.appendChild(item);
    });
  }

  function renderInvestigationBrief() {
    var box = byId('jsr-investigation-brief');
    var nextLevel = getNextAvailableLevel();
    var activePresentation = nextLevel ? getPresentation(nextLevel.id) : null;
    box.innerHTML =
      briefCard('下一目标', activePresentation ? activePresentation.objective : '全部证据已完成，可以进入结案复盘。') +
      briefCard('建议动作', activePresentation ? activePresentation.action : '查看结案报告、复盘所有线索与成就。') +
      briefCard('线索用途', activePresentation ? activePresentation.clueUse : '所有线索已经进入最终报告与时间线。');
  }

  function openLevel(level) {
    currentLevel = level;
    revealedHints = Math.min(state.usedHintsByLevel[level.id] || 0, level.hints.length);
    state.currentLevelId = level.id;
    global.JSReverseProgress.save(state);
    switchView('level');
    renderSummary();
    renderLevelPresentation(level);
    byId('jsr-level-title').textContent = level.title;
    byId('jsr-level-brief').textContent = level.caseBrief;
    byId('jsr-evidence-file').textContent = level.evidenceFile;
    byId('jsr-level-group').textContent = level.group;
    byId('jsr-acceptance').textContent = level.acceptance;
    byId('jsr-current-stars').textContent = global.JSReverseProgress.computeStars(state, level.id) + ' 星';
    byId('jsr-attempts').textContent = '尝试次数：' + (state.attemptsByLevel[level.id] || 0);
    byId('jsr-stage-badge').textContent = getStageArc(level.group).title;
    setFeedback(global.JSReverseProgress.isCompleted(state, level.id)
      ? '当前证据已破解，你可以复盘思路或继续查看线索。'
      : '准备分析当前证据。', '');
    byId('jsr-code-preview').textContent = '正在加载证据片段...';
    byId('jsr-tutorial').innerHTML = level.tutorial;
    renderHints(level);
    renderTask(level);
    loadCodePreview(level);
    triggerStageReveal();
    focusLevelView();
  }

  function renderLevelPresentation(level) {
    var presentation = getPresentation(level.id);
    byId('jsr-level-presentation').innerHTML =
      briefCard('当前任务目标', presentation.objective) +
      briefCard('建议分析动作', presentation.action) +
      briefCard('本关产出物', presentation.deliverable) +
      briefCard('通关后线索用途', presentation.clueUse);
  }

  function renderHints(level) {
    var list = byId('jsr-hints');
    list.innerHTML = '';
    level.hints.forEach(function (hint, index) {
      var item = document.createElement('li');
      item.textContent = index < revealedHints ? hint : '分析结果已隐藏';
      item.className = index < revealedHints ? 'revealed' : '';
      list.appendChild(item);
    });
  }

  function renderTask(level) {
    var area = byId('jsr-task-area');
    area.innerHTML = '';

    if (level.type === 'quiz') {
      renderQuizTask(level, area);
    } else {
      renderReverseTask(level, area);
    }
  }

  function renderQuizTask(level, area) {
    if (level.id === 'level1') {
      area.innerHTML =
        inputField('plainText', '明文', level.starterInput.plainText, true) +
        inputField('encodedText', '给定编码串', level.starterInput.encodedText, true) +
        inputField('encoded', '请提交 Base64 编码结果') +
        inputField('decoded', '请提交解码后的明文');
    } else if (level.id === 'level2') {
      area.innerHTML =
        inputField('plainText', '原文', level.starterInput.plainText, true) +
        inputField('md5', 'MD5 结果') +
        inputField('sha256', 'SHA256 结果') +
        inputField('reversible', '摘要是否可逆（填“可逆”或“不可逆”）');
    } else if (level.id === 'level3') {
      area.innerHTML =
        inputField('key', '固定密钥', level.starterInput.key, true) +
        inputField('plainText', '待加密明文', level.starterInput.plainText, true) +
        inputField('encryptedText', '待解密密文', level.starterInput.encryptedText, true) +
        inputField('encrypted', '请输入加密结果') +
        inputField('decrypted', '请输入解密结果');
    } else if (level.id === 'level4') {
      area.innerHTML =
        inputField('timestamp', 'timestamp', level.starterInput.timestamp, true) +
        inputField('uid', 'uid', level.starterInput.uid, true) +
        inputField('secret', 'secret', level.starterInput.secret, true) +
        inputField('sign', '请输入正确 sign');
    }
  }

  function renderReverseTask(level, area) {
    var presentation = getPresentation(level.id);
    area.innerHTML =
      inputField('answer', '提交你的逆向结果') +
      '<div class="jsr-inline-note-group">' +
      '<p class="jsr-inline-note">建议动作：' + escapeHtml(presentation.action) + '</p>' +
      '<p class="jsr-inline-note">本关产出物：' + escapeHtml(presentation.deliverable) + '</p>' +
      '</div>';
  }

  function inputField(name, label, value, readonly) {
    return '<div class="jsr-input-group">' +
      '<label for="jsr-' + name + '">' + label + '</label>' +
      '<input id="jsr-' + name + '" ' + (readonly ? 'readonly' : '') + ' value="' + escapeAttr(value || '') + '">' +
      '</div>';
  }

  function revealHint() {
    if (!currentLevel || revealedHints >= currentLevel.hints.length) {
      if (currentLevel && revealedHints >= currentLevel.hints.length) {
        setFeedback('已经展示全部分析提示。', 'info');
      }
      return;
    }
    revealedHints += 1;
    global.JSReverseProgress.registerHint(state, currentLevel.id);
    byId('jsr-current-stars').textContent = global.JSReverseProgress.computeStars(state, currentLevel.id) + ' 星';
    renderHints(currentLevel);
    setFeedback('新的分析提示已加入案卷侧栏。', 'info');
    animatePanel('jsr-hints-panel');
  }

  function submitLevel() {
    if (!currentLevel) {
      return;
    }
    global.JSReverseProgress.incrementAttempts(state, currentLevel.id);
    byId('jsr-attempts').textContent = '尝试次数：' + (state.attemptsByLevel[currentLevel.id] || 0);
    setValidatingState(true);
    setFeedback('正在比对你的结果与证据特征...', 'pending');

    var inputs = collectInputs(currentLevel);
    var result = global.JSReverseVerify.verify(currentLevel, inputs, state);

    if (result.success) {
      state = global.JSReverseProgress.completeLevel(state, currentLevel, result);
      renderSummary();
      playSuccessSequence(currentLevel);
      if (currentLevel.id === 'level18') {
        renderReport();
        switchView('report');
        focusTop(false);
      } else {
        renderHub();
        openLevel(currentLevel);
        setFeedback(result.message, 'success');
      }
    } else {
      setFeedback(result.message, 'error');
    }

    setValidatingState(false);
  }

  function collectInputs(level) {
    if (level.type === 'reverse') {
      return { answer: readInput('answer') };
    }
    if (level.id === 'level1') {
      return { encoded: readInput('encoded'), decoded: readInput('decoded') };
    }
    if (level.id === 'level2') {
      return { md5: readInput('md5'), sha256: readInput('sha256'), reversible: readInput('reversible') };
    }
    if (level.id === 'level3') {
      return { encrypted: readInput('encrypted'), decrypted: readInput('decrypted') };
    }
    return { sign: readInput('sign') };
  }

  function renderReport() {
    var box = byId('jsr-report-summary');
    var rating = getCaseRating();
    byId('jsr-report-headline').textContent = '攻击者利用逐步升级的加密、混淆与运行时展开手法伪造请求并隐藏主控逻辑。你已经完成整条调查链的重建。';
    box.innerHTML =
      '<div class="jsr-report-grid">' +
      summaryCard('总星数', global.JSReverseProgress.getStars(state)) +
      summaryCard('总积分', state.score) +
      summaryCard('身份评级', rating.title) +
      summaryCard('已归档徽章', Object.keys(state.badges).length) +
      '</div>' +
      '<div class="jsr-report-rating">' +
      '<strong>' + rating.title + '</strong>' +
      '<p>' + rating.description + '</p>' +
      '</div>';

    var clues = byId('jsr-report-clues');
    clues.innerHTML = state.unlockedClues.map(function (clue) {
      return '<div class="jsr-report-clue"><strong>' + clue.title + '</strong><p>' + escapeHtml(clue.clue) + '</p></div>';
    }).join('');

    var reportTimeline = byId('jsr-report-timeline');
    reportTimeline.innerHTML = '';
    renderTimelineInto(reportTimeline);
  }

  function loadCodePreview(level) {
    if (!level.script) {
      byId('jsr-code-preview').textContent = level.codePreview || '暂无代码片段';
      return;
    }

    fetch(level.script)
      .then(function (response) {
        if (!response.ok) {
          throw new Error('加载失败');
        }
        return response.text();
      })
      .then(function (text) {
        byId('jsr-code-preview').textContent = text;
      })
      .catch(function () {
        byId('jsr-code-preview').textContent = level.codePreview || '暂无代码片段';
      });
  }

  function restoreSession() {
    renderHub();
    if (Object.keys(state.completedLevels).length === global.JS_REVERSE_LEVELS.length) {
      renderReport();
      switchView('report');
      focusTop(false);
      return;
    }

    if (state.currentLevelId) {
      var level = getLevelById(state.currentLevelId);
      if (level) {
        openLevel(level);
      }
    }
  }

  function summaryCard(label, value) {
    return '<div class="jsr-summary-card"><span>' + label + '</span><strong>' + value + '</strong></div>';
  }

  function openTools() {
    byId('jsr-tools-drawer').classList.remove('d-none');
    byId('jsr-tools-drawer').setAttribute('aria-hidden', 'false');
    byId('jsr-open-tools').setAttribute('aria-expanded', 'true');
    document.body.classList.add('jsr-drawer-open');
    setToolFilter(currentToolFilter);
  }

  function closeTools() {
    byId('jsr-tools-drawer').classList.add('d-none');
    byId('jsr-tools-drawer').setAttribute('aria-hidden', 'true');
    byId('jsr-open-tools').setAttribute('aria-expanded', 'false');
    document.body.classList.remove('jsr-drawer-open');
  }

  function setToolFilter(filter) {
    currentToolFilter = filter;
    Array.prototype.forEach.call(document.querySelectorAll('.jsr-tool-tab'), function (button) {
      button.classList.toggle('active', button.getAttribute('data-tool-filter') === filter);
    });
    Array.prototype.forEach.call(document.querySelectorAll('.jsr-tool-card'), function (card) {
      var visible = filter === 'all' || card.getAttribute('data-tool-category') === filter;
      card.classList.toggle('d-none', !visible);
    });
  }

  function onReset() {
    state = global.JSReverseProgress.reset();
    currentLevel = null;
    revealedHints = 0;
    closeTools();
    renderHub();
    setFeedback('训练场进度已清空，你可以从第 1 关重新开始。', 'info');
    focusTop(false);
  }

  function switchView(name) {
    toggleView('hub-view', name === 'hub');
    toggleView('level-view', name === 'level');
    toggleView('report-view', name === 'report');
  }

  function toggleView(id, visible) {
    var node = byId(id);
    node.classList.toggle('d-none', !visible);
    node.setAttribute('aria-hidden', visible ? 'false' : 'true');
    node.setAttribute('data-view-state', visible ? 'active' : 'inactive');
  }

  function setValidatingState(flag) {
    var button = byId('jsr-validate-button');
    button.disabled = flag;
    button.textContent = flag ? '验证中...' : '提交验证';
  }

  function setFeedback(message, tone) {
    var feedback = byId('jsr-feedback');
    if (!feedback) {
      return;
    }
    feedback.className = 'jsr-feedback' + (tone ? ' ' + tone : '');
    feedback.textContent = message;
  }

  function triggerStageReveal() {
    animatePanel('jsr-level-sidebar');
    animatePanel('jsr-task-panel');
    animatePanel('jsr-preview-panel');
  }

  function playSuccessSequence(level) {
    var card = document.querySelector('[data-level-id="' + level.id + '"]');
    if (card) {
      card.classList.add('jsr-flash-success');
      setTimeout(function () {
        card.classList.remove('jsr-flash-success');
      }, 900);
    }
    animatePanel('jsr-feedback');
  }

  function animatePanel(id) {
    var node = byId(id);
    if (!node || prefersReducedMotion()) {
      return;
    }
    node.classList.remove('jsr-pulse-reveal');
    void node.offsetWidth;
    node.classList.add('jsr-pulse-reveal');
  }

  function focusLevelView() {
    focusTop(false);
    var title = byId('jsr-level-title');
    if (title) {
      title.setAttribute('tabindex', '-1');
      title.focus({ preventScroll: true });
    }
  }

  function focusTop(smooth) {
    window.scrollTo({ top: 0, behavior: smooth === false ? 'auto' : 'smooth' });
  }

  function getLevelById(levelId) {
    for (var i = 0; i < global.JS_REVERSE_LEVELS.length; i += 1) {
      if (global.JS_REVERSE_LEVELS[i].id === levelId) {
        return global.JS_REVERSE_LEVELS[i];
      }
    }
    return null;
  }

  function getLevelsByGroup(group) {
    return global.JS_REVERSE_LEVELS.filter(function (level) {
      return level.group === group;
    });
  }

  function getPresentation(levelId) {
    return global.JS_REVERSE_PRESENTATION[levelId] || {
      objective: '继续推进当前证据。',
      action: '观察返回值与调用路径。',
      deliverable: '本关最终答案。',
      clueUse: '用于推进案件时间线。'
    };
  }

  function getStageArc(group) {
    for (var i = 0; i < global.JS_REVERSE_STAGE_ARCS.length; i += 1) {
      if (global.JS_REVERSE_STAGE_ARCS[i].group === group) {
        return global.JS_REVERSE_STAGE_ARCS[i];
      }
    }
    return global.JS_REVERSE_STAGE_ARCS[0];
  }

  function getNextAvailableLevel() {
    for (var i = 0; i < global.JS_REVERSE_LEVELS.length; i += 1) {
      if (!global.JSReverseProgress.isCompleted(state, global.JS_REVERSE_LEVELS[i].id)) {
        return global.JS_REVERSE_LEVELS[i];
      }
    }
    return null;
  }

  function getLevelState(level, unlocked) {
    if (global.JSReverseProgress.isCompleted(state, level.id)) {
      return 'completed';
    }
    if (state.currentLevelId === level.id) {
      return 'active';
    }
    return unlocked ? 'ready' : 'locked';
  }

  function getLevelStatusLabel(stateLabel) {
    if (stateLabel === 'completed') return '已破解';
    if (stateLabel === 'active') return '当前追踪';
    if (stateLabel === 'ready') return '待分析';
    return '封存';
  }

  function getLevelStars(levelId) {
    if (!state.starsByLevel[levelId]) {
      return '未结案';
    }
    return state.starsByLevel[levelId] + ' 星';
  }

  function getStageNote() {
    var solved = Object.keys(state.completedLevels).length;
    if (solved === 0) {
      return '先从基础通信与签名判断开始，把最浅层的伪装拆开。';
    }
    if (solved < 4) {
      return '现场勘查阶段进行中，抓住“是否可逆”和“参数怎么拼”这两条线。';
    }
    if (solved < 8) {
      return '初步取证阶段已经展开，变量名和包装层都只是拖延阅读的表象。';
    }
    if (solved < 12) {
      return '深度分析阶段重点看字符串表与索引顺序，别被字面文本误导。';
    }
    if (solved < 16) {
      return '追踪溯源阶段开始追会执行的路径，把死代码和烟雾弹全部甩开。';
    }
    if (solved < 18) {
      return '终极揭秘只剩主控脚本与简化 VM，保持先结果后路径的节奏。';
    }
    return '所有证据已归档，结案报告已经准备完毕。';
  }

  function getCaseSummary() {
    var solved = Object.keys(state.completedLevels).length;
    if (solved < 4) {
      return '异常通信、固定密钥与签名规则共同指向一条伪装传输链。';
    }
    if (solved < 12) {
      return '攻击脚本开始系统性地隐藏变量、入口与字符串，说明这是有准备的前端链路。';
    }
    if (solved < 18) {
      return '控制流、动态执行与多层封装已经暴露，主控脚本正在逐渐显形。';
    }
    return '主控逻辑、简化 VM 与最终结案口令已全部归档，攻击链复盘完成。';
  }

  function getGlobalObjective() {
    var nextLevel = getNextAvailableLevel();
    if (!nextLevel) {
      return '进入结案复盘，确认身份评级、徽章与完整线索时间线。';
    }
    return getPresentation(nextLevel.id).objective;
  }

  function getCaseRating() {
    var stars = global.JSReverseProgress.getStars(state);
    if (stars >= 48) {
      return { title: '终局破译师', description: '几乎没有走弯路，整条攻击链被你干净地拆开并归档。' };
    }
    if (stars >= 40) {
      return { title: '主控链侦查员', description: '你已经能稳定识别多层混淆与动态执行中的关键入口。' };
    }
    return { title: '案卷复原员', description: '你完成了完整调查，已经具备从浅层伪装追到核心逻辑的能力。' };
  }

  function prefersReducedMotion() {
    return global.matchMedia && global.matchMedia('(prefers-reduced-motion: reduce)').matches;
  }

  function briefCard(label, text) {
    return '<div class="jsr-brief-card"><span>' + label + '</span><strong>' + escapeHtml(text) + '</strong></div>';
  }

  function readInput(id) {
    var node = byId('jsr-' + id);
    return node ? node.value : '';
  }

  function byId(id) {
    return document.getElementById(id);
  }

  function escapeHtml(text) {
    return String(text).replace(/[&<>"']/g, function (char) {
      return ({
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#39;'
      })[char];
    });
  }

  function escapeAttr(text) {
    return escapeHtml(text);
  }
})(window);
