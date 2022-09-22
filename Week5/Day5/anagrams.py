from anagram_checker import *



def anagrams (word):
    list_words=AnagramChecker(None).get_anagrams(word)
    if len(list_words)>0:
        print(f'Your Word:{word}')
        print("This is a valid English word")
        print(f"Anagrams for your word {list_words}")
    if len(list_words)==0:
        print(f'Your Word: {word}')
        print("This is not a valid English word")

anagrams('asdfa')