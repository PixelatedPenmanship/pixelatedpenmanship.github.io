"""
Hook to automatically generate a standard RSS 2.0 feed for Pixelated Penmanship blog posts.
Outputs to site/blog/feed_rss_created.xml and site/blog/rss.xml on post_build.
"""

from pathlib import Path
from datetime import datetime, timezone
import xml.etree.ElementTree as ET
import re

def on_post_build(config):
    site_dir = Path(config['site_dir'])
    site_url = config.get('site_url', 'https://pixelpenman.com').rstrip('/')
    site_name = config.get('site_name', 'Pixelated Penmanship')
    site_description = config.get('site_description', 'Where wet nibs meet clean code. Systems engineering, embedded cybersecurity, and the analog craft of fountain pens.')

    posts = []
    for post_html in site_dir.glob('blog/20*/*/*/*/index.html'):
        try:
            text = post_html.read_text(encoding='utf-8')
            
            # Extract H1 or Title
            h1_m = re.search(r'<h1[^>]*>(.*?)</h1>', text, re.DOTALL)
            title = re.sub(r'<[^>]+>', '', h1_m.group(1)).strip() if h1_m else None
            if not title:
                title_m = re.search(r'<title>(.*?)</title>', text)
                title = title_m.group(1).split(' - ')[0].strip() if title_m else 'Article'

            # Extract Date
            date_m = re.search(r'<time datetime=\"([^\"]+)\"', text)
            if date_m:
                date_str = date_m.group(1)
                try:
                    # e.g. 2025-02-26 00:00:00+00:00 or 2025-02-26
                    pub_date = datetime.fromisoformat(date_str)
                except ValueError:
                    pub_date = datetime.now(timezone.utc)
            else:
                pub_date = datetime.now(timezone.utc)

            # Extract Description from meta description
            desc_m = re.search(r'<meta name=\"description\" content=\"([^\"]+)\"', text)
            description = desc_m.group(1).strip() if desc_m else title

            rel_folder = post_html.relative_to(site_dir).parent
            post_url = f"{site_url}/{rel_folder}/"

            posts.append({
                'title': title,
                'date': pub_date,
                'description': description,
                'url': post_url
            })
        except Exception:
            continue

    # Sort descending by date
    posts.sort(key=lambda x: x['date'], reverse=True)

    # Build RSS 2.0 XML
    rss = ET.Element('rss', version='2.0', attrib={'xmlns:atom': 'http://www.w3.org/2005/Atom'})
    channel = ET.SubElement(rss, 'channel')

    ET.SubElement(channel, 'title').text = site_name
    ET.SubElement(channel, 'link').text = f"{site_url}/blog/"
    ET.SubElement(channel, 'description').text = site_description
    ET.SubElement(channel, 'language').text = 'en'
    ET.SubElement(channel, 'lastBuildDate').text = datetime.now(timezone.utc).strftime('%a, %d %b %Y %H:%M:%S GMT')

    atom_link = ET.SubElement(channel, 'atom:link', {
        'href': f"{site_url}/blog/feed_rss_created.xml",
        'rel': 'self',
        'type': 'application/rss+xml'
    })

    for p in posts:
        item = ET.SubElement(channel, 'item')
        ET.SubElement(item, 'title').text = p['title']
        ET.SubElement(item, 'link').text = p['url']
        ET.SubElement(item, 'guid', isPermaLink='true').text = p['url']
        ET.SubElement(item, 'description').text = p['description']
        ET.SubElement(item, 'pubDate').text = p['date'].strftime('%a, %d %b %Y %H:%M:%S GMT')

    tree = ET.ElementTree(rss)
    ET.indent(tree, space='  ')

    blog_site_dir = site_dir / 'blog'
    blog_site_dir.mkdir(parents=True, exist_ok=True)
    
    feed_path = blog_site_dir / 'feed_rss_created.xml'
    rss_path = blog_site_dir / 'rss.xml'
    
    tree.write(feed_path, encoding='utf-8', xml_declaration=True)
    tree.write(rss_path, encoding='utf-8', xml_declaration=True)
