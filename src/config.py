import os
from os.path import abspath, join, dirname

debug       = False
configdir   = '/etc/courier'
userdir     = '/srv/courier'
localconf   = abspath(join(dirname(abspath(__file__)), "..", "localconf"))
helper_path = abspath(join(dirname(abspath(__file__)), "..", "bin", "courier-config"))

def from_localconf(name, default=None, strip=True):
  try:
    with open(join(localconf, name)) as f:
      s = f.read()
      if strip: s = s.strip()
      return s
  except:
    return default

virt_user   = from_localconf("virt_user",   "vmail")
virt_group  = from_localconf("virt_group",  "vmail")
admin_login = from_localconf("admin_login", "admin")
admin_pass  = from_localconf("admin_pass")


os.environ['COURIER_CONFIG_DIR'] = configdir


