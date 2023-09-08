from PC_1_1_Tools import *
def lesson_12():

    def title():
        new_page()
        print("\n                                -----------------------------    Lesson 12> Working with Functions   -----------------------------")

    def definition():
        title()
        print("A function is a block of code which only runs when it is called. You can pass data, known as parameters, "
              "\ninto a function. A function can return data as a result.\n"
              "\nThe following are the different types of Python Functions:"
              "\n             *         Python Built-in Functions.  "
              "\n             *         Python Recursion Functions."
              "\n             *         Python Lambda Functions."
              "\n             *         Python User-defined Functions."
              )
        end()

    def EX1():
        title()
        print("                                    ****  Exercise 1 -  Simple  FUNCTION that says HI    ****  ")
        print(" * Here is an example of a simple function to say \"HI\".")
        print(
            " * When you name a function you want to use all lower case and in mult words us a   \"_\" where you would normally use a space. ")
        print("\nHere is the code we are going to use:")
        print("                    def say_hi(): ")
        print("                         print(\"Hello User\")")

        def say_hi():
            print("Hello User")

        print("\n * So at any time we can call the function that we named (say_hi) by just typing \"say_hi()\".")
        print(" Example:  here is the code were using:")
        print("                         say_hi()")
        say_hi()

    def EX2():
        title()
        print("                                    ****  Exercise 2 -  Simple  FUNCTION that says HI with hard coded names    ****  ")
        print(" * Now when you call the function and add a name in the call comman it will print out hello with a name that is hard coded")
        print(" * We are going to use the same FUNCTION name.  Now the variable data is in the call command.  I'll show you an example, so hopefully it will make more since")
        print("\ndef say_hi(name):")
        print("     print(\"Hello User \" + name)")
        print("say_hi(\"Dan \")")
        print("say_hi(\"George\")")
        def say_hi(name):
            print("Hello User " + name)

        print("\n         Here is the output:")
        say_hi("Dan ")
        say_hi("George ")

    def EX3():
        title()
        print("                                    **** Exercise 3 - Simple  FUNCTION that says HI with hard coded names and age (Mult Parameters) ****")
        print(" *Now we add more than 1 parameter.  We'll include the age\n")
        print("The code to be used is:")
        print("             def say_hi(name, age):")
        print("                  print(\"Hello User \" + name + \"is your age really \" + age + \"?\")")
        print("             say_hi(\"Dan \", \"17\")")
        print("             say_hi(\"George \", \"12\")\n")
        print(" Now lets run the code:")

        def say_hi(name, age):
            print("Hello User " + name + "is your age really " + age + "?")

        say_hi("Dan ", "17")
        say_hi("George ", "12")

    def EX4():
        title()
        print("                                    **** Exercise 4 - Simple  FUNCTION that says HI with hard coded names and age (age as numeric) ****")
        print(" *This time were going to use the age variable but as an integer instead of a string.")
        print(
            " * Looks exactly the same but set the parameter is a numeric.  So in order to print it in a sentence we have to converte to a string.")
        print(" * Hopefully it will make more since when you see the code.\n")
        print("             def say_hi(name, age):")
        print(
            "                     print(\"Hello User \" + name + \"is your age really \" + str(age) + \"?\")           - Note [str(age)] is changing the variable \"age\" to a string")
        print(
            "             say_hi(\"Dan \", 21)                                                                                              - Note - 21 is entered as an number")
        print(
            "             say_hi(\"George \", 19)                                                                                         - Note - 19 is entered as an number")
        print("\n Now lets run the code:")
        def say_hi(name, age):
            print("Hello User " + name + "is your age really " + str(age) + "?")


        say_hi("Dan ", 21)
        say_hi("George ", 19)

        print(
            " \n*You can pass any kind of data to include strings, numbers, bullion's, arrays, or whatever you want. ")

    def end():

        a = input("\n Please Select:  "
                  "\n  (D)   Description of Lesson "
                  "\n  (R)   Run all Lessons "
                  "\n  (1) Exercise 1 -  Simple  FUNCTION that says HI "
                  "\n  (2) Exercise 2 -  Simple  FUNCTION that says HI with hard coded names    "
                  "\n  (3) Exercise 3 -  Simple  FUNCTION that says HI with hard coded names and age (Mult Parameters) "
                  "\n  (4) Exercise 4  - Simple  FUNCTION that says HI with hard coded names and age (age as numeric)  "

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

