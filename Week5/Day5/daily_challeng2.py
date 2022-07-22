# What is a class?

# Classes are used to create new user-defined data structures that contain arbitrary information about something.a class provides structure—it’s a blueprint for how something should be defined, but it doesn’t offer any actual content itself

# What is an instance?
# While the class is the blueprint, an instance is a copy of the class with actual values, literally an object belonging to a specific class

# What is encapsulation?
# encapsulation prevents data from direct modification.

# What is abstraction?
# Abstraction in python is defined as a process of handling complexity by hiding unnecessary information from the user.
# What is inheritance?
# inheritance allows us to define a class that inherits all the methods and properties from another class.
# What is multiple inheritance?
# A class can be derived from more than one base class in Python.the features of all the base classes are inherited into the derived class.
# What is polymorphism?
# Polymorphism lets us define methods in the child class that have the same name as the methods in the parent class
# What is method resolution order or MRO?
# The Python Method Resolution Order defines the class search path used by Python to search for the right method to use in classes having multi-inheritance


class Deck():
    def __init__(self) -> None:
        Deck.setdeck(self)
    
    def setdeck(self):
        self.deck = list()
        self.suit = ['H','D', 'C', 'S']
        self.value = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        for x in self.suit:
            for y in self.value:
                card=x,y
                self.deck.append(card)

    def shuffle(self):
        Deck.setdeck(self)
        import random
        for i in range(len(self.deck)):
            x = random.randint(0,len(self.deck)-1)
            y = self.deck[x]
            self.deck[x] = self.deck[i]
            self.deck[i] = y
        print(self.deck)

    def deal(self) -> str:
        y = self.deck[0]
        del self.deck[0]
        print(self.deck,len(self.deck))
        print(y)
        return y
exercise_2 = Deck()
exercise_2.shuffle()
exercise_2.deal()
exercise_2.deal()
exercise_2.deal()
exercise_2.deal()