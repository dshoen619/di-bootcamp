import random 

class Dog ():
    name_list=[]
    def __init__(self, name, age, weight,):
        self.name=name
        self.age=age
        self.weight=weight



    def bark(self):
        bark_string=f"{self.name} is barking"
        return bark_string

    def run_speed(self):
        running_speed=(self.weight/self.age)*10
        return running_speed
    
    def fight(self, other_dog):
        dog_1_speed=Dog.run_speed(self)
        dog_1_weight=self.weight
        dog_1_strength= dog_1_speed*dog_1_weight

        other_dog_speed= other_dog.run_speed()
        other_dog_weight=other_dog.weight
        other_dog_strength= other_dog_speed*other_dog_weight

        if dog_1_strength>other_dog_strength:
            print(f"{self.name} wins!")
        if dog_1_strength<other_dog_strength:
            print(f"{other_dog.name} wins!")


class Petdog(Dog):

    def __init__(self,name, age, weight, trained=False):
        super().__init__(name,age,weight)
        self.trained=trained

    def train(self):
        print(Dog.bark(self))
        self.trained=True


    def play(self, *dogs):
        names_dogs=str(self.name)
        for i in dogs:
            names_dogs+=', ' +i.name
        print(f"{names_dogs} all play together")

    def do_a_trick(self):
        random_num=random.randint(0,3)
        if self.trained==True:
            if random_num==0:
                print(f"{self.name} does a barrel roll")
            if random_num==1:
                print(f"{self.name} stands on his back legs")
            if random_num==2:
                print(f"{self.name} shakes your hand")
            if random_num==3:
                print(f"{self.name} plays dead")
        else:
            print(f"{self.name} not trained")

dog2 = Petdog('Ariel', 6, 60)
dog3 = Petdog('Guy', 2, 80)
dog1 = Petdog('David', 3, 30)


dog1.train()

dog1.play(dog2, dog3)

dog3.train()
dog3.do_a_trick()
dog1.do_a_trick()



        




