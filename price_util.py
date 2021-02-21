# test print

import os
import requests
import json

mykey = os.getenv( 'NOMICS_API_KEY' )

# input: ticker symbol in string
# output: a list consisting timestamp and price of the crypto
def getBasic( id ):
	reqUrl = "https://api.nomics.com/v1/currencies/ticker?"
	key = "key=" + mykey
	ids = "&ids=" + id
	interval = "&interval=1d"
	
	response = requests.get( reqUrl + key + ids + interval )

	if( response.status_code != 200 ):
		return None
	else:
		data = response.json()[0]

		imgUrl =  "https://cryptoicons.org/api/icon/" +  id.lower() + "/400"
		return [ data['name'], data['rank'], data['price'], data['price_timestamp'], data['1d']['price_change_pct'], imgUrl ]



# input: ticker symbol in string
# output: crypto url
def getUrl( id ):
	reqUrl = "https://api.nomics.com/v1/currencies?"
	key = "key=" + mykey
	ids = "&ids=" + id

	res = requests.get( reqUrl + key + ids )

	if( res.status_code != 200 ):
		return None
	else:
		data = res.json()[0]
		return [ data['description'], data['website_url' ] ]



# input: ticker symbol in string
# output:
def getSparkline( id, s, e ):
	reqUrl = "https://api.nomics.com/v1/currencies/sparkline?"
	key = "key=" + mykey
	ids = "&ids=" + id
	start = "&start=" + s + "T00%3A00%3A00Z"
	end = "&end=" + e + "T00%3A00%3A00Z"

	res = requests.get( reqUrl + key + ids + start + end )

	if( res.status_code != 200 ):
		return None
	else:
		data = res.json()[0]
		return [ data['timestamps'], data['prices'] ]



# input: image url, image file name
# output: N/A (saves an image file at current directory)
def saveImg( url, filename ):
	res = requests.get( url )
	
	f = open( filename, "wb" )
	f.write( res.content )
	f.close()


print( getBasic( 'BTC' ) )
print( getUrl( 'BTC' ) )
#print( json.dumps( getSparkline( 'BTC', "2021-02-10", "2021-02-20" ), indent=2 ) )
#saveImg( "https://s3.us-east-2.amazonaws.com/nomics-api/static/images/currencies/btc", "1.svg"  )


