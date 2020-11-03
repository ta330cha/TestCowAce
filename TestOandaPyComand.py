#! /usr/bin/env python

#---Packages---#
import urllib.parse as pyurllib
import requests as requests
import sys
import datetime
import json
from collections import OrderedDict
import pprint
import numpy as np

#---My Package---#
import OandaPyLib as opl
from ArpCSVList import ArpCSVList

#---Test Data---#

#---Manager---#
dataMng = ArpCSVList()


#---Start Script---#
opl.BuyStop(105.000, 106.010, 1)
opl.SellStop(101.000, 100.000, 1)
opl.BuyLimit(101.500, 108.000, 1)
opl.SellLimit(110.500, 109.000, 1)

timeGetPrice, ask, bid = opl.GetPrices()
print(ask)
print(bid)
dataMng.setMarketPrice(ask, bid)

#---End---#