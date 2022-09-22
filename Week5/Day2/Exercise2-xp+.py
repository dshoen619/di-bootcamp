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

class TheIncredibles(Family):
    
    def __init__(self, members,last_name):
        self.members=members
        self.last_name=last_name

    def use_power(self):
        for i in self.members:
            if i['age']>18:
                print(i['power'])
            else:
                raise Exception(f"{i['name']} under 18")

    def incredible_presentation(self):
        for i in self.members:
            print(f"{i['name']} {self.last_name} has a suuper power of {i['power']}")
        

        


family_list_1= [
    {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
    {'name':'Sarah','age':19,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
]

family1=Family(family_list_1,'Shoen')
family1_incredible=TheIncredibles(family_list_1,'Shoen')

family1_incredible.use_power()

family1_incredible.born(fname='Jack', age=2, gender='Male', is_child=True, power='Unkown Power', incredible_name='Baby Jack')
family1_incredible.incredible_presentation()

