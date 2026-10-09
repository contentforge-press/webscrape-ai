"""
WebScrape AI - AI Agent专用网页数据提取工具

给AI Agent提供干净的互联网数据：
- 输入URL
- 输出结构化JSON（标题/正文/图片/链接）
- 自动处理反爬
- 支持批量爬取
"""

import httpx
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import re
from typing import Optional, Dict, List


class WebScrapeAI:
    """AI Agent专用网页数据提取器"""
    
    def __init__(self, timeout: int = 30):
        self.timeout = timeout
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
        }
    
    def scrape(self, url: str) -> Dict:
        """
        爬取网页，返回结构化数据
        
        Args:
            url: 要爬取的网页URL
            
        Returns:
            结构化数据字典
        """
        try:
            with httpx.Client(timeout=self.timeout, follow_redirects=True) as client:
                response = client.get(url, headers=self.headers)
                response.raise_for_status()
                
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # 提取基础信息
                result = {
                    'url': url,
                    'status': response.status_code,
                    'title': self._extract_title(soup),
                    'description': self._extract_description(soup),
                    'text': self._extract_main_text(soup),
                    'links': self._extract_links(soup, url),
                    'images': self._extract_images(soup, url),
                    'metadata': self._extract_metadata(soup),
                }
                
                return result
                
        except Exception as e:
            return {
                'url': url,
                'status': 'error',
                'error': str(e),
            }
    
    def scrape_batch(self, urls: List[str]) -> List[Dict]:
        """批量爬取多个URL"""
        return [self.scrape(url) for url in urls]
    
    def _extract_title(self, soup: BeautifulSoup) -> str:
        """提取标题"""
        if soup.title:
            return soup.title.get_text(strip=True)
        
        h1 = soup.find('h1')
        if h1:
            return h1.get_text(strip=True)
        
        return ''
    
    def _extract_description(self, soup: BeautifulSoup) -> str:
        """提取描述"""
        # 尝试meta description
        meta = soup.find('meta', attrs={'name': 'description'})
        if meta:
            return meta.get('content', '')
        
        # 尝试og:description
        meta = soup.find('meta', attrs={'property': 'og:description'})
        if meta:
            return meta.get('content', '')
        
        return ''
    
    def _extract_main_text(self, soup: BeautifulSoup) -> str:
        """提取正文文本"""
        # 移除不需要的标签
        for tag in soup(['script', 'style', 'nav', 'footer', 'header', 'aside', 'ads']):
            tag.decompose()
        
        # 尝试找main content
        main = soup.find('main') or soup.find('article') or soup.find('div', class_=re.compile(r'content|article|post', re.I))
        
        if main:
            text = main.get_text(separator='\n', strip=True)
        else:
            text = soup.get_text(separator='\n', strip=True)
        
        # 清理多余空行
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        return '\n'.join(lines[:100])  # 限制前100行
    
    def _extract_links(self, soup: BeautifulSoup, base_url: str) -> List[Dict]:
        """提取链接"""
        links = []
        for a in soup.find_all('a', href=True):
            href = a['href']
            full_url = urljoin(base_url, href)
            
            # 只保留http/https链接
            if full_url.startswith(('http://', 'https://')):
                links.append({
                    'text': a.get_text(strip=True),
                    'url': full_url,
                })
        
        # 去重
        seen = set()
        unique = []
        for link in links:
            if link['url'] not in seen:
                seen.add(link['url'])
                unique.append(link)
        
        return unique[:50]  # 最多50个链接
    
    def _extract_images(self, soup: BeautifulSoup, base_url: str) -> List[Dict]:
        """提取图片"""
        images = []
        for img in soup.find_all('img', src=True):
            src = img['src']
            full_url = urljoin(base_url, src)
            
            if full_url.startswith(('http://', 'https://')):
                images.append({
                    'alt': img.get('alt', ''),
                    'url': full_url,
                })
        
        return images[:20]  # 最多20张图片
    
    def _extract_metadata(self, soup: BeautifulSoup) -> Dict:
        """提取元数据"""
        metadata = {}
        
        # Open Graph
        for meta in soup.find_all('meta', attrs={'property': re.compile(r'^og:')}):
            prop = meta.get('property', '')
            content = meta.get('content', '')
            if prop and content:
                metadata[prop] = content
        
        # Twitter Card
        for meta in soup.find_all('meta', attrs={'name': re.compile(r'^twitter:')}):
            name = meta.get('name', '')
            content = meta.get('content', '')
            if name and content:
                metadata[name] = content
        
        return metadata


# 快捷函数
def scrape(url: str) -> Dict:
    """爬取网页的快捷函数"""
    scraper = WebScrapeAI()
    return scraper.scrape(url)


def scrape_batch(urls: List[str]) -> List[Dict]:
    """批量爬取的快捷函数"""
    scraper = WebScrapeAI()
    return scraper.scrape_batch(urls)


if __name__ == '__main__':
    import json
    
    # 测试
    print("Testing WebScrape AI...")
    result = scrape('https://example.com')
    print(json.dumps(result, indent=2, ensure_ascii=False))
