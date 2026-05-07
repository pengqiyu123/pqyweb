const { test, expect } = require('@playwright/test');

const STORAGE_KEY = 'js_reverse_progress';

function buildState(completedLevelNumbers) {
  const completedLevels = {};
  const starsByLevel = {};
  const unlockedClues = [];
  const attemptsByLevel = {};
  const usedHintsByLevel = {};
  const badges = {};
  const achievements = {};

  completedLevelNumbers.forEach((num) => {
    const id = `level${num}`;
    completedLevels[id] = { completedAt: '2026-05-07T00:00:00.000Z', stars: 3 };
    starsByLevel[id] = 3;
    unlockedClues.push({
      id,
      title: id,
      clue: id
    });
    attemptsByLevel[id] = 1;
    usedHintsByLevel[id] = 0;
  });

  if (completedLevelNumbers.length >= 4) {
    badges.badge_1 = { unlockedAt: '2026-05-07T00:00:00.000Z', title: '现场勘查员', group: '现场勘查' };
  }
  if (completedLevelNumbers.length >= 8) {
    badges.badge_2 = { unlockedAt: '2026-05-07T00:00:00.000Z', title: '初步取证员', group: '初步取证' };
  }
  if (completedLevelNumbers.length >= 12) {
    badges.badge_3 = { unlockedAt: '2026-05-07T00:00:00.000Z', title: '深度分析员', group: '深度分析' };
  }
  if (completedLevelNumbers.length >= 16) {
    badges.badge_4 = { unlockedAt: '2026-05-07T00:00:00.000Z', title: '溯源追踪员', group: '追踪溯源' };
  }

  return {
    completedLevels,
    attemptsByLevel,
    usedHintsByLevel,
    starsByLevel,
    score: completedLevelNumbers.reduce((sum, num) => {
      if (num <= 4) return sum + 100;
      if (num <= 8) return sum + 150;
      if (num <= 12) return sum + 200;
      if (num <= 16) return sum + 250;
      return sum + 400;
    }, 0),
    achievements,
    badges,
    unlockedClues,
    storyProgress: Math.round((unlockedClues.length / 18) * 100),
    finishedAt: completedLevelNumbers.length === 18 ? '2026-05-07T00:00:00.000Z' : '',
    currentLevelId: completedLevelNumbers.length === 18 ? 'level18' : `level${Math.min(completedLevelNumbers.length + 1, 18)}`
  };
}

async function seedProgress(page, completedLevelNumbers, extraStorage) {
  const state = buildState(completedLevelNumbers);
  await page.context().addInitScript(({ storageKey, payload, extra }) => {
    window.localStorage.setItem(storageKey, JSON.stringify(payload));
    Object.keys(extra || {}).forEach((key) => {
      window.localStorage.setItem(key, extra[key]);
    });
  }, { storageKey: STORAGE_KEY, payload: state, extra: extraStorage || {} });
}

async function gotoHub(page) {
  await page.goto('JS%20Reverse/index.html');
  await expect(page.getByTestId('jsr-app')).toBeVisible();
  await expect(page.getByTestId('jsr-hero')).toBeVisible();
}

async function ensureHubVisible(page) {
  const hubView = page.getByTestId('hub-view');
  const levelView = page.getByTestId('level-view');
  const reportView = page.getByTestId('report-view');

  if (await hubView.getAttribute('data-view-state') === 'active') {
    return;
  }

  if (await levelView.getAttribute('data-view-state') === 'active') {
    await page.locator('#jsr-back-button').click();
    await expect(hubView).toHaveAttribute('data-view-state', 'active');
    return;
  }

  if (await reportView.getAttribute('data-view-state') === 'active') {
    await page.locator('#jsr-report-back').click();
    await expect(hubView).toHaveAttribute('data-view-state', 'active');
    return;
  }

  await expect(hubView).toHaveAttribute('data-view-state', 'active');
}

test.describe('JS Reverse 首页入口', () => {
  ['index1.html', 'index2.html', 'index3.html'].forEach((entry) => {
    test(`入口 ${entry} 显示 JS逆向闯关 卡片`, async ({ page }) => {
      await page.goto(entry);
      const card = page.locator('a[href="JS Reverse/index.html"]').filter({ hasText: 'JS逆向闯关' }).first();
      await expect(card).toBeVisible();
      await expect(card).toHaveAttribute('href', /JS Reverse\/index\.html/);
    });
  });
});

test.describe('JS Reverse 主线验收', () => {
  test('第1关提示、通关、刷新保留进度', async ({ page }) => {
    await gotoHub(page);
    await page.locator('[data-level-id="level1"]').click();
    await page.getByTestId('jsr-hint-button').click();
    await expect(page.getByTestId('jsr-feedback')).toContainText('新的分析提示');
    await page.locator('#jsr-encoded').fill('aGVsbG8tcHF5');
    await page.locator('#jsr-decoded').fill("alert('pqy')");
    await page.getByTestId('jsr-submit').click();
    await expect(page.getByTestId('jsr-feedback')).toContainText('破译成功');
    await page.reload();
    await expect(page.getByTestId('level-view')).toBeVisible();
    await expect(page.locator('#jsr-current-stars')).toContainText('2 星');
  });

  test('第3关 AES 真实验证', async ({ page }) => {
    await seedProgress(page, [1, 2], {});
    await gotoHub(page);
    await ensureHubVisible(page);
    await page.locator('[data-level-id="level3"]').click();
    const encrypted = await page.evaluate(() => window.CryptoJS.AES.encrypt('case-open', 'shadow-key-2026').toString());
    await page.locator('#jsr-encrypted').fill(encrypted);
    await page.locator('#jsr-decrypted').fill('shadow-terminal');
    await page.getByTestId('jsr-submit').click();
    await expect(page.getByTestId('jsr-feedback')).toContainText('破译成功');
  });

  test('第18关后进入结案页', async ({ page }) => {
    await seedProgress(page, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], {});
    await gotoHub(page);
    await ensureHubVisible(page);
    await page.locator('[data-level-id="level18"]').click();
    await page.locator('#jsr-answer').fill('shadow-case-closed');
    await page.getByTestId('jsr-submit').click();
    await expect(page.getByTestId('report-view')).toBeVisible();
    await expect(page.getByText('CASE CLOSED')).toBeVisible();
  });
});

[
  { name: '第5关 reverse 通关', completed: [1, 2, 3, 4], level: 'level5', answer: 'shadow-pw' },
  { name: '第10关 reverse 通关', completed: [1, 2, 3, 4, 5, 6, 7, 8, 9], level: 'level10', answer: 'case-token' },
  { name: '第11关 reverse 通关', completed: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], level: 'level11', answer: 'hidden-seed' },
  { name: '第13关 reverse 通关', completed: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], level: 'level13', answer: '2-0-3-1' },
  { name: '第15关 reverse 通关', completed: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], level: 'level15', answer: 'shadow-token' }
].forEach((scenario) => {
  test(scenario.name, async ({ page }) => {
    await seedProgress(page, scenario.completed, {});
    await gotoHub(page);
    await ensureHubVisible(page);
    await page.locator(`[data-level-id="${scenario.level}"]`).click();
    await page.locator('#jsr-answer').fill(scenario.answer);
    await page.getByTestId('jsr-submit').click();
    await expect(page.getByTestId('jsr-feedback')).toContainText('破译成功');
  });
});

test.describe('JS Reverse 工具工作台与重置', () => {
  test('工具面板基础能力可用', async ({ page }) => {
    await gotoHub(page);
    await page.getByRole('button', { name: '工具工作台' }).click();
    await expect(page.getByTestId('jsr-tools-drawer')).toBeVisible();

    await page.locator('#jsr-tool-base64-input').fill('hello-pqy');
    await page.locator('#jsr-tool-base64-encode').click();
    await expect(page.locator('#jsr-tool-base64-output')).toHaveValue('aGVsbG8tcHF5');

    await page.locator('#jsr-tool-hash-input').fill('shadow-entry');
    await page.locator('#jsr-tool-md5').click();
    await expect(page.locator('#jsr-tool-hash-output')).toHaveValue('1e877c51542abb783d71845c0e2ab62d');
    await page.locator('#jsr-tool-sha256').click();
    await expect(page.locator('#jsr-tool-hash-output')).toHaveValue('1d0bdb2ccaca599827e3ec26447ff03bb9dc8dd86ed82376ecacb010fa108c40');

    await page.locator('#jsr-tool-aes-key').fill('shadow-key-2026');
    await page.locator('#jsr-tool-aes-input').fill('case-open');
    await page.locator('#jsr-tool-aes-encrypt').click();
    const aesCipher = await page.locator('#jsr-tool-aes-output').inputValue();
    await page.locator('#jsr-tool-aes-input').fill(aesCipher);
    await page.locator('#jsr-tool-aes-decrypt').click();
    await expect(page.locator('#jsr-tool-aes-output')).toHaveValue('case-open');

    await page.locator('#jsr-tool-beautify-input').fill('function x(){return 1;}');
    await page.locator('#jsr-tool-beautify').click();
    await expect(page.locator('#jsr-tool-beautify-output')).toHaveValue(/function x\(\)/);

    await page.locator('#jsr-tool-hex-input').fill('pqy');
    await page.locator('#jsr-tool-to-hex').click();
    await expect(page.locator('#jsr-tool-hex-output')).toHaveValue('707179');
  });

  test('重新调查只清空训练场状态', async ({ page }) => {
    await seedProgress(page, [1, 2, 3], { preserved_key: 'keep-me' });
    await gotoHub(page);
    await ensureHubVisible(page);
    await page.getByRole('button', { name: '重新调查' }).click();
    const values = await page.evaluate((storageKey) => ({
      jsr: window.localStorage.getItem(storageKey),
      preserved: window.localStorage.getItem('preserved_key')
    }), STORAGE_KEY);
    expect(values.preserved).toBe('keep-me');
    expect(values.jsr).toContain('"completedLevels":{}');
  });
});
