#Recap – What is a float? What is the difference between an integer and a float?
# An integer is a number without any decimal spots. A float has decimals
# 
# Can you think of another way to generate a sequence of floats?
# Create a for loop of integers i increasing by 1 every loop. Every loop divide i by 3.3 and add that result to a list thus creating sequence of floats.
# 

float_list=[]
for i in range(3,11):
    number= i/2
    float_list.append(number)
print(float_list)
