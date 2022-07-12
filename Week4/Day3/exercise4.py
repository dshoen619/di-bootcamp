users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
disney_users_A={}
disney_users_B={}
disney_users_C={}
disney_users_D={}
disney_users_E={}
j=0

#1
for i in users:
    disney_users_A[i]=j
    j+=1

print(disney_users_A)

#2
j=0
for i in users:
    disney_users_B[j]=i
    j+=1

print(disney_users_B)

#3
sorted_users=sorted(users)
j=0

for i in sorted_users:
    disney_users_C[i]=j
    j+=1

print(disney_users_C)

#4
j=0
for i in users:
    if 'i' in i:
        disney_users_D[i]=j
        j+=1

print(disney_users_D)

j=0
for i in users:
    if i[0]=='M' or i[0]=='P':
        disney_users_E[i]=j
        j+=1

print(disney_users_E)