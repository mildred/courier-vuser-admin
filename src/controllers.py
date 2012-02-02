import web
import config
import auth
import view
import system

from os.path import join

class Index:        
  def GET(self):
    user, admin = auth.get()
    return view.render.index(user, admin)

class Users:
  def GET(self):
    auth.get()
    try:
      log, userlist = system.call_helper(["userdb"])
      return view.render.users(userlist.strip().split("\n"))
    except Exception as e:
      return view.render.report("Error", e.message)

class NewUser:

  def GET(self):
    auth.get()
    return view.render.new_user()

  def POST(self):
    d = web.input(username = "", password = "", password2 = "")
    if d.password != d.password2:
      return view.render.new_user("Password do not match", **d)

    try:
      log = system.call_helper(["createuser",
        d.username,
        join(config.userdir, d.username),
        config.virt_user,
        config.virt_group], input="%s\n" % d.password)
      return view.render.report("New User", log)
    except Exception as e:
      return view.render.new_user(e.message, **d)
