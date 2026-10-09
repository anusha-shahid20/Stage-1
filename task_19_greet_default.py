def greet(name, lang="urdu"):
    if lang == "urdu":
        print(f"Assalam-o-Alaikum, {name}!")
    elif lang == "english":
        print(f"Hello, {name}!")
    elif lang == "spanish":
        print(f"Hola, {name}!")
    elif lang == "french":
        print(f"Bonjour, {name}!")
    elif lang == "arabic":
        print(f"Marhaba, {name}!")
    else:
        print(f"Hi, {name}!")

name = input("Enter your name: ")
lang = input("Enter language (urdu/english/spanish/french/arabic): ")

greet(name, lang)