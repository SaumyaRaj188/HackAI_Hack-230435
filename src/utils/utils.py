import os
import requests

'''
this file defines two utility functions

1 convert: will be used for parsing user input

2 get_rate: will be used for fetching exchange rates from the api
'''


#function to convert user input
def convert(secondary, min_threshold, max_threshold):
    s = secondary.split()
    tmin = min_threshold.split()
    tmax = max_threshold.split()

    tmin = [float(i) for i in tmin]
    tmax = [float(i) for i in tmax]

    dmin = dict(zip(s, tmin))
    dmax = dict(zip(s, tmax))

    return s, dmin, dmax

API_KEY = os.environ.get("CURRENCY_EXCHANGE_API") # api key is stored in environment variable so that it is not exposed in pulblic repository

BASE_URL = "https://api.apilayer.com/currency_data/live?" #THIS THE BASE URL OF THE API USED

payload = {}
headers= {
  "apikey": API_KEY
}

#function to get exchange rate of currencies 
def get_rate(secondary_currencies,base_currency="EUR"):
    '''
    this function is to fetch exchange rates of currencies

    parameters
        secondary_currencies: list of currencies whose values are to be fetched
        base_currency: str representing the currency w.r.t which other rates have to be fetched | default=EUR

    the code below will finally return a dictionary containg the values of exchange rates eg. { "INR":80.14, "AED": 4.13 }
    '''
    #building final url for fetching, eg. https://api.apilayer.com/currency_data/live?source=USD&currencies=INR,AED
    url = BASE_URL
    url+=f"source={base_currency}&currencies="
    for i in secondary_currencies:
        url+=i + ","
    url = url[:-1]
    #fetching rates
    response = requests.request("GET", url, headers=headers, data = payload) 

    #checking if fetching was successfull
    status_code = response.status_code
    assert status_code==200 #raise assertionError if some problem during fetching occured

    result = response.json()

    #converting result to out desired format
    final_dict = {}
    for i in secondary_currencies:
        final_dict[i] = result["quotes"][base_currency+i]
    return final_dict
    
#the part of code below is not executed when main.py is executed, this is only for checking
#outputs while working on this file
#so you may ignore this
if __name__=="__main__":
    print(get_rate(["INR","AED"],"EUR"))