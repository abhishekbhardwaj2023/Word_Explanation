from typing import KeysView
import pandas

#read data
data = pandas.read_csv("D:\VS_Code Programs\Python\Alphabet split full-form Project\list_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

def generate_phoenetic():
    word = input("Enter a word: ").upper()     #enter the word
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the word please.")    #expected error
    else:
        print(output_list)

more_word = '1'
while more_word == '1':
    generate_phoenetic()
    more_word = input("Want to search more? [0/1]: ")
    
