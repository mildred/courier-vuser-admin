import os

debug       = False
configdir   = '/etc/courier'
userdir     = '/srv/courier'
virt_user   = 'vmail'
virt_group  = 'vmail'
admin_login = 'admin'
admin_pass  = None

os.environ['COURIER_CONFIG_DIR'] = configdir


