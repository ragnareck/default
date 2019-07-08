#!/usr/bin/env python3
# -*- coding: utf-8 -*-

ignore = ['dulpex', 'alias', 'Current configuration']
key = ""
def filter(filename, ignore):
    config1 = list()
    with open(filename, 'r') as fi:
        config = fi.read().strip().split('\n')
        #print(config)
        for command in config:
            command = command.rstrip()
            config1.append(command)
            if command[0] is "!":
                config1.remove(command)
        for command in config1:
#            command1 = config.split()
            for words in command:
                print(command)
                for word in ignore:
                    print(word)
                    if words is word:
                        print(command)
                        config1.remove(command)
#    print(config1)
    return config1
config1 = filter('config_sw1.txt',ignore)
#print(config1)
#idef ignore_command(config1,ignore):
 #   config1.split()
value = list()
conf_dict = {}
for command in config1:
    if command[0].isalnum() and key is None:
        key = command
    elif command[0].isalnum():
        conf_dict[key] = value
        key = command
        value = list()
    else:
        value.append(command)
#print(conf_dict)


