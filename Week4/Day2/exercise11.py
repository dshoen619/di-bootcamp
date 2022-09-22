sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches=[]

for i in range(0,2):
    sandwich_orders.append("Pastrami sandwich")

print(sandwich_orders)

print("The deli has run out of pastrami")

while sandwich_orders.count("Pastrami sandwich")>0:
    sandwich_orders.remove("Pastrami sandwich")

for i in sandwich_orders:
    finished_sandwiches.append(i)

for j in finished_sandwiches:
    print(f"I made your {j} sandwich")


