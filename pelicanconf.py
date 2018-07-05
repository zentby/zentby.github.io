#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Yang'
SITENAME = 'Yang Talks'
SITETITLE = 'Yang Talks'
SITEURL = 'https://en.yangtalks.com'
MAIN_MENU = True

THEME = "./theme"
GOOGLE_ANALYTICS = 'UA-84962714-2'

DISQUS_SITENAME = "yangtalks"
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

ROBOTS = 'index, follow'
PATH = 'content'
STATIC_PATHS = ['images', 'static']
EXTRA_PATH_METADATA = {
    'images/favicon.png': {'path': 'favicon.ico'}, 
    'static/CNAME': {'path': 'CNAME'}
    }
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'

TIMEZONE = 'Pacific/Auckland'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Github', 'http://github.com/zentby')

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/zentby/', '<i class="fab fa-linkedin"></i>'),
          ('github', 'https://github.com/zentby', '<i class="fab fa-github"></i>'),
          ('email', 'mailto:zentby@gmail.com', '<i class="far fa-envelope"></i>'))

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
