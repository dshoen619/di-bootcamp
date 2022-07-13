

def random():
    import random
    user_number=int(input("Enter a number between 1-100"))
    while user_number<1 or user_number>100:
        user_number=int(input("Enter a number between 1-100"))
    random_number= random.randint(1,100)

    if user_number==random_number:
        print("Congrats you have the same number!")
    if user_number!=random_number:
        print(f"Sorry, you failed :( Your Number: {user_number}; Random Number: {random_number}")


random()

