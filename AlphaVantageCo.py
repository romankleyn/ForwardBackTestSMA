#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from json import loads
from urllib.request import urlopen
import pandas

def History(ticker = 'MSFT', interval = 'EOD', APIKEY = 'demo',pd = True):
    ticker = ticker.upper()
    if APIKEY == 'demo' and ticker != 'MSFT':
        raise Exception('Please register at www.alphavantage.co for a free API*'+
            ' *free at time of creating this. Not affiliated with the service, just a user and a fan.')
    elif type(interval) == int and interval not in [1, 5, 15, 30, 60]:
        raise Exception('Intervals are 1, 5, 15, 30, 60 and EOD.'
            +' Please check at www.alphavantage.co for more information regarding the API*'
            +' *free at time of creating this. Not affiliated with the service, just a user and a fan.')

    url2 = 'DAILY&symbol={}&outputsize=full&apikey={}'.format(ticker, APIKEY)
    TimeSeries = 'Daily'
    if interval in [1, 5, 15, 30, 60]:
        url2 = 'INTRADAY&symbol={0}&interval={1}min&outputsize=full&apikey={}'.format(ticker, interval, APIKEY)
        TimeSeries = str(interval)+'min'
               
    url = 'http://www.alphavantage.co/query?function=TIME_SERIES_'+url2
    urlData = loads(urlopen(url).read().decode('utf-8'))['Time Series ({})'.format(TimeSeries)]
    dataset = pandas.DataFrame.from_dict(urlData, orient='index').rename(index=str,
                columns={'1. open':'OPEN', '2. high':'HIGH', '3. low': 'LOW', '4. close':'CLOSE', '5. volume':'VOLUME'}).apply(pandas.to_numeric)
    dataset.index.name = 'DATE'
    
    if pd == False:
    	print('ok')
    	dataset = dataset.to_dict()
    return dataset