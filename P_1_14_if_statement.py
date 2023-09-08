from PC_1_1_Tools import *
def lesson_14():

    def title():
        new_page()
        print("\n             -----------------------------    Lesson - 14  Working with IF Statments   -----------------------------\n")

    def definition():
        title()
        print("\n Python if statement is one of the most commonly used conditional statements in programming "
              "\n languages. It decides whether certain statements need to be executed or not. It checks for a given"
              "\n condition, if the condition is true, then the set of code present inside the ” if ” block will be executed "
              "\n otherwise not")
        end()

    def EX1():
        title()
        print("                                             ****  Exercise 1 -  IF STATEMENT with Boolean Values - Boolean Value = True ****  ")
        print("We are going to make a simple IF STATEMENT using Boolean value of [True] in the variable [is male]")
        print("Condition 1 - boleen value of  [is male] = [True]\n")
        print("    Here is the code:")
        print("             is_male = True")
        print("             if is_male:")
        print("                 print(\"You are a male\")")
        print("             else:")
        print("                 print(\"you are not a male\")\n")
        print("\nHere is the output:")
        is_male = True
        if is_male:
           print("You are a male")
        else:
            print("you are not a male")
            input("Press <Enter> to continue the lesson")

    def EX2():
        title()
        print("                                             ****  Exercise 2 -  IF STATEMENT with Boolean Values - Boolean Value = False   ****  ")
        print("\nCondition 2 - Boolean value of and if [is_male] = [False]")
        print("    Here is the code:")
        print("             is_male = False")
        print("             if is_male:")
        print("                 print(\"You are a male\")")
        print("             else:")
        print("                 print(\"you are not a male\")\n")
        print("Here is the output:")
        is_male = False

        if is_male:
            print("You are a male")
        else:
            print("you are not a male")

    def EX3():
        title()
        print("                                     **** Exercise 3   IF STATEMENT with [if] [and] and [elif]  ****\n")
        print("We are going to make a more complex IF STATEMENT using boleen value of  [is male]  and [is_tall] =  ")
        print("Boolean value of [is_male] = [True] and [is_tall] = [True]\n")

        print("Here is the code")
        print("    is_male = True")
        print("    is_tall = True")
        print("    if is_male and is_tall:")
        print("        print(\"You are a male and tall\")")
        print("    elif is_male and not (is_tall):")
        print("        print(\"Your a Short Male\")")
        print("    elif not (is_male) and (is_tall):")
        print("        print(\"Your a Tall Female \")")
        print("    else:")
        print("        print(\"Your a Short Female\")")

        is_male = True
        is_tall = True

        if is_male and is_tall:
            print("You are a male and tall")
        elif is_male and not (is_tall):
            print("Your a Short Male")
        elif not (is_male) and (is_tall):
            print("Your a Tall Female ")
        else:
            print("Your a Short Female")

    def EX4():
        print("                                     **** Exercise 4   IF STATEMENT with [if] [and] and [elif]  ****\n")

        print("We are going to make a more complex IF STATEMENT using booleen value of  [is male]  and [is_tall] =  ")
        print("\\, Boolean value of [is_male] = [True] and [is_tall] = [True]\n")

        print("Here is the code")
        print("    is_male = True")
        print("    is_tall = False")
        print("    if is_male and is_tall:")
        print("        print(\"You are a male and tall\")")
        print("    elif is_male and not (is_tall):")
        print("        print(\"Your a Short Male\")")
        print("    elif not (is_male) and (is_tall):")
        print("        print(\"Your a Tall Female \")")
        print("    else:")
        print("        print(\"Your a Short Female\")")

        is_male = True
        is_tall = False

        if is_male and is_tall:
            print("You are a male and tall")
        elif is_male and not (is_tall):
            print("Your a Short Male")
        elif not (is_male) and (is_tall):
            print("Your a Tall Female ")
        else:
            print("Your a Short Female")

    def end():

        a = input("\n Please Select:  "
                  "\n  (D)   Description of Lesson "
                  "\n  (R)   Run all Lessons "
                  "\n  (1) Exercise 1 -  IF STATEMENT with Boolean Values - Boolean Value = True   "
                  "\n  (2) Exercise 2 -  IF STATEMENT with Boolean Values - Boolean Value = False        "
                  "\n  (3) Exercise 3   IF STATEMENT with [if] [and] and [elif]  "
                  "\n  (4) Exercise 4   IF STATEMENT with [if] [and] and [elif]    "

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

