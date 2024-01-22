import os
import openai

openai.api_key = "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 "
 
response = openai.Completion.create(
engine="davinci-codex",
prompt="Hi My name is ",
temperature=0,
max_tokens=64,
top_p=1,
frequency_penalty=0,
presence_penalty=0
    )
print(response.choices)
