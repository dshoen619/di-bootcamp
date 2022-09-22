from re import sub
import requests
import json
import random
import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'davidshoen1'
DATABASE = 'w6d5_countries'

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, dbname=DATABASE )
cursor = connection.cursor()

url = 'https://restcountries.com/v3.1/all'

data = requests.get(url)
data=data.json()




for i in range(10):
    rand_country_index=random.randint(0,len(data))

    name=data[rand_country_index]['name']['common']

    capital= str(data[rand_country_index]['capital'])
    capital_stripped=capital.strip("[]")

    flag= data[rand_country_index]['flags']['png']

    subregion=data[rand_country_index]['subregion']

    population=data[rand_country_index]['population']
    query5= f"Insert into countries(name,capital,flag, subregion, population) Values ('{name}',{(capital_stripped)},'{flag}','{subregion}','{population}')"
    cursor.execute(query5)
    connection.commit()


    print(name)