import os
from os.path import abspath, join, dirname

debug       = False
configdir   = '/etc/courier'
userdir     = '/srv/courier'
virt_user   = 'vmail'
virt_group  = 'vmail'
admin_login = 'admin'
with open(join(configdir, "webadmin", "password")) as f:
  admin_pass  = f.read().strip()
helper_path = abspath(join(dirname(abspath(__file__)), "..", "bin", "courier-config"))

os.environ['COURIER_CONFIG_DIR'] = configdir


