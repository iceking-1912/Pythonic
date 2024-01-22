import os
import openai
import json


openai.api_key = os.getenv("OPENAI_API_KEY")

myprompt = "Hi there"

response = openai.Completion.create(
        engine="davinci",
        prompt=myprompt,
        max_tokens=15,
)
print(response.choices[0].text)
#print(content)


