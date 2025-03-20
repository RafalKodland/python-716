meme_dict = {
            "CRINGE": "Coś wyjątkowo dziwnego lub zawstydzającego",
            "LOL": "Częsta reakcja na coś zabawnego",
            }

word = input("Wpisz słowo, którego nie rozumiesz (używaj wielkich liter!): ").upper()

if word in meme_dict.keys():
    print(word, ": ", meme_dict[word])
else:
    print("Nie ma takiego słowa w naszym słowniku")
