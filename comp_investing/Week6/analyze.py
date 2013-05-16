#!/usr/bin/env python
import sys
import numpy as np
import csv
import copy
import datetime as dt
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.DataAccess as da
import QSTK.qstkutil.tsutil as tsu

def get_timestamps(start_date, end_date):
  return du.getNYSEdays(start_date, end_date+dt.timedelta(days=1), dt.timedelta(hours=16))

def get_index_values(date_start, date_end, index):
  ldt_timestamps = get_timestamps(date_start, date_end)
  ls_symbols = [index]
  dataobj = da.DataAccess('Yahoo')
  ls_keys = ['close']
  ldf_data = dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
  d_data = dict(zip(ls_keys, ldf_data))
  return ldf_data[0]

def read(input_file):  
  print 'Input file %s'%(input_file)
  dates = []
  values = []
  with open(input_file, 'rU') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
      date = dt.datetime(int(row[0]), int(row[1]), int(row[2]))
      value = float(row[3])
      dates.append(date)
      values.append(value)
  return (dates, values)

def compute_sharpe_ratio(values):
  return tsu.get_sharpe_ratio(values)

def compute_std_dev(values):
  return np.std(values)

def compute_average(values):
  return np.average(values)

def compute_total(values):
  return (values[-1]/values[0])

def compute(values):
  na_price = np.array(values)
  na_normalized_price = na_price / na_price[0]
  tsu.returnize0(na_normalized_price)  
  return (compute_sharpe_ratio(na_normalized_price),
          compute_std_dev(na_normalized_price),
          compute_average(na_normalized_price),
          compute_total(na_price))

def main():
  argv = sys.argv[1:]
  if len(argv)!=2:
    print "Not enough arguments"
    return 1
  
  input_file = argv[0]
  index = argv[1]
  vals = read(input_file)
  dates = vals[0]
  values= vals[1]
  index_values = get_index_values(dates[0], dates[-1], index).values
  (fund_sharpe_ratio,  fund_stddev, fund_average, fund_total) = compute(values)
  (index_sharpe_ratio, index_stddev, index_average, index_total) = compute(index_values)
  display_total(dates[-1], values[-1])
  display_date_range(dates[0], dates[-1])
  display_sharpe('Fund', fund_sharpe_ratio)
  display_sharpe(index, index_sharpe_ratio)
  print ''
  display_total_ret('Fund', fund_total)
  display_total_ret(index, index_total)
  print ''
  display_stddev('Fund', fund_stddev)
  display_stddev(index, index_stddev)
  print ''
  display_daily('Fund', fund_average)
  display_daily(index, index_average)
  

def display_sharpe(label, value):
  print 'Sharpe Ratio of %s: %f'%(label, value)

def display_total_ret(label, value):
  print 'Total Return of %s : %f'%(label, value)
  
def display_stddev(label, value):
  print 'Standard Deviation of %s: %f'%(label, value)

def display_daily(label, value):
  print 'Average Daily Return of %s: %f'%(label, value)

def display_date_range(date_start, date_end):
  print 'Details of the Performance of the portfolio :\n'
  print 'Data Range :  %s  to  %s\n'%(str(date_start), str(date_end))
  
def display_total(date, total):
  print 'The final value of the portfolio using the sample file is -- %d, %d, %d, %d\n'%(date.year, date.month, date.day, int(total))
    
if __name__=='__main__':
  sys.exit(main())
