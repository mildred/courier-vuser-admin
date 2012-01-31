import web
import config
import re
import base64

def get():
  auth = web.ctx.env.get('HTTP_AUTHORIZATION')
  authreq = False
  if auth is None:
    authreq = True
  else:
    auth = re.sub('^Basic ','',auth)
    username, password = base64.decodestring(auth).split(':')
    if username == config.admin_login:
      if password != config.admin_pass:
        authreq = True
    else:
      authreq = True
  if authreq:
    web.header('WWW-Authenticate','Basic realm="Authenticate"')
    web.ctx.status = '401 Unauthorized'
    raise web.Unauthorized()
  return username

