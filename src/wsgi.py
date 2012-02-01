#!/usr/bin/env python
# See: <http://webpy.org/cookbook/mod_wsgi-apache>

import sys, os
from os.path import abspath, dirname, join

sys.path.insert(0, join(dirname(abspath(__file__)), "..", "override"))
sys.path.insert(0, dirname(abspath(__file__)))

import web, app, config

web.config.debug = False
config.debug = False

application = app.app.wsgifunc()

