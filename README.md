# 导航网站服务器搭建指南

## 🚀 快速开始

### 方法1: 使用批处理文件（推荐Windows用户）
1. 双击 `start-server.bat` 文件
2. 脚本会自动检查环境并启动服务器

### 方法2: 使用PowerShell脚本
1. 右键点击 `start-server.ps1`
2. 选择"使用PowerShell运行"
3. 如果遇到执行策略问题，请先运行：`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

### 方法3: 手动启动
```bash
# 安装依赖
npm install

# 启动服务器
npm start
```

## 📋 系统要求

- **Node.js**: 版本 14.0.0 或更高
- **操作系统**: Windows 10/11, macOS, Linux
- **网络**: 需要网络连接来下载依赖包

## 🔧 安装Node.js

如果您的电脑上没有安装Node.js，请：

1. 访问 [https://nodejs.org/](https://nodejs.org/)
2. 下载并安装LTS版本
3. 安装完成后重启命令提示符或PowerShell

## 🌐 访问网站

### 本机访问
- 地址：`http://localhost:8000`
- 前端页面：`http://localhost:8000/frontend/`
- 说明：只有您自己的电脑可以访问

### 局域网访问（其他人可以访问）
- 地址：`http://[您的IP地址]:8000`
- 例如：`http://192.168.1.100:8000`
- 前端页面：`http://[您的IP地址]:8000/frontend/`
- 说明：连接到同一WiFi网络的其他设备可以访问

## ⚠️ 重要注意事项

### 1. 防火墙设置
确保Windows防火墙允许端口8000的访问：
1. 打开"Windows安全中心"
2. 点击"防火墙和网络保护"
3. 点击"允许应用通过防火墙"
4. 确保Node.js被允许通过防火墙

### 2. 网络配置
- 其他设备必须连接到同一个WiFi网络
- 如果使用公司网络，可能需要IT部门协助开放端口

### 3. 安全考虑
- 这是一个开发服务器，不建议直接暴露到公网
- 如需公网访问，建议使用专业的托管服务

## 🛠️ 故障排除

### 问题1: 端口被占用
```
Error: listen EADDRINUSE: address already in use :::8000
```
**解决方案**: 
- 关闭其他可能占用8000端口的程序
- 或者修改 `backend/server.js` 中的端口号

### 问题2: 依赖安装失败
**解决方案**:
- 检查网络连接
- 尝试使用国内镜像：`npm config set registry https://registry.npmmirror.com`
- 清除npm缓存：`npm cache clean --force`

### 问题3: 其他设备无法访问
**解决方案**:
1. 确认防火墙设置
2. 检查IP地址是否正确
3. 尝试临时关闭防火墙测试
4. 确保使用正确的端口号8000

## 📁 项目结构

```
pqy_web/
├── frontend/           # 前端文件
│   ├── index.html     # 主页面
│   ├── css/           # 样式文件
│   ├── js/            # JavaScript文件
│   ├── images/        # 图片资源
│   ├── 成语学习.html  # 成语学习页面
│   ├── 成语趣解.html  # 成语趣解页面
│   ├── 太阳系.html    # 太阳系页面
│   ├── 3D地球模型.html # 3D地球模型页面
│   ├── 古诗排序.html  # 古诗排序页面
│   ├── 速算.html       # 速算练习页面
│   ├── 敲木鱼.html     # 敲木鱼页面
│   ├── 偏旁部首拼汉字.html # 偏旁部首拼汉字页面
│   ├── 分数大小比较.html   # 分数大小比较页面
│   ├── 一次方程学习.html   # 一次方程学习页面
│   ├── 二次方程学习.html   # 二次方程学习页面
│   ├── 三视图教学.html     # 三视图教学页面
│   ├── 食物链学习.html     # 食物链学习页面
│   └── ...           # 其他学习页面
├── backend/            # 后端文件
│   └── server.js      # 服务器代码
├── 中华成语/           # 成语数据
│   ├── Idiom stories.json # 成语故事数据
│   ├── chengyu_all_simple.json # 成语数据
│   └── ...           # 其他成语相关文件
├── um-web.legacy.v1.10.8/  # 音乐解码工具
├── package.json        # 项目配置
├── start-server.bat    # Windows启动脚本
├── start-server.ps1    # PowerShell启动脚本
└── README.md           # 说明文档
```

## 🔄 停止服务器

在运行服务器的命令行窗口中按 `Ctrl + C` 即可停止服务器。

## 📞 获取帮助

如果遇到问题，请检查：
1. Node.js版本是否正确（需要14.0.0或更高版本）
2. 依赖是否安装完整
3. 端口8000是否被占用
4. 防火墙设置是否正确
5. 确保使用正确的访问地址：http://localhost:8000/frontend/

---

**祝您使用愉快！** 🎉
