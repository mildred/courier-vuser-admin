#!/usr/bin/env python

import sys, os
from os.path import abspath, dirname, join

sys.path.insert(0, join(dirname(abspath(__file__)), "..", "override"))
sys.path.insert(0, dirname(abspath(__file__)))

import web, app, config

web.config.debug = config.debug
app.app.run()

