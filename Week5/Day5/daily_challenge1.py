import requests
import time

resp=requests.get('https://www.google.com/')
print(resp.elapsed.total_seconds())