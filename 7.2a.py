#!/usr/bin/env python3
# -*- coding: utf-8 -*-
vvod = raw_input('vvedite src name: ')
print(vvod)
print(type(vvod))
vivod = raw_input('vvedite dest name: ')
#vivod = 'config_sw1_clear.txt'
ignore = ['duplex', 'alias','Current configuration']
with open(vvod, 'r') as conf, open(vivod, 'w+') as conf1:    
    for string in conf:
        if string[0] == '!':
            continue
        for elem in ignore:
            if string.count(elem) > 0:
                print string.count(elem)
                break
            elif ignore[-1] == elem:
                string.rstrip()
                conf1.write(string)
#cat config_sw1_clear.txt

