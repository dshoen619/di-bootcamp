import requests
import json
import csv

headers={"content-type": "application/json"}
data={"course_id": "MATH140"}
r=requests.get("https://api.umd.io/v1/courses/list", headers=headers )



search= r.json()

counter=0
for i in search:
    counter+=1

print(counter)