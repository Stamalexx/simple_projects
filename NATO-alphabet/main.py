import pandas
"""Converts a word or your name in to nato phonetic alphabet"""
check = True
df_nato = pandas.read_csv("nato_phonetic_alphabet.csv")
dic_nato = {row.letter:row.code for (index, row) in df_nato.iterrows()}


while check:
    user_input = input("Enter your name or a word ")
    try:
        user_list_input = [dic_nato[letter] for letter in user_input.upper()]
    except KeyError:
        print("Only letters are allowed")
    else:
        print(f"Your word in phonetic alphabet {user_list_input}")
        check = False
