import socket
from subprocess import check_output
from itertools import zip_longest


class DiskScan():

    def localdisk(hostname):
        kname = check_output(("lsblk", "-io", "KNAME")).decode("utf-8").split()

        print(kname)
DiskScan.localdisk(hostname = socket.gethostname())