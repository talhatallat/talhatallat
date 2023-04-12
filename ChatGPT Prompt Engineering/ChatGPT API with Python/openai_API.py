import openai

openai.api_key = "YOUR API KEY HERE"

def BasicGeneration(userPrompt):
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content": userPrompt}]
    )
    return completion.choices[0].message.content


prompt = "Who is current Prime Minister of UK?"


response = BasicGeneration(prompt)
print(response)
