#! /usr/bin/env python

#---Packages---#
import urllib.parse as pyurllib
import requests as requests
import sys
import os
import datetime
import time
import json
from collections import OrderedDict
import pprint
import numpy as np
import csv
import OandaPyLib as opl

#---Settings---#
TESTDATAFILE = 'MarketPrice.csv'

#---Script---#

#ファイル読み込み
with open (TESTDATAFILE) as csvfile:
	sr = csv.reader(csvfile, delimiter=',', quotechar=',')
	for row in sr:
		dtNow = datetime.datetime.now()
		ask = row[0]
		bid = row[1]
		opl.DumpPrice(dtNow, ask, bid)



#---END---#