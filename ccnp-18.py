import requests

r= requests.get('https://www.google.ca')
print(r.text)