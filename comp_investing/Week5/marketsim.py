#!/usr/bin/env python
import sys
import numpy as np
import csv
import copy
import datetime as dt
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.DataAccess as da

portfolio_value = 0

class Order(object):
  def __init__(self, year, month, day, symbol, order, amount):
    self.date = dt.datetime(year, month, day)
    self.symbol = symbol
    self.order = order
    self.amount = int(amount)


class Day(object):
  def __init__(self, date, symbols, total_amount):
    self.total_amount = total_amount
    self.cumulative = 0
    self.equities = {}
    self.day = date
    for sym in symbols:
      self.equities[sym] = 0
      
  def buy(self, symbol, amount, price):
    self.equities[symbol] = self.equities[symbol]+amount
    self.total_amount = self.total_amount - (amount*price)
    
  def sell(self, symbol, amount, price):
    self.equities[symbol] = self.equities[symbol]-amount
    self.total_amount = self.total_amount + (amount*price)
    
  def __str__(self):
    return str(self.day)+' '+str(self.equities)+' '+str(self.total_amount)+' '+str(self.cumulative)

def createDay(date, previousDay):
  day = Day(date, [], 0)
  day.total_amount = previousDay.total_amount
  day.equities = copy.deepcopy(previousDay.equities)
  return day
  
def write(output_path, daily):
  with open(output_path, 'wt') as outfile:
    for day in daily:
      outfile.write('%d,%d,%d,%.2f\n'%(day.day.year, day.day.month, day.day.day, day.cumulative))
      
def read(input_file):
  print 'Input file %s'%(input_file)
  orders = []
  with open(input_file, 'rU') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
      orders.append(Order(int(row[0]), int(row[1]), int(row[2]), row[3], row[4], row[5]))
  return orders
  
def get_dates_range(orders):
  return (orders[0].date, orders[-1].date)

def get_timestamps(start_date, end_date):
  return du.getNYSEdays(start_date, end_date+dt.timedelta(days=1), dt.timedelta(hours=16))


def get_data(ldt_timestamps, ls_symbols):
  dataobj = da.DataAccess('Yahoo')
  ls_keys = ['close']
  ldf_data = dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
  d_data = dict(zip(ls_keys, ldf_data))
  return ldf_data[0]

def get_symbols(orders):
  symbols = []
  for i in orders:
    if i.symbol not in symbols:
      symbols.append(i.symbol)
  return symbols

def get_price(date, symbol, data):
  return data[symbol].ix[date]

def get_orders_on_date(date, orders):
  dt_orders = []
  for order in orders:
    if order.date.date() == date.date():
      dt_orders.append(order)
  return dt_orders
  
def process_orders(ldt_timestamps, orders, data):
  global portfolio_value
  
  print 'Value: '+str(portfolio_value)
  symbols = get_symbols(orders)
  previousDay = Day(ldt_timestamps[0], symbols, portfolio_value)
  daily = []
  for date in ldt_timestamps:
    day = createDay(date, previousDay)
    orders_on_date = get_orders_on_date(date, orders)
    #print orders_on_date
    for order in orders_on_date:
      price = get_price(date, order.symbol, data)
      
      if order.order == 'Buy':
        day.buy(order.symbol, order.amount, price)
      else:
        day.sell(order.symbol, order.amount, price)
    #print day
    previousDay = day
    daily.append(day)
  return daily
    
def process_days(daily, data):
  for day in daily:    
    for equity in day.equities:
      price = get_price(day.day, equity, data)
      day.cumulative = day.cumulative+(day.equities[equity]*price)
    day.cumulative = day.total_amount+day.cumulative
    
def main():
  global portfolio_value
  argv = sys.argv[1:]
  if len(argv)!=3:
    print "Not enough arguments"
    return 1
  portfolio_value = int(argv[0])
  input_file = argv[1]
  output_file = argv[2]
  orders = read(input_file)
  dates = get_dates_range(orders)
  
  ldt_timestamps = get_timestamps(dates[0], dates[1])
  
  ls_symbols = get_symbols(orders)
  
  dt_data = get_data(ldt_timestamps, ls_symbols)
  print dt_data
    
  daily = process_orders(ldt_timestamps, orders, dt_data)
  process_days(daily, dt_data)
      
  for day in daily:
    print day
  
  write(output_file, daily)
    
if __name__=='__main__':
  sys.exit(main())
