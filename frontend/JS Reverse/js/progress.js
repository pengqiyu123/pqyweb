(function (global) {
  var STORAGE_KEY = 'js_reverse_progress';

  function createEmptyState() {
    return {
      completedLevels: {},
      attemptsByLevel: {},
      usedHintsByLevel: {},
      starsByLevel: {},
      score: 0,
      achievements: {},
      badges: {},
      unlockedClues: [],
      storyProgress: 0,
      finishedAt: '',
      currentLevelId: ''
    };
  }

  function load() {
    try {
      var raw = global.localStorage.getItem(STORAGE_KEY);
      if (!raw) {
        return createEmptyState();
      }
      return Object.assign(createEmptyState(), JSON.parse(raw));
    } catch (error) {
      console.error('读取 JS Reverse 进度失败', error);
      return createEmptyState();
    }
  }

  function save(state) {
    global.localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
  }

  function incrementAttempts(state, levelId) {
    state.attemptsByLevel[levelId] = (state.attemptsByLevel[levelId] || 0) + 1;
    save(state);
  }

  function registerHint(state, levelId) {
    state.usedHintsByLevel[levelId] = (state.usedHintsByLevel[levelId] || 0) + 1;
    save(state);
  }

  function computeStars(state, levelId) {
    var hints = state.usedHintsByLevel[levelId] || 0;
    if (hints === 0) {
      return 3;
    }
    if (hints === 1) {
      return 2;
    }
    return 1;
  }

  function getStageScore(levelId) {
    var num = parseInt(levelId.replace('level', ''), 10);
    if (num <= 4) return 100;
    if (num <= 8) return 150;
    if (num <= 12) return 200;
    if (num <= 16) return 250;
    return 400;
  }

  function completeLevel(state, level, result) {
    var stars = result.starsEarned || computeStars(state, level.id);
    if (!state.completedLevels[level.id]) {
      state.score += result.scoreEarned || getStageScore(level.id);
      state.unlockedClues.push({
        id: level.id,
        title: level.title,
        clue: result.unlockedClue || level.clueFragment
      });
    }

    state.completedLevels[level.id] = {
      completedAt: new Date().toISOString(),
      stars: stars
    };
    state.starsByLevel[level.id] = Math.max(stars, state.starsByLevel[level.id] || 0);
    state.storyProgress = Math.round((state.unlockedClues.length / global.JS_REVERSE_LEVELS.length) * 100);

    updateBadges(state);
    updateAchievements(state);

    if (state.unlockedClues.length === global.JS_REVERSE_LEVELS.length) {
      state.finishedAt = new Date().toISOString();
    }

    save(state);
    return state;
  }

  function updateAchievements(state) {
    global.JS_REVERSE_ACHIEVEMENTS.forEach(function (achievement) {
      if (!state.achievements[achievement.id] && achievement.check(state)) {
        state.achievements[achievement.id] = {
          unlockedAt: new Date().toISOString(),
          title: achievement.title,
          description: achievement.description
        };
      }
    });
  }

  function updateBadges(state) {
    global.JS_REVERSE_BADGES.forEach(function (badge) {
      if (!state.badges[badge.id] && allCompleted(state, badge.range[0], badge.range[1])) {
        state.badges[badge.id] = {
          unlockedAt: new Date().toISOString(),
          title: badge.title,
          group: badge.group
        };
      }
    });
  }

  function allCompleted(state, start, end) {
    for (var i = start; i <= end; i += 1) {
      if (!state.completedLevels['level' + i]) {
        return false;
      }
    }
    return true;
  }

  function reset() {
    var state = createEmptyState();
    save(state);
    return state;
  }

  function isCompleted(state, levelId) {
    return !!state.completedLevels[levelId];
  }

  function getStars(state) {
    return Object.keys(state.starsByLevel).reduce(function (sum, key) {
      return sum + state.starsByLevel[key];
    }, 0);
  }

  global.JSReverseProgress = {
    storageKey: STORAGE_KEY,
    load: load,
    save: save,
    reset: reset,
    incrementAttempts: incrementAttempts,
    registerHint: registerHint,
    computeStars: computeStars,
    completeLevel: completeLevel,
    isCompleted: isCompleted,
    getStars: getStars
  };
})(window);
