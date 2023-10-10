# HackAI_Hack-230435
**HackAI IITB Techfest**

Team: Hack-230435

Members:

1. Yashi Pitti: [@YashiPi](https://github.com/YashiPi)
2. Aditya: [@adityasabkb](https://github.com/adityasabkb)
3. Saumya Raj Singh: [@SaumyaRaj188](https://github.com/SaumyaRaj188)
4. Ishita Srivastava: [@oi-taa](https://github.com/oi-taa)


## Currency Exchange Agent

This is an AI agent that utilizes **Fetch.ai’s uAgents library** to:
 1. Allows users to select their base currency and one or more foreign currencies they wish to monitor.
 2. Connects to a currency exchange API to fetch real-time exchange rates.
 3. Lets users set thresholds for alerts (e.g., notify me if 1 USD becomes more than 82.60 INR or less
than 82.55 EUR).
 4. Sends an alert/notification to the user when the exchange rate crosses the thresholds they've set.
 5. Maintain a record by storing the fetch requests to a log file with unix-timestamps.

    
**Note:** This agent fetch updated values every **60 seconds** (Values are updated at the API endpoint every 60 seconds). 
Fetch time can be edited by changing the ***period*** variable inside ***src/agents/client/client.py*** but it is not recommended as it waste API calls.


### Prerequisites (optional):
Poetry is used to create a virtual enviornment so other python
 processes do not interfere with the uagents functions
```
pip install poetry
```




### Installation:

1. Clone the git repository to your computer
```
git clone https://github.com/adityasabkb/hackAI.git
cd HackAI_Hack-230435
```


2. Create Virtual Enviornment (optional)
```
poetry init -n && poetry shell
```



3. Install Requirements
```
pip install -r requirements.txt
```

4. Adding API key to path variable
   1. Sign-in on [Currency Data API](https://apilayer.com/marketplace/currency_data-api) on APILayer to get your API key.
   2. Create .env file inside ***HackAI_Hack-230435/src/***.
   3. Add variable **CURRENCY_EXCHANGE_API=< your API key >** to the .env file inside the src folder.


### Run:

```
cd src
python main.py
```

Running the agent will prompt the user to set:
   1. Base Currency (eg. USD)
   2. One or more secondary currencies (seperated by spaces eg. JPY INR EUR)
   3. Maximum threshold values (seperated by spaces eg. 20 75 19)
   4. Minimum threshold values (seperated by spaces eg. 10 65 17)

Updated values will be printed every 60 seconds and will be saved inside the log.txt file along with the unix-timestamps.

