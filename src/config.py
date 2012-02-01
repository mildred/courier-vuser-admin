import os

debug       = False
configdir   = '/etc/courier'
userdir     = '/srv/courier'
virt_user   = 'vmail'
virt_group  = 'vmail'
admin_login = 'admin'
admin_pass  = None
helper_path = os.path.abspath(ospath.join(os.path.dirname(os.path.abspath(__file__)), "..", "bin", "courier-config"))

os.environ['COURIER_CONFIG_DIR'] = configdir


