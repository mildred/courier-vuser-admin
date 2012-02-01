#!/usr/bin/env python

import web
from controllers import *

urls = (
  '/',         'Index',
  '/users',    'Users',
  '/new_user', 'NewUser')

app = web.application(urls, globals())

