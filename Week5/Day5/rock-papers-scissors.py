standings={'Win':0, 'loss':0, 'draw': 0}

def get_user_menu_choice():
    choice_menu={1:'Play a new game', 2:'Show scores', 3:'Quit'}
    print(choice_menu)

def print_results(results):
    for i in results:
        print(f"{i} : {results[i]}")
    print("Thanks for playing")

def main():

    get_user_menu_choice()
    user_choice=input("Choose from menu; 1, 2, or 3")
    while user_choice!='1' and user_choice!='2' and user_choice!='3':
        get_user_menu_choice()
        user_choice=input("Choose from menu; 1, 2, or 3")

    while user_choice!='3':
        if user_choice=='1':
            from game import play
            standings[play()]+=1
        if user_choice=='2':
            print_results(standings)
            
        get_user_menu_choice()
        user_choice=input("Choose from menu; 1, 2, or 3")
    if user_choice=='3':
        print_results(standings)
        print("Goodbye")
        return

main()


