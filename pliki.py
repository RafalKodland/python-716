from os import listdir
from random import randint

name = "John"
surname = "Snow"
age = 21
purse = 500
in_home = 7000

print(f"To są twoje dane: {name} {surname} w wieku {age} lat. Jego majątek to {purse+in_home} monet. \nA to pliki w folderze memy {randint(5, 50)}")

print(listdir("memy"))


file = open(r"testowanie\test.txt", 'r', encoding="utf-8")
lines = file.readlines()
file.close()


file = open(r"testowanie\test.txt", 'w', encoding="utf-8")

lines_upper = []
for line in lines:
    lines_upper.append(line.upper())
file.writelines(lines_upper)

file.close()


with open(r"testowanie\test.txt", 'a', encoding="utf-8") as file:
    file.write("\nTo jest dodatkowa dopisana linia")