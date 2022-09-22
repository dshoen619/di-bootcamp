def get_random_temp(season):
    import random
    if season=='winter':
        random_temp=random.randint(-10,0)
    if season=='spring':
        random_temp=random.randint(17,23)
    if season=='summer':
        random_temp=random.randint(24,40)
    if season=='fall':
        random_temp=random.randint(1,16)
    
    return random_temp

def main():
    user_season=input("What season: fall, winter, spring, summer?")
    random_temp_c= get_random_temp(user_season)
    print(f"The temperature right now is {random_temp_c} degrees Celsius")
    if random_temp_c<0:
        print("Brrr thats freeezing! Wear something warm")
    if random_temp_c>0 and random_temp_c<=16:
        print("Dont forget your coat")
    if random_temp_c>16 and random_temp_c<=23:
        print("Wear a coat but maybe leave the mittens at home")
    if random_temp_c>23 and random_temp_c<=32:
        print("Wear a parka or sweashirt")
    if random_temp_c>32 and random_temp_c<=40:
        print("Its hot out today")

main()





