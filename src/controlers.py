import config
import auth

class Index:        
  def GET(self):
    auth.get()
    return 'You are %s' % user

