brand={
'name': 'Zara' ,
'creation_date': 1975 ,
'creator_name': 'Amancio Ortega Gaona' ,
'type_of_clothes': ['men', 'women', 'children', 'home'] ,
'international_competitors': ['Gap', 'H&M', 'Benetton'] ,
'number_stores': 7000 ,
'major_color':{ 
    'France': 'blue', 
    'Spain': 'red', 
    'US': ['pink', 'green']
}
}
#3
brand['number_stores']=2
#4
clients=""
for i in  brand['type_of_clothes']:
    clients+=" "+i+','

print(f"Zaras clients are those shopping for clothing for {clients}")

#5
brand['country_creation']='Spain'

#6
if 'international_competitors' in brand:
    brand['international_competitors'].append('Desigual')

#7
del brand['creation_date']

#8
print(brand['international_competitors'][2])

#9

print(brand['major_color']['US'])

#10
print(len(brand))

#11
print(brand.keys())

#12
more_on_zara={
'creation_date': 1975 ,
'number_stores': 10000
}

brand.update(more_on_zara)
print(brand)

#13 
print(brand['number_stores'])
