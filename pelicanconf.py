#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Paul Salden'
SITENAME = u'paulsalden.com'
SITEURL = 'https://paulsalden.com'

PATH = 'content'

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('pwnagedeluxe.nl', 'https://pwnagedeluxe.nl/'),)

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'

PLUGINS = ['tipue_search', 'render_math']

DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')
