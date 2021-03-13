#! /usr/bin/env python
# -*- coding: utf-8 -*-

#---Packages---#
import json

#---FILE_NAME---#
ConfigFileName = './Configs/AccountInfo.json'

with open(ConfigFileName, "r") as fr:
	__config = json.load(fr)

def get(key):
	return __config[key]

#---END---#