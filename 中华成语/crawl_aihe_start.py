#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json
import re
import time

def get_idiom_links():
    """获取所有成语故事链接，从爱鹤失众开始"""
    url = "http://www.hydcd.cn/cy/chengyugushi.htm"
    
    try:
        response = requests.get(url, timeout=10)
        response.encoding = 'gbk'
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 查找所有包含成语故事的链接
        links = []
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            # 查找以gushi/开头且以.htm结尾的链接
            if href.startswith('gushi/') and href.endswith('.htm') and a_tag.get_text(strip=True):
                full_url = f"http://www.hydcd.cn/cy/{href}"
                links.append((a_tag.get_text(strip=True), full_url))
        
        # 保持原始顺序，不去重不排序
        print(f"找到{len(links)}个成语故事链接")
        
        # 找到爱鹤失众的位置，从那里开始
        start_index = 0
        for i, (name, url) in enumerate(links):
            if '爱鹤失众' in name:
                start_index = i
                break
        
        print(f"爱鹤失众在第{start_index + 1}个位置，从这里开始爬取")
        return links[start_index:]  # 从爱鹤失众开始
        
    except Exception as e:
        print(f"获取链接列表失败: {e}")
        return []

def crawl_idiom_story(url):
    """爬取单个成语故事"""
    try:
        response = requests.get(url, timeout=10)
        response.encoding = 'gbk'
        soup = BeautifulSoup(response.text, 'html.parser')
        
        title = soup.find('title')
        if title:
            title_text = title.text.strip()
            idiom_name = title_text.split('的故事')[0]
        else:
            idiom_name = "未知成语"
        
        # 提取故事内容 - 查找特定样式的font标签
        story_content = ""
        story_font = soup.find('font', {'color': '#10102C', 'style': 'font-size: 12pt'})
        if story_font:
            story_content = str(story_font)
        
        if not story_content:
            print(f"警告: {idiom_name} 的故事内容为空")
            return None
        
        return {
            "idiom": idiom_name,
            "story": story_content,
            "source_url": url
        }
        
    except Exception as e:
        print(f"爬取 {url} 失败: {e}")
        return None

def main():
    print("开始爬取成语故事（从爱鹤失众开始）...")
    
    links = get_idiom_links()
    print(f"找到 {len(links)} 个成语故事链接")
    
    if not links:
        print("未找到任何链接，退出")
        return
    
    print(f"将爬取从爱鹤失众开始的全部 {len(links)} 个成语故事")
    
    results = []
    success_count = 0
    
    for i, (idiom_name, url) in enumerate(links, 1):
        print(f"正在爬取 {i}/{len(links)}: {idiom_name}")
        
        result = crawl_idiom_story(url)
        if result:
            results.append(result)
            success_count += 1
            print(f"成功: {result['idiom']}")
        else:
            print(f"失败: {idiom_name}")
        
        time.sleep(1)
        
        # 每爬取50个保存一次备份
        if i % 50 == 0:
            backup_file = f"idiom_stories_aihe_backup_{i}.json"
            with open(backup_file, 'w', encoding='utf-8') as f:
                json.dump(results, f, ensure_ascii=False, indent=2)
            print(f"已保存备份: {backup_file}")
    
    print(f"\n爬取完成！成功: {success_count}/{len(links)}")
    
    output_file = "idiom_stories_aihe.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"结果已保存到: {output_file}")
    print(f"共爬取 {len(results)} 个成语故事")

if __name__ == "__main__":
    main()