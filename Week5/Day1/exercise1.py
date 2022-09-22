cat_list={}
class Cat:

    cat_list= {}

    def __init__(self,cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
        Cat.cat_list[self.name]= self.age


first_cat= Cat(cat_name="Molly",cat_age=4)
second_cat=Cat(cat_name="Jeffrey", cat_age=2)

print(Cat.cat_list['Jeffrey'])
for i in Cat.cat_list.keys():
    print(i)

def find_oldest_cat():

    for i in Cat.cat_list.keys():
        if Cat.cat_list[i]==max(Cat.cat_list.values()):
            print(f"{i} is the oldest cat")

find_oldest_cat()

