class Text:

    def __init__(self, sentence):
        self.sentence=sentence

    def frequence(self):
        sentence=self.sentence
        list_words=sentence.split()
        dict_words={}
        for i in list_words:
            dict_words[i]=list_words.count(i)
        print(dict_words)
    
    def most_common_word(self):
        sentence=self.sentence
        list_words=sentence.split()
        dict_words={}
        for i in list_words:
            dict_words[i]=list_words.count(i)

        most_common = max(dict_words.values())

        for k,v in dict_words.items():
            if v==most_common:
                print(k)

    def unique_words(self):
        sentence=self.sentence
        list_words=sentence.split()
        dict_words={}
        for i in list_words:
            dict_words[i]=list_words.count(i)

        for k,v in dict_words.items():
            if v==1:
                print(k)



            
f=open('the_stranger.txt')
lines_to_read=f.read()

stranger_string=""
for i in lines_to_read:
    stranger_string+=i+" "

# sentence1=Text('A good book would sometimes cost as much as a good house')

sentence1=Text(stranger_string)
sentence1.most_common_word()

