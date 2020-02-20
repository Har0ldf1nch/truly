import requests
import urllib


site = raw_input('Page URL:')
check = requests.get(site).status_code
if check==200:
 print 'Connection Succesfull'
 web_code = urllib.urlopen(site).read()
 if 'WordPress' in web_code:
  print 'Processing...'
  print 'Its a Wordpress Site'
  site = site + '/?author=1'
  print (site)
 else:
  print 'Its not a Wordpress Site'

else: 
 print 'cannot reach webpage'
	


