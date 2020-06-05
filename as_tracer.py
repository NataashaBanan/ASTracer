import subprocess

from work_with_api import request_ip_data
from trace_output_parser import parse, IP


def get_output(ip_name):# получили в arr строки выхода
    with subprocess.Popen(["tracert", ip_name],
                          shell=True, stdout=subprocess.PIPE) as p:
        arr = p.stdout.readlines()
    return arr

try:
    ip_name = IP.search(input()).group(0)
except AttributeError:
    print("bad input")
    ip_name = "192.168.1.1"

arr = parse(get_output(ip_name))

for i in range(len(arr)):
    print(i + 1, arr[i], request_ip_data(arr[i]))

# print(request_ip_data("85.112.122.131"))
