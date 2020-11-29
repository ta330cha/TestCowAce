#---PACKAGES---#
import time
import sys
import threading
from datetime import datetime
import os
import pandas as pd
import numpy as np
from scipy import signal
from scipy.fftpack import fft, fftshift
from sklearn.linear_model import LinearRegression

#---Library---#
import OandaPyLib as opl
import MovingAverage as ma
import FibonacciRetracement as fr

#---Settings---#
diff = 0.01

#---Func---#
def linearReg(data):
	retReg = 0
	try:
		size = data.size
		xaxis = np.arange(size)
		print(xaxis)
		print(data)
		model_lr = LinearRegression()
		model_lr.fit(xaxis, data)
		intercept = model_lr.intercept_
		if trend > 0 + diff:
			retReg = 1
		elif trend < 0 - diff:
			retReg = -1
	except Exception as e:
		print(e)
	return retReg

def CovTrend(data):
	retReg = 0
	try:
		size = data.size
		xaxis = np.arange(size)
		cov = np.cov(xaxis, data)[0][1]
		print(cov)
		if cov > diff:
			retReg = 1
		elif cov < diff:
			retReg = -1
		else:
			retReg = 0
	except Exception as e:
		print(e)
	return retReg

def EstDecisionTrend(askData, bidData):
	retReg = 0
	try:
		#tempData = (bidData - askData)/2
		retReg = CovTrend(askData)
	except Exception as e:
		print(e)
	return retReg

#---END---#