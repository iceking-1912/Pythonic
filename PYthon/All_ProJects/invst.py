
from alpha_vantage.timeseries import TimeSeries
from pprint import pprint


API_KEY="FT76X1HUZGUQZXME"

ts = TimeSeries(API_KEY)
# Get json object with the intraday data and another with  the call's metadata
data, meta_data = ts.get_intraday('GOOGL')
pprint(data)