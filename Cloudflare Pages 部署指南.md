# Cloudflare Pages 部署指南

## 准备工作
1. 注册 Cloudflare 账号：https://dash.cloudflare.com/sign-up
2. 准备 GitHub 账号（用于代码托管）

## 部署步骤

### 第一步：将代码推送到 GitHub

1. 在 GitHub 创建新仓库（如：`pqy-web-navigation`）
2. 将项目文件推送到仓库：

```bash
# 初始化 Git
cd d:\\python\\pqy_web
git init
git add .
git commit -m "初始提交：教育导航网站"

# 连接到 GitHub 仓库
git remote add origin https://github.com/你的用户名/pqy-web-navigation.git
git branch -M main
git push -u origin main
```

### 第二步：在 Cloudflare Pages 部署

1. 登录 Cloudflare Dashboard：https://dash.cloudflare.com/
2. 点击左侧菜单 "Workers & Pages"
3. 点击 "Create application" → "Pages"
4. 选择 "Connect to Git"
5. 授权 Cloudflare 访问你的 GitHub 账户
6. 选择你的仓库：`pqy-web-navigation`
7. 配置构建设置：
   - **构建命令**：留空（因为是静态网站）
   - **构建输出目录**：`frontend`
   - **根目录**：留空
8. 点击 "Save and Deploy"

### 第三步：配置自定义域名（可选）

1. 在 Pages 项目页面，点击 "Custom domains"
2. 添加你的域名（需要先添加到 Cloudflare DNS）
3. 等待 DNS 生效

## 项目结构说明

- `frontend/` - 前端文件目录（Cloudflare Pages 的构建输出目录）
- `_redirects` - SPA 路由重定向配置
- 其他文件：后端和工具文件（不会被部署）

## 访问地址

部署完成后，你将获得类似这样的访问地址：
- **免费域名**：https://pqy-web-navigation.pages.dev（立即可用，完全免费）
- **自定义域名**：https://你的域名.com（可选，需要购买域名）

## 自动部署

每次向 GitHub 仓库推送代码时，Cloudflare Pages 会自动重新部署。

## 优势

- ✅ **完全免费**（每月10万次请求，无带宽限制）
- ✅ **全球CDN加速**
- ✅ **自动HTTPS**
- ✅ **自定义域名支持**
- ✅ **自动部署**
- ✅ **无需服务器维护**

## 注意事项

1. 确保 `frontend` 目录包含所有必要的静态文件
2. 如果使用后端API，需要单独部署到其他服务
3. 大文件（如图片、视频）建议使用CDN优化