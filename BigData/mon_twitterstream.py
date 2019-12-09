import oauth2 as oauth

import urllib2 as urllib

#Les clés de notre page twitter
api_key = "bfrzljA9EmLC7uZjb5Qt6lGq9"
api_secret = "cZ7juq8ZFjVJMTxmLqzXONOqV3V3jBcHGk5StasWzARKZnQlWh"
access_token_key = "721323229470703616-IrZXRhyoG1FwKUogN4q0l8J6j1xc8F1"
access_token_secret = "MlgSOQcEBaKA1mh0NjlMCCpsVIqws80C2WkRwFX99XA0L"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url,
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

def fetchsamples():
    #liste des membres
  url = "https://api.twitter.com/1.1/lists/memberships.json"
  #url = "https://stream.twitter.com/1.1/statuses/sample.json"
  #url = "https://api.twitter.com/1.1/search/tweets.json?q=Macron&until=2019-11-22"
  #url = "https://api.twitter.com/1.1/search/tweets.json?q=Musk@limit=1000000000"

 #le lien de l'adresse de marseille
 # url = "https://api.twitter.com/1.1/search/tweets.json?q=Marseille"
  parameters = []
  response = twitterreq(url, "GET", parameters)
  for line in response:
    print(line.strip())

if __name__ == '__main__':
  fetchsamples()
