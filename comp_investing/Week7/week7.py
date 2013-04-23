#!/usr/bin/env python
import sys
import numpy as np
import csv
import copy
import datetime as dt
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.DataAccess as da
from pandas import rolling_mean
from pandas import rolling_std


def get_timestamps(start_date, end_date):
  return du.getNYSEdays(start_date, end_date+dt.timedelta(days=1), dt.timedelta(hours=16))


def get_data(ldt_timestamps, ls_symbols):
  dataobj = da.DataAccess('Yahoo')
  ls_keys = ['close']
  ldf_data = dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
  d_data = dict(zip(ls_keys, ldf_data))
  return ldf_data[0]
  
def get_price(date, symbol, data):
  return data[symbol].ix[date]
  
def compute_bollinger(price, rmean, rstddev):
  return (price - rmean) / (rstddev)
  
def main(): 
  dt_start = dt.datetime(2010, 1, 1)
  dt_end = dt.datetime(2010, 12, 31)
  ldt_timestamps = get_timestamps(dt_start, dt_end)
  ls_symbols = ['AAPL', 'GOOG','IBM','MSFT']
  
  window = 20
  dt_data = get_data(ldt_timestamps, ls_symbols)
  #print dt_data
  header = 'Day\t\t'
  for symbol in ls_symbols:
    header += '\t'+symbol
  means = {}
  std_deviation = {}
  print header
  for symbol in ls_symbols:
    means[symbol] = rolling_mean(dt_data[symbol], window)
    std_deviation[symbol] = rolling_std(dt_data[symbol], window)
    
  for date in ldt_timestamps:
    row = '%s'%(str(date))
    for symbol in ls_symbols:
      price = get_price(date, symbol, dt_data)
      rmean = means[symbol][date]
      #print '!'+str(rmean)
      #print dict(rmean)
      rstddev = std_deviation[symbol][date]
      bollinger_value = compute_bollinger(price, rmean, rstddev)
      row += '\t%s -> %s'%(symbol, str(bollinger_value))
    print row
      
if __name__=='__main__':
  sys.exit(main())