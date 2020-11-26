#---PACKAGES---#
import time
import sys
import threading
from datetime import datetime
import os
import pandas as pd
import numpy as np

#---Library---#
import ArpCSVList as dataMng

#---FileName---#
DataFileName = "MarketPrice.csv"
MovingAverageSDataFileName = "MovingAverageS.csv"
MovingAverageMDataFileName = "MovingAverageM.csv"
MovingAverageLDataFileName = "MovingAverageL.csv"

#---MovingAverageSize---#
SizeS = 10
SizeM = 20
SizeL = 40

#---Func---#
def writeCSV(prices, FileName):
	try:
		with open(FileName, "a") as fw:
			writer = csv.writer(fw)
			writer.writerow(prices)
		return True
	except Exception as e:
		print(e)
	return False

def getData(size):
	ret = None
	try:
		df = pd.read_csv(DataFileName)
		ret = df.tail(size)
	except Exception as e:
		print(e)
	return ret

def MeanData(size):
	ret = None
	try:
		data = getData(size)
		ret = np.mean(data)
	except Exception as e:
		print(e)
	return ret

def SetMovingAverage():
	try:
		writeCSV(MeanData(SizeS), MovingAverageSDataFileName)
		writeCSV(MeanData(SizeM), MovingAverageMDataFileName)
		writeCSV(MeanData(SizeL), MovingAverageLDataFileName)
		return True
	except Exception as e:
		ret = False
		print(e)
	return False

#---END---#