from TechnicalAnalysis import SMA, round_down
from numpy import where
import pandas

#algo
def SimpleAlgo(data_feed, MAs):
	#Basic bullS bearL
	bull, bear = 1, 0
	Signal = pandas.DataFrame()
	nMA1, nMA2 = MAs
	#SMA
	SMA(data_feed, nMA1)
	SMA(data_feed, nMA2)
	#Signal
	MA_1, MA_2 = 'SMA_'+str(nMA1), 'SMA_'+str(nMA2)
	SMAname = '{}_{}_MA_Ind'.format(nMA1, nMA2)
	Signal[SMAname] = where(data_feed[MA_1] > data_feed[MA_2], bull, where(data_feed[MA_2] > data_feed[MA_1], bear, 2))
	return Signal