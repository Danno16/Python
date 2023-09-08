from PC_1_1_Tools import *

def lesson_19():

    def title():
        new_page()
        print( "\n                                   -----------------------------------    Lesson 19 - THE GUESSING GAME   -----------------------------\n")

    def definition():
        title()
        print("In this Lesson, we are building a couple of simple guessing games.")
        print("We are going to use the tools we have learned in previouse lessons.  The pimary tools (or commands) is:")
        print("                                          - Inputs   ")
        print("                                          - Variables")
        print("                                          - IF Statements   ")
        print("                                          - While  Loops\n")
        print("So lets have fun!!!")
        end()


    def run_all_games():
        game_1()
        game_2()
        game_3()
        game_4()
        continue_lesson()
        end()

    def game_1():
        title()

        print("Guessing Game - 1: In this first game, there are no clues and no limits of number of tries.  The guess word is - \"glass\"\n")

        secret_word = "glass"
        guess = ""
        i = 0
        while secret_word != guess:
            i = i + 1
            guess = input("Guess number ---- " + str(i) + " Guess the Secret Word: ")

        print("\nYou Guessed it.  Yeah I know this game is lame, but It'll get better.\n")
        continue_lesson()

    def print_game_1():
        title()
        print("                         secret_word = \"glass\"   ")
        print("                         guess = \"\"  ")
        print("                          i = 0\") ")
        print("                          while secret_word != guess:  ")
        print("                              i = i + 1   ")
        print("                              guess = input(\"Guess number ---- \" + str(i) + \" Guess the Secret Word: \")  ")
        print("                          print(\"\\nYou Guessed it.  Yeah I know this game is lame, but It'll get better.\")  \n\n")
        continue_lesson()



    def game_2():
        title()
        print("Guessing Game - 2: Now we are going to make this game a little smarter.  We're going to set a limit of 3 tries.  The guess word is - \"glass\"\n")
        secret_word = "glass"
        guess = ""
        guess_count = 0
        guess_limit = 3
        out_of_guesses = False

        while guess != secret_word and not out_of_guesses:
            if guess_count < guess_limit:
                guess_count += 1
                guess = input("Guess #" + str(guess_count) + " Enter guess:   ")

            else:
                out_of_guesses = True

        if out_of_guesses:
            print("\nYou loose.  You had to make it in " + str(guess_limit) + " Tries.")
        else:
            print("\nYou win. You did it in " + str(guess_count) + " Tries.")
        continue_lesson()

    def print_game_2():
        title()
        print("     print(\"Guessing Game - 2: Now we are going to make this game a little smarter.  We're going to set a limit of 3 tries.  The guess word is - \"glass\"\\n\")   ")
        print("     secret_word = \"glass\" ")
        print("     guess = \"\" ")
        print("     guess_count = 0 ")
        print("     guess_limit = 3 ")
        print("     out_of_guesses = False ")

        print("     while guess != secret_word and not out_of_guesses:")
        print("         if guess_count < guess_limit:  ")
        print("             guess_count += 1  ")
        print("                     guess = input(\"Guess #\" + str(guess_count) + \" Enter guess:   \")   ")
        print("                 else:  ")
        print("                     out_of_guesses = True   ")

        print("             if out_of_guesses:  ")
        print("                 print(\"\\nYou loose.  You had to make it in \" + str(guess_limit) + \" Tries.\")   ")
        print("                 else:  ")
        print("                     print(\"\\nYou win. You did it in \" + str(guess_count) + \" Tries.\")\n")
        continue_lesson()


    def game_3():
        title()
        print("Guessing Game - 3: Now in this game, we are going to make it even more smarter.  It will have clues and you have 5 turns to figure out the word..\n")
        print("                  ****   please use all lower case   ****")
        print("Good luck!!!!\n")
        clues = {
            1: "It is pretty easy to learn and use. ",
            2: "It is a computer language (not BASIC, COBALT, FORTRAN, VISUAL BASIC, or the dreaded Assembly Language.",
            3: "It was named after snake. ",
            4: "I use PyCharm or VS code to code in it. ",
            5: "This program is built in it. ",
        }

        word = "python"
        guess = ""
        count = 0
        max_count = 5
        win = False

        while guess != word and not win:
            if count < max_count:
                count += 1
                print("Clue number - " + str(count) + " - " + clues[count])
                guess = input(" Guess number " + str(count) + ".  Enter guess : ")
            else:
                win = True

        if win:
            print(" \nYou Loose.  You only had " + str(count) + " tries.")
        else:
            print(" \nYou Win!!!!!!!!!  You did it in " + str(count) + " tries.")
        continue_lesson()

    def print_game_3():
        title()
        print("Guessing Game - 3: Now in this game, we are going to make it even more smarter.  It will have clues and you have 5 turns to figure out the word..\n")
        print("                  ****   please use all lower case   ****")
        print("Good luck!!!!\n")
        clues = {
            1: "It is pretty easy to learn and use. ",
            2: "It is a computer language (not BASIC, COBALT, FORTRAN, VISUAL BASIC, or the dreaded Assembly Language.",
            3: "It was named after snake. ",
            4: "I use PyCharm or VS code to code in it. ",
            5: "This program is built in it. ",
        }

        word = "python"
        guess = ""
        count = 0
        max_count = 5
        win = False

        while guess != word and not win:
            if count < max_count:
                count += 1
                print("Clue number - " + str(count) + " - " + clues[count])
                guess = input(" Guess number " + str(count) + ".  Enter guess : ")
            else:
                win = True

        if win:
            print(" \nYou Loose.  You only had " + str(count) + " tries.")
        else:
            print(" \nYou Win!!!!!!!!!  You did it in " + str(count) + " tries.")
        continue_lesson()

    def game_4():
        title()
        print("Guessing Game - 4: Now its your turn.  Your going to enter the guess word and the 5 clues.\n")
        print("         *****  NOTE - It is case sensitive  ****** ")
        print("Here we go!!!!\n")
        word = input("What is the guess word?  ")
        max_count = 5
        clue_1 = input("What is the first clue?  ")
        clue_2 = input("What is the second clue?  ")
        clue_3 = input("What is the third clue?  ")
        clue_4 = input("What is the forth clue? ")
        clue_5 = input("What is the fifth clue?  ")

        clues = {
            1: clue_1,
            2: clue_2,
            3: clue_3,
            4: clue_4,
            5: clue_5,
             }
        guess = ""
        count = 0
        win = False
        continue_lesson()
        title()
        print("You have 5 tries to guess the secrete word.  Good Luck!!!!")
        while guess != word and not win:
            if count < int(max_count):
               count += 1
               print("Clue number - " + str(count) + " - " + clues[count])
               guess = input(" Guess number " + str(count) + ".  Enter guess :")
            else:
               win = True

        if win:
          print(" You Loose.  You only had " + str(count) + " tries.")
        else:
          print(" You Win!!!!!!!!!  You did it in " + str(count) + " tries.")


    def print_game_4():
        title()
        print("             print(\"Guessing Game - 4: Now its your turn.  Your going to enter the guess word and the 5 clues.\\n\")  ")
        print("             print(\"         *****  NOTE - It is case sensitive  ****** \") ")
        print("             print(\"Here we go!!!!\\n\") ")
        print("             word = input(\"What is the guess word?  \") ")
        print("             max_count = 5   ")
        print("             clue_1 = input(\"What is the first clue?  \")   ")
        print("             clue_2 = input(\"What is the second clue?  \")   ")
        print("             clue_3 = input(\"What is the third clue?  \")   ")
        print("             clue_4 = input(\"What is the forth clue?  \")   ")
        print("             clue_5 = input(\"What is the fifth clue?  \")   ")

        print("             clues = {   ")
        print("                  1: clue_1,   ")
        print("                 2: clue_2,   ")
        print("                 3: clue_3,   ")
        print("                 4: clue_4,   ")
        print("                 5: clue_5,   ")
        print("             }  ")
        print("             guess = ""    ")
        print("             count = 0  ")
        print("             win = False  ")
        print("             continue_lesson()  ")
        print("             title()  ")
        print("             print(\"You have 5 tries to guess the secrete word.  Good Luck!!!!\")  ")
        print("             while guess != word and not win:  ")
        print("                 if count < int(max_count):  ")
        print("                     count += 1  ")
        print("                     print(\"Clue number - \" + str(count) + \" - \" + clues[count])  ")
        print("                     guess = input(\" Guess number \" + str(count) + \".  Enter guess : ")
        print("                 else:  ")
        print("                    win = True  ")

        print("             if win:  ")
        print("                 print(\" \nYou Loose.  You only had \" + str(count) + \" tries.\")  ")
        print("              else:")
        print("                 print(\" \nYou Win!!!!!!!!!  You did it in \" + str(count) + \" tries.\")  ")





    def end():
        a = input("\n Please Select: "
            "\n           (R) Run all the Example games "
            "\n           (1) Guessing Game - No Limits - No Clues                                                             (A) Show code for Game 1"
            "\n           (2) Guessing Game - 3 limit try - no Clues                                                               (B) Show code for Game 2"
            "\n           (3) Guessing Game - 5 limit try - Includes Clues                                                     (C) Show code for Game 3"
            "\n           (4) Guessing game - You enter the secrete word and clues                                    (D) Show code for Game 4\n"
            "\n           (D) Description "
            "\n           <Enter>  for main menu: ")
        if str(a) == "r":
            run_all_games()
            lesson_19()
        if str(a) == "R":
            run_all_games()
            lesson_19()
        if str(a) == "1":
            game_1()
            lesson_19()

        if str(a) == "A":
            print_game_1()
            lesson_19()
        if str(a) == "a":
            print_game_1()
            lesson_19()

        if str(a) == "B":
            print_game_2()
            lesson_19()
        if str(a) == "b":
            print_game_2()
            lesson_19()

        if str(a) == "D":
            print_game_4()
            continue_lesson()
            lesson_19()
        if str(a) == "d":
            print_game_4()
            continue_lesson()
            lesson_19()

        if str(a) == "2":
            game_2()
            lesson_19()
        if str(a) == "3":
            game_3()
            lesson_19()
        if str(a) == "4":
            game_4()
            lesson_19()


        if str(a) == "d":
            lesson_19()
        if str(a) == "D":
            lesson_19()
        else:
            import P_1_1_Python_Main_Menu
            P_1_1_Python_Main_Menu.main_menu_1

    definition()

