/**
 * Service Worker for 导航网站
 * 提供离线缓存、推送通知等PWA功能
 */

const CACHE_NAME = 'navigation-site-v1.0.0';
const STATIC_CACHE = 'static-v1.0.0';
const DYNAMIC_CACHE = 'dynamic-v1.0.0';

// 需要缓存的静态资源
const STATIC_ASSETS = [
    '/',
    '/index.html',
    '/css/main.css',
    '/js/device-adapter.js',
    '/js/theme.js',
    '/js/search.js',
    '/js/api.service.js',
    '/manifest.json',
    'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css',
    'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js',
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css'
];

// 需要缓存的动态资源
const DYNAMIC_ASSETS = [
    '/api/health',
    '/api/convert-suffix'
];

// 安装事件
self.addEventListener('install', (event) => {
    console.log('🚀 Service Worker 安装中...');
    
    event.waitUntil(
        caches.open(STATIC_CACHE)
            .then((cache) => {
                console.log('📦 缓存静态资源');
                return cache.addAll(STATIC_ASSETS);
            })
            .then(() => {
                console.log('✅ 静态资源缓存完成');
                return self.skipWaiting();
            })
            .catch((error) => {
                console.error('❌ 静态资源缓存失败:', error);
            })
    );
});

// 激活事件
self.addEventListener('activate', (event) => {
    console.log('🔄 Service Worker 激活中...');
    
    event.waitUntil(
        caches.keys()
            .then((cacheNames) => {
                return Promise.all(
                    cacheNames.map((cacheName) => {
                        if (cacheName !== STATIC_CACHE && cacheName !== DYNAMIC_CACHE) {
                            console.log('🗑️ 删除旧缓存:', cacheName);
                            return caches.delete(cacheName);
                        }
                    })
                );
            })
            .then(() => {
                console.log('✅ 旧缓存清理完成');
                return self.clients.claim();
            })
    );
});

// 拦截网络请求
self.addEventListener('fetch', (event) => {
    const { request } = event;
    const url = new URL(request.url);
    
    // 只处理同源请求
    if (url.origin !== self.location.origin) {
        return;
    }
    
    // 处理API请求
    if (url.pathname.startsWith('/api/')) {
        event.respondWith(handleApiRequest(request));
        return;
    }
    
    // 处理静态资源请求
    if (request.method === 'GET') {
        event.respondWith(handleStaticRequest(request));
        return;
    }
});

/**
 * 处理API请求
 */
async function handleApiRequest(request) {
    try {
        // 尝试从网络获取
        const response = await fetch(request);
        
        // 如果是成功的响应，缓存到动态缓存
        if (response.ok) {
            const cache = await caches.open(DYNAMIC_CACHE);
            cache.put(request, response.clone());
        }
        
        return response;
    } catch (error) {
        console.log('🌐 网络请求失败，尝试从缓存获取:', error);
        
        // 从缓存获取
        const cachedResponse = await caches.match(request);
        if (cachedResponse) {
            return cachedResponse;
        }
        
        // 返回离线页面
        return new Response(
            JSON.stringify({
                success: false,
                message: '网络连接失败，请检查网络设置',
                offline: true
            }), {
                status: 503,
                statusText: 'Service Unavailable',
                headers: {
                    'Content-Type': 'application/json'
                }
            }
        );
    }
}

/**
 * 处理静态资源请求
 */
async function handleStaticRequest(request) {
    try {
        // 首先尝试从缓存获取
        const cachedResponse = await caches.match(request);
        if (cachedResponse) {
            return cachedResponse;
        }
        
        // 缓存中没有，从网络获取
        const response = await fetch(request);
        
        // 如果是成功的响应，缓存到静态缓存
        if (response.ok) {
            const cache = await caches.open(STATIC_CACHE);
            cache.put(request, response.clone());
        }
        
        return response;
    } catch (error) {
        console.log('📦 静态资源获取失败:', error);
        
        // 返回默认响应
        if (request.destination === 'image') {
            return new Response(
                '<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100"><rect width="100" height="100" fill="#f0f0f0"/><text x="50" y="50" text-anchor="middle" dy=".3em" fill="#999">图片加载失败</text></svg>',
                {
                    headers: {
                        'Content-Type': 'image/svg+xml'
                    }
                }
            );
        }
        
        return new Response('资源加载失败', {
            status: 404,
            statusText: 'Not Found'
        });
    }
}

/**
 * 推送通知事件
 */
self.addEventListener('push', (event) => {
    console.log('📱 收到推送通知');
    
    const options = {
        body: event.data ? event.data.text() : '您有新的通知',
        icon: '/images/icon-192x192.png',
        badge: '/images/badge-72x72.png',
        vibrate: [100, 50, 100],
        data: {
            dateOfArrival: Date.now(),
            primaryKey: 1
        },
        actions: [
            {
                action: 'explore',
                title: '查看',
                icon: '/images/checkmark.png'
            },
            {
                action: 'close',
                title: '关闭',
                icon: '/images/xmark.png'
            }
        ]
    };
    
    event.waitUntil(
        self.registration.showNotification('导航网站', options)
    );
});

/**
 * 通知点击事件
 */
self.addEventListener('notificationclick', (event) => {
    console.log('👆 通知被点击:', event.action);
    
    event.notification.close();
    
    if (event.action === 'explore') {
        // 打开网站
        event.waitUntil(
            clients.openWindow('/')
        );
    }
});

/**
 * 后台同步事件
 */
self.addEventListener('sync', (event) => {
    console.log('🔄 后台同步:', event.tag);
    
    if (event.tag === 'background-sync') {
        event.waitUntil(doBackgroundSync());
    }
});

/**
 * 执行后台同步
 */
async function doBackgroundSync() {
    try {
        // 这里可以执行一些后台任务
        console.log('🔄 执行后台同步任务');
        
        // 清理过期缓存
        await cleanExpiredCache();
        
        // 预加载重要资源
        await preloadImportantAssets();
        
    } catch (error) {
        console.error('❌ 后台同步失败:', error);
    }
}

/**
 * 清理过期缓存
 */
async function cleanExpiredCache() {
    const cacheNames = await caches.keys();
    const now = Date.now();
    const maxAge = 7 * 24 * 60 * 60 * 1000; // 7天
    
    for (const cacheName of cacheNames) {
        if (cacheName.startsWith('dynamic-')) {
            const cache = await caches.open(cacheName);
            const requests = await cache.keys();
            
            for (const request of requests) {
                const response = await cache.match(request);
                if (response) {
                    const date = response.headers.get('date');
                    if (date && (now - new Date(date).getTime()) > maxAge) {
                        await cache.delete(request);
                    }
                }
            }
        }
    }
}

/**
 * 预加载重要资源
 */
async function preloadImportantAssets() {
    const cache = await caches.open(STATIC_CACHE);
    const importantAssets = [
        '/css/main.css',
        '/js/device-adapter.js'
    ];
    
    for (const asset of importantAssets) {
        try {
            await cache.add(asset);
        } catch (error) {
            console.log('⚠️ 预加载资源失败:', asset, error);
        }
    }
}

// 监听消息
self.addEventListener('message', (event) => {
    console.log('📨 收到消息:', event.data);
    
    if (event.data && event.data.type === 'SKIP_WAITING') {
        self.skipWaiting();
    }
    
    if (event.data && event.data.type === 'GET_VERSION') {
        event.ports[0].postMessage({
            version: CACHE_NAME,
            staticCache: STATIC_CACHE,
            dynamicCache: DYNAMIC_CACHE
        });
    }
});

console.log('🚀 Service Worker 加载完成');
