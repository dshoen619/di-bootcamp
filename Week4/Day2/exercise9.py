family=input("Whats the age of everyone who wants a ticket? Enter ages seperated by space")

family_age_list=list(family.split(" "))

print(family_age_list)
total_cost=0

for i in family_age_list:
    j=int(i)
    if j<3:
        total_cost+=0
    if 3<=j and j<=12:
        total_cost+=10
    if j>12:
        total_cost+=15
print(total_cost)

list_names=["Mark", "Ariel", "Guy", "Noah"]
new_list=[]

for i in list_names:
    print(i)
    age= int(input(f"{i}, how old are you?"))
    if int(age)<16 or int(age)>21:
        new_list.append(i)
    


list_names=new_list
print(list_names)        




