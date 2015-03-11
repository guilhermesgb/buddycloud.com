#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

SITENAME = "XMPP"
SITEURL = ""
TIMEZONE = "Europe/Paris"  #Unused (Pelican complains if you don't provide it)
DEFAULT_LANG = "en"

DEFAULT_METADATA = [
  ('top_menu_show', 'false'),
  ('top_menu_order', '-1'),
  ('dropdown_menu_show', 'false'),
  ('dropdown_menu_size', '0'),
  ('footer_show', 'false'),
  ('footer_order', '-1'),
  ('content_layout', 'single-column'),
  ('is_blog', 'false'),
]

STATIC_PATHS = [ 'CNAME' ]

ARTICLE_PATHS = [ 'posts/blog', 'posts/learn' ]
ARTICLE_URL = 'posts/{blog_id}/{date:%Y}/{date:%b}/{date:%d}/{slug}'
ARTICLE_SAVE_AS = 'posts/{blog_id}/{date:%Y}/{date:%b}/{date:%d}/{slug}.html'

USE_FOLDER_AS_CATEGORY = False
DEFAULT_PAGINATION = 5
#DIRECT_TEMPLATES = [ 'page', 'categories', 'authors', 'archives' ]
#PAGINATED_DIRECT_TEMPLATES = [ 'page' ]

THEME = "theme"

MD_EXTENSIONS = [ 'codehilite(css_class=highlight)', 'extra' ]
