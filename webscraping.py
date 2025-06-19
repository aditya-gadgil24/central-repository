# SHREE

# code block
import requests
url = 'https://en.wikipedia.org/wiki/Nvidia'
content = requests.get(url)
print(content.text)



