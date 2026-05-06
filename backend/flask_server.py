#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
后缀名转换工具Flask服务器
"""

from flask import Flask, request, jsonify, send_file, render_template_string
from flask_cors import CORS
import os
import tempfile
import threading
import time
from pathlib import Path
from suffix_converter import get_converter
import logging

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)  # 允许跨域请求

# 响应头中间件
@app.after_request
def add_security_headers(response):
    # 添加基本安全头
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    return response

# 添加静态文件服务
@app.route('/frontend/<path:filename>')
def serve_frontend(filename):
    """提供前端文件服务"""
    try:
        frontend_dir = Path("../frontend")
        file_path = frontend_dir / filename
        if file_path.exists() and file_path.is_file():
            return send_file(str(file_path))
        else:
            return "文件未找到", 404
    except Exception as e:
        return f"错误: {str(e)}", 500

# 添加CSS和JS文件服务
@app.route('/css/<path:filename>')
def serve_css(filename):
    """提供CSS文件服务"""
    try:
        css_dir = Path("../frontend/css")
        file_path = css_dir / filename
        if file_path.exists() and file_path.is_file():
            return send_file(str(file_path), mimetype='text/css')
        else:
            return "CSS文件未找到", 404
    except Exception as e:
        return f"错误: {str(e)}", 500

@app.route('/js/<path:filename>')
def serve_js(filename):
    """提供JS文件服务"""
    try:
        js_dir = Path("../frontend/js")
        file_path = js_dir / filename
        if file_path.exists() and file_path.is_file():
            return send_file(str(file_path), mimetype='application/javascript')
        else:
            return "JS文件未找到", 404
    except Exception as e:
        return f"错误: {str(e)}", 500

@app.route('/images/<path:filename>')
def serve_images(filename):
    """提供图片文件服务"""
    try:
        images_dir = Path("../frontend/images")
        file_path = images_dir / filename
        if file_path.exists() and file_path.is_file():
            return send_file(str(file_path))
        else:
            return "图片文件未找到", 404
    except Exception as e:
        return f"错误: {str(e)}", 500

@app.route('/um-web/<path:filename>')
def serve_um_web(filename):
    try:
        um_dir = Path("../um-web.legacy.v1.10.8")
        file_path = um_dir / filename
        if file_path.exists() and file_path.is_file():
            return send_file(str(file_path))
        else:
            return "文件未找到", 404
    except Exception as e:
        return f"错误: {str(e)}", 500

# 获取转换器实例
converter = get_converter()

@app.route('/')
def index():
    """主页 - 显示前端页面"""
    try:
        # 读取前端页面文件
        frontend_path = Path("../frontend/index.html")
        if frontend_path.exists():
            with open(frontend_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return content
        else:
            # 如果文件不存在，返回默认页面
            return render_template_string('''
            <!DOCTYPE html>
            <html>
            <head>
                <title>后缀名转换工具</title>
                <meta charset="utf-8">
            </head>
            <body>
                <h1>后缀名转换工具</h1>
                <p>前端页面文件未找到，请检查 frontend/index.html 是否存在</p>
                <p>当前路径: {}</p>
            </body>
            </html>
            '''.format(frontend_path.absolute()))
    except Exception as e:
        return f"<h1>错误</h1><p>无法加载前端页面: {str(e)}</p>"

@app.route('/api/convert-suffix', methods=['POST'])
def convert_suffix():
    """处理文件后缀名转换请求"""
    try:
        # 检查是否有文件上传
        if 'files' not in request.files:
            return jsonify({
                'success': False,
                'message': '没有文件上传'
            }), 400
        
        files = request.files.getlist('files')
        if not files or files[0].filename == '':
            return jsonify({
                'success': False,
                'message': '没有选择文件'
            }), 400
        
        # 获取参数
        target_extension = request.form.get('target_extension', 'txt')
        preserve_original = request.form.get('preserve_original', 'true').lower() == 'true'
        
        # 验证目标后缀名
        if not target_extension or len(target_extension) > 10:
            return jsonify({
                'success': False,
                'message': '无效的目标后缀名'
            }), 400
        
        # 保存上传的文件
        saved_files = []
        upload_dir = Path("uploads")
        upload_dir.mkdir(exist_ok=True)
        
        for file in files:
            if file.filename:
                # 生成安全的文件名
                safe_filename = f"{int(time.time())}_{file.filename}"
                file_path = upload_dir / safe_filename
                
                # 保存文件
                file.save(str(file_path))
                saved_files.append(str(file_path))
                
                logger.info(f"文件上传成功: {file.filename} -> {file_path}")
        
        if not saved_files:
            return jsonify({
                'success': False,
                'message': '文件保存失败'
            }), 500
        
        # 创建转换任务
        conversion_id = converter.create_conversion_task(
            files=saved_files,
            target_extension=target_extension,
            preserve_original=preserve_original
        )
        
        # 在后台线程中处理转换
        def process_in_background():
            try:
                converter.process_conversion(conversion_id)
            except Exception as e:
                logger.error(f"后台转换失败: {e}")
        
        thread = threading.Thread(target=process_in_background)
        thread.daemon = True
        thread.start()
        
        return jsonify({
            'success': True,
            'conversion_id': conversion_id,
            'message': '转换任务已创建，正在处理中'
        })
        
    except Exception as e:
        logger.error(f"转换请求处理失败: {e}")
        return jsonify({
            'success': False,
            'message': f'服务器错误: {str(e)}'
        }), 500

@app.route('/api/conversion-status/<conversion_id>')
def get_conversion_status(conversion_id):
    """获取转换任务状态"""
    try:
        status = converter.get_conversion_status(conversion_id)
        return jsonify(status)
    except Exception as e:
        logger.error(f"获取转换状态失败: {e}")
        return jsonify({
            'success': False,
            'message': f'获取状态失败: {str(e)}'
        }), 500

@app.route('/download/<conversion_id>')
def download_result(conversion_id):
    """下载转换结果"""
    try:
        status = converter.get_conversion_status(conversion_id)
        
        if not status['success'] or status['status'] != 'completed':
            return jsonify({
                'success': False,
                'message': '转换任务未完成或不存在'
            }), 404
        
        # 获取输出文件路径
        conversion = converter.conversions[conversion_id]
        output_path = conversion.get('output_path')
        
        if not output_path or not os.path.exists(output_path):
            return jsonify({
                'success': False,
                'message': '输出文件不存在'
            }), 404
        
        # 发送文件
        filename = os.path.basename(output_path)
        return send_file(
            output_path,
            as_attachment=True,
            download_name=filename,
            mimetype='application/zip'
        )
        
    except Exception as e:
        logger.error(f"下载文件失败: {e}")
        return jsonify({
            'success': False,
            'message': f'下载失败: {str(e)}'
        }), 500

@app.route('/api/health')
def health_check():
    """健康检查"""
    return jsonify({
        'status': 'OK',
        'service': 'suffix-converter',
        'timestamp': time.time(),
        'active_conversions': len(converter.conversions)
    })

@app.route('/api/cleanup/<conversion_id>', methods=['DELETE'])
def cleanup_conversion(conversion_id):
    """清理转换任务"""
    try:
        converter.cleanup_conversion(conversion_id)
        return jsonify({
            'success': True,
            'message': '转换任务已清理'
        })
    except Exception as e:
        logger.error(f"清理转换任务失败: {e}")
        return jsonify({
            'success': False,
            'message': f'清理失败: {str(e)}'
        }), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'message': '接口不存在'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        'success': False,
        'message': '服务器内部错误'
    }), 500

if __name__ == '__main__':
    # 创建必要的目录
    os.makedirs("uploads", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)
    
    print("🚀 后缀名转换工具API服务启动中...")
    print("📁 上传目录: uploads/")
    print("📁 输出目录: outputs/")
    print("🌐 服务地址: http://localhost:5000")
    print("📋 API文档:")
    print("   POST /api/convert-suffix - 上传文件并开始转换")
    print("   GET  /api/conversion-status/{id} - 查询转换状态")
    print("   GET  /download/{id} - 下载转换结果")
    print("   GET  /api/health - 健康检查")
    print("   DELETE /api/cleanup/{id} - 清理转换任务")
    
    # 启动Flask服务器
    app.run(
        host='0.0.0.0',  # 允许外部访问
        port=5000,
        debug=False,  # 生产环境设置为False
        threaded=True  # 启用多线程
    )
