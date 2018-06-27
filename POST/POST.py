import requests                                 #http://docs.python-requests.org/en
import sys                                      #sys.argv[] is an array of arguments passed to prog
r = requests.post(sys.argv[1], data = {})       #empty data, junk

print (r.status_code, r.reason)
print (r.text[:100]  + '...')                   #horrible output method
