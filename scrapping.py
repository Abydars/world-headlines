# import libraries

import requests
import json
from bs4 import BeautifulSoup

structs = [
    {
        'url': 'https://www.bbc.com/news',
        'heading': 'div.nw-c-top-stories__primary-item h3.gs-c-promo-heading__title',
        'content': 'div.nw-c-top-stories__primary-item p.gs-c-promo-summary',
        'link': 'div.nw-c-top-stories__primary-item a.gs-c-promo-heading',
        'image': 'div.nw-c-top-stories__primary-item div.gs-c-promo-image img',
        'ref': 'BBC News'
    },
    {
        'url': 'https://dunyanews.tv/',
        'heading': 'div.top_story div.ovrtexts p',
        'content': '',
        'link': 'div.top_story a',
        'image': 'div.top_story img',
        'ref': 'Dunya News'
    },
    {
        'url': 'https://www.dawn.com/',
        'heading': 'article.box.story h2.story__title a',
        'content': 'article.box.story .story__excerpt',
        'link': 'article.box.story h2.story__title a',
        'image': 'article.box.story .media__item img',
        'ref': 'Dawn News'
    },
    {
        'url': 'https://www.businessplustv.pk/',
        'heading': 'div.features-video-box .hover-box h2 a',
        'content': '',
        'link': 'div.features-video-box .hover-box h2 a',
        'image': 'div.features-video-box div.thumb-wrap img',
        'ref': 'Business Plus Tv'
    },
    {
        'url': 'https://www.news18.com/',
        'heading': 'div.lead-story .lstory-top h1',
        'content': '',
        'link': 'div.lead-story .lstory-top a',
        'image': 'div.lead-story .lstory-top img',
        'ref': 'News18'
    },
    {
        'url': 'https://www.aljazeera.com/',
        'heading': 'div#queen-is-dead-page h1 a.queen-top-sec-title',
        'content': 'div#queen-is-dead-page p.queen-top-desc',
        'link': 'div#queen-is-dead-page h1 a.queen-top-sec-title',
        'image': '',
        'ref': 'Al Jazeera'
    }
]

data = []

for struct in structs:
    page = requests.get(struct['url'], timeout=5)
    soup = BeautifulSoup(page.content, 'html.parser')

    heading = soup.select_one(struct['heading']).text if struct['heading'] != '' else ''
    content = soup.select_one(struct['content']).text if struct['content'] != '' else ''
    link = struct['url']+soup.select_one(struct['link'])['href'] if struct['link'] != '' else ''
    image = soup.select_one(struct['image'])['src'] if struct['image'] != '' else ''

    data.append({
        'heading': heading.strip(),
        'content': content.strip(),
        'link': link,
        'image': image,
        'reference': struct['ref']
        })

print(json.dumps(data))