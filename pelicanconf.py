#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Christian Seyda'
SITENAME = 'My blog'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['static']

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('linkedin', 'https://de.linkedin.com/in/christian-seyda-73b37ba3'),
          ('github', 'https://github.com/cseyda'),
          ('twitter', 'https://twitter.com/ChristianSeyda'))

DEFAULT_PAGINATION = False

TYPOGRIFY = True
# Pelican settings
THEME = '/home/seydanator/pelican-themes/pelican-blue/'
SIDEBAR_DIGEST = 'Programmer and Web Developer'
FAVICON = 'url-to-favicon'
DISPLAY_PAGES_ON_MENU = True
TWITTER_USERNAME = 'ChristianSeyda'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
