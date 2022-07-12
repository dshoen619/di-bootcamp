word=input("Enter a word")
word_dict={}
index_count=0



for i in word:
    if i in word_dict:
        word_dict[i].append(index_count)
    if i not in word_dict:
        word_dict[i]=[]
        word_dict[i].append(index_count)

    index_count+=1

print(word_dict)