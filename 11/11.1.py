#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def parse(filename):
    with open(filename,'r') as fi:
        cdp_neigh = fi.pop[0:2]
        dev, loc_int, _, _, _, port_id = [command.split for command in cdp_neigh]
        
