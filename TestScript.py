import numpy as np
from scipy import signal
from scipy.fftpack import fft, fftshift
from sklearn.linear_model import LinearRegression



x = np.array([1, 2, 5, 10, 28, 40])
y = np.array([2, 3, 2,  3,  4,  6])

cov = np.cov(x, y)[0][1]

print(cov)

