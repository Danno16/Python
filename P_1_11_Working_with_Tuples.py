from PC_1_1_Tools import *
def lesson_11():

    def title():
        new_page()
        print("\n                                -----------------------------    Lesson 11> Working with Tuples   -----------------------------\n")

    def definition():
        title()
        print( "       - a TUPLE is a type of data structure which means its a (container) where we can store different values simular to a list. ")
        print("       - a TUPLE Cannot be changed or modified.\n ")
        print("       - The difference between TUPLE  and LIST:\n")
        print(
            "                ---- In a list you can add, delete, append, clear or any of  functions that were in the list section.")
        print("                ---- In Tuple once its made it cannot be changed.")
        print("                ---- A Tuple is used for data that will  never be changed (SSN, coordinates and etc).")
        end()

    def EX1():
        title()
        print("                                    ****  Exercise 1 -  Creating a TUPLE    ****  ")
        print(" Let set up a TUPLE using the variable called {cord}.  Here is the line of code we are using:")
        print("                cord = (4, 5)")
        print(" \nNow we will print the TUPLE")
        cord = (4, 5)
        print("                 " + str(cord))

    def EX2():
        title()
        cord = (4, 5)
        print("                                    ****  Exercise 2 -  Indexing a TUPLE    ****  ")
        print("\n        Lets index the first value in the TUPLE at position 0")
        print("         The code we are using is:")
        print("                     print(cord[0])")
        print("                " + str(cord[0]))

        print("\n        Lets index the second value in the TUPLE at position 1")
        print("         The code we are using is:")
        print("                     print(cord[1])")
        print("                " + str(cord[1]))
        print("\n     As a reminder, here is our TUPLE" + str(cord))

    def EX3():
        title()
        print("                                    **** Exercise 3 - Using a TUPLE with Multiple Entries  ****")
        print(
            " Here is the TUPLE that I created using multiple entries. Here is the command I used:")
        print("cord2 = [(4, 5), (2, 12), (15, 18), (17, 13), (14, 15), (19, 52)]\n")
        print("Now let's print the TUPLE.   ")
        print("print(cord2)")
        cord2 = [(4, 5), (2, 12), (15, 18), (17, 13), (14, 15), (19, 52)]
        print(cord2)



    def EX4():
        title()
        cord2 = [(4, 5), (2, 12), (15, 18), (17, 13), (14, 15), (19, 52)]
        print("                                    **** Exercise 4 - Using a TUPLE with Multiple Entries printing just the given positions ****")
        print("Here is the cord:")
        print(cord2)
        print(
            " Lets  look at the 5th position of the TUPLE. using the 4 as the reference.  Here is the code I used:")
        print("print(cord2[4])")
        print(cord2[4])
        print("\n Now lets look at 3rd position of the Tuple using the 2 as the reference. :"
            "\ncode used:")
        print("print(cord2[2])"
              "\nOutput:")
        print(cord2[2])

        print("\n For our final example lets look at the 1st position of the Tuple using the 0 as the reference:"
            "\ncode used:")
        print("print(cord2[0])"
              "\nOutput:")
        print(cord2[2])

    def end():

        a = input("\n Please Select:  "
                  "\n  (D)   Description of Lesson "
                  "\n  (R)   Run all Lessons "
                  "\n  (1)  Exercise 1 -  Creating a TUPLE  "
                  "\n  (2)  Exercise 2 -  Indexing a TUPLE      "
                  "\n  (3)  Exercise 3 -  Using a TUPLE with Multiple Entries "
                  "\n  (4)  Exercise 4 - Using a TUPLE with Multiple Entries printing just the given positions "

                  "\n           <Enter>  for main menu: ")

        if str(a) == "d":
            definition()

        if str(a) == "D":
            definition()

        if str(a) == "r":
            EX1()
            continue_lesson()
            EX2()
            continue_lesson()
            EX3()
            continue_lesson()
            EX4()
            end()

        if str(a) == "R":
            EX1()
            continue_lesson()
            EX2()
            continue_lesson()
            EX3()
            continue_lesson()
            EX4()
            end()


        if str(a) == "1":
            EX1()
            end()
        if str(a) == "2":
            EX2()
            end()
        if str(a) == "3":
            EX3()
            end()
        if str(a) == "4":
            EX4()
            end()

        else:
            import P_1_1_Python_Main_Menu
            P_1_1_Python_Main_Menu.main_menu_1

    definition()

