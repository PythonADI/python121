langs = ["C", "C++", "Java", "C#"]

# langs.insert(0, "Python")
langs.insert(len(langs) // 2, "Python")

langs.remove("Java")


print(langs)