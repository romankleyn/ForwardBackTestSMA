#Bloomberg: United States Rates & Bonds: https://www.bloomberg.com/markets/rates-bonds/government-bonds/us
from requests import *

def tbill(m = 3):
	if m not in [3,6,12]:
		raise Exception('Use T-bill yields of 3, 6 and 12')
	bbURL = 'https://www.bloomberg.com/markets/rates-bonds/government-bonds/us'
	f = 'GB{0}:GOV </div> <div class="data-table-row-cell__link-block" data-type="full"> {0} Month </div> </td>  <td class="data-table-row-cell" data-type="value">0.00</td>  <td class="data-table-row-cell" data-type="value" next-value="'.format(m)
	g = get(bbURL).text.split(f)[1].split('"')[0]
	return float(g.strip('%'))/100