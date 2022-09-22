word_list=[]
class AnagramChecker():
    def __init__(self, file1):
        self.file1=open('anagrams.txt','r')


    def is_valid_word(self, word):
        real_word=bool
        self.word=word
        for i in self.file1:
            word_list.append(i.strip('\n'))
        # print(word_list)
        if self.word.upper() not in word_list:
            print("Not here, Try again with new word")
            real_word=False
            return real_word
        else:
            real_word=True
            return real_word

    def get_anagrams(self,word):
        self.word=word
        x= AnagramChecker(None).is_valid_word(self.word)
        anagram_list=[]
        if x== True:
            for i in word_list:
                if sorted(self.word.upper())==sorted(i):
                    anagram_list.append(i)
        return anagram_list



# AnagramChecker(None).get_anagrams('hate')