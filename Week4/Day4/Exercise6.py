magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians():
    for i in magician_names:
        print(i)

# show_magicians()

def make_great():
    index_counter=0
    for i in magician_names:
        magician_names[index_counter]= i +" the Great"
        index_counter+=1

make_great()
show_magicians()





