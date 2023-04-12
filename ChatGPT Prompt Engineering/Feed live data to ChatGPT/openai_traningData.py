import openai
import json # reads json data which is response from the api
import requests # communicates with api

openai.api_key = "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"

def BasicGeneration(userPrompt): 
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content": userPrompt}]
    )
    return completion.choices[0].message.content

st.title('Bitcoin Analyzer with chatGPT Prompting with Python')
st.subheader('Analyzing Live Crypto Prices')

def GetBitCoinPrices():

    # Define the API endpoint and query parameters
    url = "https://coinranking1.p.rapidapi.com/coin/Qwsogvtv82FCd/history"
    querystring = {
        "referenceCurrencyUuid":"yhjMzLPhuIDl",
        "timePeriod":"7d"
    }

    # Define the request headers with API key and host
    headers = {
	    "X-RapidAPI-Key": "YOUR RAPID-API KEY",
	    "X-RapidAPI-Host": "YOUR RAPID-API HOST"
    }

    # Send a GET request to the API endpoint with query parameters and headers
    response = requests.request("GET", url, headers=headers, params=querystring)

    # Parse the response data as a JSON object
    JSONResult = json.loads(response.text)

    # Extract the "history" field from the JSON response
    history = JSONResult["data"]["history"]

    # Extract the "price" field from each element in the "history" array and add to a list
    prices = []
    for change in history:
        prices.append(change["price"])

    # Join the list of prices into a comma-separated string
    pricesList = ','.join(prices)

    # Return the comma-separated string of prices
    return pricesList

bitcoinPrices = GetBitCoinPrices()
  
chatGPTPrompt = f"""You are an expert crypto trader with more than 10 years of experience, 
                    I will provide you with a list of bitcoin prices for the last 7 days
                    can you provide me with a technical analysis
                    of Bitcoin based on these prices. here is what I want: 
                    Price Overview, 
                    Moving Averages, 
                    Relative Strength Index (RSI),
                    Moving Average Convergence Divergence (MACD),
                    Advice and Suggestion,
                    Do I buy or sell?
                    Please be as detailed as much as you can, and explain in a way any beginner can understand. and make sure to use headings
                    Here is the price list: {bitcoinPrices}"""

analysis = BasicGeneration(chatGPTPrompt)
print(analysis)


