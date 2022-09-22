class Game:

    def __init__(self, user_item,computer_item):
        self.user_item=user_item
        self.computer_item=computer_item

    def get_user_item(self, user_item):
        self.user_item=input("Select rock, paper, or scissors")
        while self.user_item.lower()!='rock' and self.user_item.lower()!='paper' and self.user_item.lower()!='scissors' :
                self.user_item=input("Select rock, paper, or scissors")        
        return self.user_item.lower()
    
    def get_computer_item(self, computer_item):
        import random
        game_list=['rock','paper','scissors']
        self.computer_item=random.choice(game_list)
        return self.computer_item

    def get_game_result(self,user_item,computer_item):

        user= Game.get_user_item(self,user_item)
        computer= Game.get_computer_item(self,computer_item)

        if user=='paper' and computer=='scissors':
            result='loss'
        if user=='scissors' and computer=='rock':
            result='loss'
        if user=='rock' and computer=='paper':
            result='loss'
        if user==computer:
            result='draw'
        if user=='paper' and computer=='rock':
            result='Win'
        if user=='scissors' and computer=='Paper':
            result='Win'
        if user=='rock' and computer=='scissors':
            result='Win'
        return(result)


def play():
    g1=Game(None,None)
    return g1.get_game_result(None,None)

