# WebScrape AI

**Give your AI agent clean data from the web. One URL in, structured JSON out. Built for LLMs.**

## Why WebScrape AI?

AI agents need clean data to think. But the web is messy.

- ✅ **One URL in, clean JSON out** - Title, text, links, images
- ✅ **Built for AI agents** - No noise, just structured data
- ✅ **Handles anti-bot** - Real browser headers, follows redirects
- ✅ **Batch mode** - Scrape 100 URLs at once
- ✅ **Zero config** - Install, import, scrape

## Quick Start

```python
from webscrape_ai import scrape

result = scrape('https://example.com')
print(result['title'])    # Page title
print(result['text'])      # Clean main text
print(result['links'])     # All links
```

## Output Format

```json
{
  "url": "https://example.com",
  "status": 200,
  "title": "Example Domain",
  "text": "Example Domain\nThis domain is for use...",
  "links": [{"text": "More info", "url": "https://iana.org"}],
  "images": []
}
```

## Use Cases

- **AI Agents** - Give your LLM real-time web data
- **RAG Systems** - Build knowledge bases from any website
- **Competitive Monitoring** - Track competitors' websites
- **Content Research** - Extract articles and blog posts

## Installation

```bash
pip install -r requirements.txt
```

## Why Not Just BeautifulSoup?

Because you're an AI agent, not a scraping expert.

WebScrape AI handles anti-bot, redirects, main content extraction, and clean output. You just need clean data.

## Star History

If this helps your AI agent, please star the repo! ⭐

## License

MIT
