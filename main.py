from pprint import pprint
import requests

countries = requests.get( "https://restcountries.com/v3.1/name/russia").json()
pprint( countries)

requests.get( "https://restcountries.com/v3.1/name/russia").json()



import sys
print(sys.executable)
