from PC_1_1_Tools import *

def lesson_23():
    def title():
        new_page()
        print(
            "\n                                   -----------------------------------    Lesson 23 - BUILDING A TRANSLATOR  -----------------------------\n")

    def definition():
        title()
        print(" In this lesson were going to have a little fun.  What we are going to concentrate on:")
        print("                                                          *  for / in")
        print("                                                          *  if / else / return\n")
        print(" We will recap what these terms mean:")
        print("                                 -for       = loops are used when you have a block of code which you want to repeat a fixed number of times.")
        print("                                - if          = It decides whether certain statements need to be executed or not.")
        print("                                - return   = used in a loop to return a value.")



        end()

    def run_all():
        example_1()
        continue_lesson()
        example_2()
        continue_lesson()
        example_3()
        continue_lesson()
        example_4()
        continue_lesson()


    def example_1():
        title()
        print("                          ----  Example 1 - Replacing Vowels with input Value ")
        def a(e):
            d = ""
            for c in e:  # like for c = 1 to len(e)
                if c in "AEIOUaeiou":
                    d = d + f
                else:
                    d = d + c
            return d

        print("In this example, we are going to ask for a phrase and replacement value.  What it will do is replace "
              "\nany vowels with the replacement value.  Give it a try and you'll see what I mean.\n")
        e = input("Enter a Phrase: ")
        f = input("Replacement: ")
        print("\n                             Output - " + a(e) )

        g = input("\nDo you want to try again? (Y/N):")
        if(g) == "y":
             example_1()
        elif(g) == "Y":
             example_1()
        else:
            lesson_23()

    def example_1_code():
        title()
        print("                          ----  Example 1 Code - Replacing Vowels with input Value \n")
        print("                     1       def a(e):  ")
        print("                     2           d = \"\" ")
        print("                     3           for c in e:  # like for c = 1 to len(e) ")
        print("                     4               if c in \"AEIOUaeiou\": ")
        print("                     5                   d = d + f ")
        print("                     6               else: ")
        print("                     7                   d = d + c ")
        print("                     8           return d ")
        print("                     8        e = input(\"Enter a Phrase: \")   ")
        print("                     9        f = input(\"Replacement: \")   ")
        print("                     8        print(a(e))   \n ")


    def example_2():
        title()
        title()
        print("                                                                     Example 2 - Replacing Vowels with input Value (Setting the variable to LOWER case). \n ")
        def a(e):
            d = ""
            for c in e:  # like for c = 1 to len(e)
                if c.lower() in "aeiou":
                    d = d + f
                else:
                    d = d + c
            return d

        print("In this example, we are going to ask for a phrase and replacement value.  What it will do is replace "
              "\nany vowels and replace it with the replacement value. This difference with this exercise vs previous one"
              "\nis in the previous exercise, the coder had to enter  both lower and upper case in the comparison.  In "
              "\nthis exercise what we did is to make the variable all LOWER case then do the comparison.   "
              "\nNOTE this when you review the code.\n")
        e = input("Enter a Phrase: ")
        f = input("Replacement: ")
        print("\n                             Output - " + a(e) )

        g = input("\nDo you want to try again? (Y/N):")
        if(g) == "y":
             example_2()
        elif(g) == "Y":
             example_2()
        else:
            lesson_23()

    def example_2_code():

        title()
        print("                                 Example 2 - Replacing Vowels with input Value (Setting the variable to LOWER case). \n ")


        print("                     1       def a(e):             ")
        print("                     2           d = \"\"                ")
        print("                     3           for c in e:   ")
        print("                     4               if c.lower() in \"aeiou\":     ----   NOTE  the \".lower \"")
        print("                     5                   d = d + f ")
        print("                     6               else: ")
        print("                     7                   d = d + c ")
        print("                     8           return d ")
        print("                     8        e = input(\"Enter a Phrase: \")   ")
        print("                     9        f = input(\"Replacement: \")   ")
        print("                     8        print(a(e))   \n ")

    def example_3():
        title()
        title()
        print("                              Example 3 - Replacing Vowels with input Value (Setting the variable to UPPER case). \n ")
        def a(e):
            d = ""
            for c in e:  # like for c = 1 to len(e)
                if c.upper() in "AEIOU":
                    d = d + f
                else:
                    d = d + c
            return d

        print("In this example, we are going to ask for a phrase and replacement value.  What it will do is replace "
              "\nany vowels and replace it with the replacement value. This difference with this exercise vs previous one"
              "\nis in the previous exercise, the coder had to enter  both lower and upper case in the comparison.  In "
              "\nthis exercise what we did is to make the variable all UPPER case then do the comparison.   "
              "\nNOTE this when you review the code.\n")
        e = input("Enter a Phrase: ")
        f = input("Replacement: ")
        print("\n                             Output - " + a(e) )

        g = input("\nDo you want to try again? (Y/N):")
        if(g) == "y":
             example_2()
        elif(g) == "Y":
             example_2()
        else:
            lesson_23()

    def example_3_code():

        title()
        print("                          ----  Example 3 - Replacing Vowels with input Value (Setting the variable to UPPER case). \n")


        print("                     1       def a(e):             ")
        print("                     2           d = \"\"                ")
        print("                     3           for c in e:   ")
        print("                     4               if c.upper() in \"AEIOU\":     ----   NOTE  the \".upper \"")
        print("                     5                   d = d + f ")
        print("                     6               else: ")
        print("                     7                   d = d + c ")
        print("                     8           return d ")
        print("                     8        e = input(\"Enter a Phrase: \")   ")
        print("                     9        f = input(\"Replacement: \")   ")
        print("                     8        print(a(e))   \n ")

    def end():
        a = input("\n Please Select: To see the code behind the example put \"C\" before the number\n"
                  "\n (D)   Description of Lesson "
                  "\n (C1) / (1) Example 1 - Replacing Vowels with input Value           "
                  "\n (C2) / (2) Example 2 - Replacing Vowels with input Value (Setting the variable to LOWER case).      "
                  "\n (C3) / (3) Example 3 - Replacing Vowels with input Value (Setting the variable to UPPER case).      "


                  "\n (D) Description\n "
                  "\n           <Enter>  for main menu: ")

        if str(a) == "1":
            example_1()
            continue_lesson()
            definition()

        if str(a) == "c1":
            example_1_code()
            continue_lesson()
            definition()

        if str(a) == "C1":
            example_1_code()
            continue_lesson()
            definition()

        if str(a) == "2":
            example_2()
            continue_lesson()
            end()

        if str(a) == "c2":
            example_2_code()
            continue_lesson()
            definition()

        if str(a) == "C2":
            example_2_code()
            continue_lesson()
            definition()

        if str(a) == "3":
            example_3()
            continue_lesson()
            end()

        if str(a) == "c3":
            example_3_code()
            continue_lesson()
            definition()

        if str(a) == "C3":
            example_3_code()
            continue_lesson()
            definition()

        if str(a) == "r":
            run_all()
        if str(a) == "R":
            run_all()

        if str(a) == "d":
            definition()
        if str(a) == "D":
            definition()
        else:
            import P_1_1_Python_Main_Menu
            P_1_1_Python_Main_Menu.main_menu_1
    definition()