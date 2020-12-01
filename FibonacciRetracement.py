#---PACKAGES---#
import time
import sys
import threading
from datetime import datetime
import os
import math
import pandas as pd
import numpy as np
from scipy import signal
from scipy.fftpack import fft, fftshift

#---Library---#
import OandaPyLib as opl
import MovingAverage as ma

#---MovingAverageSize---#
SizeS = 5
SizeM = 7
SizeL = 10

#---Settings---#
FibonacciRate = 0.618
Digit = 4
DigitDec = 10 ** (Digit - 1)

#---Func---#
def getFloor(val):
	ret = math.floor(val * DigitDec) / DigitDec
	return ret

def EstMaximaAndMinimal(data):
	retMax = 0
	retMin = 0
	try:
		dt = fft(data, 2048) / (len(data)/2.0)
		freq = np.linspace(-0.5, 0.5, len(dt))
		response = 20 * np.log10(np.abs(fftshift(dt / abs(dt).max())))
		maxld = signal.argrelmax(response)
		minld = signal.argrelmin(response)
		retMax = data[maxld]
		retMin = data[minld]
	except Exception as e:
		print(e)
	return retMax, retMin

def EstMaxAndMin(dtData):
	retMin = dtData.min()
	retMax = dtData.max()
	return retMin, retMax

def EstFibonacciRetracement(askData, bidData):
	askMin, askMax = EstMaxAndMin(askData)
	bidMin, bidMax = EstMaxAndMin(bidData)
	retMax = 0
	retMin = 0
	try:
		distL = (bidMax - askMin) * FibonacciRate
		distS = (askMax - bidMin) * FibonacciRate
		if distS > 0:
			retMax = getFloor(askMin + distS)
			retMin = getFloor(bidMax - distS)
	except Exception as e:
		print(e)
	return retMax, retMin

#---END---#