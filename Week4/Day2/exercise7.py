favorite_fruits= input("What are your favorite fruits? (seperate with a space")

list_fruits= list(favorite_fruits.split(" "))

name_any_fruit= input("Name any fruit")

if name_any_fruit in list_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")



