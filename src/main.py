#!/usr/bin/env python

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import web
from controllers import *

urls = (
  '/',         'Index',
  '/users',    'Users',
  '/new_user', 'NewUser')

app = web.application(urls, globals())


if __name__ == "__main__":
  web.config.debug = config.debug
  app.run()
