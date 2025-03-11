import pandas
"""Converts a word or your name in to nato phonetic"""

df_nato = pandas.read_csv("nato_phonetic_alphabet.csv")
dic_nato = {row.letter:row.code for (index, row) in df_nato.iterrows()}
user_input = input("Enter your name or a word")
user_list_input = [dic_nato[letter] for letter in user_input.upper()]

print(f"Your word in phonetic alphabet {user_list_input}")
