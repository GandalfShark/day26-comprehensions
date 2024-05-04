"""
Nato alphabet tool:
take a word and convert it to a nato alphabet phrase
use the supplied csv, pandas and dictionary comprehension
"""
import pandas as pd

def create_dict():
    data = pd.read_csv('nato_phonetic_alphabet.csv')
    nato_dict = {rows.letter: rows.code for (index, rows) in data.iterrows()}
    return nato_dict

def convert_to_nato_alphabet(word_in):
    phrase_out = [nato_dict[let] for let in word_in]
    return phrase_out

# main loop #
run = True
nato_dict = create_dict()


while run:
    print('Enter a word or phrase to convert to NATO alphabet\n or type EXIT to exit')
    input_word = input('Enter a word: ')
    if input_word == 'EXIT':
        run = False
    else:
        input_word = input_word.upper()
        out_phrase = convert_to_nato_alphabet(input_word)
        print(out_phrase)
