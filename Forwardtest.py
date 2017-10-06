import pandas
from numpy import where
from time import localtime, strftime, time, sleep
from FakeBroker import FakeBroker
from algo import SimpleAlgo
from TechnicalAnalysis  import round_down
#Default Commisions are based on interactive broker US exchange rates and assuming all orders are filled instantly. 
class test:
	def __init__(self, APIKEY = 'demo'):
		self.logID = round(time()*1000)
		self.FB = FakeBroker(APIKEY)
		self.TradeN = 1
		#Prexisitng short so starts with long postion always
		self.TradeLog = {0:{'Date': 0, 'Time': 0, 'Seconds': 0, 'Signal': 0, 'Price': 0, 'Commission': 0, 'Shares': 0, 'TotalCost': 0,'Funds': 0}}
	
	def live(self, ticker = 'MSFT', MAs = [4,8], data_interval = 'Daily', funds = 100000, freqr = 15, commissionPerShare = 0.0035, maxCommissionPercent = .005): 
		if len(MAs) != 2:
			raise Exception('Need 2 numbers in a list for the moving average')
		ifunds = funds
		twait = freqr*60
		tstart = (9*3600)+(30*60)
		tfinish = 16*3600
		status = True
		t = localtime()
		timeRefresh = t.tm_sec + (t.tm_min * 60) + (t.tm_hour * 3600)
		
		#Live Run
		while status:
			#Trading time data
			stat = 0
			t = localtime()
			todaytime = t.tm_sec + (t.tm_min * 60) + (t.tm_hour * 3600)
			
			#trade signal 
			if todaytime >= tstart and todaytime <= tfinish:
				data_feed = self.FB.Feed(ticker.upper(), data_interval = data_interval)
				signals = SimpleAlgo(data_feed, MAs)
				currentSignal = signals.iloc[-1].values.astype(int)[0]

				#Current Position Eval
				p = data_feed['CLOSE'].iloc[-1]
				c = min(commissionPerShare, maxCommissionPercent*p)
				LastTrade = self.TradeLog[self.TradeN-1]
				sc = p-c
				
				#bull buy assets
				if currentSignal != LastTrade['Signal'] and currentSignal == 1:
					sc = p+c
					ns = round_down(funds/sc, -2)
					tc = sc*ns
					funds -= tc
					TradeData = {'Timestamp': time(), 'Signal': currentSignal, 'Price': p, 'Commission': c, 'Shares': ns, 
									'TotalCost': -tc,'Funds': funds,'Returns':0}
					self.TradeLog[self.TradeN] = TradeData
					open('TradeLogs/{}_TradeLog_{}.txt'.format(ticker,self.logID),'a').write('{}:{}\n'.format(self.TradeN, TradeData))
					self.TradeN += 1

				elif currentSignal != LastTrade['Signal'] and currentSignal == 0 and sc > LastTrade['Price']+LastTrade['Commission']:
					ns = LastTrade['Shares']
					tc = sc*ns
					funds += tc
					TradeData = {'Timestamp': time(), 'Signal': currentSignal, 'Price': p, 'Commission': c, 'Shares': ns, 
									'TotalCost': tc,'Funds': funds,'Returns':(tc/-LastTrade['TotalCost'])-1}
					self.TradeLog[self.TradeN] = TradeData
					open('TradeLogs/{}_TradeLog_{}.txt'.format(ticker,self.logID),'a').write('{}:{}\n'.format(self.TradeN, TradeData))
					self.TradeN += 1
				
				for trade in self.TradeLog:
					print(trade, self.TradeLog[trade])
				sleep(twait)
			
			elif todaytime < tstart or todaytime > tfinish:
				print('not trading')
				if todaytime > tfinish:
					sleep(((24*3600)-todaytime)+tstart)
				elif todaytime < tstart:
					sleep(tstart-todaytime)
