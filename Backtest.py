import pandas
from numpy import where
from TechnicalAnalysis import SMA
from rfRate import tbill
from AlphaVantageCo import History
'''!!!!!-----NOTE-----!!!!!
>>>Assumptions:
>>>Algo does not sell at a loss and waits for rebound.
>>>Default Commisions are based on interactive broker US exchange rates.
>>>assuming all orders are fully filled instantly at according price. 
>>>risk-free rate is based on Tbill because of short holding period and freq. Options of [3,6,12].
>>>Tbill Data = Bloomberg: United States Rates & Bonds - https://www.bloomberg.com/markets/rates-bonds/government-bonds/us
>>>Market is based on SPY ETF by default
>>>Stock Data = AlphaVantage.co
!!!!!-----NOTE-----!!!!!'''
class Backtest:
	def __init__(self, ticker = 'MSFT', period = 'max', nMA1 = 4, nMA2 = 8, tbill = 3, 
		         funds = 100000, commissionPerShare = 0.0035, maxCommissionPercent = .005, 
		         mkt = 'SPY', freqt = 'EOD', APIKEY = 'demo'):
		
		self.ticker = ticker.upper()
		self.dataSet = History(self.ticker, APIKEY=APIKEY, interval = freqt)
		if period != 'max':
			self.dataSet = self.dataSet.tail(period)
			self.period = period
		else:
			self.period = len(self.dataSet)

		if nMA1 > nMA2:
			nMA1, nMA2 = nMA2, nMA1

		self.nMA1, self.nMA2=  nMA1, nMA2
		SMA(self.dataSet, nMA1)
		SMA(self.dataSet, nMA2)

		self.signals()
		self.simulation(funds, commissionPerShare, maxCommissionPercent)

		if APIKEY != 'demo':
			self.SPdata = History(ticker = mkt, APIKEY = APIKEY, interval = freqt)
			if period != 'max':
				self.SPdata = self.SPdata.tail(period)
			self.ratios(mkt, tbill)
		else:
			print('|---Cannot do ratios without comparison data---|\n|---Please visit alphavantage.co for a free APIKEY to get other data---|')

	def signals(self):
		bull, bear, cross = 'bull', 'bear', 'cross'
		MA_1, MA_2 = 'SMA_'+str(self.nMA1), 'SMA_'+str(self.nMA2)
		self.SMAname = '{}_{}_MA_Ind'.format(self.nMA1, self.nMA2)
		self.dataSet[self.SMAname] = where(self.dataSet[MA_1] > self.dataSet[MA_2], bull, where(self.dataSet[MA_2] > self.dataSet[MA_1], bear, where(self.dataSet[MA_1] == self.dataSet[MA_2], cross, '')))

	def simulation(self, funds, commissionPerShare, maxCommissionPercent):
		self.commissionPerShare, self.maxCommissionPercent = commissionPerShare, maxCommissionPercent
		ifunds,bull,bear = funds,'bull','bear'
		data = self.dataSet[['CLOSE', self.SMAname]]
		date = self.dataSet.index.values
		simLedger, dv, n = {}, 0, 1

		try:
			hp = 0 
			for d in data.values:
				p,sig,ret = d[0],d[1],0
				#print(p,sig,ret)
				
				#Long stock initally 
				if n == 1 and sig == bull:
					c = min(commissionPerShare, maxCommissionPercent*p)
					pc = p+c
					shares = int(funds/pc)
					funds -= (pc*shares)
					simLedger[n] = {'Date': date[dv],'Price': p,'Commission': c,'Signal': sig, 'Shares': shares, 'Funds': funds, 'Ret': ret, 'HP':0}
					n += 1

				#After first long pattern continues
				elif n > 1 and sig != simLedger[n-1]['Signal']:
					#bearish and profitable
					if sig == bear and p > simLedger[n-1]['Price']:
						shares = simLedger[n-1]['Shares']
						c = min(commissionPerShare, maxCommissionPercent*p)
						funds += ((p-c)*shares)
						ret = (funds/(simLedger[n-1]['Funds']+((simLedger[n-1]['Price']+simLedger[n-1]['Commission'])*simLedger[n-1]['Shares'])))-1
						simLedger[n] = {'Date': date[dv],'Price': p,'Commission': c,'Signal': sig, 'Shares': shares, 'Funds': funds, 'Ret': ret, 'HP':hp}
						n+=1
						#print(ret)

					elif sig == bull:
						c = min(commissionPerShare, maxCommissionPercent*p)
						pc = p+c
						shares = int(funds/pc)
						funds -= (pc*shares)
						hp = 0 
						simLedger[n] = {'Date': date[dv],'Price': p,'Commission': c,'Signal': sig, 'Shares': shares, 'Funds': funds, 'Ret': ret, 'HP':hp}
						n+=1
				hp += 1
				dv += 1
		except KeyError:
			pass

		if simLedger[n-1]['Signal'] == bear:
			tRet = (simLedger[n-1]['Funds']/ifunds)-1
		else:
			tRet = ((simLedger[n-1]['Funds']+((simLedger[n-1]['Price']+simLedger[n-1]['Commission'])*simLedger[n-1]['Shares']))/ifunds)-1
		hold_ret = (self.dataSet['CLOSE'][-1]/(self.dataSet['CLOSE'][0]+min(self.commissionPerShare, self.maxCommissionPercent*self.dataSet['CLOSE'][0])))-1
		self.tRet = tRet
		
		#Avg Return
		avgR = [simLedger[x]['Ret'] for x in range(1,len(simLedger)+1) if simLedger[x]['Signal'] == bear]
		le = len(avgR)
		if le > 0:
			avgRet = sum(avgR)/len(avgR)
		else:
			avgRet = sum(avgR)/1
		
		#Holding period
		li = [simLedger[x]['HP'] for x in simLedger if simLedger[x]['Signal'] == 'bear']
		la = len(li)
		if la > 0:
			at = sum(li)/len(li)
		else:
			at = sum(li)/1
		self.HP = sum(li)

		#Trade Log
		print('Sim-Trade Log')
		for sx in simLedger:
			print(sx,simLedger[sx])
		#Non Mkt Ratios
		print('Total Return:',self.tRet)
		print('Buy & Hold return:',hold_ret)
		print('Buy & Hold Excess Return:',tRet-hold_ret)
		print('AVG Return for {} & {} in {}: {}%'.format(self.nMA1, self.nMA2, self.period, round(avgRet*100, 5)), avgR)
		print('Avg holding period:', at,'days -- Total holding period:', self.HP,'days ->',li,'\n')

	def ratios(self, mkt, m):
		#RiskFree is set to mimic return if money was invested into Tbills instead: rf adjusted to backtest period with simple intrest --> DailyTbill*period
		rf = (tbill(m)/365)*self.period
		spRet = (self.SPdata['CLOSE'][-1]/(self.SPdata['CLOSE'][0]+min(self.commissionPerShare, self.maxCommissionPercent*self.SPdata['CLOSE'][0])))-1
		dataClose, spClose = self.dataSet['CLOSE'].pct_change(), self.SPdata['CLOSE'].pct_change()
		stdp, stdm = dataClose.std(), spClose.std()
		corr = spClose.corr(dataClose)
		cov = spClose.cov(dataClose)
		#Beta: ρP,M * (σP / σM)
		beta = corr*(stdp/stdm)
		beta2 = cov/spClose.var()
		#print(beta, beta2)
		#Sharpe: (rP – rF) / σP ||all in relation to the period of test, making rf daily simple return||
		sharpe = (self.tRet-rf)/stdp
		#Jensen: (rP ‐ rF) ‐ βP * (rM ‐ rF)
		jensen = (self.tRet-rf)-(beta*(spRet-rf))
		#M^2: rF + (rP – rF) * (σM / σP)
		m2 = rf + ((self.tRet-rf) * (stdp/stdm))
		#Treynor: (rP – rF) / βP
		treynor = (self.tRet-rf)/beta
		#Information Ratio: (rP-rM)/Sp-i
		inforatio = (self.tRet-spRet)/(stdp-stdm)
		#diff adjusted returns
		print('Using {} for market and {} Month T-Bill yield for risk-free rate'.format(mkt,m))
		print('{} Adjusted Returns+:\nCorr: {}\nBeta: {}\nSharpe: {}\nJensen: {}\nM^2: {}\nTreynor: {}\nInformation Ratio: {}\nMarket Excess: {}\nRisk-Free Excess: {}\n'.
			format(self.ticker, corr, beta, sharpe, jensen, m2, treynor, inforatio, self.tRet-spRet,self.tRet-rf))
		print('Market Return',spRet,'\nRisk-Free Return','{} in {} days'.format(rf, self.period))