family = {"rick": 2, 'beth': 13, 'morty': 5, 'summer': 8}


total_cost=0

for key in family:
    if family[key]<3:
        print(f"{key} you dont have to pay anything")
        total_cost+=0
    if family[key]>3 and family[key]<12:
        print(f"{key}, your ticket is $10")
        total_cost+=10
    if family[key]>12:
        print(f"{key}, your ticket is $15")
        total_cost+=15

print(total_cost)