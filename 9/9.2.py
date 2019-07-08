#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def generate_trunk_config():
    trunk_dict = { 'FastEthernet0/1':[10,20],'FastEthernet0/2':[11,30],'FastEthernet0/4':[17] }
    trunk_template = ['switchport trunk encapsulation dot1q','switchport mode trunk','switchport trunk native vlan 999','switchport trunk allowed vlan']
    for intf, vlanid in trunk_dict.items():
        trunk_template1 = list(trunk_template)
        for command in trunk_template1:
            if command.endswith('allowed vlan'):
                command1 = command + ' ' + ', '.join([str(vlan) for vlan in vlanid])
                trunk_template1.remove(command)
                trunk_template1.append(command1)
        print(trunk_template1)
generate_trunk_config()
