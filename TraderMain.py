#! /usr/bin/env python
# -*- coding: utf-8 -*-

#---Packages---#
import socket
import time
import sys
import threading
from datetime import datetime

#---Threads---#
from ThreadTrader import ThreadTrader

#---Settings---#
Interval = 60 # = 60sec = 1min

#---File Names---#


def main():
    threadTimer = ThreadTrader(Interval)
    threadTimer.start()
    logger = "---THREAD START---"
    print(logger)

if __name__ == '__main__':
    main()

#---END---#