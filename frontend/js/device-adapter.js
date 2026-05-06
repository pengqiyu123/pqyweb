/**
 * 设备适配和优化模块
 */

class DeviceAdapter {
    constructor() {
        this.deviceInfo = this.detectDevice();
        this.init();
    }

    detectDevice() {
        const userAgent = navigator.userAgent;
        return {
            isMobile: /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(userAgent),
            isTablet: /iPad|Android(?=.*\bMobile\b)(?=.*\bSafari\b)/i.test(userAgent),
            isDesktop: !(/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(userAgent)),
            isIOS: /iPad|iPhone|iPod/.test(userAgent),
            isAndroid: /Android/.test(userAgent),
            isTouch: 'ontouchstart' in window || navigator.maxTouchPoints > 0,
            screenWidth: window.screen.width,
            screenHeight: window.screen.height,
            pixelRatio: window.devicePixelRatio || 1,
            viewportWidth: window.innerWidth,
            viewportHeight: window.innerHeight
        };
    }

    init() {
        console.log('🔧 设备适配初始化:', this.deviceInfo);
        this.setDeviceClasses();
        if (this.deviceInfo.isTouch) {
            this.optimizeTouch();
        }
        this.handleResize();
    }

    setDeviceClasses() {
        const body = document.body;
        if (this.deviceInfo.isMobile) {
            body.classList.add('device-mobile');
        } else if (this.deviceInfo.isTablet) {
            body.classList.add('device-tablet');
        } else {
            body.classList.add('device-desktop');
        }
        if (this.deviceInfo.isTouch) {
            body.classList.add('touch-device');
        }
    }

    optimizeTouch() {
        let lastTouchEnd = 0;
        document.addEventListener('touchend', (event) => {
            const now = (new Date()).getTime();
            if (now - lastTouchEnd <= 300) {
                event.preventDefault();
            }
            lastTouchEnd = now;
        }, false);
    }

    handleResize() {
        window.addEventListener('resize', () => {
            this.updateLayout();
        });
    }

    updateLayout() {
        const width = window.innerWidth;
        if (width <= 768) {
            const sidebar = document.querySelector('.site-aside');
            if (sidebar) {
                sidebar.style.display = 'none';
            }
        }
    }
}

window.deviceAdapter = new DeviceAdapter();
