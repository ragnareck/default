#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
import sys
#import numpy 
vlan = int(input('vvedite vlan: '))
if type(vlan) != int:
    print('razyi glaza')
    sys.exit()
array = list()
with open('CAM_table.txt', 'r') as macs:
    for string in macs:
        if string.count('Gi') > 0:
#            print(string.rstrip())
            perem = string.split()
            del perem[2]
            array.append(perem)
    array.sort()
    for stri in array:
        print '   '.join(stri)
        print(stri[0])
        if int(stri[0]) != int(vlan):
            print(type(vlan))
            print int(stri[0])
            print('nety')
            sys.exit()
        else:
            print stri

