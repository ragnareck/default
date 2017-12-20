#!/usr/bin/env python3
# -*- coding: utf-8 -*-
with open('CAM_table.txt', 'r') as macs:
    for string in macs:
        if string.count('Gi') > 0:
#            print(string.rstrip())
            string.split().pop(2)
            print(string)


