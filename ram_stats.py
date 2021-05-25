#!/usr/bin/python3

import psutil

ram_stats = psutil.virtual_memory()

print('RAM memory % used:', ram_stats[2])