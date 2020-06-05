import re

IP = re.compile("(\d{1,3}.){3}\d{1,3}")


def tail(arr):
    i = 0
    el = arr[i]
    while el[0:3] != b"  1" and i < len(arr) - 1:
        i += 1
        el = arr[i]
    arr = arr[i:]
    return arr
    # отрезали лишнее в начале


def head(arr):
    i = 0
    el = arr[i]
    while el != b"\r\n" and str(el).find(" * ") == -1:
        i += 1
        el = arr[i]
    arr = arr[0:i]
    return arr
    # отрезали лишнее в конце


def get_ips(arr):
    for i in range(len(arr)):
        arr[i] = IP.search(str(arr[i])).group(0)
    return arr


def parse(arr):
    return get_ips(head(tail(arr)))
