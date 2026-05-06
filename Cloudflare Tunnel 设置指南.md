# Cloudflare Tunnel 设置指南

## 什么是 Cloudflare Tunnel？
Cloudflare Tunnel 是一个免费的内网穿透服务，比 ngrok 更稳定，不会频繁更换地址。

## 设置步骤

### 1. 注册 Cloudflare 账号
- 访问 https://cloudflare.com/
- 注册免费账号

### 2. 添加域名
- 在 Cloudflare 控制台添加你的域名
- 或者使用 Cloudflare 提供的免费子域名

### 3. 安装 cloudflared
```bash
# Windows (使用 winget)
winget install Cloudflare.cloudflared

# 或者手动下载
# https://github.com/cloudflare/cloudflared/releases
```

### 4. 登录 Cloudflare
```bash
cloudflared tunnel login
```

### 5. 创建隧道
```bash
# 创建隧道
cloudflared tunnel create suffix-converter

# 配置隧道
cloudflared tunnel route dns suffix-converter your-subdomain.yourdomain.com
```

### 6. 创建配置文件
在项目根目录创建 `tunnel.yml`：
```yaml
tunnel: YOUR_TUNNEL_ID
credentials-file: C:\Users\YOUR_USERNAME\.cloudflared\YOUR_TUNNEL_ID.json

ingress:
  - hostname: your-subdomain.yourdomain.com
    service: http://localhost:5000
  - service: http_status:404
```

### 7. 启动隧道
```bash
cloudflared tunnel run suffix-converter
```

## 优势
- ✅ 完全免费
- ✅ 地址稳定不变
- ✅ 全球CDN加速
- ✅ 自动HTTPS
- ✅ 无流量限制

## 注意事项
- 需要有一个域名（可以是免费域名）
- 首次设置相对复杂，但一次设置永久使用
