#!/usr/bin/python3

import shutil

total, used, free = shutil.disk_usage("/")

print(f"Free: {free / (2**30)} GiB")