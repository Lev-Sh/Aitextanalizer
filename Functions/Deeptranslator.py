from deep_translator import GoogleTranslator
text = input("What do you want to translate: ")
translator = GoogleTranslator(to_lang="ru")
translation = translator.translate(text)
print(translation)