import web
import config
import auth
import view
import system
import courier

from courier.userdb import UserDB
from os import path

class Index:        
  def GET(self):
    user, admin = auth.get()
    return view.render.index(user, admin)

class NewUser:
  def GET(self):
    auth.get()
    return view.render.new_user()
  def POST(self):
    d = web.input(username = "", password = "", password2 = "")
    if d.password != d.password2:
      return view.render.new_user("Password do not match", **d)
    db = UserDB(config.configdir)
    if d.username in db:
      return view.render.new_user("Username %s exists" % d.username, **d)
    params = {}
    params['uid'] = system.uid_for_user(config.virt_user)
    params['gid'] = system.uid_for_user(config.virt_group)
    params['home']= path.join(config.userdir, d.username)
    params['systempw']  = courier.userdbpw(d.password, "md5")
    params['hmac-md5pw']= courier.userdbpw(d.password, "hmac-md5")
    log = courier.create_home(params['home'], config.virt_user, config.virt_group)
    log += db.create(d.username, params)
    log += system.call(["makeuserdb"])
    return view.render.report("New User", log)
