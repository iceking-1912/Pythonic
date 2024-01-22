
import requests

protocol='https://'
website = input('Wed Site Name-')

url = protocol + website

print(url)

response = requests.get(url)

print(response.true)
