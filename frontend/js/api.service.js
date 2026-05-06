// API服务管理
class ApiService {
    constructor() {
        this.baseURL = window.location.origin;
        this.apiVersion = 'v1';
        this.init();
    }

    init() {
        // 检查API连接状态
        this.checkApiHealth();
    }

    // 检查API健康状态
    async checkApiHealth() {
        try {
            const response = await fetch(`${this.baseURL}/api/health`);
            if (response.ok) {
                const data = await response.json();
                console.log('✅ API服务正常:', data);
                return true;
            }
        } catch (error) {
            console.warn('⚠️ API服务不可用:', error.message);
            return false;
        }
    }

    // 通用请求方法
    async request(endpoint, options = {}) {
        const url = `${this.baseURL}${endpoint}`;
        const defaultOptions = {
            headers: {
                'Content-Type': 'application/json',
            },
            ...options
        };

        try {
            const response = await fetch(url, defaultOptions);
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            return await response.json();
        } catch (error) {
            console.error('API请求失败:', error);
            throw error;
        }
    }

    // GET请求
    async get(endpoint, params = {}) {
        const queryString = new URLSearchParams(params).toString();
        const url = queryString ? `${endpoint}?${queryString}` : endpoint;
        
        return this.request(url, { method: 'GET' });
    }

    // POST请求
    async post(endpoint, data = {}) {
        return this.request(endpoint, {
            method: 'POST',
            body: JSON.stringify(data)
        });
    }

    // PUT请求
    async put(endpoint, data = {}) {
        return this.request(endpoint, {
            method: 'PUT',
            body: JSON.stringify(data)
        });
    }

    // DELETE请求
    async delete(endpoint) {
        return this.request(endpoint, { method: 'DELETE' });
    }

    // 用户认证相关API
    async login(credentials) {
        return this.post('/api/auth/login', credentials);
    }

    async register(userData) {
        return this.post('/api/auth/register', userData);
    }

    async logout() {
        return this.post('/api/auth/logout');
    }

    // 用户信息相关API
    async getUserProfile() {
        return this.get('/api/users/profile');
    }

    async updateUserProfile(profileData) {
        return this.put('/api/users/profile', profileData);
    }

    // 文件相关API
    async uploadFile(file, onProgress) {
        const formData = new FormData();
        formData.append('file', file);

        return this.request('/api/files/upload', {
            method: 'POST',
            body: formData,
            headers: {
                // 不设置Content-Type，让浏览器自动设置
            }
        });
    }

    async getFiles() {
        return this.get('/api/files');
    }

    async deleteFile(fileId) {
        return this.delete(`/api/files/${fileId}`);
    }

    // 工具相关API
    async getTools() {
        return this.get('/api/tools');
    }

    async getToolById(toolId) {
        return this.get(`/api/tools/${toolId}`);
    }

    // 音乐相关API
    async getMusicSites() {
        return this.get('/api/music/sites');
    }

    async searchMusic(query) {
        return this.get('/api/music/search', { q: query });
    }

    // 搜索相关API
    async searchSite(query) {
        return this.get('/api/search', { q: query });
    }

    // 统计相关API
    async getSiteStats() {
        return this.get('/api/stats');
    }

    async logPageView(page) {
        return this.post('/api/stats/pageview', { page });
    }

    // 错误处理
    handleError(error, context = '') {
        console.error(`API错误 [${context}]:`, error);
        
        // 可以在这里添加全局错误处理逻辑
        // 例如：显示错误提示、记录错误日志等
        
        return {
            success: false,
            error: error.message,
            context
        };
    }

    // 设置认证token
    setAuthToken(token) {
        if (token) {
            localStorage.setItem('authToken', token);
        } else {
            localStorage.removeItem('authToken');
        }
    }

    // 获取认证token
    getAuthToken() {
        return localStorage.getItem('authToken');
    }

    // 检查是否已认证
    isAuthenticated() {
        return !!this.getAuthToken();
    }

    // 添加认证头到请求
    addAuthHeader(options = {}) {
        const token = this.getAuthToken();
        if (token) {
            options.headers = {
                ...options.headers,
                'Authorization': `Bearer ${token}`
            };
        }
        return options;
    }
}

// 初始化API服务
const apiService = new ApiService();

// 导出API服务（如果使用模块系统）
if (typeof module !== 'undefined' && module.exports) {
    module.exports = ApiService;
}
