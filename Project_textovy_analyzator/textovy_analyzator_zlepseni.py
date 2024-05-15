"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Marcela Vilášková
email: vilaskova.marcela@seznam.cz
discord: marcela6101
"""
from task_template import TEXTS

user = ["bob", "ann", "mike", "liz"]
passwords = ["123", "pass123", "password123", "pass123"]
login = dict(zip(user, passwords))
name = input("User:")
password = input("Password:")
if login.get(name) == password:
    print("-" * 40)
    print("Welcome to the app,", name)
    print("We have 3 texts to be analyzed.")
else:
    print("Unregistered user, terminating the program..")
    exit()
print("-" * 40)
number = [1,2,3]

while number:
    try:
       number = int(input("Enter a number btw. 1 and 3 to select:"))
    except ValueError:
        print("You typed a letter. Enter a number btw. 1 and 3 to select:")
        continue
    if number <=0 or number > 3:
        print("You typed wrong number. Enter a number btw. 1 and 3 to select:")
    elif number == 1 or number == 2 or number == 3:
        phrase_on_index = TEXTS[int(number) - 1]
        words_in_phrase = phrase_on_index.split()
        sum_words_in_phrase = len(words_in_phrase)
        print("-" * 40)
        print(f"There are {sum_words_in_phrase} words in the selected text.")
        counter_first_big = 0
        couter_big = 0
        counter_small = 0
        counter_number = 0
        total = 0
        for word in words_in_phrase:
            if word[0].isupper():
                counter_first_big += 1
            if word.isupper() and word.isalpha():
                couter_big += 1
            if word.islower():
                counter_small += 1
            if word.isdigit():
                counter_number += 1
                total += int(word)
        print(f"There are {counter_first_big} titlecase words.")
        print(f"There are {couter_big} uppercase words.")
        print(f"There are {counter_small} lowercase words.")
        print(f"There are {counter_number} numeric strings.")
        print(f"The sum of all the numbers {total}.")
        print("-" * 40)
        print("LEN|\t\tOCCURENCES\t\t|NR.")
        print("-" * 40)
        words_in_phrase_without_commas = [s.replace(",", "") if "," in s else s for s in words_in_phrase]
        words_in_phrase_without_commas_dots = [s.replace(".", "") if "." in s else s for s in words_in_phrase_without_commas]
        words = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0}
        for w in words_in_phrase_without_commas_dots:
            lenght_word = len(w)
            if lenght_word in words:
                words[lenght_word] += 1
            else:
                words[lenght_word] = 1

        print("  1|", words[1] * "*",(21 - words[1]) * " ","|", words[1])
        print("  2|", words[2] * "*",(21 - words[2]) * " ","|", words[2])
        print("  3|", words[3] * "*",(21 - words[3]) * " ","|", words[3])
        print("  4|", words[4] * "*",(21 - words[4]) * " ","|", words[4])
        print("  5|", words[5] * "*",(21 - words[5]) * " ","|", words[5])
        print("  6|", words[6] * "*",(21 - words[6]) * " ","|", words[6])
        print("  7|", words[7] * "*",(21 - words[7]) * " ","|", words[7])
        print("  8|", words[8] * "*",(21 - words[8]) * " ","|", words[8])
        print("  9|", words[9] * "*",(21 - words[9]) * " ","|", words[9])
        print(" 10|", words[10] * "*",(21 - words[10]) * " ","|", words[10])
        print(" 11|", words[11] * "*",(21 - words[11]) * " ","|", words[11])
        break

