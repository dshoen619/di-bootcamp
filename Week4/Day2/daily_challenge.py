#1
user_number= int(input("enter a number"))
user_length=int(input("enter a length"))

challenge_list=[]

for i in range(1,user_length+1):
    number_to_add=user_number*i
    challenge_list.append(number_to_add)


print(challenge_list)


