from uagents import Agent,Context
from messages import *
from utils import convert
from agents.fetcher import fetcher



'''

this file defines the client agent which is responisble for
periodically sending displaying exchange rates to user
and displaying alerts when required

'''
#Fetch Time
period = 60.0

#taking inputs from user
base_currency = input("enter base currency eg. USD: ")
secondary_currencies = input("enter currencies to be monitored\nwith spaces between them eg . JPY INR EUR : ")
max_threshold = input("enter maximum thresholds for respective currencies eg. 20 75 19: ")
min_threshold = input("enter minimum thresholds for respective currencies eg. 10 65 17: ")

secondary_currencies, min_threshold, max_threshold = convert(secondary_currencies, min_threshold, max_threshold)

#this is the client agent which will send periodic request to fetcher agent
#after recieving rates, it will display rates and alerts
client = Agent(name="Clinet Agent")

@client.on_interval(period=period, messages= FetchRequest)
async def fetch_rates(ctx: Context):
    '''
    this is a periodic asynchronus funtion for sending fetch request
    to the fetcher agent
    '''
    await ctx.send(fetcher.address, FetchRequest(base_currency=base_currency, secondary_currencies=secondary_currencies)
)

@client.on_message(FetchResponse)
async def print_rates(ctx: Context,_sender: str, msg: FetchResponse):
    '''
    this function defines the behaviour of client agent when
    it recieves message from fetcher agent
    '''
    if msg.success:
        #displays rates if they were fetched successfully
        
        #the loop displays same rates 30 time every two seconds
        #as exchange rates update frequency is 1 min

        #creating log line which will be added to log.txt
        ctx.logger.info(f"rates are: {msg.rates}  w.r.t base {base_currency}")
        
        #checking for threshold violation
        for i in msg.rates.keys():
            if (msg.rates[i] >= max_threshold[i]) or (msg.rates[i]<=min_threshold[i]):
                alert_msg = f"ALERT!! {i} is crossing threshold"
                ctx.logger.critical(alert_msg)
            
    else:
        #displays error if error occured during fetching rates
        ctx.logger.error("Not able to fetch rates")
        
            

    