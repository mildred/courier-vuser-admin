from os import path
from generic_config import get_config_contents


class UserDB:
  def __init__(self, configdir):
    self.configdir = configdir
    self.config = path.join(configdir, "userdb")
    self.readdb()
    if not path.isdir(self.config):
      raise Exception("%s should be a directory" % self.config)
  
  def __contains__(self, username):
    return username in self.users
  
  def readdb(self):
    content = get_config_contents(self.config)
    self.users = {}
    for line in content.splitlines():
      user, _, args = line.partition("\t")
      if user:
        params = {}
        for arg in args.split("|"):
          key, _, val = arg.partition("=")
          params[key] = val
        self.users[user] = params
    return self.users
  
  def create(self, username, params):
    fn = path.join(self.config, username)
    if path.exists(fn):
      raise Exception("File %s exists" % fn)
    content = "%s\t%s\n" % (username, "|".join(["%s=%s" % (k, params[k]) for k in params]))
    with open(fn, 'w') as f:
      f.write(content)
    self.users[username] = params
    return "Write file %s:\n%s" % (fn, content)
