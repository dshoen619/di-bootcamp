topping=input("enter a pizza topping")
topping_list=[]
total_price=10

while topping!="quit":
    print(f"{topping} will be added to the pizza")
    topping_list.append(topping)
    total_price+=2.5
    topping=input("enter a pizza topping")



print(topping_list)
print(total_price)

    