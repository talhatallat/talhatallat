# Advance prompting -- ask chatGPT to perform analysis over the imported data

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
