#!/usr/bin/env python3.8

#Returns list of numerals within range given by low and high

import sys

def prime_numbers(low, high):
    if type(low) != int or type(high) != int:
        print("Only ints supported", file=sys.stderr)
        return list()
    elif low == high:
        print("low and high thresholds are equal", file=sys.stderr)
        return list()

    result_list = list()
    for i in range(low, high, (1 if low < high else -1)):
        result_list.append(i)
    result_list.sort()
    return result_list

#Prints text stats
def text_stat(filename):
    if type(filename) != str:
        return {"error": "Unsupported argument type(only str allowed)"}

    latin_letters = list(map(chr, range(ord('a'), ord('z')+1)))
    rus_letters = list(map(chr, range(ord('а'), ord('я')+1)))
    result_dict = {"paragraph_amount": 0, "word_amount": 0,
            "bilingual_word_amount": 0}
    try:
        end_of_paragr = True
        with open(filename, 'r') as f:
            for line in f:
                if line == '\n':
                    if end_of_paragr != True:
                        result_dict['paragraph_amount'] += 1
                        end_of_paragr = True
                        continue
                    else:
                        continue
                line = line.lower()
                line_content = line.split('\n')
                line_content_length = len(line_content) 
                result_dict['word_amount'] += line_content_length
                for word in line_content[:line_content_length]:
                    if word == '':
                        continue
                    latin_letter = False
                    rus_letter = False
                    letters = dict()
                    for letter in word:
                        if letter in latin_letters:
                            latin_letter = True
                        elif letter in rus_letters:
                            rus_letter = True
                        else:
                            continue
                        if letter in letters.keys():
                            letters[letter][0] += 1
                        else:
                            letters[letter] = [1, 1]
                    if latin_letter == True and rus_letter == True:
                        result_dict['bilingual_word_amount'] += 1
                    latin_letter = False
                    rus_letter = False
                    for k, v in letters.items():
                        if k in result_dict.keys():
                            result_dict[k] = tuple([result_dict[k][0] + v[0], result_dict[k][1] + v[1]])
                        else:
                            result_dict[k] = tuple(v)
                end_of_paragr = False
    except Exception as e:
        raise e
        return {"error": str(e)}
    
    return result_dict

#Converts roman numerals to decimals
def roman_numerals_to_int(roman_numeral):
    if type(roman_numeral) != str:
        return {"error": "Unsupported argument type(only str allowed)"}

    roman2dec_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    roman_numeral = roman_numeral.upper()
    res = None
    for i in range(0, len(roman_numeral)-1):
        if roman_numeral[i] in roman2dec_dict.keys():
            if res == None:
                res = roman2dec_dict[roman_numeral[i]]
            else:
                if i+1 in range(i, len(roman_numeral)):
                    if roman_numeral[i+1] in roman2dec_dict.keys():
                        if roman2dec_dict[roman_numeral[i+1]] > roman2dec_dict[roman_numeral[i]]:
                            res += roman2dec_dict[roman_numeral[i+1]] - roman2dec_dict[roman_numeral[i]]
                            i += 1
                        else:
                            res += roman2dec_dict[roman_numeral[i]]
                            res += roman2dec_dict[roman_numeral[i+1]]
                            i += 1
                    else:
                        print("{} is not roman literal({})".format(numeral, roman_numeral), file=sys.stderr)
                        return None
                else:
                    res += roman2dec_dict[roman_numeral[i]]
        else:
            print("{} is not roman literal({})".format(numeral, roman_numeral), file=sys.stderr)
            return None
    return res

