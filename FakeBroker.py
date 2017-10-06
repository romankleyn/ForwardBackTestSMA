from json import loads
from urllib.request import urlopen
import pandas

#Fake Broker API
class FakeBroker:
	def __init__(self, APIKEY = 'demo'):
		self.APIKEY = APIKEY
		self.TradeLog = {}
		self.trade = 1
		print('FakeBroker Connected')

	def Feed(self, ticker = 'MSFT', data_interval = 'Daily', outputsize = 'compact'):
		ticker = ticker.upper()
		if data_interval in [1, 5, 15, 30, 60]:
			url2 = 'INTRADAY&symbol={}&interval={}min&outputsize=full&apikey={}'.format(ticker, data_interval, self.APIKEY)
			TimeSeries = str(data_interval)+'min'
		else:
			url2 = 'DAILY&symbol={}&outputsize={}&apikey={}'.format(ticker, outputsize,self.APIKEY)
			TimeSeries = data_interval
		url = 'http://www.alphavantage.co/query?function=TIME_SERIES_'+url2
		print(url)

		while True:
			try:
				urlData = loads(urlopen(url).read().decode('utf-8'))
				data = urlData['Time Series ({})'.format(TimeSeries)]
			except:
				continue
			break
		try:
			timeData = urlData["Meta Data"]["3. Last Refreshed"].split(' ')[1]
			print(timeData)
		except:
			pass

		dataset = pandas.DataFrame.from_dict(data, orient='index').rename(index=str,
		columns={'1. open':'OPEN', '2. high':'HIGH', '3. low': 'LOW', '4. close':'CLOSE', '5. volume':'VOLUME'}).apply(pandas.to_numeric)
		dataset.index.name = 'DATE'
		return dataset