# WebScrape AI

**Give your AI agent clean data from the entire internet.**

One line of code. Any URL. Structured JSON back. Built for AI agents.

## Why WebScrape AI?

AI agents need clean data to think. But the internet is messy.

- ✅ **One URL in, clean JSON out** - Title, main text, links, images, metadata
- ✅ **Built for AI agents** - No noise, just structured data
- ✅ **Handles anti-bot** - Real browser headers, follows redirects
- ✅ **Batch mode** - Scrape 100 URLs at once
- ✅ **Zero config** - Install, import, scrape

## Quick Start

```python
from webscrape_ai import scrape

# Scrape any URL
result = scrape('https://example.com')

print(result['title'])        # Page title
print(result['text'])          # Clean main text
print(result['links'])         # All links
print(result['images'])        # All images
```

## Output Format

```json
{
  "url": "https://example.com",
  "status": 200,
  "title": "Example Domain",
  "description": "This domain is for use in illustrative examples...",
  "text": "Example Domain\nThis domain is for use in illustrative examples...",
  "links": [
    {
      "text": "More information...",
      "url": "https://www.iana.org/domains/example"
    }
  ],
  "images": [],
  "metadata": {
    "og:title": "Example Domain",
    "og:description": "This domain is for use..."
  }
}
```

## Batch Scraping

```python
from webscrape_ai import scrape_batch

urls = [
    'https://example.com',
    'https://google.com',
    'https://github.com'
]

results = scrape_batch(urls)
```

## Use Cases

- **AI Agents** - Give your LLM real-time web data
- **RAG Systems** - Build knowledge bases from any website
- **Competitive Monitoring** - Track competitors' websites
- **Content Research** - Extract articles and blog posts
- **Data Pipelines** - Feed structured data to your workflows

## Installation

```bash
pip install -r requirements.txt
```

## Why Not Just Use BeautifulSoup?

Because you're an AI agent, not a web scraping expert.

WebScrape AI handles:
- ✅ Anti-bot detection (real browser headers)
- ✅ Redirect following
- ✅ Main content extraction (strips nav/footer/ads)
- ✅ Clean text output (no garbage)
- ✅ Structured JSON (ready for LLMs)

You just need one thing: clean data. We handle the rest.

## Star History

If this helps your AI agent, please star the repo! ⭐

## License

MIT
