my_fav_numbers = set([1, 2, 3,4])

my_fav_numbers.add(13)
my_fav_numbers.add(16)

my_fav_numbers.remove(16)
print(my_fav_numbers)

friend_fav_numbers=set([10,20,30,40])

our_fav_numbers=my_fav_numbers

for i in friend_fav_numbers:
    our_fav_numbers.add(i)

print(our_fav_numbers)
    