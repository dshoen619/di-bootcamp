def random_module():
    user_number=int(input("Enter a number between 1-100"))
    while user_number>100 or user_number<1:
        user_number=int(input("Enter a number between 1-100"))

    import random

    random_number=random.randint(1,100)

    if user_number==random_number:
        print("Success, Same number")
    else:
        print(f"Different numbers. Your number:{user_number}, Comp_number:{random_number}")

random_module()
