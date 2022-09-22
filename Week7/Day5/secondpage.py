import requests
import json
import csv

page_counter=0

for i in range(453):

headers={"content-type": "application/json"}
data={"val":"","veterinary":False,"cytotoxic":False,"prescription":False,"isGSL":False,"healthServices":False,"isPeopleMedication":True,"fromCanceledDrags":None,"toCanceledDrags":None,"fromUpdateInstructions":None,"toUpdateInstructions":None,"fromNewDrags":None,"toNewDrags":None,"newDragsDrop":0,"pageIndex":page_counter,"orderBy":1,"types":"0"}
r=requests.post("https://israeldrugs.health.gov.il/GovServiceList/IDRServer/SearchByAdv", data=json.dumps(data), headers=headers )
search= r.json()

counter=0
for res in search:
    fields=res.keys()
    break

rows=[]
for res in search:
    rows.append(res)


with open('Drugs_Intel_Assignment copy.csv', 'a') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
    for i in rows:

        writer.writerow(i)
    
    page_counter+=1