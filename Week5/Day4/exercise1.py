def get_words_from_file():
    words_list=[]
    f=open('sowpods.txt')
    for line in f:
        words_list.append(line)
    return words_list

def get_random_sentence(length):
    words_list=get_words_from_file()
    import random
    random_sentence_list=[]
    for i in range(0,length):
        random_index=random.randint(0,len(words_list))
        chosen_word=words_list[random_index].strip('\n')
        random_sentence_list.append(chosen_word)
    
    random_sentence_string=""
    for i in random_sentence_list:

        random_sentence_string+=i.lower()+" "


    print(random_sentence_string)


def main():
    print("This function will create a sentence of your desired length between 2 and 20 words")
    length=input("How many words in your sentence? (2-20)")

    if length.isnumeric()==False:
        print('INVALID INPUT. GOODBYE')
        return
    if int(length)<2 or int(length)>20:
        print("INVALID INPUT. GOODBYE")
        return
    else:
        get_random_sentence(int(length))

    


main()
