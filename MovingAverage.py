#---PACKAGES---#
import time
import sys
import threading
from datetime import datetime
import os
import pandas as pd
import numpy as np

#---MovingAverageSize---#
SizeS = 5
SizeM = 7
SizeL = 10

#---Func---#
def MovingAverage(data, size):
	ret = None
	try:
		#ret = np.convolve(data, np.ones(size)/size, mode='valid')
		ret = np.convolve(data, np.ones(size)/size, mode='same')
	except Exception as e:
		print(e)
	return ret

def GetMovingAverages(data):
	dataS = None
	dataM = None
	dataL = None
	try:
		dataS = MovingAverage(data, SizeS)
		dataM = MovingAverage(data, SizeM)
		dataL = MovingAverage(data, SizeL)
	except Exception as e:
		print(e)
	return dataS, dataM, dataL

#---END---#