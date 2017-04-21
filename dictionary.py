import csv
import sys
import os


# menu with possible actions
def output():

    os.system('clear')
    print("""Dictionary of little programmer:
    1) search explanation by appellation
    2) add new definition
    3) show all appellations alphabetically
    4) show available appelations by typing letters"
    0) exit""")


# diffrent choices
def main():

    # main loop
    while True:

        # setting csv file
        with open('csv.csv', 'r') as files:
            reader = csv.reader(files)
            dictio = {rows[0]: tuple(rows[1:3]) for rows in reader}

        try:
            output()
            chose = int(input("Choose chose: "))
        except ValueError:
            continue

        if chose == 0:
            sys.exit()

        elif chose == 1:

            for key in dictio:
                print(key.upper())
            explanation = input("Choose definition: ")
            if explanation in dictio.keys():
                    print(dictio[explanation])
                    skip = input("\nPress Enter to continue")
                    if skip == "":
                        continue
        # adding new definition
        elif chose == 2:

            word = input("Type issue that you want to next define: ")
            new_explanation = input("Simple definition with source seperated by coma:  ")
            new_def = ','.join((word, new_explanation)) + '\n'
            adder = open('csv.csv', 'a')
            adder.write(new_def)
            adder.close()

            skip = input("\nPress Enter to continue")
            if skip == "":
                continue

        # sorting
        elif chose == 3:

            lista = sorted(dictio.keys())
            for i in lista:
                print(i.upper())
            skip = input("\nPress Enter to continue")
            if skip == "":
                continue

        # finding definition by first letter in appelation
        elif chose == 4:

            letter = input("\nEnter first letter of definition: ")
            words = []
            for key in dictio.keys():
                if letter.lower() in key[0].lower():
                    words.append(key)
            if len(words) > 0:
                for word in words:
                    print(word.upper())
                choose = input("Choose definition ")
                skip = True
                for key in dictio.keys():
                    if key == choose:
                        definition = dictio[key]
                        print("{}: {}".format(key.upper(), definition))
                        skip = False
                skip = input("Press Enter to continue")
                if skip == "":
                    continue

            else:
                print("\nThere is no such word in our dictionary.\n")
                skip = input("Press Enter to continue")
                if skip == "":
                    continue
        else:
            print("Wrong input!")


main()
