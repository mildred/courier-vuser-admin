import web
import config
import re
import base64

def get(admin=True):
  auth = web.ctx.env.get('HTTP_AUTHORIZATION')
  authreq = False
  isAdmin = False
  if auth is None:
    authreq = "You need to authenticate"
  else:
    auth = re.sub('^Basic ','',auth)
    username, password = base64.decodestring(auth).split(':')
    if username == config.admin_login:
      if password != config.admin_pass:
        authreq = "Wrong admin password"
      else:
        isAdmin = True
    else:
      authreq = "Unable to login with %s" % username
  if authreq or (admin and not isAdmin):
    web.header('WWW-Authenticate', 'Basic realm="%s"' % authreq)
    web.ctx.status = '401 Unauthorized'
    raise web.Unauthorized()
  return username, isAdmin

