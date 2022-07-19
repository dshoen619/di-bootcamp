import string
import random


string_length_five=""
i=0

# random_index_number=random.randint(0,52)  

while len(string_length_five)<5:
    random_index_number=random.randint(0,52) 
    letter=string.ascii_letters[random_index_number]
    string_length_five+=letter

print(string_length_five)

