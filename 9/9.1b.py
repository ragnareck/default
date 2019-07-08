#!/usr/bin/env python3
# -*- coding: utf-8 -*-
access_dict = {'FastEthernet0/12': 10, 'FastEthernet0/14':11, 'FastEthernet0/16':17, 'FastEthernet0/17':150 }
access_template = [ 'switchport mode access', 'switchport access vlan', 'switchport nonegotiate', 'spanning-tree portfast', 'spanning-tree bpduguard enable' ]
port_security = [ 'switchport port-security maiximum 2', 'switchport port_security violation restrict', 'switcport port_security' ]
def edit_conf(psecurity):
    global access_template, port_security, access_dict
    if psecurity:
        access_template.extend(port_security)
    ps_dict = {}
    for intf,vlan in access_dict.items():
        access_template_copy = list(access_template)
        for command in access_template_copy:
            if command.endswith('access vlan'):
                command1 = command + ' ' + str(vlan)
                access_template_copy.remove(command)
                access_template_copy.insert(2,command1)
#print(command)
           # print(command)
        ps_dict[intf] = access_template_copy
    print(ps_dict)
edit_conf(psecurity=True)

