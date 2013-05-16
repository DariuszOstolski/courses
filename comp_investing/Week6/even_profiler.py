'''
(c) 2011, 2012 Georgia Tech Research Corporation
This source code is released under the New BSD license.  Please see
http://wiki.quantsoftware.org/index.php?title=QSTK_License
for license details.

Created on January, 23, 2013

@author: Sourabh Bajaj
@contact: sourabhbajaj@gatech.edu
@summary: Event Profiler Tutorial
'''


import pandas as pd
import numpy as np
import math
import copy
import QSTK.qstkutil.qsdateutil as du
import datetime as dt
import QSTK.qstkutil.DataAccess as da
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkstudy.EventProfiler as ep
from sets import Set
"""
Accepts a list of symbols along with start and end date
Returns the Event Matrix which is a pandas Datamatrix
Event matrix has the following structure :
    |IBM |GOOG|XOM |MSFT| GS | JP |
(d1)|nan |nan | 1  |nan |nan | 1  |
(d2)|nan | 1  |nan |nan |nan |nan |
(d3)| 1  |nan | 1  |nan | 1  |nan |
(d4)|nan |  1 |nan | 1  |nan |nan |
...................................
...................................
Also, d1 = start date
nan = no information about any event.
1 = status bit(positively confirms the event occurence)
"""

def write_buy(date, symbol, amount):
  write_order('Buy', date, symbol, amount)

def write_sell(date, symbol, amount):
  write_order('Sell', date, symbol, amount)

  
def write_order(buy_or_sell, date, symbol, amount):
   with open('orders_events.csv', 'at+') as outfile:
     outfile.write('%d,%d,%d,%s,%s,%d\n'%(date.year, date.month, date.day, symbol, buy_or_sell, int(amount)))
     
def find_events(ls_symbols, d_data):
    ''' Finding the event dataframe '''
    df_close = d_data['actual_close']
    ts_market = df_close['SPY']

    print "Finding Events"

    # Creating an empty dataframe
    df_events = copy.deepcopy(df_close)
    df_events = df_events * np.NAN
    
    event_set = Set()
    # Time stamps for the event range
    ldt_timestamps = df_close.index
    number_of_events = 0
    event_date = 0
    for s_sym in ls_symbols:
        for i in range(1, len(ldt_timestamps)):
            # Calculating the returns for this timestamp
            f_symprice_today = df_close[s_sym].ix[ldt_timestamps[i]]
            f_symprice_yest = df_close[s_sym].ix[ldt_timestamps[i - 1]]

            if  f_symprice_yest>=10.0 and f_symprice_today<10.0:
	      #print s_sym,ldt_timestamps[i-1], df_close[s_sym].ix[ldt_timestamps[i-1]], ldt_timestamps[i], df_close[s_sym].ix[ldt_timestamps[i]]
	      write_buy(ldt_timestamps[i], s_sym, 100)
	      sell_idx = min(i+5, len(ldt_timestamps)-1)
	      write_sell(ldt_timestamps[sell_idx], s_sym, 100)
	      df_events[s_sym].ix[ldt_timestamps[i]] = int(1)
	      number_of_events += 1            
	      #event_set.add( ldt_timestamps[i])
    print number_of_events
    num = 0
    for s_sym in ls_symbols:
       for i in range(1, len(ldt_timestamps)):
	 if df_events[s_sym].ix[ldt_timestamps[i]] >= 0.99 and df_events[s_sym].ix[ldt_timestamps[i]] <= 1.001:
	   num = num +1
    print num
    return df_events


if __name__ == '__main__':
    dt_start = dt.datetime(2008, 1, 1)
    dt_end = dt.datetime(2009, 12, 31)
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt.timedelta(hours=16))
 

    dataobj = da.DataAccess('Yahoo')
    ls_symbols = dataobj.get_symbols_from_list("sp5002012")
    ls_symbols.append('SPY')
    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
    ldf_data = dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)

    d_data = dict(zip(ls_keys, ldf_data))
    for s_key in ls_keys:
        d_data[s_key] = d_data[s_key].fillna(method = 'ffill')
        d_data[s_key] = d_data[s_key].fillna(method = 'bfill')
        d_data[s_key] = d_data[s_key].fillna(1.0)

    df_events = find_events(ls_symbols, d_data)
    print "Creating Study"
    print df_events
    
    ep.eventprofiler(df_events, d_data, i_lookback=20, i_lookforward=20,
                s_filename='MyEventStudy.pdf', b_market_neutral=True, b_errorbars=True,
                s_market_sym='SPY')
