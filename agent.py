#!/home/lowkeyshift/Documents/yt_videos/Python/real_world_python_tuts/venv/bin/python3

import grp, os, pwd, socket, sys, time
from host_scan import HostScan as hs
from disk_scan import DiskScan as ds
from signal import signal, SIGINT, SIGTERM
from sys import exit

def drop_privileges(uid='nobody', gid='nogroup'):
    if os.getuid() != 0:
        return

    running_uid = pwd.getpwnam(uid).pw_uid
    running_gid = grp.getgrnam(gid).gr_gid

    os.initgroups(uid, running_gid)

    os.setgid(running_gid)
    os.setuid(running_uid)

    old_umask = os.umask(0o77)

def get_shutdown_handler(message=None):
    def handler(signum, frame):
        print(message)
        exit(0)
    return handler

signal(SIGINT, get_shutdown_handler('SIGINT recieved'))
signal(SIGTERM, get_shutdown_handler('SIGTERM recieved'))

drop_privileges(uid='lowkeyshift', gid='lowkeyshift')

starttime = time.time()
while True:
    orginal_stdout = sys.stdout
    hs_out = hs.localhost(hostname = socket.gethostname())
    ds_out = ds.localdisk(hostname = socket.gethostname())

    with open('/home/lowkeyshift/Documents/yt_videos/Python/real_world_python_tuts/agent_log', 'a') as f:
        sys.stdout = f
        print("Collected Metadata at {}".format(starttime))
        print(hs_out)
        print(ds_out)
        sys.stdout = orginal_stdout
    time.sleep(5 - starttime % 5)
    pass