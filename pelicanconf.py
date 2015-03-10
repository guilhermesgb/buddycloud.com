#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

SITEURL = "http://xmpp.org" #Unused (Pelican complains if you don't provide it)
TIMEZONE = "Europe/Munich"  #Unused (Pelican complains if you don't provide it)
SITENAME = "XMPP | The most secure messaging protocol | WebRTC, IOT, Social"
DIRECT_TEMPLATES = ['index']
STATIC_PATHS = [ 'img', 'CNAME' ]
THEME = 'theme'
MD_EXTENSIONS = [ 'codehilite(css_class=highlight)', 'extra' ]
DEFAULT_PAGINATION = 3

import os, sys
sys.path.append(os.path.join(os.getcwd(), "jinjaext"))
from table_of_contents import TableOfContents as TOC

JINJA_FILTERS = {
		  'extract_toc_info' : TOC.extractTableOfContentsInfo,
		  'create_toc' : TOC.createTableOfContents,
		  'add_toc_hooks' : TOC.addTableOfContentsHooks
		}
