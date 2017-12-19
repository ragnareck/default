!/usr/bin/env python3
 -*- coding: utf-8 -*-
ignore = ['duplex', 'alias','current configuration']
i = 0
with open('config.sw1.txt', 'r+') as conf:
    for string in conf:
        if string[0] == '!':
            pass
        elif string.find(ignore[1]) > 0:
            pass
        else
            string.rstrip()
            print(string)

