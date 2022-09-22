
class Dog ():
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



dog1 = Dog('David', 3, 30)
dog2 = Dog('Ariel', 6, 60)
dog3 = Dog('Guy', 2, 80)

print(dog1.bark())
print(dog2.run_speed())
dog3.fight(dog2)


