#! /usr/bin/env python

#---PACKAGES---#
import time
import sys
import threading
from datetime import datetime
import os
from types import resolve_bases
import requests
import json
import configparser

def printDebug1(text, funcname):
	temp = f'{text} @ {funcname}'
	print(temp)
