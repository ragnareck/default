#!/usr/bin/env python3
# -*- coding: utf-8 -*-
access_dict = {'FastEthernet0/12': 10, 'FastEthernet0/14':11, 'FastEthernet0/16':17, 'FastEthernet0/17':150 }
access_template = [ 'switchport mode access', 'switchport access vlan', 'switchport nonegotiate', 'spanning-tree portfast', 'spanning-tree bpduguard enable' ]
port_security = [ 'switchport port-security maiximum 2', 'switchport port_security violation restrict', 'switcport port_security' ]
def edit_conf(psecurity):
#    global access_template, port_security
    if psecurity:
        access_template.extend(port_security)
    for intf,vlan in access_dict.items():
        print('interface FastEthernet' + intf)
        for command in access_template:
            if command.endswith('access vlan'):
                print(' {} {}'.format(command, vlan))
            else:
                print(' {}'.format(command))
edit_conf(psecurity=True)

