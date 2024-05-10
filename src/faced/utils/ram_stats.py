from __future__ import absolute_import

import psutil
import os

def get_cpu_usage():
    load1, load5, load15 = psutil.getloadavg()
    cpu_usage = (load15/os.cpu_count()) * 100
    print("The CPU usage is : ", cpu_usage)
    return cpu_usage

def get_ram_usage():
    print('RAM memory % used:', psutil.virtual_memory()[2])
    print('RAM Used (GB):', psutil.virtual_memory()[3]/1000000000)
    return psutil.virtual_memory()[2]

