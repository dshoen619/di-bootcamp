# 1
for x in range(1,5):
    print("Hello world")

#2
result= (99**3)*8
print(result)

#3

# >>> 5 < 3  # False
# >>> 3 == 3  # True
# >>> 3 == "3" #Fasle
# >>> "3" > 3  #False
# >>> "Hello" == "hello" #True

# 4

computer_brand="Apple"

sentence= "I have a "+computer_brand+" computer"
print(sentence)

#5

name = "david"
age=26
shoe_size=11
info= f"Hello, my name is {name}. I am {age} years old and I have a shoe size of {shoe_size}"
print(info)

#6
a=3
b=2

if a>b:
    print("Hello world")

#7
number = input("Enter a number")
if int(number)%2==0:
    print("even")
else:
    print("odd")

#8
name ="david"
user_name=input("whats your name?")

if name==user_name:
    print("No Way!")
else:
    print("we dont have the same name but that pretty cool")

#9

height_inches= input("whats your height in inches")
height_cm= int(height_inches)*2.54

if height_cm>145:
    print("You can ride")
else:
    print("grow some more")
