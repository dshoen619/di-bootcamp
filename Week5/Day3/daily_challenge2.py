from translate import Translator



french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 

translate_dict={}

for word in french_words:
    translator= Translator(to_lang="en", from_lang="fr")
    translation = translator.translate(word)
    translate_dict[word]=translation


print(translate_dict)
