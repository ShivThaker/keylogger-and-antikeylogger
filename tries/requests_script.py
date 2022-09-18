import requests


# allows us to send http requests using python
# returns a "response object" with all response data (content, encoding, status, etc)

x = requests.get('https://w3schools.com/python/demopage.htm')
print(x.text)
print(x.content)
print(x.raw)
print(x.history)