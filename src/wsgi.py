#!/usr/bin/env python
# See: <http://webpy.org/cookbook/mod_wsgi-apache>

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import main
import web
import config

web.config.debug = False
config.debug = False

application = artcdn.app.wsgifunc()

