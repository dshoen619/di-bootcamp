matrix=[
    '7i3',
    'Tsi',
    'h%x',
    'i #',
    'sM ',
    '$a ',
    '#t%',
    '^r!',
]
counter=0
coded_string=""
decoded_string=""
while counter<3:
    for string_object in matrix:
        coded_string+=string_object[counter]
    counter+=1
    
length=len(coded_string)

for i in range(length):
    if coded_string[i-1]==" ":
        continue
    if coded_string[i].isalpha()==True:
        decoded_string+=coded_string[i]
    if coded_string[i].isalpha()==False and (coded_string[i-1].isalpha()==False) and i!=0:
        decoded_string+=" "

print(decoded_string)




