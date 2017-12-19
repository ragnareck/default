#!/usr/bin/env python3
# -*- coding: utf-8 -*-
ignore = ['duplex', 'alias','Current configuration']
i = 0
with open('config_sw1.txt', 'r+') as conf:
    for string in conf:
        if string[0] == '!':
            continue
        for elem in ignore:
            if string.count(elem) > 0:
                print string.count(elem)
                break
            elif ignore[-1] == elem:
                string.rstrip()
                print(string)
                

