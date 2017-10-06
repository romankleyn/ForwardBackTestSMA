
### Data
____________
Data from http://alphavantage.co/, free API's.

### TradeLog
____________
1:{'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
2:{'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
3:{'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
4:{'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
5:{'Signal': 1, 'Funds': 1591.2499999999854, 'TotalCost': -99812.950000000012, 'Commission': 0.0035, 'Timestamp': 1507317746.510177, 'Price': 58.710000000000001, 'Returns': 0, 'Shares': 1700}

### Example
____________
```python
import forwardRunner
```

    APIKEY: demo
    Time Interval: 1
    using 1 interval
    FakeBroker Connected
    Ticker symbol: SQM
    Frequecny min: 1
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	14:57:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:02:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:02:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:04:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:04:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:06:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:06:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:08:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:08:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:10:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:10:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:12:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:14:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:14:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:16:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:16:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:19:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:20:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:20:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:22:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	5 {'Signal': 1, 'Funds': 1591.2499999999854, 'TotalCost': -99812.950000000012, 'Commission': 0.0035, 'Timestamp': 1507317746.510177, 'Price': 58.710000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:22:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	5 {'Signal': 1, 'Funds': 1591.2499999999854, 'TotalCost': -99812.950000000012, 'Commission': 0.0035, 'Timestamp': 1507317746.510177, 'Price': 58.710000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:24:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	5 {'Signal': 1, 'Funds': 1591.2499999999854, 'TotalCost': -99812.950000000012, 'Commission': 0.0035, 'Timestamp': 1507317746.510177, 'Price': 58.710000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:26:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	5 {'Signal': 1, 'Funds': 1591.2499999999854, 'TotalCost': -99812.950000000012, 'Commission': 0.0035, 'Timestamp': 1507317746.510177, 'Price': 58.710000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:26:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	5 {'Signal': 1, 'Funds': 1591.2499999999854, 'TotalCost': -99812.950000000012, 'Commission': 0.0035, 'Timestamp': 1507317746.510177, 'Price': 58.710000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:28:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	5 {'Signal': 1, 'Funds': 1591.2499999999854, 'TotalCost': -99812.950000000012, 'Commission': 0.0035, 'Timestamp': 1507317746.510177, 'Price': 58.710000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:28:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	5 {'Signal': 1, 'Funds': 1591.2499999999854, 'TotalCost': -99812.950000000012, 'Commission': 0.0035, 'Timestamp': 1507317746.510177, 'Price': 58.710000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:31:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	5 {'Signal': 1, 'Funds': 1591.2499999999854, 'TotalCost': -99812.950000000012, 'Commission': 0.0035, 'Timestamp': 1507317746.510177, 'Price': 58.710000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:32:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	5 {'Signal': 1, 'Funds': 1591.2499999999854, 'TotalCost': -99812.950000000012, 'Commission': 0.0035, 'Timestamp': 1507317746.510177, 'Price': 58.710000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:32:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	5 {'Signal': 1, 'Funds': 1591.2499999999854, 'TotalCost': -99812.950000000012, 'Commission': 0.0035, 'Timestamp': 1507317746.510177, 'Price': 58.710000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:34:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	5 {'Signal': 1, 'Funds': 1591.2499999999854, 'TotalCost': -99812.950000000012, 'Commission': 0.0035, 'Timestamp': 1507317746.510177, 'Price': 58.710000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:34:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	5 {'Signal': 1, 'Funds': 1591.2499999999854, 'TotalCost': -99812.950000000012, 'Commission': 0.0035, 'Timestamp': 1507317746.510177, 'Price': 58.710000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:36:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	5 {'Signal': 1, 'Funds': 1591.2499999999854, 'TotalCost': -99812.950000000012, 'Commission': 0.0035, 'Timestamp': 1507317746.510177, 'Price': 58.710000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:36:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	5 {'Signal': 1, 'Funds': 1591.2499999999854, 'TotalCost': -99812.950000000012, 'Commission': 0.0035, 'Timestamp': 1507317746.510177, 'Price': 58.710000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:38:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	5 {'Signal': 1, 'Funds': 1591.2499999999854, 'TotalCost': -99812.950000000012, 'Commission': 0.0035, 'Timestamp': 1507317746.510177, 'Price': 58.710000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:40:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	5 {'Signal': 1, 'Funds': 1591.2499999999854, 'TotalCost': -99812.950000000012, 'Commission': 0.0035, 'Timestamp': 1507317746.510177, 'Price': 58.710000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:40:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	5 {'Signal': 1, 'Funds': 1591.2499999999854, 'TotalCost': -99812.950000000012, 'Commission': 0.0035, 'Timestamp': 1507317746.510177, 'Price': 58.710000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:42:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	5 {'Signal': 1, 'Funds': 1591.2499999999854, 'TotalCost': -99812.950000000012, 'Commission': 0.0035, 'Timestamp': 1507317746.510177, 'Price': 58.710000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:42:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	5 {'Signal': 1, 'Funds': 1591.2499999999854, 'TotalCost': -99812.950000000012, 'Commission': 0.0035, 'Timestamp': 1507317746.510177, 'Price': 58.710000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:44:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	5 {'Signal': 1, 'Funds': 1591.2499999999854, 'TotalCost': -99812.950000000012, 'Commission': 0.0035, 'Timestamp': 1507317746.510177, 'Price': 58.710000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:44:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	5 {'Signal': 1, 'Funds': 1591.2499999999854, 'TotalCost': -99812.950000000012, 'Commission': 0.0035, 'Timestamp': 1507317746.510177, 'Price': 58.710000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:46:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	5 {'Signal': 1, 'Funds': 1591.2499999999854, 'TotalCost': -99812.950000000012, 'Commission': 0.0035, 'Timestamp': 1507317746.510177, 'Price': 58.710000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:46:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	5 {'Signal': 1, 'Funds': 1591.2499999999854, 'TotalCost': -99812.950000000012, 'Commission': 0.0035, 'Timestamp': 1507317746.510177, 'Price': 58.710000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:48:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	5 {'Signal': 1, 'Funds': 1591.2499999999854, 'TotalCost': -99812.950000000012, 'Commission': 0.0035, 'Timestamp': 1507317746.510177, 'Price': 58.710000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:48:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	5 {'Signal': 1, 'Funds': 1591.2499999999854, 'TotalCost': -99812.950000000012, 'Commission': 0.0035, 'Timestamp': 1507317746.510177, 'Price': 58.710000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:48:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	5 {'Signal': 1, 'Funds': 1591.2499999999854, 'TotalCost': -99812.950000000012, 'Commission': 0.0035, 'Timestamp': 1507317746.510177, 'Price': 58.710000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:48:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	5 {'Signal': 1, 'Funds': 1591.2499999999854, 'TotalCost': -99812.950000000012, 'Commission': 0.0035, 'Timestamp': 1507317746.510177, 'Price': 58.710000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:52:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	5 {'Signal': 1, 'Funds': 1591.2499999999854, 'TotalCost': -99812.950000000012, 'Commission': 0.0035, 'Timestamp': 1507317746.510177, 'Price': 58.710000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:52:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	5 {'Signal': 1, 'Funds': 1591.2499999999854, 'TotalCost': -99812.950000000012, 'Commission': 0.0035, 'Timestamp': 1507317746.510177, 'Price': 58.710000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:54:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	5 {'Signal': 1, 'Funds': 1591.2499999999854, 'TotalCost': -99812.950000000012, 'Commission': 0.0035, 'Timestamp': 1507317746.510177, 'Price': 58.710000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:54:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	5 {'Signal': 1, 'Funds': 1591.2499999999854, 'TotalCost': -99812.950000000012, 'Commission': 0.0035, 'Timestamp': 1507317746.510177, 'Price': 58.710000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:56:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	5 {'Signal': 1, 'Funds': 1591.2499999999854, 'TotalCost': -99812.950000000012, 'Commission': 0.0035, 'Timestamp': 1507317746.510177, 'Price': 58.710000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:56:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	5 {'Signal': 1, 'Funds': 1591.2499999999854, 'TotalCost': -99812.950000000012, 'Commission': 0.0035, 'Timestamp': 1507317746.510177, 'Price': 58.710000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:58:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	5 {'Signal': 1, 'Funds': 1591.2499999999854, 'TotalCost': -99812.950000000012, 'Commission': 0.0035, 'Timestamp': 1507317746.510177, 'Price': 58.710000000000001, 'Returns': 0, 'Shares': 1700}
	http://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SQM&interval=1min&outputsize=full&apikey=demo
	15:58:00
	0 {'Signal': 0, 'Seconds': 0, 'TotalCost': 0, 'Date': 0, 'Commission': 0, 'Price': 0, 'Shares': 0, 'Funds': 0, 'Time': 0}
	1 {'Signal': 1, 'Funds': 1819.0500000000029, 'TotalCost': -98180.949999999997, 'Commission': 0.0035, 'Timestamp': 1507306973.077467, 'Price': 57.75, 'Returns': 0, 'Shares': 1700}
	2 {'Signal': 0, 'Funds': 101246.10000000001, 'TotalCost': 99427.050000000003, 'Commission': 0.0035, 'Timestamp': 1507310105.9787967, 'Price': 58.490000000000002, 'Returns': 0.012691871488308193, 'Shares': 1700}
	3 {'Signal': 1, 'Funds': 1620.1499999999942, 'TotalCost': -99625.950000000012, 'Commission': 0.0035, 'Timestamp': 1507310682.6584315, 'Price': 58.600000000000001, 'Returns': 0, 'Shares': 1700}
	4 {'Signal': 0, 'Funds': 101404.2, 'TotalCost': 99784.050000000003, 'Commission': 0.0035, 'Timestamp': 1507317181.597492, 'Price': 58.700000000000003, 'Returns': 0.0015869359338605005, 'Shares': 1700}
	5 {'Signal': 1, 'Funds': 1591.2499999999854, 'TotalCost': -99812.950000000012, 'Commission': 0.0035, 'Timestamp': 1507317746.510177, 'Price': 58.710000000000001, 'Returns': 0, 'Shares': 1700}
	not trading


