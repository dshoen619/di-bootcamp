import requests, json, csv


def courselist_sql():
    counter=1

    results=['a']
    while len(results)>0:
        course_list=[]
        headers={"content-type": "application/json"}
        page={'page':counter}
        r= requests.get(f"https://api.umd.io/v1/courses", headers=headers, params=page)
        results=r.json()
        if not results:
            break
        fields=results[0].keys()
        counter+=1

        for res in results:
            course_list.append(res)

        with open('CourseInfo.csv', 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = fields)
            if counter==2:
                writer.writeheader()
            for i in course_list:

                writer.writerow(i)

def add_professors():
    counter=1
    results=['a']
    while len(results)>0:
        course_list=[]
        headers={"content-type": "application/json"}
        page={'page':counter}
        r= requests.get(f"https://api.umd.io/v1/professors", headers=headers, params=page)
        results=r.json()

        fields=results[0].keys()
        counter+=1

        for res in results:
            course_list.append(res)

        with open('professor_list.csv', 'a') as csvfile:

            writer = csv.DictWriter(csvfile, fieldnames = fields)
            if counter==2:
                writer.writeheader()
            for i in course_list:
                writer.writerow(i)

add_professors()