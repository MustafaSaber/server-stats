#!/usr/bin/python3

import sys
import psutil
import csv
from datetime import datetime

csv_path = ""

try:
    csv_path = sys.argv[1]
except IndexError as e:
    csv_path = "CPU.csv"

fieldnames = ["timestamp", "utilization"]
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

cpu = psutil.cpu_percent(interval=1)

print(f"date and time = {dt_string} and CPU is {cpu}, output path is {csv_path}")

temp_dict = {"timestamp": dt_string, "utilization": cpu}

with open(csv_path, "a", encoding="UTF8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    # writer.writeheader()
    writer.writerow(temp_dict)
