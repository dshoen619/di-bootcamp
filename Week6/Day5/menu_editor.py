from XP import *

def load_manager(item,cost):
    new_instance=MenuItem(item,cost)
    return new_instance

def show_user_menu():
    menu_list =['1.Insert','2.delete','3.Update','4.show menu']
    for i in menu_list:
        print(i)
    user_menu_choice=input("Pick an option(1-4)")
    if user_menu_choice=='1':
        add_item_to_menu()
    if user_menu_choice=='2':
        remove_item_from_menu()
    if user_menu_choice=='3':
        show_rest_menu()
    if user_menu_choice=='4':
        MenuItem(None,None).all()
        return


def add_item_to_menu():
        food_item=input('Enter an item to put on the menu')
        item_cost=int(input('What is the cost?'))
        instance = load_manager(food_item,item_cost)
        instance.save()
        instance.all()
        print('Item added successfully')

def remove_item_from_menu():
        MenuItem(None,None).all()
        food_item=input('Enter an item to remove the menu')
        item_cost=None
        instance = load_manager(food_item,item_cost)
        instance.delete()
        instance.all()

def show_rest_menu():
    MenuItem(None,None).all()


show_user_menu()
    