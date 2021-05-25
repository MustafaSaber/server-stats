#!/usr/bin/python3

import psutil
import csv
from datetime import datetime


fieldnames = ["timestamp", "utilization"]
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

ram_stats = psutil.virtual_memory()

print('RAM memory % used:', ram_stats[2])

temp_dict =  {
    "timestamp": dt_string,
    "utilization": ram_stats[2]
}

with open('/opt/MEM.csv', 'a', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    # writer.writeheader()
    writer.writerow(temp_dict)