#! /usr/bin/env python
# -*- coding: utf-8 -*-

#---Packages---#
import json

#---DATA---#


class Config:
	def __init__(self, ConfigFileName):
		print(ConfigFileName)
		self.__config = None
		with open(ConfigFileName, "r") as fr:
			self.__config = json.load(fr)
	
	def Get(self, key):
		return self.__config[key]

#---END---#