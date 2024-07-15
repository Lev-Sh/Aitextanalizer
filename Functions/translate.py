from translate import Translator

text = input("What do you want to translate: ")
translator = Translator(to_lang="ru")
translation = translator.translate(text)
print(translation)