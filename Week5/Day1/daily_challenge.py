animal_dict={}
animals_list=[]
animals_list_sorted=[]
class Farm():

    def __init__(self, farm_name):
        
        self.name= farm_name
    
    def print_farm_name(name):
        print(f"{name}'s farm'")

    def add_animal(animal_name, number):

        if animal_name in animal_dict.keys():
            animal_dict[animal_name]+=number
        else:
            animal_dict[animal_name]=number 

    def get_info():
        return "E-I-E-I-O!"

    def get_animal_types():
        for i in animal_dict.keys():
            animals_list.append(i)
        animals_sorted_list=sorted(animals_list)
        print(animals_sorted_list)
    
    def get_short_info():
        animals_sorted_list=sorted(animals_list)
        print(f"Mcdonald's Farm has {animals_sorted_list[0]}'s',{animals_sorted_list[1]}'s', and {animals_sorted_list[2]}")


macdonald=Farm(farm_name="Mcdonald")
Farm.print_farm_name("Mcdonald")

Farm.add_animal('cow',5)
Farm.add_animal('sheep',1)
Farm.add_animal('sheep',1)
Farm.add_animal('goat',12)

print(animal_dict)
print(Farm.get_info())

Farm.get_animal_types()
Farm.get_short_info()




