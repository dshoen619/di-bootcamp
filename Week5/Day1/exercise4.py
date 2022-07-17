animals=[]
new_dict={}
class Zoo():

    def __init__(self,zoo_name):
        self.name=zoo_name

    def add_animal(new_animal):
        if new_animal not in animals:
            animals.append(new_animal)

    def get_animals():
        for i in animals:
            print(i)

    def sell_animal(animal_sold):
        if animal_sold in animals:
            animals.remove(animal_sold)

    def sort_animals():
        # new_dict={}
        sorted_list=sorted(animals)
        print(sorted_list)
        alphabet_list=[]
        counter=1
        for i in sorted_list:
            if len(alphabet_list)==0:
                alphabet_list.append(i)
                new_dict[counter]=alphabet_list

            if i[0]==alphabet_list[0][0] and i not in alphabet_list:
                alphabet_list.append(i)
                new_dict[counter]=alphabet_list

            if len(alphabet_list)>0 and i[0]!=alphabet_list[0][0]:
                alphabet_list=[]
                alphabet_list.append(i)
                counter+=1
                new_dict[counter]=alphabet_list

            else:
                new_dict[counter]=alphabet_list


    def get_groups():
        for i in new_dict:
            print(f"{i}:{new_dict[i]}")


    def ramat_gan_safari():
            Zoo.add_animal('panda')
            Zoo.add_animal('monkey')
            Zoo.add_animal('cat')
            Zoo.add_animal('cheetah')
            Zoo.add_animal('eel')

            Zoo.get_animals()

            Zoo.sell_animal("eel")

            Zoo.sort_animals()
            Zoo.get_groups()


Zoo.ramat_gan_safari()

# Zoo.sort_animals()
# Zoo.get_groups()