CompInvesti Homework 6
Contents
[hide]

    1 Overview
    2 To Do
    3 Experiments to Run
    4 Other Details
    5 Example Output
    6 Assessment

Overview

In this homework you will investigate event studies based on technical indicators. I mentioned "in class" that I believe that technical indicators for a stock that move against the way the market is moving may have more validity than otherwise. So for this exercise we will investigate that hypothesis.

The project is to look for events with Bollinger Bands where the Bollinger value for an individual stock is significantly different than it currently is for the market.
To Do

Part 1: Implement Bollinger bands as an indicator using 20 day look back. The upper band should represent the mean plus one standard deviation and the lower band is the mean minus one standard deviation. Have your code output the indicator value in a range of -1 to 1. This is similar to the last homework so you have already completed that.

Part 2: Now create an event study with the signal being:

Bollinger value for the equity today <= -2.0
Bollinger value for the equity yesterday >= -2.0
Bollinger value for SPY today >= 1.0

So we're looking for situations where the stock has punched through the lower band and the market is substantially in the other direction. That suggests that something special is happening with the stock.

Part 3: Now use the indicator you created as the part 2 of the homework 5 and create an event study to find potentially interesting results.
Experiments to Run

You should run two experiments.

    Experiment 1: Implement Bollinger bands and convert the value between -1 and 1. 

Then create an event study with the following parameters.

        Event:
            Bollinger value for the equity today <= -2.0
            Bollinger value for the equity yesterday >= -2.0
            Bollinger value for SPY today >= 1.0 
        Startdate: 1 Jan 2008
        Enddate: 31 Dec 2009
        20 day lookback for Bollinger bands
        Symbol list: SP5002012
        Adjusted close. 

    Experiment 2: Event study using the indicator of your choice. 

