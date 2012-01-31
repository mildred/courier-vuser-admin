#!/usr/bin/env python

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import web
from controlers import *

urls = (
  '/',      'Index')

app = web.application(urls, globals())


if __name__ == "__main__":
  web.config.debug = config.debug
  app.run()
