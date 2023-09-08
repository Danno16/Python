from PC_1_1_Tools import *
from math import *
def lesson_5():

    def title():
        new_page()
        print("\n                                -----------------------------    Lesson 5 - Working with Print Functions    -----------------------------\n")

    def definition():
        title()
        print( "In this Exercise, We are going To:"
               "\n                      ---     Covert all the numbers to UPPER/LOWER case"
               "\n                      ---     Checks to see if all UPPER/LOWER Case   "
               "\n                      ---     Makes it all UPPER/LOWER Case then sees if it is all UPPER/LOWER case "
               "\n                      ---     Length of the string  "
               "\n                      ---     Concatenate and Length of the string     "
               "\n                      ---     1st, 3rd, and 5th Letter of the string "
               "\n                      ---     Give position of given letter"
               "\n                      ---     Replaces a letter with another letter"
               )
        end()




    def EX1():
        title()
        print(
            "\n                                    ****  Exercise 1 -  Print Functions  **** \n ")
        print("We are going to concentrate are some of the functions that are available in python.")
        print("We are going to show the code for the function and description then the output.")
        print("We are going to use 2 Variables {first_name} and {last_name}\n")
        print("first_name = \"Albert\"")
        print("first_name = \"Einstein\"")
        first_name = "Albert"
        last_name = "Einstein"
        input("\n\nPress <Enter> to Continue: ")

        print(
            "\n\n\n\n\n\n\n\n          CODE                                                     Description                                                            Output")
        print(
            "`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
        print(
            "  print(first_name.upper())                       Makes it all UPPER Case                                                       " + (
                first_name.upper()))
        print(
            "  print(first_name.lower())                        Makes it all lower Case                                                           " + (
                first_name.lower()))
        print(
            "  print(first_name.isupper())                    Checks to see if all UPPER Case                                           " + str(
                first_name.isupper()))
        print(
            "  print(first_name.islower())                     Checks to see if all LOWER Case                                          " + str(
                first_name.islower()))
        print(
            "  print(first_name.upper().isupper())       Makes it all Upper Case then sees if it is all upper  case       " + str(
                first_name.upper().isupper()))
        print(
            "  print(first_name.lower().islower())        Makes it all LOWER Case then sees if it is all upper  case.   " + str(
                first_name.lower().islower()))
        print(
            "  print(len(first_name))                            Length of the string (were using the first name                         " + str(
                len(first_name)))
        print(
            "  print(len(first_name + Last_name))      Length of the string with concatenation                                     " + str(
                len(first_name + last_name)))
        print(
            "  print(first_name[0])                               1st Letter of the string                                                               " + (
            first_name[0]))
        print(
            "  print(first_name[2])                               3d Letter of the string                                                                " + (
            first_name[2]))
        print(
            "  print(first_name[4])                               5th  Letter of the string                                                              " + (
            first_name[4]))
        print(
            "  print(first_name.index(\"A\"))                Tells me what position the letter \"A\" is                                      " + str(
                first_name.index("A")))
        print(
            "  print(first_name.index(\"e\"))                 Tells me what position the letter \"e\" is                                      " + str(
                first_name.index("e")))
        print(
            "  print(first_name.replace(\"S\", \"P\"))    Replaces the b with a P                                                              " + first_name.replace(
                "b", " - P - "))
        input("\n\nPress <Enter> to go to Lesson Main Menu: ")


    def EX2():
        title()
        print(
            "\n                                    ****  Exercise 2 -  Print Functions using Input Variable  **** \n ")
        print(
              "\nOkay Lets have some.  Enter a name or sentence, and were going to apply some of the print functions we learned ")
        example_2 = input("Because of the print function parameters we used, Please use:"
                    "\n                 - At least 5 Letters."
                    "\n                     - Please use at least 1 \"a\""
                    "\n                     - Please use at least 1 \"e\""
                          "\n\nInput a name or sentence:  ")

        try:
            title()
            print("The input variable is called \"example_2\".  Here is the line of code - example_2 = input(\"input a name or sentence\")\n"
                  "Here is what you entered - "+ example_2)
            print("\n         CODE                                                     Description                                                            Output")
            print(
                "`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
            print(
                "  print(example_2.upper())                       Makes it all UPPER Case                                                       " + (
                    example_2.upper()))
            print(
                "  print(example_2.lower())                        Makes it all lower Case                                                           " + (
                    example_2.lower()))
            print(
                "  print(example_2.isupper())                    Checks to see if all UPPER Case                                           " + str(
                    example_2.isupper()))
            print(
                "  print(example_2.islower())                     Checks to see if all LOWER Case                                          " + str(
                    example_2.islower()))
            print(
                "  print(example_2.upper().isupper())       Makes it all Upper Case then sees if it is all upper  case       " + str(
                    example_2.upper().isupper()))
            print(
                "  print(example_2.lower().islower())        Makes it all LOWER Case then sees if it is all upper  case.   " + str(
                    example_2.lower().islower()))
            print(
                "  print(len(example_2))                            Length of the string (were using the first name                         " + str(
                    len(example_2)))

            print(
                "  print(example_2[0])                               1st Letter of the string                                                               " + (
                example_2[0]))
            print(
                "  print(example_2[2])                               3d Letter of the string                                                                " + (
                example_2[2]))
            print(
                "  print(example_2[4])                               5th  Letter of the string                                                              " + (
                example_2[4]))
            print(
                "  print(example_2.index(\"a\"))                Tells me what position the letter \"a\" is                                      " + str(
                    example_2.index("a")))
            print(
                "  print(example_2.index(\"e\"))                 Tells me what position the letter \"e\" is                                      " + str(
                    example_2.index("e")))
            print(
                "  print(example_2.replace(\"a\", \"-  Apple -\"))    Replaces the a with a \"- Apple - \"                        " + example_2.replace(
                    "a", " - Apple - "))
        except IndexError:
            print("\nPlease use at least 5 Letters")
            input("Press <Enter> to try again:  ")
            EX2()

        except ValueError:
            print("\nPlease use at least one \"a\" and \"e\"")
            input("Press <Enter> to try again:  ")
            EX2()

        input("\n\nPress <Enter> to go to Lesson Main Menu: ")


    def end():
        print("\n                                         -----------------------------    Lesson Main Menu  -----------------------------")
        a = input("\n Please Select:  "
                  "\n  (D)   Description of Lesson "
                  "\n  (1)    Exercise 1 -  Print Functions "
                  "\n  (2)    Exercise 2 -  Print Functions using Input Variable "

                  "\n           <Enter>  for main menu: ")

        if str(a) == "d":
            definition()

        if str(a) == "D":
            definition()


        if str(a) == "1":
            EX1()
            end()
        if str(a) == "2":
            EX2()
            end()

        else:
            import P_1_1_Python_Main_Menu
            P_1_1_Python_Main_Menu.main_menu_1

    definition()

