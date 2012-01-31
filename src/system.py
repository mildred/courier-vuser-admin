import subprocess

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

def call(args):
  log = "> " + " ".join(args) + "\n"
  log += subprocess.check_output(args)
  return log
