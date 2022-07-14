
board= [ list("1|2|3"),
        "---------------------------",
        list("4|5|6"),
        "---------------------------",
        list("7|8|9")]

def tic_tac_toe():
    count_turns=0
    guess_list=[]
    while count_turns<10:

        for i in board:
            print(i)
        counter_2=0
        user_o=str(input("o, Your move"))
        while user_o in guess_list:
            print("This spot is already occupied, guess again")
            user_o=str(input("o, Your move"))
        guess_list.append(user_o)
        

        counter_row1=0
        print(" ")
        print(" ")
        for row in board:
            counter_number=0
            for number in row:
                if number==user_o:
                    board[counter_row1][counter_number]='o'
                counter_number+=1
            counter_row1+=1
            print(row)

        print(" ")
        print(" ")

        # -------Horizontal check---------

        if board[0][0]==board[0][2]==board[0][4]:
            print("Winner!")
            break
        if board[2][0]==board[2][2]==board[2][4]:
            print("Winner!")
            break
        if board[4][0]==board[4][2]==board[4][4]:
            print("Winner!")
            break
        # ------- End Horizontal check---------
        
        #---------Vertical Check---------------
        if board[0][0]==board[2][0]==board[4][0]:
            print("Winner!")
            break
        if board[0][2]==board[2][2]==board[4][2]:
            print("Winner!")
            break
        if board[0][4]==board[1][4]==board[4][4]:
            print("Winner!")
            break
        #--------- End Vertical Check---------------

        #---------Diagnols Check--------------------
        if board[0][0]==board[2][2]==board[4][4]:
            print("Winner!")
            break
        if board[0][4]==board[2][2]==board[4][0]:
            print("Winner")
            break
        #---------End Diagnols Check--------------------

        user_x=str(input("x, Your move"))
        while user_x in guess_list:
            print("This spot is already occupied, guess again")
            user_x=str(input("x, Your move"))
        guess_list.append(user_x)


        counter_row2=0
        for row in board:
            counter_number=0
            for number in row:
                if number==user_x:
                    board[counter_row2][counter_number]='x'
                counter_number+=1
            counter_row2+=1
            # print(row)

        print(" ")
        print(" ")
        # ---------- Horizontal check---------
        if board[0][0]==board[0][2]==board[0][4]:
            print("Winner!")
            break
        if board[2][0]==board[2][2]==board[2][4]:
            print("Winner!")
            break
        if board[4][0]==board[4][2]==board[4][4]:
            print("Winner!")
            break
        # ------- End Horizontal check---------
        
        #---------Vertical Check---------------
        if board[0][0]==board[2][0]==board[4][0]:
            print("Winner!")
            break
        if board[0][2]==board[2][2]==board[4][2]:
            print("Winner!")
            break
        if board[0][4]==board[1][4]==board[4][4]:
            print("Winner!")
            break
        #--------- End Vertical Check---------------

        #---------Diagnols Check--------------------
        if board[0][0]==board[2][2]==board[4][4]:
            print("Winner!")
            break
        if board[0][4]==board[2][2]==board[4][0]:
            print("Winner")
            break
        #---------End Diagnols Check--------------------

        
        count_turns+=1





tic_tac_toe()






