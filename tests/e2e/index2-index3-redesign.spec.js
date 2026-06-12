const { test, expect } = require('@playwright/test');

async function gotoIndex2(page, hash = '') {
  await page.goto(`index2.html${hash}`);
  await expect(page.getByTestId('terminal-page')).toBeVisible();
}

async function gotoIndex3(page) {
  await page.goto('index3.html');
  await expect(page.getByTestId('paper-page')).toBeVisible();
}

test.describe('Index2 赛博终端', () => {
  test('侧边栏切换 5 个栏目，并正确渲染百度网盘资源', async ({ page }) => {
    await gotoIndex2(page);

    await expect(page.getByTestId('terminal-nav-tools')).toHaveAttribute('aria-selected', 'true');
    await expect(page.locator('#panelTitle')).toContainText('工具银河');
    await expect(page.locator('a[href="JS Reverse/index.html"]').filter({ hasText: 'JS逆向闯关' })).toHaveCount(0);

    await page.getByTestId('terminal-nav-learning').click();
    await expect(page.getByTestId('terminal-nav-learning')).toHaveAttribute('aria-selected', 'true');
    await expect(page.locator('a[href="JS Reverse/index.html"]').filter({ hasText: 'JS逆向闯关' })).toBeVisible();

    await page.getByTestId('terminal-nav-resources').click();
    await expect(page.getByTestId('terminal-nav-resources')).toHaveAttribute('aria-selected', 'true');
    await expect(page.locator('#panelTitle')).toContainText('百度资源');
    await expect(page.locator('.terminal-card[data-group="resources"]')).toHaveCount(7);
    await expect(page.getByTestId('terminal-grid')).toContainText('打印机');
    await expect(page.getByTestId('terminal-grid')).toContainText('剪映邪修导出 10.7.0');

    const links = await page.locator('.terminal-card[data-group="resources"]').evaluateAll((cards) =>
      cards.map((card) => ({
        href: card.href,
        target: card.target,
        rel: card.rel
      }))
    );

    expect(links).toHaveLength(7);
    for (const link of links) {
      expect(link.href).toContain('https://pan.baidu.com/');
      expect(link.target).toBe('_blank');
      expect(link.rel.split(/\s+/)).toEqual(expect.arrayContaining(['noopener', 'noreferrer']));
    }
  });

  test('搜索只过滤当前栏目，并保留稳定布局反馈', async ({ page }) => {
    await gotoIndex2(page, '#resources');
    await expect(page.locator('.terminal-card[data-group="resources"]')).toHaveCount(7);

    await page.getByTestId('terminal-search').fill('剪映');
    await expect(page.locator('.terminal-card[data-group="resources"][data-match="true"]')).toHaveCount(1);
    await expect(page.getByTestId('terminal-count')).toContainText('1/7');
    await expect(page.getByTestId('terminal-empty')).toBeHidden();

    await page.getByTestId('terminal-search').fill('没有这个资源');
    await expect(page.locator('.terminal-card[data-group="resources"][data-match="true"]')).toHaveCount(0);
    await expect(page.getByTestId('terminal-empty')).toBeVisible();

    await page.getByTestId('terminal-search').fill('');
    await expect(page.locator('.terminal-card[data-group="resources"][data-match="true"]')).toHaveCount(7);
    await expect(page.getByTestId('terminal-count')).toContainText('7 ITEMS');
  });

  test('移动端侧边栏变为底部水平导航', async ({ page }, testInfo) => {
    test.skip(testInfo.project.name !== 'mobile', '移动端布局只在 mobile project 验证');

    await gotoIndex2(page);
    const navStyle = await page.getByTestId('terminal-nav').evaluate((nav) => {
      const style = window.getComputedStyle(nav);
      return {
        position: style.position,
        bottom: style.bottom,
        direction: style.flexDirection
      };
    });

    expect(navStyle.position).toBe('fixed');
    expect(navStyle.bottom).toBe('0px');
    expect(navStyle.direction).toBe('row');
  });
});

test.describe('Index3 纸艺工坊', () => {
  test('纵向渲染 5 个栏目，并用水平卡片展示 7 条百度网盘资源', async ({ page }) => {
    await gotoIndex3(page);

    await expect(page.locator('.paper-section')).toHaveCount(5);
    await expect(page.getByTestId('paper-section-tools')).toBeVisible();
    await expect(page.getByTestId('paper-section-resources')).toBeVisible();
    await expect(page.getByTestId('paper-section-fun')).toBeVisible();
    await expect(page.getByTestId('paper-section-learning')).toBeVisible();
    await expect(page.getByTestId('paper-section-ai')).toBeVisible();
    await expect(page.getByTestId('paper-resource-card')).toHaveCount(7);
    await expect(page.getByTestId('paper-resource-rail')).toContainText('打印机');

    const railOverflow = await page.getByTestId('paper-resource-rail').evaluate((rail) => rail.scrollWidth > rail.clientWidth);
    expect(railOverflow).toBe(true);

    const links = await page.getByTestId('paper-resource-card').evaluateAll((cards) =>
      cards.map((card) => ({
        href: card.href,
        target: card.target,
        rel: card.rel
      }))
    );

    expect(links).toHaveLength(7);
    for (const link of links) {
      expect(link.href).toContain('https://pan.baidu.com/');
      expect(link.target).toBe('_blank');
      expect(link.rel.split(/\s+/)).toEqual(expect.arrayContaining(['noopener', 'noreferrer']));
    }
  });

  test('全站搜索隐藏无匹配栏目，清空后恢复', async ({ page }) => {
    await gotoIndex3(page);

    await page.getByTestId('paper-search').fill('剪映');
    await expect(page.getByTestId('paper-section-resources')).toBeVisible();
    await expect(page.locator('[data-section-card="resources"][data-match="true"]')).toHaveCount(1);
    await expect(page.getByTestId('paper-section-tools')).toBeHidden();
    await expect(page.getByText(/^1\/\d+$/)).toBeVisible();

    await page.getByTestId('paper-search').fill('绝对不存在的资源名');
    await expect(page.getByTestId('paper-no-results')).toBeVisible();

    await page.getByTestId('paper-search').fill('');
    await expect(page.getByTestId('paper-no-results')).toBeHidden();
    await expect(page.locator('.paper-section')).toHaveCount(5);
    await expect(page.getByTestId('paper-section-tools')).toBeVisible();
  });

  test('滚动后显示回到顶部按钮', async ({ page }) => {
    await gotoIndex3(page);

    await expect(page.getByTestId('paper-back-top')).not.toHaveClass(/is-visible/);
    await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight));
    await expect(page.getByTestId('paper-back-top')).toHaveClass(/is-visible/);
    await page.getByTestId('paper-back-top').click();
    await expect.poll(() => page.evaluate(() => window.scrollY)).toBeLessThan(40);
  });

  test('移动端 Bento 变单列，百度资源保持水平滚动', async ({ page }, testInfo) => {
    test.skip(testInfo.project.name !== 'mobile', '移动端布局只在 mobile project 验证');

    await gotoIndex3(page);
    const columnCount = await page.locator('.bento-grid').first().evaluate((grid) => {
      return window.getComputedStyle(grid).gridTemplateColumns.split(' ').filter(Boolean).length;
    });
    const railOverflow = await page.getByTestId('paper-resource-rail').evaluate((rail) => rail.scrollWidth > rail.clientWidth);

    expect(columnCount).toBe(1);
    expect(railOverflow).toBe(true);
  });
});
