#!/usr/bin/python
'''
(c) 2011, 2012 Georgia Tech Research Corporation
This source code is released under the New BSD license.  Please see
http://wiki.quantsoftware.org/index.php?title=QSTK_License
for license details.

Created on January, 24, 2013

@author: Sourabh Bajaj
@contact: sourabhbajaj@gatech.edu
@summary: Example tutorial code.
'''

# QSTK Imports
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da

# Third Party Imports
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
print "Pandas Version", pd.__version__

def simulate(dt_start, dt_end, ls_symbols, allocations):
  dt_timeofday = dt.timedelta(hours=16)
  # Get a list of trading days between the start and the end.
  ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)
  c_dataobj = da.DataAccess('Yahoo')
  # Keys to be read from the data, it is good to read everything in one go.
  ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']

  # Reading the data, now d_data is a dictionary with the keys above.
  # Timestamps and symbols are the ones that were specified before.
  ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
  d_data = dict(zip(ls_keys, ldf_data))

  # Getting the numpy ndarray of close prices.
  na_price = d_data['close'].values
  # Normalizing the prices to start at 1 and see relative returns
  na_normalized_price = na_price / na_price[0, :]
  na_rets = na_normalized_price.copy()

  # Calculate the daily returns of the prices. (Inplace calculation)
  # returnize0 works on ndarray and not dataframes.
  tsu.returnize0(na_rets)

  #print na_normalized_price
  daily = np.zeros(len(na_normalized_price))
  i = 0
  for row in na_normalized_price:
    daily[i] = row[0]*allocations[0]+row[1]*allocations[1]+row[2]*allocations[2]+row[3]*allocations[3]
    i += 1
  #print daily
  daily_returns = daily.copy()
  tsu.returnize0(daily_returns)
  #print daily_returns
  return (tsu.get_sharpe_ratio(daily_returns), np.std(daily_returns), np.average(daily_returns), (daily[-1]/daily[0]))
  
  
def main():
  ls_symbols =  ['BRCM', 'TXN', 'IBM', 'HNZ'] 
  #allocations = [0.4, 0.0, 0.2, 0.4]
  # Start and End date of the charts
  dt_start = dt.datetime(2011, 1, 1)
  dt_end = dt.datetime(2011, 12, 31)
  sharpe_ratio_max = 0
  allocations_optimal = []
  for i in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
    for j in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
      for k in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
	for l in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
	  value = ((i+j+k+l)-1.0) 
	  if value < 10**-8 and value>-10**-8:
	    allocations = [i, j, k, l]
	    #print allocations
	    (sharpe_ratio, a, b, c)= simulate(dt_start, dt_end, ls_symbols, allocations)
	    if sharpe_ratio>sharpe_ratio_max:
	      sharpe_ratio_max = sharpe_ratio
	      allocations_optimal = allocations
  
  #print allocations_optimal, sharpe_ratio_max
  (sharpe_ratio, volatility, average, cumulative) = simulate(dt_start, dt_end, ls_symbols, allocations_optimal)	
  print 'Start date: %s'%dt_start
  print 'End date: %s'%dt_end
  print 'Symbols: %s'%(str(ls_symbols))
  print 'Optimal allocations: %s'%(allocations_optimal)
  print 'Sharpe ratio: %s'%(sharpe_ratio)
  print 'Volatility (stdev of daily returns): %s'%(volatility)
  print 'Average Daily Return: %s'%(average)
  print 'Cumulative Return: %s'%(cumulative)
  
def main_old():
    ''' Main Function'''

    # List of symbols
    ls_symbols = ['AAPL', 'GOOG', 'XOM', 'GLD']

    # Start and End date of the charts
    dt_start = dt.datetime(2011, 1, 1)
    dt_end = dt.datetime(2011, 12, 31)
    simulate(dt_start, dt_end, ls_symbols, [0.1,0.1,0.1,0.1])
    
    # We need closing prices so the timestamp should be hours=16.
    dt_timeofday = dt.timedelta(hours=16)

    # Get a list of trading days between the start and the end.
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)

    # Creating an object of the dataaccess class with Yahoo as the source.
    c_dataobj = da.DataAccess('Yahoo')

    # Keys to be read from the data, it is good to read everything in one go.
    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']

    # Reading the data, now d_data is a dictionary with the keys above.
    # Timestamps and symbols are the ones that were specified before.
    ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
    d_data = dict(zip(ls_keys, ldf_data))

    # Getting the numpy ndarray of close prices.
    na_price = d_data['close'].values

    # Plotting the prices with x-axis=timestamps
    #plt.clf()
    #plt.plot(ldt_timestamps, na_price)
    #plt.legend(ls_symbols)
    #plt.ylabel('Adjusted Close')
    #plt.xlabel('Date')
    #plt.savefig('adjustedclose.pdf', format='pdf')

    # Normalizing the prices to start at 1 and see relative returns
    na_normalized_price = na_price / na_price[0, :]

    # Plotting the prices with x-axis=timestamps
    #plt.clf()
    #plt.plot(ldt_timestamps, na_normalized_price)
    #plt.legend(ls_symbols)
    #plt.ylabel('Normalized Close')
    #plt.xlabel('Date')
    #plt.savefig('normalized.pdf', format='pdf')

    # Copy the normalized prices to a new ndarry to find returns.
    na_rets = na_normalized_price.copy()

    # Calculate the daily returns of the prices. (Inplace calculation)
    # returnize0 works on ndarray and not dataframes.
    tsu.returnize0(na_rets)

    # Plotting the plot of daily returns
    #plt.clf()
    #plt.plot(ldt_timestamps[0:50], na_rets[0:50, 3])  # $SPX 50 days
    #plt.plot(ldt_timestamps[0:50], na_rets[0:50, 4])  # XOM 50 days
    #plt.axhline(y=0, color='r')
    #plt.legend(['$SPX', 'XOM'])
    #plt.ylabel('Daily Returns')
    #plt.xlabel('Date')
    #plt.savefig('rets.pdf', format='pdf')

    # Plotting the scatter plot of daily returns between XOM VS $SPX
    #plt.clf()
    #plt.scatter(na_rets[:, 3], na_rets[:, 4], c='blue')
    #plt.ylabel('XOM')
    #plt.xlabel('$SPX')
    #plt.savefig('scatterSPXvXOM.pdf', format='pdf')

    # Plotting the scatter plot of daily returns between $SPX VS GLD
    #plt.clf()
    #plt.scatter(na_rets[:, 3], na_rets[:, 1], c='blue')  # $SPX v GLD
    #plt.ylabel('GLD')
    #plt.xlabel('$SPX')
    #plt.savefig('scatterSPXvGLD.pdf', format='pdf')

if __name__ == '__main__':
    main()
