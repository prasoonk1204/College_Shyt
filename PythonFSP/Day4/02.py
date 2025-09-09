# forming a set from a  list
set1 = set(["Amitava", "Male", 30, "Amitava", 30, "Male", "Pune"])
print(set1, len(set1), type(set1), id(set1))

# forming a set from a tuple
set2 = set(("Amitava", "Male", 30, "Amitava", 30, "Male", "Pune"))
print(set2, len(set2), type(set2), id(set2))

# forming set directly
set3 = {"Amitava", "Male", 30, "Amitava", 30, "Male", "Pune"}
print(set3, len(set3), type(set3), id(set3))


# union operation

snakes = {"python", "cobra", "viper"}
print(snakes, len(snakes))

lang = {"java", "cpp", "python"}
print(lang, len(lang))

result = snakes.union(lang)
print(result, len(result))

result = lang | snakes
print(result, len(result))


# intersection operation

result = snakes.intersection(lang)
print(result, len(result))

result = lang & snakes
print(result, len(result))


# intersection_update

lang.intersection_update(snakes)
print(snakes, len(snakes))
print(lang, len(lang))


# difference operation
snakes = {'python', 'cobra', 'viper'}
print(snakes, len(snakes))
languages = {'java', 'c++', 'python'}
print(languages, len(languages))
result = snakes.difference(languages)
print(result, len(result))
result = snakes - languages
print(result, len(result))


# difference update operation
snakes = {'python', 'cobra', 'viper'}
print(snakes, len(snakes))
languages = {'java', 'c++', 'python'}
print(languages, len(languages))
languages.difference_update(snakes)
print(snakes, len(snakes))
print(languages, len(languages))


# symmetric difference operation
snakes = {"python", "cobra", "viper"}
lang = {"java", "cpp", "python"}

result = snakes.symmetric_difference(lang)
print(result, len(result))

result = lang ^ snakes
print(result, len(result))


# symmetric difference update operation
snakes = {"python", "cobra", "viper"}
lang = {"java", "cpp", "python"}

snakes.symmetric_difference(lang)
print("Lang:", lang, len(lang))
print("Snakes:", snakes, len(snakes))

lang ^ snakes
print("Lang:", lang, len(lang))
print("Snakes:", snakes, len(snakes))


# frozenset symmetric difference update operation
snakes = frozenset({"python", "cobra", "viper"})
lang = frozenset({"java", "cpp", "python"})

snakes.symmetric_difference(lang)
print("Lang:", lang, len(lang))
print("Snakes:", snakes, len(snakes))

lang ^ snakes
print("Lang:", lang, len(lang))
print("Snakes:", snakes, len(snakes))