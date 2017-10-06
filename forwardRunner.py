from Forwardtest import test
data_interval = 'Daily'
try:
	APIKEY = input('APIKEY: ')
	if APIKEY == 'demo' or APIKEY == '':
		test().live(data_interval = 15, freqr = 1)
	else:
		data_interval = int(input('Time Interval: '))
		print('using {} interval'.format(data_interval))
except:
	pass
test(APIKEY = APIKEY).live(ticker = input('Ticker symbol: '), data_interval = data_interval, freqr = int(input('Frequecny min: ')))
