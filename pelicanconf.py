#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

SITENAME = "XMPP"
SITEURL = ""
TIMEZONE = "Europe/Munich"  #Unused (Pelican complains if you don't provide it)
DIRECT_TEMPLATES = ['index']
STATIC_PATHS = [ 'img', 'CNAME' ]
THEME = 'theme'
MD_EXTENSIONS = [ 'codehilite(css_class=highlight)', 'extra' ]
DEFAULT_PAGINATION = 3
