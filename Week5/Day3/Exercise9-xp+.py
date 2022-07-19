from faker import Faker

fake=Faker()
users=[{'name':"",'address':"",'language_code':""}]

for i in users:
    for j in i:
        if j=='name':
            i[j]=fake.name()
        if j=='address':
            i[j]=fake.address()
        if j=='language_code':
            i[j]=fake.country()
print(users)