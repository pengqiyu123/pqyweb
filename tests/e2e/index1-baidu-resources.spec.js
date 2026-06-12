const { test, expect } = require('@playwright/test');

async function gotoIndex1(page, hash = '') {
  await page.goto(`index1.html${hash}`);
  await expect(page.getByTestId('tab-shell')).toBeVisible();
}

test.describe('Index1 百度网盘资源栏目', () => {
  test('Tab 导航默认显示工具银河，并可通过 hash 打开百度资源', async ({ page }) => {
    await gotoIndex1(page);
    await expect(page.getByTestId('tab-button-tools')).toHaveAttribute('aria-selected', 'true');
    await expect(page.locator('#tools')).toBeVisible();
    await expect(page.locator('#resources')).toBeHidden();

    await page.getByTestId('tab-button-resources').click();
    await expect(page).toHaveURL(/#resources$/);
    await expect(page.getByTestId('tab-button-resources')).toHaveAttribute('aria-selected', 'true');
    await expect(page.locator('#resources')).toBeVisible();
    await expect(page.locator('#tools')).toBeHidden();

    await page.reload();
    await expect(page.getByTestId('tab-button-resources')).toHaveAttribute('aria-selected', 'true');
    await expect(page.locator('#resources')).toBeVisible();
  });

  test('工具银河移除打印机，百度资源分页视图显示 7 个网盘资源', async ({ page }) => {
    await gotoIndex1(page, '#resources');

    await page.getByTestId('tab-button-tools').click();
    await expect(page.locator('#tools')).not.toContainText('打印机');

    await page.getByTestId('tab-button-resources').click();
    await expect(page.getByTestId('resource-view-page')).toHaveAttribute('aria-pressed', 'true');
    await expect(page.getByTestId('baidu-resource-card')).toHaveCount(7);
    await expect(page.getByTestId('resource-pagination-status')).toContainText('1 / 1');
    await expect(page.getByTestId('resource-next-page')).toBeDisabled();
    await expect(page.locator('#resources')).toContainText('打印机');
    await expect(page.locator('#resources')).toContainText('Open-AutoGLM');
    await expect(page.locator('#resources')).toContainText('剪映邪修导出 10.7.0');
  });

  test('折叠视图默认收起，点击后展开详情', async ({ page }) => {
    await gotoIndex1(page, '#resources');

    await page.getByTestId('resource-view-accordion').click();
    await expect(page.getByTestId('resource-view-accordion')).toHaveAttribute('aria-pressed', 'true');
    await expect(page.getByTestId('baidu-resource-accordion')).toHaveCount(7);
    await expect(page.getByTestId('accordion-panel-bd_printer')).toBeHidden();

    await page.getByTestId('accordion-trigger-bd_printer').click();
    await expect(page.getByTestId('accordion-panel-bd_printer')).toBeVisible();
    await expect(page.getByTestId('accordion-panel-bd_printer')).toContainText('网盘资源链接，包含打印机相关文件');
  });

  test('分类视图按 category 分组，并记住上次视图选择', async ({ page }) => {
    await gotoIndex1(page, '#resources');

    await page.getByTestId('resource-view-category').click();
    await expect(page.getByTestId('resource-view-category')).toHaveAttribute('aria-pressed', 'true');
    await expect(page.getByTestId('resource-category-group')).toHaveCount(6);
    await expect(page.getByTestId('category-title-AI 工具')).toContainText('AI 工具');
    await expect(page.getByTestId('category-title-办公设备')).toContainText('办公设备');

    await page.reload();
    await expect(page.getByTestId('resource-view-category')).toHaveAttribute('aria-pressed', 'true');
    await expect(page.getByTestId('resource-category-group')).toHaveCount(6);
  });

  test('百度网盘外链使用安全的新窗口属性', async ({ page }) => {
    await gotoIndex1(page, '#resources');

    const links = await page.getByTestId('baidu-resource-card').evaluateAll((cards) =>
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
});
