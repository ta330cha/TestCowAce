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

#---Test Data---#



#---Start Script---#
opl.buyStop(opl.BuyLots, 110.000, 111.000)
opl.sellStop(opl.SellLots, 108.000, 107.500)
opl.buyLimit(opl.BuyLots, 107.500, 108.000)
opl.sellLimit(opl.SellLots, 110.500, 109.000)


#---End---#