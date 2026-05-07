(function (global) {
  function normalize(value) {
    return String(value == null ? '' : value).trim();
  }

  function verify(level, inputMap, state) {
    if (level.type === 'quiz') {
      return verifyQuiz(level, inputMap, state);
    }
    return verifyReverse(level, inputMap, state);
  }

  function verifyQuiz(level, inputMap, state) {
    var ok = false;

    if (level.id === 'level1') {
      ok = normalize(inputMap.encoded) === level.expectedOutput.encoded &&
        normalize(inputMap.decoded) === level.expectedOutput.decoded;
    } else if (level.id === 'level2') {
      ok = normalize(inputMap.md5).toLowerCase() === level.expectedOutput.md5 &&
        normalize(inputMap.sha256).toLowerCase() === level.expectedOutput.sha256 &&
        normalize(inputMap.reversible) === level.expectedOutput.reversible;
    } else if (level.id === 'level3') {
      ok = verifyAES(level, inputMap) &&
        normalize(inputMap.decrypted) === level.expectedOutput.decrypted;
    } else if (level.id === 'level4') {
      ok = normalize(inputMap.sign).toLowerCase() === level.expectedOutput.sign;
    }

    return buildResult(ok, level, state);
  }

  function verifyReverse(level, inputMap, state) {
    var answer = normalize(inputMap.answer);
    var digest = global.CryptoJS.SHA256(answer + level.salt).toString();
    return buildResult(digest === level.answerHash, level, state);
  }

  function verifyAES(level, inputMap) {
    var encrypted = normalize(inputMap.encrypted);
    if (!encrypted) {
      return false;
    }

    try {
      var decrypted = global.CryptoJS.AES.decrypt(encrypted, level.starterInput.key).toString(global.CryptoJS.enc.Utf8);
      return decrypted === level.expectedOutput.encryptedPlainText;
    } catch (error) {
      return false;
    }
  }

  function buildResult(ok, level, state) {
    var stars = global.JSReverseProgress.computeStars(state, level.id);
    return {
      success: ok,
      message: ok ? '破译成功，线索已解锁。' : '解密失败，请继续分析。',
      starsEarned: ok ? stars : 0,
      scoreEarned: ok ? getScore(level.id) : 0,
      unlockedClue: ok ? level.clueFragment : ''
    };
  }

  function getScore(levelId) {
    var levelNum = parseInt(levelId.replace('level', ''), 10);
    if (levelNum <= 4) return 100;
    if (levelNum <= 8) return 150;
    if (levelNum <= 12) return 200;
    if (levelNum <= 16) return 250;
    return 400;
  }

  global.JSReverseVerify = {
    verify: verify
  };
})(window);
