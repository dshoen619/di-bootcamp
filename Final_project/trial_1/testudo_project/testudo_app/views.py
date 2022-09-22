from django.shortcuts import render
import sys
import requests
import csv

def courselist_sql():
    headers={"content-type": "application/json"}
    r= requests.get("https://api.umd.io/v1/courses/list", headers=headers )
    results=r.json()

    list_courses=[]
    for i in results:
        list_courses.append(i['course_id'])

    for i in list_courses:
        url = f"https://api.umd.io/v1/courses/{i}"
        s = requests.get(url, headers=headers)
        results2=s.json()


    for res in results2:
        fields=res.keys()       
        break
    
    full_info=[]
    for info in results2:
        full_info.append(info)

    with open('schedule_classes.csv', 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
    
        for i in full_info:
            writer.writerow(i)
            


    return list_courses


courselist_sql()

