const { defineConfig, devices } = require('@playwright/test');

module.exports = defineConfig({
  testDir: './tests/e2e',
  fullyParallel: false,
  retries: 0,
  timeout: 60000,
  expect: {
    timeout: 10000
  },
  reporter: [['list']],
  use: {
    baseURL: 'http://127.0.0.1:8017/frontend/',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure'
  },
  projects: [
    {
      name: 'desktop',
      use: {
        ...devices['Desktop Chrome'],
        channel: 'chrome',
        viewport: { width: 1440, height: 900 }
      }
    },
    {
      name: 'mobile',
      use: {
        ...devices['Pixel 5'],
        channel: 'chrome',
        viewport: { width: 390, height: 844 }
      }
    }
  ],
  webServer: {
    command: 'node -e "process.env.PORT=\'8017\'; require(\'./backend/server.js\')"',
    url: 'http://127.0.0.1:8017/frontend/',
    reuseExistingServer: true,
    timeout: 120000
  }
});
