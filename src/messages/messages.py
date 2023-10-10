from uagents import Model

'''
this file defines basic message types which will be used by the agents
'''

class FetchRequest(Model):
    '''
    Message model for Fetch request
    client agent will send fetch requests to fetcher agent
    the message will contain two variables,
    base_currency : string eg. USD, AED, INR
    secondary_currencies: list of currencies whose rates have to be fetched eg. [INR,JPY,CAD]
    '''
    base_currency: str
    secondary_currencies: list

class FetchResponse(Model):
    '''
    Message model for fetch response
    after fetching required data the fetcher will return
    message containing two variables
    success: True if rates were successfully fetched, False otherwise
    rates: dictionary containg exchange rates of secondary currencies with respect to base currency eg. { "INR":80.14, "AED": 4.13 }
    '''
    success: bool
    rates: dict

