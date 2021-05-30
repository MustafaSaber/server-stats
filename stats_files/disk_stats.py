#!/usr/bin/python3

import sys
import shutil
import csv
from datetime import datetime

csv_path = ""

try:
    csv_path = sys.argv[1]
except IndexError as e:
    csv_path = "DISK.csv"

fieldnames = ["timestamp", "utilization"]
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

_, _, free = shutil.disk_usage("/")

free = free / (2 ** 30)

print(f"Free: {free} GiB, output path is {csv_path}")

temp_dict = {"timestamp": dt_string, "utilization": free}

with open(csv_path, "a", encoding="UTF8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    # writer.writeheader()
    writer.writerow(temp_dict)
