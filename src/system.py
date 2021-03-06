import subprocess
import config

def gid_for_group(group):
  with open("/etc/group") as f:
    for line in f.readline():
      elems = line.split(":")
      if elems[0] == group:
        return int(elems[2])

def uid_for_user(user):
  with open("/etc/passwd") as f:
    for line in f.readline():
      elems = line.split(":")
      if elems[0] == user:
        return int(elems[2])

def call(args, input=None):
  log = "> " + " ".join(args) + "\n"
  if input:
    stdin = subprocess.PIPE
  else:
    stdin = None
  p = subprocess.Popen(args, stdin=stdin, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  out, err = p.communicate(input=input)
  log += out
  if p.returncode != 0:
    raise Exception("Returned %d:\n> %s\n%s" % (p.returncode, " ".join(args), out))  
  return log, out

def call_helper(args, input=None):
  return call([config.helper_path] + args, input=input)

