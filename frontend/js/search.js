// 搜索功能管理
class SearchManager {
    constructor() {
        this.searchEngines = {
            'baidu': {
                name: '百度',
                url: 'https://www.baidu.com/s?wd=',
                icon: 'fas fa-search'
            },
            'bing': {
                name: 'Bing',
                url: 'https://www.bing.com/search?q=',
                icon: 'fas fa-search'
            },
            'google': {
                name: 'Google',
                url: 'https://www.google.com/search?q=',
                icon: 'fas fa-search'
            },
            'site': {
                name: '站内',
                url: '#',
                icon: 'fas fa-home'
            }
        };
        
        this.currentEngine = 'baidu';
        this.init();
    }

    init() {
        this.bindEvents();
        this.updateEngineDisplay();
    }

    bindEvents() {
        document.addEventListener('DOMContentLoaded', () => {
            const searchInput = document.getElementById('searchInput');
            const searchButton = document.getElementById('searchButton');
            const searchEngineDropdown = document.getElementById('searchEngine');
            
            if (searchButton && searchInput) {
                // 搜索按钮点击事件
                searchButton.addEventListener('click', () => {
                    this.performSearch();
                });
                
                // 回车搜索
                searchInput.addEventListener('keypress', (e) => {
                    if (e.key === 'Enter') {
                        this.performSearch();
                    }
                });
                
                // 搜索框输入事件
                searchInput.addEventListener('input', (e) => {
                    this.handleSearchInput(e.target.value);
                });
            }
            
            // 搜索引擎切换事件
            if (searchEngineDropdown) {
                const engineItems = searchEngineDropdown.querySelectorAll('.dropdown-item');
                engineItems.forEach(item => {
                    item.addEventListener('click', (e) => {
                        e.preventDefault();
                        const engine = item.getAttribute('data-engine');
                        this.switchEngine(engine);
                    });
                });
            }
        });
    }

    switchEngine(engine) {
        if (this.searchEngines[engine]) {
            this.currentEngine = engine;
            this.updateEngineDisplay();
            console.log(`🔍 搜索引擎已切换为: ${this.searchEngines[engine].name}`);
        }
    }

    updateEngineDisplay() {
        const searchEngineDropdown = document.getElementById('searchEngine');
        if (searchEngineDropdown) {
            const engine = this.searchEngines[this.currentEngine];
            const icon = searchEngineDropdown.querySelector('i');
            const text = searchEngineDropdown.querySelector('span') || document.createElement('span');
            
            if (icon) {
                icon.className = engine.icon;
            }
            
            if (!searchEngineDropdown.querySelector('span')) {
                searchEngineDropdown.appendChild(text);
            }
            
            text.textContent = engine.name;
        }
    }

    performSearch() {
        const searchInput = document.getElementById('searchInput');
        const query = searchInput.value.trim();
        
        if (!query) {
            this.showSearchError('请输入搜索内容');
            return;
        }
        
        if (this.currentEngine === 'site') {
            this.performSiteSearch(query);
        } else {
            this.performExternalSearch(query);
        }
    }

    performExternalSearch(query) {
        const engine = this.searchEngines[this.currentEngine];
        const searchUrl = engine.url + encodeURIComponent(query);
        
        // 在新标签页中打开搜索结果
        window.open(searchUrl, '_blank');
        
        // 记录搜索历史
        this.saveSearchHistory(query, this.currentEngine);
        
        console.log(`🔍 使用 ${engine.name} 搜索: ${query}`);
    }

    performSiteSearch(query) {
        // 站内搜索功能（可以扩展为搜索本地内容）
        console.log(`🏠 站内搜索: ${query}`);
        
        // 这里可以添加站内搜索逻辑
        // 例如：搜索工具名称、音乐网站等
        this.searchLocalContent(query);
    }

    searchLocalContent(query) {
        // 简单的站内搜索实现
        const searchResults = [];
        const searchableElements = document.querySelectorAll('.tool-name, .nav-link-card span');
        
        searchableElements.forEach(element => {
            const text = element.textContent.toLowerCase();
            if (text.includes(query.toLowerCase())) {
                // 高亮搜索结果
                element.style.backgroundColor = '#ffeb3b';
                element.style.color = '#333';
                
                // 滚动到搜索结果
                element.scrollIntoView({ behavior: 'smooth', block: 'center' });
                
                searchResults.push(element.textContent);
            }
        });
        
        if (searchResults.length > 0) {
            this.showSearchResults(searchResults);
        } else {
            this.showSearchError('未找到相关内容');
        }
    }

    handleSearchInput(value) {
        // 实时搜索建议（可以扩展）
        if (value.length > 2) {
            // 这里可以添加搜索建议功能
            console.log(`💡 搜索建议: ${value}`);
        }
    }

    showSearchResults(results) {
        // 显示搜索结果提示
        const message = `找到 ${results.length} 个相关结果`;
        this.showMessage(message, 'success');
    }

    showSearchError(message) {
        this.showMessage(message, 'error');
    }

    showMessage(message, type) {
        // 创建消息提示
        const messageDiv = document.createElement('div');
        messageDiv.className = `alert alert-${type === 'error' ? 'danger' : 'success'} alert-dismissible fade show`;
        messageDiv.style.position = 'fixed';
        messageDiv.style.top = '100px';
        messageDiv.style.right = '20px';
        messageDiv.style.zIndex = '9999';
        messageDiv.style.minWidth = '300px';
        
        messageDiv.innerHTML = `
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;
        
        document.body.appendChild(messageDiv);
        
        // 自动隐藏消息
        setTimeout(() => {
            if (messageDiv.parentNode) {
                messageDiv.remove();
            }
        }, 3000);
    }

    saveSearchHistory(query, engine) {
        // 保存搜索历史到本地存储
        const history = JSON.parse(localStorage.getItem('searchHistory') || '[]');
        const searchRecord = {
            query,
            engine,
            timestamp: new Date().toISOString()
        };
        
        // 添加到历史记录开头
        history.unshift(searchRecord);
        
        // 限制历史记录数量
        if (history.length > 50) {
            history.splice(50);
        }
        
        localStorage.setItem('searchHistory', JSON.stringify(history));
    }

    getSearchHistory() {
        return JSON.parse(localStorage.getItem('searchHistory') || '[]');
    }

    clearSearchHistory() {
        localStorage.removeItem('searchHistory');
        console.log('🗑️ 搜索历史已清空');
    }
}

// 初始化搜索管理器
const searchManager = new SearchManager();

// 导出搜索管理器（如果使用模块系统）
if (typeof module !== 'undefined' && module.exports) {
    module.exports = SearchManager;
}
