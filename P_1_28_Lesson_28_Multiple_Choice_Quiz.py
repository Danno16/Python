
from PC_1_1_Tools import *
from PC_1_1_1_Class_file import Car
from PC_1_1_1_Class_file import Question

def lesson_28():
    ''''***********************************************************************************************************************
    *                                                               Car Trivia  - Game 1                                                                    *
    *************************************************************************************************************************'''

    def f1_car_trivia():
        title()
        print(
            "                                                            ------------            Car Trivia  - Game 1              --------------- \n")


        question_prompts = [
            "1. What is the best selling electric car model of all time?"
            "\n (a) Tesla Model S"
            "\n (b) Tesla Model 3"
            "\n (c) Tesla Model X"
            "\n (d) Tesla Model Y\n\n",

            "2. What German car brand has a logo that features four interlocking rings??"
            "\n (a)  BMW"
            "\n (b)  Audi"
            "\n (c)  Mercedes"
            "\n (d)  all the above\n\n",

            "3. What car company has produced the Corolla model since 1966?"
            "\n (a)  Datsun"
            "\n (b)  Toyota"
            "\n (c)  Nissian"
            "\n (d)  Honda\n",

            "4. What car brand produces the popular F-150 truck?"
            "\n (a)  Chevy"
            "\n (b)  Dodge"
            "\n (c)  Ford"
            "\n (d)  Pizza \n",

        ]

        questions = [
            Question(question_prompts[0], "b"),
            Question(question_prompts[1], "b"),
            Question(question_prompts[2], "b"),
            Question(question_prompts[3], "c"),

        ]

        def run_test(questions):
            score = 0
            for question in questions:
                answer = input(question.prompt + "Please select multiple choice:  ")
                if answer == question.answer:
                    print("Your are Correct\n")
                    score += 1
                else:
                    print("Incorrect\n")
            print("                     ****        Your got " + str(score) + "/" + str(
                len(questions)) + " Correct!!!              ****")

        run_test(questions)

        a = input("\nEnter \"y\" to play again or <Enter> to  Quiz Menu>):  ")
        if str(a) == "y":
            t1_python_trivia_1()
        elif str(a) == "y":
            t1_python_trivia_1()
        else:
            menu()


    '''  ==================================================================================
                                                                Tech Quiz Section
        ==================================================================================='''

    ''''***********************************************************************************************************************
    *                                                               Python Trivia  - Game 1                                                                    *
    *************************************************************************************************************************'''

    def t1_python_trivia_1():
        title()
        print(
            "                                                      ------------            Python Trivia  - Game 1              --------------- \n")
        question_prompts = [
            "1. Who developed Python Programming Language?"
            "\n (a) Wick van Rossum"
            "\n (b)  Rasmus Lerdorf"
            "\n (c)  Guido van Rossum"
            "\n (d)  Niene Stom\n\n",

            "2. Which type of Programming does Python support?"
            "\n (a)  object-oriented programming"
            "\n (b)  structured programming"
            "\n (c)  functional programming"
            "\n (d)  all the above\n\n",

            "3. Is Python case sensitive when dealing with identifiers?"
            "\n (a)  no"
            "\n (b)  yes"
            "\n (c)  machine dependent"
            "\n (d)  Non of the above\n",

            "4. Which of the following is the correct extension of the Python file?"
            "\n (a)  python"
            "\n (b)  .pl"
            "\n (c)  .py"
            "\n (d)  .p \n",

            "5. Is Python code compiled or interpreted?"
            "\n (a)  Python code is both compiled and interpreted"
            "\n (b)  Python code is neither compiled nor interpreted"
            "\n (c)  Python code is only compiled"
            "\n (d)  Python code is only interpreted \n",

            "6. All keywords in Python are in _________"
            "\n (a)  Capitalized"
            "\n (b)  lower case"
            "\n (c)  UPPER CASE"
            "\n (d)  None of the Above \n",

            "7. What will be the value of the following Python expression?\n 4 + 3 % 5"
            "\n (a)  7"
            "\n (b)  2"
            "\n (c)  4"
            "\n (d)  1 \n",

            "8. Which of the following is used to define a block of code in Python language?"
            "\n (a)  Indentation"
            "\n (b)  Key"
            "\n (c)  Brackets"
            "\n (d)  All the above \n",

            "9. Which keyword is used for function in Python language?"
            "\n (a)  Function"
            "\n (b)  def"
            "\n (c)  Fun"
            "\n (d)  Define \n",

            "10.  Which of the following character is used to give single-line comments in Python?"
            "\n (a)  //"
            "\n (b)  #"
            "\n (c)  !"
            "\n (d)  /* \n",

        ]

        questions = [
            Question(question_prompts[0], "c"),
            Question(question_prompts[1], "d"),
            Question(question_prompts[2], "b"),
            Question(question_prompts[3], "c"),
            Question(question_prompts[4], "a"),
            Question(question_prompts[5], "d"),
            Question(question_prompts[6], "a"),
            Question(question_prompts[7], "a"),
            Question(question_prompts[8], "b"),
            Question(question_prompts[9], "b"),
        ]

        def run_test(questions):
            score = 0
            for question in questions:
                answer = input(question.prompt + "Please select multiple choice:  ")
                if answer == question.answer:
                    print("Your are Correct\n")
                    score += 1
                else:
                    print("Incorrect\n")
            print("                     ****        Your got " + str(score) + "/" + str(
                len(questions)) + " Correct!!!              ****")

        run_test(questions)

        a = input("\nEnter \"y\" to play again or <Enter> to  Quiz Menu>):  ")
        if str(a) == "y":
            t1_python_trivia_1()
        elif str(a) == "y":
            t1_python_trivia_1()
        else:
            menu()

    ''''***********************************************************************************************************************
    *                                                               Python Trivia  - Game 2                                                                    *
    *************************************************************************************************************************'''

    def t2_python_trivia_2():
        title()
        print(
            "                                                        ------------            Python Trivia  - Game 2              --------------- \n")
        question_prompts = [
            "11. What will be the output of the following Python code?\n"
            "\ni = 1"
            "\nwhile True:"
            "\n    if i%3 == 0:"
            "\n    print(i)\n"
            "\n   i + = 1\n"

            "\n (a) 1 2 3"
            "\n (b)  error - shouldn’t be a space between + and = in +="
            "\n (c)  1 2"
            "\n (d)  None of the above\n\n",

            "12. Which of the following functions can help us to find the version of python that we are currently working on?"
            "\n (a)  sys.version(1)"
            "\n (b)  sys.version(0)"
            "\n (c)  sys.version()"
            "\n (d)  sys.version\n\n",

            "13. Python supports the creation of anonymous functions at runtime, using a construct called __________"
            "\n (a)  pi"
            "\n (b)  anonymous"
            "\n (c)  lambda"
            "\n (d)  Non of the above\n",

            "14. What is the order of precedence in python?"
            "\n (a)  Exponential, Parentheses, Multiplication, Division, Addition, Subtraction"
            "\n (b)  Exponential, Parentheses, Division, Multiplication, Addition, Subtraction"
            "\n (c)  Parentheses, Exponential, Multiplication, Division, Subtraction, Addition"
            "\n (d)  Parentheses, Exponential, Multiplication, Division, Addition, Subtraction \n",

            "15. What will be the output of the following Python code snippet if x=1?\n"
            "x<<2"
            "\n (a)  4"
            "\n (b)  2"
            "\n (c)  Python code is only compiled"
            "\n (d)  Python code is only interpreted \n",

            "16. What does pip stand for python"
            "\n (a)  Pip Installs Python"
            "\n (b)  Pip Installs Packages"
            "\n (c)  Preferred Installer Program"
            "\n (d)  all of the Above \n",

            "17. Which of the following is true for variable names in Python?"
            "\n (a)  underscore and ampersand are the only two special characters allowed"
            "\n (b)  unlimited length"
            "\n (c)  all private members must have leading and trailing underscores"
            "\n (d)  none of the Above \n",

            "18. What are the values of the following Python expressions?"
            "\n2**(3**2)"
            "\n(2**3)**2"
            "\n2**3**2\n"
            "\n (a)  512, 64, 512"
            "\n (b)  512, 512, 512"
            "\n (c)   64, 512, 64"
            "\n (d)   64, 64, 64 \n",

            "19. Which of the following is the truncation division operator in Python?"
            "\n (a)  |"
            "\n (b)  //"
            "\n (c)  /"
            "\n (d)  % \n",

            "20. What will be the output of the following Python code?"
            "\n l=[1, 0, 2, 0, 'hello', \'', []]"
            "\nlist(filter(bool, l))\n"
            "\n (a)   [1, 0, 2, ‘hello’, ”, []]"
            "\n (b)  Error"
            "\n (c)   [1, 2, ‘hello’]"
            "\n (d)   [1, 0, 2, 0, ‘hello’, ”, []] \n",

        ]

        questions = [
            Question(question_prompts[0], "b"),
            Question(question_prompts[1], "d"),
            Question(question_prompts[2], "c"),
            Question(question_prompts[3], "d"),
            Question(question_prompts[4], "a"),
            Question(question_prompts[5], "c"),
            Question(question_prompts[6], "b"),
            Question(question_prompts[7], "a"),
            Question(question_prompts[8], "b"),
            Question(question_prompts[9], "c"),
        ]

        def run_test(questions):
            score = 0
            for question in questions:
                answer = input(question.prompt + "Please select multiple choice:  ")
                if answer == question.answer:
                    print("Your are Correct\n")
                    score += 1
                else:
                    print("Incorrect\n")
            print("                     ****        Your got " + str(score) + "/" + str(
                len(questions)) + " Correct!!!              ****")

        run_test(questions)

        a = input("\nEnter \"y\" to play again or <Enter> to  Quiz Menu>):  ")
        if str(a) == "y":
            t2_python_trivia_2()
        elif str(a) == "y":
            t2_python_trivia_2()
        else:
            menu()

    ''''***********************************************************************************************************************
    *                                                               Python Trivia  - Game 3                                                                    *
    *************************************************************************************************************************'''

    def t3_python_trivia_3():
        title()
        print(
            "                                                        ------------            Python Trivia  - Game 3              --------------- \n")

        question_prompts = [
            " 0b- 21. Which of the following functions is a built-in function in python?"

            "\n (a) factorial()"
            "\n (b) print()"
            "\n (c) seed()"
            "\n (d) sqrt()\n\n",

            "1b- 22. Which of the following is the use of id() function in python?\n"
            "\n (a)  Every object does not have a unique id"
            "\n (b)  Id returns the identity of the object"
            "\n (c)  All of the mentioned"
            "\n (d)  None of the mentioned\n\n",

            "2a- 23. The following python program can work with ____ parameters.\n"
            "\n     def f(x):"
            "\n          def f1(*args, **kwargs):"
            "\n                     print(\"Sanfoundry\")"
            "\n                     return x(*args, **kwargs)"
            "\n     return f1\n"
            "\n (a)  any number of"
            "\n (b)  0"
            "\n (c)  1"
            "\n (d)  2\n",

            "3d 24. What will be the output of the following Python function?"
            "\nmin(max(False,-3,-4), 2,7)\n"

            "\n (a)  4"
            "\n (b)  -3"
            "\n (c)  2"
            "\n (d)  False \n",

            "4c- 25. Which of the following is not a core data type in Python programming?\n"

            "\n (a)  Tuples"
            "\n (b)  Lists"
            "\n (c)  Class"
            "\n (d)  Dictionary\n",

            "5d- 26. How you  doing?"

            "\n (a)  Been Better"
            "\n (b)  okay"
            "\n (c)  good"
            "\n (d)  Great\n",

            "6b- 27. Which of these is the definition for packages in Python?"
            "\n (a)  A set of main modules"
            "\n (b)  A folder of python modules"
            "\n (c)  A number of files containing Python definitions and statements"
            "\n (d) A set of programs making use of Python modules \n",

            "7c- 28. What will be the output of the following Python function?"
            "\nlen([\"hello\",2, 4, 6])"

            "\n (a)  Error"
            "\n (b)  6"
            "\n (c)  4"
            "\n (d)  3 \n",

            "8d  29. What will be the output of the following Python code?"
            "\n     x = 'abcd'"
            "\n     for i in x:"
            "\n         print(i.upper())"

            "\n (a) a\n B\n C\n D"
            "\n (b) a b c d"
            "\n (c)  error"
            "\n (d) A\n B\n C\n D"

            "8c  30. What is the order of namespaces in which Python looks for an identifier?"


            "\n (a) Python first searches the built-in namespace, then the global namespace and finally the local namespace"
            "\n (b) Python first searches the built-in namespace, then the local namespace and finally the global namespace"
            "\n (c) Python first searches the local namespace, then the global namespace and finally the built-in namespace"
            "\n (d) Python first searches the global namespace, then the local namespace and finally the built-in namespace"
        ]

        questions = [
            Question(question_prompts[0], "b"),
            Question(question_prompts[1], "b"),
            Question(question_prompts[2], "a"),
            Question(question_prompts[3], "d"),
            Question(question_prompts[4], "c"),
            Question(question_prompts[5], "d"),
            Question(question_prompts[6], "b"),
            Question(question_prompts[7], "c"),

        ]

        def run_test(questions):
            score = 0
            for question in questions:
                answer = input(question.prompt + "\nPlease select multiple choice:  ")

                if answer == question.answer:
                    print("Your are Correct\n")
                    score += 1
                else:
                    print("Incorrect\n")
            print("                     ****        Your got " + str(score) + "/" + str(
                len(questions)) + " Correct!!!              ****")

        run_test(questions)

        a = input("\nEnter \"y\" to play again or <Enter> to  Quiz Menu>):  ")
        if str(a) == "y":
            t3_python_trivia_3()
        elif str(a) == "y":
            t3_python_trivia_3()
        else:
            menu()

    ''''***********************************************************************************************************************
    *                                                               Coding                                                                  *
    *************************************************************************************************************************'''

    def title():
        new_page()
        print(
            "\n                                   -----------------------------------    Lesson - 28  Quiz Time   -----------------------------\n")

    def menu():
        title()
        print("Now were going to have some fun.  I created a series of multiple choice quiz.   "
              "\nIt's for both to have fun and help learn programming and to help me learn classes better"
              "\n                See below for quizes  \n"
              "\n                                      Fun                                               Health                                        Technology"
              "\n--------------------------------------------------------------------------------------------------------------------------------------"
              "\n                               F1 - Cars  (WIP)                           H1 - Weight Lifting  (TBD)        T1 - Python Programming - Easy "
              "\n                               F2 - Motorcycles (TBD)                H2 - Cardio             (TBD)         T2 - Python Programming - Medium"
              "\n                               F3 - SXS (TBD)                            H3 - Outdoor Activity  (TBD       T3 - Python Programming - Hard)"
              "\n                               F4 - Electric Bikes (TBD)             H4 - Everyday Activity  (TBD     T4 - HTML \ CSS Programming (TBD"
              "\n                               F5 - Electric Motorcycles (TBD)                                                      T5 - Selenium (TBD)"
              "\n                                                                                                                                         T6 - JavaStrip (TBD)"
              "\n                                                                                                                                         T7 - Python GUI (TBD)"
              )
        end()

    def end():
        a = input("\nPlease select Quiz:  ")

        if str(a) == "f1":
            f1_car_trivia()
        elif str(a) == "F1":
            f1_car_trivia()
        elif str(a) == "t1":
            t1_python_trivia_1()
        elif str(a) == "T1":
            t1_python_trivia_1()
        elif str(a) == "t2":
            t2_python_trivia_2()
        elif str(a) == "T2":
            t2_python_trivia_2()
        elif str(a) == "t3":
            t3_python_trivia_3()
        elif str(a) == "T3":
            t3_python_trivia_3()
        else:
            import P_1_1_Python_Main_Menu
            P_1_1_Python_Main_Menu.main_menu_1

    menu()
