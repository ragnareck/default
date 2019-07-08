#!/usr/bin/env python3
# -*- coding: utf-8 -*-

access_dict = {'FastEthernet0/12': 10, 'FastEthernet0/14':11, 'FastEthernet0/16':17, 'FastEthernet0/17':150 }
access_template = { 'switchport mode access', 'switchport access vlan', 'switchport nonegotiate', 'spanning-tree portfast', 'spanning-tree bpduguard enable' }
def edit_conf():
    for int,vlan in access_dict.items():
        print('interface FastEthernet' + int)
        for command in access_template:
            if command.endswith('access vlan'):
                print(' {} {}'.format(command, vlan))
            else:
                print(' {}'.format(command))
edit_conf()

