
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def get_int_vlan_map(filename):
    int_list = list()
    trunk_list = list()
    access_list = list()
    access_dict = {}
    trunk_dict = {}
    with open(filename, 'r') as f:
        config = f.read().split('!')
        for block in config:
            if block.strip().startswith('interface Fast'):
                int_list.append(block)
    for int_conf in int_list:
        for int_str in int_conf.strip('\n').split('\n'):
            if int_str.endswith('mode access'):
                access_list.append(int_conf)
            elif int_str.endswith('mode trunk'):
                trunk_list.append(int_conf)
    for access_str in access_list:
#        print(access_str)
        int_acc_com = access_str.strip().split('\n')
        for int_acc_str in int_acc_com:
            if int_acc_str.startswith('int'):
                intf = int_acc_str
            if access_str.find('switchport access vlan') == -1:
                print(int_acc_str)
                vlan = 1
                access_dict[intf] = vlan
                break
            elif int_acc_str.startswith(' switchport acc'):
                [int(vlan) for vlan in int_acc_str.split(' ') if vlan.isdigit()]
                access_dict[intf] = vlan
    for trunk_str in trunk_list:
        int_trunk_com = trunk_str.strip().split('\n')
        for int_trunk_str in int_trunk_com:
            if int_trunk_str.startswith('int'):
                intf = int_trunk_str
            if int_trunk_str.startswith(' switchport trunk allowed'):
                word_list = int_trunk_str.split(' ')
                trunk_vlan_list = [ int(vlan) for vlan in word_list[-1].split(',') if vlan.isdigit ]
                trunk_dict[intf] = trunk_vlan_list 
#    print(trunk_dict)
    print(access_dict)
get_int_vlan_map('config_sw2.txt')

