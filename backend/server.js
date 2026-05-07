#!/usr/bin/env node

const express = require('express');
const path = require('path');
const cors = require('cors');
const fs = require('fs');

const app = express();
const PORT = Number(process.env.PORT || 8000);

// 中间件
app.use(cors());
app.use(express.json());

// 添加基本安全头
app.use((req, res, next) => {
    // 设置基本安全头
    res.setHeader('X-Content-Type-Options', 'nosniff');
    res.setHeader('X-Frame-Options', 'DENY');
    next();
});

app.use(express.static('.'));

// 静态文件服务 - frontend目录
app.use('/frontend', express.static(path.join(__dirname, '../frontend')));

// 静态文件服务 - 其他资源
app.use('/css', express.static(path.join(__dirname, '../frontend/css')));
app.use('/js', express.static(path.join(__dirname, '../frontend/js')));
app.use('/images', express.static(path.join(__dirname, '../frontend/images')));

// 成语故事数据API
app.get('/api/idiom-stories', (req, res) => {
    try {
        const storiesPath = path.join(__dirname, '../中华成语/Idiom stories1.json');
        if (fs.existsSync(storiesPath)) {
            const data = fs.readFileSync(storiesPath, 'utf8');
            res.json(JSON.parse(data));
        } else {
            // 备用文件
            const fallbackPath = path.join(__dirname, '../中华成语/Idiom stories.json');
            if (fs.existsSync(fallbackPath)) {
                const data = fs.readFileSync(fallbackPath, 'utf8');
                res.json(JSON.parse(data));
            } else {
                res.status(404).json({ error: '成语故事文件未找到' });
            }
        }
    } catch (error) {
        console.error('读取成语故事文件失败:', error);
        res.status(500).json({ error: '服务器内部错误' });
    }
});

// 成语数据API
app.get('/api/chengyu-data', (req, res) => {
    try {
        const chengyuPath = path.join(__dirname, '../中华成语/chengyu_all_simple.json');
        if (fs.existsSync(chengyuPath)) {
            const data = fs.readFileSync(chengyuPath, 'utf8');
            res.json(JSON.parse(data));
        } else {
            res.status(404).json({ error: '成语数据文件未找到' });
        }
    } catch (error) {
        console.error('读取成语数据文件失败:', error);
        res.status(500).json({ error: '服务器内部错误' });
    }
});

// 主页路由 - 重定向到frontend
app.get('/', (req, res) => {
    res.redirect('/frontend/');
});

// frontend目录路由
app.get('/frontend/', (req, res) => {
    const indexPath = path.join(__dirname, '../frontend/index.html');
    if (fs.existsSync(indexPath)) {
        res.sendFile(indexPath);
    } else {
        res.status(404).send('主页文件未找到');
    }
});

// 支持frontend下的HTML文件直接访问
app.get('/frontend/:filename', (req, res) => {
    const filename = req.params.filename;
    const filePath = path.join(__dirname, '../frontend', filename);
    
    if (fs.existsSync(filePath) && filename.endsWith('.html')) {
        res.sendFile(filePath);
    } else {
        res.status(404).send('文件未找到');
    }
});

// 错误处理中间件
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send('服务器内部错误');
});

// 启动服务器
app.listen(PORT, '0.0.0.0', () => {
    console.log('=================================');
    console.log('🚀 服务器启动成功');
    console.log('=================================');
    console.log(`📋 服务信息:`);
    console.log(`   本地访问: http://localhost:${PORT}`);
    console.log(`   前端页面: http://localhost:${PORT}/frontend/`);
    console.log(`   局域网访问: http://0.0.0.0:${PORT}`);
    console.log('=================================');
    console.log('📁 可用页面:');
    console.log('   /frontend/ - 主页');
    console.log('   /frontend/成语学习.html - 成语学习');
    console.log('   /frontend/成语趣解.html - 成语趣解');
    console.log('   /frontend/太阳系.html - 太阳系');
    console.log('   /frontend/3D地球模型.html - 3D地球模型');
    console.log('   /frontend/古诗排序.html - 古诗排序');
    console.log('   /frontend/速算.html - 速算练习');
    console.log('   /frontend/敲木鱼.html - 敲木鱼');
    console.log('   /frontend/偏旁部首拼汉字.html - 偏旁部首拼汉字');
    console.log('   /frontend/分数大小比较.html - 分数大小比较');
    console.log('   /frontend/一次方程学习.html - 一次方程学习');
    console.log('   /frontend/二次方程学习.html - 二次方程学习');
    console.log('   /frontend/三视图教学.html - 三视图教学');
    console.log('   /frontend/食物链学习.html - 食物链学习');
    console.log('=================================');
    console.log('🔧 API接口:');
    console.log('   GET /api/idiom-stories - 获取成语故事');
    console.log('   GET /api/chengyu-data - 获取成语数据');
    console.log('=================================');
    console.log('按 Ctrl+C 停止服务器');
});
