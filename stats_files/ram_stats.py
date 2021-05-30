#!/usr/bin/python3

import sys
import psutil
import csv
from datetime import datetime

csv_path = ""

try:
    csv_path = sys.argv[1]
except IndexError as e:
    csv_path = "MEM.csv"

fieldnames = ["timestamp", "utilization"]
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

ram_stats = psutil.virtual_memory()

print(f"RAM memory {ram_stats[2]} used, output path is {csv_path}")

temp_dict = {"timestamp": dt_string, "utilization": ram_stats[2]}

with open(csv_path, "a", encoding="UTF8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    # writer.writeheader()
    writer.writerow(temp_dict)
