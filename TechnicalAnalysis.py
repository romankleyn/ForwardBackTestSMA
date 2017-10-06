import pandas

def round_down(n, r = -1):
	n = int(n)
	if n < 100: r = -1
	return int(str(n)[:r]+(-r*'0'))

def SMA(dataset, n = 14):
    dataset['SMA_'+str(n)] = dataset.CLOSE.rolling(n).mean()
    
def EMA(dataset, n = 14):
    emaName = 'EMA_'+str(n)
    sma = dataset.CLOSE.rolling(window=n, min_periods=n).mean()[:n]
    rest = dataset.CLOSE[n:]
    ema = pandas.concat([sma, rest]).ewm(span=n, adjust=False).mean()
    dataset[emaName] = ema
    
def PERCENT(dataset):
    dataset['PERCENT'] = dataset.CLOSE.pct_change()
    
def STDEV(dataset, n = 14):
    stdName = 'STDEV_'+str(n)
    dataset[stdName] = dataset.CLOSE.rolling(window=n).std()
    
def BBAND(dataset, n = 14, dev = 2):
    emaName = 'EMA_'+str(n)
    stdName = 'STDEV_'+str(n)
    EMA(n)
    STDEV(n)
    upperband = 'UBAND_'+str(n)+'_'+str(dev)
    lowerband = 'LBAND_'+str(n)+'_'+str(dev)
    ema, std = dataset[emaName], dataset[stdName]
    uBand = ema + (std*dev)
    lBand = ema - (std*dev)
    dataset[upperband], dataset[lowerband] = uBand, lBand
        
def RSI(dataset, n = 14, column = 'CLOSE'):
    ### wilder's RSI
    rsiName = 'RSI_'+str(n)
    data = dataset[column].diff()
    dUp, dDown = data.copy(), data.copy()
        
    dUp[dUp < 0] = 0
    dDown[dDown > 0] = 0

    rollUp = dUp.rolling(n).mean()
    rollDown = dDown.rolling(n).mean().abs()
        
    RS = rollUp / rollDown
    dataset[rsiName] = 100 - (100/(1+RS))