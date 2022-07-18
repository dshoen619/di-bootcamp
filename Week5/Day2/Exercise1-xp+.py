class Family():

    def __init__(self, members,last_name):
        self.members=members
        self.last_name=last_name

    def born(self, fname, age, gender, is_child):
        self.fname=fname
        self.age=age
        self.gender=gender
        self.is_child=is_child

        new_dict={'name': self.fname, 'age':self.age, 'gender':self.gender, 'is_child':self.is_child}
        self.members.append(new_dict)
        print(self.members)
        print("Congratulations")
    
    def is_18(self,name):
        self.name=name
        for i in self.members:
            if i['name']==self.name:
                if i['age']>18:
                    return True
                else:
                    return False
    
    def family_presentation(self):
        for i in self.members:
            print(f"{i['name']} {self.last_name}")
        


family_list_1= [
    {'name':'Michael','age':20,'gender':'Male','is_child':False},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False}
]

family1=Family(family_list_1,'Shoen')

family1.born('David',26, 'Male', False)

print(family1.is_18('Michael'))

family1.family_presentation()

