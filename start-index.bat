@echo off
chcp 65001 >nul

echo ========================================
echo   导航网站本地启动脚本
echo ========================================
echo.

REM 切换到项目根目录
cd /d %~dp0

echo [1] 正在检查 Node.js...
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo 错误: 未检测到 Node.js
    echo 请先安装 Node.js 14.0.0 或更高版本: https://nodejs.org/
    pause
    exit /b 1
)

echo [2] 正在检查 npm...
npm --version >nul 2>&1
if %errorlevel% neq 0 (
    echo 错误: npm 不可用
    echo 请确保 Node.js 安装时包含了 npm
    pause
    exit /b 1
)

echo [3] 正在安装/更新依赖...
npm install
if %errorlevel% neq 0 (
    echo 依赖安装失败，尝试使用国内镜像...
    npm config set registry https://registry.npmmirror.com
    npm install
    if %errorlevel% neq 0 (
        echo 依赖安装仍然失败
        pause
        exit /b 1
    )
)

echo [4] 启动导航网站服务器 (npm start)...
echo   本机访问:  http://localhost:8000

echo.
echo 按 Ctrl+C 可以停止服务器。
echo.

npm start
