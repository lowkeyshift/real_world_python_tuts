import socket
from subprocess import check_output
from itertools import zip_longest

class DiskScan():

    def localdisk(hostname):
        kname = check_output(("lsblk", "-io", "KNAME")).decode("utf-8").split()
        TYPE = check_output(("lsblk", "-io", "TYPE")).decode("utf-8").split()
        total_size = check_output(("lsblk", "--bytes", "-io", "SIZE")).decode("utf-8").split()
        used_size = check_output(("df", "-m", "--output=used")).decode("utf-8").split()
        mountpoint = check_output(("lsblk", "-io", "MOUNTPOINT")).decode("utf-8").split('\n')
        tags = []
        data = {}

        for name,dtype,total,used,mountpoint in zip_longest(kname[1:],TYPE[1:],total_size[1:],used_size[1:],mountpoint[1:-1]):
            data.update({
                "name": name,
                "hostname": hostname,
                "d_type": dtype,
                "total_size": total,
                "mountpoint": mountpoint,
                "tags": tags
            })
            print(data)

DiskScan.localdisk(hostname = socket.gethostname())