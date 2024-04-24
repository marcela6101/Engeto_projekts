"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Marcela Vilášková
email: vilaskova.marcela@seznam.cz
discord: marcela6101
"""
from task_template import TEXTS

user = ["bob", "ann", "mike", "liz"]
password = ["123", "pass123", "password123", "pass123"]
prihl_udaje = dict(zip(user, password))
jmeno = input("User:")
heslo = input("Password:")
if prihl_udaje.get(jmeno) == heslo:
    print("-" * 40)
    print("Welcome to the app,", jmeno)
    print("We have 3 texts to be analyzed.")
else:
    print("Unregistered user, terminating the program..")
    exit()
print("-" * 40)
cislo_textu = [1, 2, 3]
zvolene_cislo = int(input("Enter a number btw. 1 and 3 to select:"))
for cislo in cislo_textu:
    if cislo == zvolene_cislo:
        veta_na_indexu = TEXTS[int(cislo) - 1]
        slova_ve_vete = veta_na_indexu.split()
        pocet_slov_ve_vete = len(slova_ve_vete)
        print("-" * 40)
        print(f"There are {pocet_slov_ve_vete} words in the selected text.")
        pocitadlo_prvni_velke = 0
        pocitadlo_velke = 0
        pocitadlo_male = 0
        pocitadlo_cisel = 0
        celkem = 0
        for slovo in slova_ve_vete:
            if slovo[0].isupper():
                pocitadlo_prvni_velke += 1
            if slovo.isupper() and slovo.isalpha():
                pocitadlo_velke += 1
            if slovo.islower():
                pocitadlo_male += 1
            if slovo.isdigit():
                pocitadlo_cisel += 1
                celkem += int(slovo)
        print(f"There are {pocitadlo_prvni_velke} titlecase words.")
        print(f"There are {pocitadlo_velke} uppercase words.")
        print(f"There are {pocitadlo_male} lowercase words.")
        print(f"There are {pocitadlo_cisel} numeric strings.")
        print(f"The sum of all the numbers {celkem}.")
        print("-" * 40)
        print("LEN|\t\tOCCURENCES\t\t|NR.")
        print("-" * 40)
        slova_ve_vete_bez_carek = [s.replace(",", "") if "," in s else s for s in slova_ve_vete]
        slova_ve_vete_bez_carek_tecek = [s.replace(".", "") if "." in s else s for s in slova_ve_vete_bez_carek]
        slovo_1 = 0
        slovo_2 = 0
        slovo_3 = 0
        slovo_4 = 0
        slovo_5 = 0
        slovo_6 = 0
        slovo_7 = 0
        slovo_8 = 0
        slovo_9 = 0
        slovo_10 = 0
        slovo_11 = 0
        for delka_slova in slova_ve_vete_bez_carek_tecek:
            if len(delka_slova) == 1:
                slovo_1 += 1
            if len(delka_slova) == 2:
                slovo_2 += 1
            if len(delka_slova) == 3:
                slovo_3 += 1
            if len(delka_slova) == 4:
                slovo_4 += 1
            if len(delka_slova) == 5:
                slovo_5 += 1
            if len(delka_slova) == 6:
                slovo_6 += 1
            if len(delka_slova) == 7:
                slovo_7 += 1
            if len(delka_slova) == 8:
                slovo_8 += 1
            if len(delka_slova) == 9:
                slovo_9 += 1
            if len(delka_slova) == 10:
                slovo_10 += 1
            if len(delka_slova) == 11:
                slovo_11 += 1
        print("  1|",slovo_1 * "*",(21 - slovo_1) * " ","|",slovo_1)
        print("  2|", slovo_2 * "*",(21 - slovo_2) * " ","|", slovo_2)
        print("  3|", slovo_3 * "*",(21 - slovo_3) * " ","|", slovo_3)
        print("  4|", slovo_4 * "*",(21 - slovo_4) * " ","|", slovo_4)
        print("  5|", slovo_5 * "*",(21 - slovo_5) * " ","|", slovo_5)
        print("  6|", slovo_6 * "*",(21 - slovo_6) * " ","|", slovo_6)
        print("  7|", slovo_7 * "*",(21 - slovo_7) * " ","|", slovo_7)
        print("  8|", slovo_8 * "*",(21 - slovo_8) * " ","|", slovo_8)
        print("  9|", slovo_9 * "*",(21 - slovo_9) * " ","|", slovo_9)
        print(" 10|", slovo_10 * "*",(21 - slovo_10) * " ","|", slovo_10)
        print(" 11|", slovo_11 * "*",(21 - slovo_11) * " ","|", slovo_11)