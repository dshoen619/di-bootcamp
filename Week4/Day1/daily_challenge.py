user_string=input("Enter a string")

while len(user_string)<10:
    print("string not lon123456789g enough")
    user_string=input("enter a string")
while len(user_string)>10:
    print("string is too long")
    user_string=input("enter a string")

print(user_string[0])
print(user_string[9])

new_string=""
for letter in user_string:
    new_string+=letter
    print(new_string)
