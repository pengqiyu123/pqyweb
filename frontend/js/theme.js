// 主题切换功能
class ThemeManager {
    constructor() {
        // 首次加载时默认使用深色模式
        this.currentTheme = localStorage.getItem('theme') || 'dark';
        this.init();
    }

    init() {
        this.applyTheme(this.currentTheme);
        this.bindEvents();
    }

    bindEvents() {
        // 绑定主题切换事件
        document.addEventListener('DOMContentLoaded', () => {
            const themeItems = document.querySelectorAll('[data-theme]');
            themeItems.forEach(item => {
                item.addEventListener('click', (e) => {
                    e.preventDefault();
                    const theme = item.getAttribute('data-theme');
                    this.setTheme(theme);
                });
            });
        });
    }

    setTheme(theme) {
        this.currentTheme = theme;
        this.applyTheme(theme);
        localStorage.setItem('theme', theme);
        
        // 更新主题下拉菜单的显示
        this.updateThemeDisplay(theme);
        
        console.log(`🎨 主题已切换为: ${theme}`);
    }

    applyTheme(theme) {
        const html = document.documentElement;
        
        // 移除现有主题
        html.removeAttribute('data-bs-theme');
        
        // 设置新主题
        if (theme !== 'default') {
            html.setAttribute('data-bs-theme', theme);
        }
        
        // 添加主题切换动画
        this.addThemeTransition();
    }

    updateThemeDisplay(theme) {
        const themeDropdown = document.getElementById('themeDropdown');
        if (themeDropdown) {
            const icon = themeDropdown.querySelector('i');
            if (icon) {
                switch (theme) {
                    case 'light':
                        icon.className = 'fas fa-sun';
                        break;
                    case 'dark':
                        icon.className = 'fas fa-moon';
                        break;
                    default:
                        icon.className = 'fas fa-adjust';
                        break;
                }
            }
        }
    }

    addThemeTransition() {
        const body = document.body;
        body.style.transition = 'all 0.3s ease';
        
        // 移除过渡效果
        setTimeout(() => {
            body.style.transition = '';
        }, 300);
    }

    getCurrentTheme() {
        return this.currentTheme;
    }

    // 自动检测系统主题
    detectSystemTheme() {
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            return 'dark';
        }
        return 'light';
    }

    // 跟随系统主题
    followSystemTheme() {
        const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
        
        const handleChange = (e) => {
            if (this.currentTheme === 'default') {
                this.applyTheme(e.matches ? 'dark' : 'light');
            }
        };

        mediaQuery.addListener(handleChange);
        handleChange(mediaQuery);
    }
}

// 初始化主题管理器
const themeManager = new ThemeManager();

// 导出主题管理器（如果使用模块系统）
if (typeof module !== 'undefined' && module.exports) {
    module.exports = ThemeManager;
}
