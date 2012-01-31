import os
import subprocess

def userdbpw(password, method=None):
  args = ["userdbpw"]
  if method == "md5":
    args.append("-md5")
  elif method == "hmac-md5":
    args.append("-hmac-md5")
  p = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
  res, _ = p.communicate(input=password + "\n")
  p.wait()
  return res.strip()

def call(args):
  log = "> " + " ".join(args) + "\n"
  log += subprocess.check_output(args)
  return log

def create_home(home, uid, gid):
  log = "Create directory %s\n" % home
  os.makedirs(home)
  log += call(["maildirmake", os.path.join(home, "Maildir")])
  log += call(["touch", os.path.join(home, ".courier")])
  log += call(["touch", os.path.join(home, ".courier-default")])
  log += call(["chown", "%s:%s" % (uid, gid), home])
  return log

