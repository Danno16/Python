
from PC_1_1_Tools import *

def lesson_26():

    def title():
        new_page()
        print(
            "\n                                   -----------------------------------    Lesson 26  - Modules and PIP  -----------------------------\n")

    def definition():
            title()
            print("\n -   Modules are simply files with the “. py” extension containing Python code that can be imported inside another Python Program.")
            print("\n -   We can consider a module to be the same as a code library or a file that contains a set of functions that you want to include in your application.")

            print("\n -   PIP is the package installer for Python. You can use pip to install packages from the Python Package Index and other indexes."
                  "\n      NOTE - PIP usually comes installed with Python Version 3 and above.\n")

            end()


    def run_all():
        print("Run All")
        end()

    def EX1():
        title()
        print("                                                                  Exercise 1 - Make sure you have PIP")
        print("\nMake sure you have pip by opening command prompt (CMD)"
              "\n           *   At the command line type \"pip --verson\" - I have verson 2.3.1"
              "\n           *   If you don't have pip you can look up in google to install\n")


    def EX2():
        title()
        print("                                                                                  Exercise 2 - Installing a module")
        print("\n How to install a Module:"
              "\n           *   We are using the example of \"Python Docs\" to install."
              "\n           *   Look in Google for the instructions.  It will say \"pip install python-docx\"."
              "\n           *    So at the command line type \"pip install python-docx\" and it will install pyton docs\"." 
              "\n           *    It stores it in Lib\site-packages.  If you downloaded it and look at Lib\site-packages, you will see it." 
              "\n           *    You will notice that it no only created a folder called \"pip install python-docx\", it also created \"docx\". "         
              "\n\n If you want to use in our program.  You just need to refer to the name of the module." 
              "\n           *  in this case it would be \"from docx import *\".\n"
                )

    def EX3():
        title()
        print("                                                                             Exercise 3 - Using modules")
        print("\n Created Modules - I created new modules (files) called:"
              "\n                       *       0-1-1_Useful-Tools.py                                      -       Where I put Various Tools I use.  "
              "\n                       *       B_1_26_Lesson_26_Modules_and_PiP.py      -       Where this lesson is stored"
              "\n                       That I will import and use the functions stored within the module "
               "\n                      There are built in modules and external modules            "
              "\n   Internal   - If you go to D\External Libraries\Lib you will see the external modules."
              "\n                       * You can access the functions in the modules by importing the given module"
              "\n                       *  \"import docx\" "
              "\n\n External Modules:"
              "\n                       * If you look in Google \"Python Module Index\" you will find Thounds of additional modules  in Google. "
             "\n                       * You can look/up install 3rd party modules  "
              "\n                                NOTE   -  You have to know what version of python to find the correct modules."
              )

    def run_all_lessons():
        EX1()
        continue_lesson()
        EX2()
        continue_lesson()
        EX3()

        end()


    def end():
        print("                                                                                  Lesson Menu")
        a = input("\n Please Select: To see the code behind the example put \"C\" before the number\n"
                  "\n  (D)   Description of Lesson "
                  "\n  (R)   Run all Lessons "
                  "\n  (1) Exercise 1 - Make sure you have PIP      "
                  "\n  (2) Exercise 2 - Installing a module                "
                  "\n  (3) Exercise 3 - Using modules    "


                  "\n           <Enter>  for main menu: ")

        if str(a) == "d":
            definition()

        if str(a) == "D":
            definition()

        if str(a) == "r":
            run_all_lessons()

        if str(a) == "R":
            run_all_lessons()

        if str(a) == "1":
            EX1()
            end()

        if str(a) == "2":
            EX2()
            end()

        if str(a) == "3":
            EX3()
            end()
        else:
            import P_1_1_Python_Main_Menu
            P_1_1_Python_Main_Menu.main_menu_1

    definition()
