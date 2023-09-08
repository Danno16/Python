from PC_1_1_Tools import *
def lesson_13():

    def title():
        new_page()
        print("\n             -----------------------------    Lesson 13> RETURN STATEMENT   -----------------------------\n")

    def definition():
        title()
        print("The Python return statement is a special statement that you can use inside a function or method to "
              "\nsend the function's result back to the caller. A return statement consists of the return keyword followed"
              "\n by an optional return value. The return value of a Python function can be any Python object.")
        end()

    def EX1():
        title()
        print("                                             ****  Exercise 1 - Using Simple Return Statement  ****"
              "\n*  This portion will go over RETURN STATEMENTs while using a funciton. ")
        print("*  This is good for when you want to call a function and get information back. ")
        print("*  The  function ware are creating is going to cube a number and return it..\n ")
        print("*  Our first simple function is to multiply a number by itself 3 times. ")
        print("*  We will use the number 25.\n ")
        print("Here is the code were using")
        print("                 def cube(num):")
        print("                     return num * num * num")
        print("                 print(cube(25))")
        print("Here is the output:")

        def cube(num):
            return num * num * num

        print(cube(25))

    def EX2():
        title()
        print("                                             ****  Exercise 2 -  FUNCTION with RETURN using a variable   ****  ")
        print(
            "*  Basically were doing the exact same function except were going to Store the value in a varable we are calling [result]. ")
        print("*  We will use the number 5 this time. ")
        print(" * Note you cannot add code after a return statement for that function.\n ")
        print("                     def cube(num):")
        print("                         return num * num * num")
        print("                     result = (cube(5))")
        print("                     print(result)\n")
        print("    Here is the output:")

        def cube(num):
            return num * num * num
        result = (cube(5))
        print(result)

    def EX3():
        title()
        print("                                     **** Exercise 3  FUNCTION with RETURN using an input variable  ****\n")
        print("Now were going to use an input statement.  This is beyond what we have go over but lets see if we "
              "\ncan stretch our coding skills a little.  "
              "\nAt this point it is fully ok if you don't understand it all but I will walk you through the code.  "
              "\nHere is the code we are using:\n")
        print(
            "    a = input(\"input number to multiply 3 times\"  - it will stop the program and store in what number the user uses in the varable \"a|\")")
        print(
            "    def mult(num):                                                  - we set up a function called \"mult\" and the call is called \"num\"")
        print(
            "        return num * num * num                               - this returns the value of num multiplied three times")
        print(
            "    result = (mult(int(a)))                                        - this stores the takes the variable of \"a\", changes it to an integer, multiplies 3 times and stores in \"result\")")
        print(
            "    print(result)                                                       - prints the value in the variable called result\n\n")
        a = input("input number to multiply 3 times:  ")

        def mult(num):
            return num * num * num

        result = (mult(int(a)))
        print(result)

    def end():

        a = input("\n Please Select:  "
                  "\n  (D)   Description of Lesson "
                  "\n  (R)   Run all Lessons "
                  "\n  (1) Exercise 1 -  Using Simple Return Statement  "
                  "\n  (2) Exercise 2 -  FUNCTION with RETURN using a variable        "
                  "\n  (3) Exercise 3 -  FUNCTION with RETURN using an input variable "

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
            end()


        if str(a) == "R":
            EX1()
            continue_lesson()
            EX2()
            continue_lesson()
            EX3()
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

