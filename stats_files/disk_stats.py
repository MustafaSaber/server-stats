#!/usr/bin/python3

import shutil
import csv
from datetime import datetime


fieldnames = ["timestamp", "utilization"]
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

_, _, free = shutil.disk_usage("/")

free = free / (2**30)

print(f"Free: {free} GiB")

temp_dict =  {
    "timestamp": dt_string,
    "utilization": free
}

with open('/opt/DISK.csv', 'a', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    # writer.writeheader()
    writer.writerow(temp_dict)