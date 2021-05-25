#!/usr/bin/python3

import psutil
import csv
from datetime import datetime


fieldnames = ["timestamp", "utilization"]
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

cpu = psutil.cpu_percent(interval=1)

print(f"date and time = {dt_string} and CPU is {cpu} ")	

temp_dict =  {
    "timestamp": dt_string,
    "utilization": cpu
}

with open('/opt/CPU.csv', 'a', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    # writer.writeheader()
    writer.writerow(temp_dict)