#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 08:16:58 2019

@author: arnold
"""

import yaml

yaml_name = "/media/i/home/arnold/development/python/machine_learning/gym/gym-maze/gym_maze/images/config.yaml"
with open(yaml_name) as yaml_data:
    config = yaml.load(yaml_data, Loader=yaml.FullLoader)

print(config)
for key, value in config['Things'].items():
    print(key, '=', str(value))
    print(value[1])