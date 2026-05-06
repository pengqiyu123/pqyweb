/**
 * 全屏按钮组件
 * 在页面右下角添加一个浮动的全屏切换按钮
 */
(function() {
    // 创建按钮样式
    const style = document.createElement('style');
    style.textContent = `
        .fullscreen-btn {
            position: fixed;
            bottom: 20px;
            right: 20px;
            width: 44px;
            height: 44px;
            border-radius: 50%;
            border: none;
            background: rgba(0, 0, 0, 0.6);
            color: white;
            font-size: 18px;
            cursor: pointer;
            z-index: 99999;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.3);
            transition: all 0.3s ease;
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
        }
        .fullscreen-btn:hover {
            background: rgba(0, 0, 0, 0.8);
            transform: scale(1.1);
        }
        .fullscreen-btn:active {
            transform: scale(0.95);
        }
        .fullscreen-btn svg {
            width: 20px;
            height: 20px;
            fill: currentColor;
        }
        @media (max-width: 480px) {
            .fullscreen-btn {
                bottom: 15px;
                right: 15px;
                width: 40px;
                height: 40px;
            }
        }
    `;
    document.head.appendChild(style);

    // 创建按钮
    const btn = document.createElement('button');
    btn.className = 'fullscreen-btn';
    btn.title = '全屏模式';
    btn.setAttribute('aria-label', '切换全屏');
    
    // 全屏图标
    const expandIcon = `<svg viewBox="0 0 24 24"><path d="M7 14H5v5h5v-2H7v-3zm-2-4h2V7h3V5H5v5zm12 7h-3v2h5v-5h-2v3zM14 5v2h3v3h2V5h-5z"/></svg>`;
    // 退出全屏图标
    const compressIcon = `<svg viewBox="0 0 24 24"><path d="M5 16h3v3h2v-5H5v2zm3-8H5v2h5V5H8v3zm6 11h2v-3h3v-2h-5v5zm2-11V5h-2v5h5V8h-3z"/></svg>`;
    
    btn.innerHTML = expandIcon;

    // 更新图标
    function updateIcon() {
        const isFullscreen = document.fullscreenElement || 
                            document.webkitFullscreenElement || 
                            document.mozFullScreenElement ||
                            document.msFullscreenElement;
        btn.innerHTML = isFullscreen ? compressIcon : expandIcon;
        btn.title = isFullscreen ? '退出全屏' : '全屏模式';
    }

    // 切换全屏
    btn.addEventListener('click', function() {
        if (!document.fullscreenElement && 
            !document.webkitFullscreenElement && 
            !document.mozFullScreenElement &&
            !document.msFullscreenElement) {
            // 进入全屏
            const elem = document.documentElement;
            if (elem.requestFullscreen) {
                elem.requestFullscreen();
            } else if (elem.webkitRequestFullscreen) {
                elem.webkitRequestFullscreen();
            } else if (elem.mozRequestFullScreen) {
                elem.mozRequestFullScreen();
            } else if (elem.msRequestFullscreen) {
                elem.msRequestFullscreen();
            }
        } else {
            // 退出全屏
            if (document.exitFullscreen) {
                document.exitFullscreen();
            } else if (document.webkitExitFullscreen) {
                document.webkitExitFullscreen();
            } else if (document.mozCancelFullScreen) {
                document.mozCancelFullScreen();
            } else if (document.msExitFullscreen) {
                document.msExitFullscreen();
            }
        }
    });

    // 监听全屏变化
    document.addEventListener('fullscreenchange', updateIcon);
    document.addEventListener('webkitfullscreenchange', updateIcon);
    document.addEventListener('mozfullscreenchange', updateIcon);
    document.addEventListener('MSFullscreenChange', updateIcon);

    // 添加到页面
    document.body.appendChild(btn);
})();
