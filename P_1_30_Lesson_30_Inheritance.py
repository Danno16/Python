
from PC_1_1_Tools import *


from PC_1_1_1_Class_file import chef_class1
from PC_1_1_1_Class_file import chef_class2



def continue_lesson():
    input(" press <Enter> to Continue: "
          "")

def new_page():
    for i in range (20):
        print("")


def lesson_30():

    def title():
        new_page()
        print(
            "\n                                   -----------------------------------    Lesson 30  - Inheritance -----------------------------\n")

    def definition():
            title()
            print("\n       *   Inheritance allows us to define a class that inherits all the methods and properties from another class. "
                  "\n           Parent class is the class being inherited from, also called base class. "
                  "\n           Child class is the class that inherits from another class, also called derived class.\n"
                  "\n       *   Inheritance is basically where we can define a bunch of attributes, functions and things inside"
                  " \n                 of a class.  Then we can create another class and inherit all of those attributes.\n"
                  "\n       *   So you can have one class that has all the functionality of another class without having to physically write out"
                  "any of the same methods or attributes."

                  "\n\n        *  There are 5 type of inheritance:"
                  "\n               -    Single Inheritance. "
                  "\n               -    Multiple Inheritance."
                  "\n               -    Multilevel Inheritance."
                  "\n               -    Hierarchical Inheritance."
                  "\n               -    Hybrid Inheritance.\n"
                  )
            continue_lesson()
            end()


    def run_all_lessons():
        EX1()
        EX2()
        EX3()
        continue_lesson()
        end()

    def EX1():
        title()
        print("                                                         Exercise 1 - Building a common class")
        print(
            "\n     Created a new class in our class file we created earlier.  The class file is calledC_1_1_1_Class_file.py"
            "\n   and the name of the new class I built is called \"chef_class1\":"
            "\n\nHere is the look at the class:\n"
            "\n                 class chef_class1:"
            "\n                           def make_chicken(self):"
            "\n                               print(\"The chef makes a chicken\""
            "\n                           def make_salad(self):"
            "\n                               print(\"The chef makes a salad\""
            "\n                           def make_special_dish(self):"
            "\n                               print(\"The chef makes BBQ ribs\"\n"
        )
        continue_lesson()
        title()

        print("  Step 2 - Now we have to import the class we just made:"
              "\n                   from C_1_1_1_Class_file import chef_class\n"
              "\n\n   Step 3 - Now here is the code we used to use the class:"
              "\n                   mychef = chef_class()"
              "\n                   mychef.make_chicken()"
              "\n                   mychef.make_chicken()"
              "\n                   mychef.make_special_dish()\n"
              "\n\n   Step 4 - Now lets run the code:"
              )

        mychef = chef_class1()
        mychef.make_chicken()
        mychef.make_salad()
        mychef.make_special_dish()
        print()
        continue_lesson()

    def EX2():
        title()
        print("                                                         Exercise 2 - Using the Common Class and adding Inheritance   ")
        print("\n       In the previous exercise, we built a common class using a chef1. Now we have another chef (chef2)"
              "\n   and chef2 has the exact same attributes as chef1.  Now we could copy and paste, but that would be "
              "\n   inefficent and if you had any updates you'd have to remember to update both chefs.  So the answer to "
              "\nthis is inherit the class.  Hopefully this will make more since when we view the code.\n  "
              
              "\n       I created a new class in our class file we created earlier.  The class file is calledC_1_1_1_Class_file.py"
              "\n   that will inherit the attributes of chef1.  The new class name is \"chef_class2\".  This will be an inherit class."
              "\n   We also added another attribute unique to chef 2, which is \"is_pizza\". "

              "\n\nHere is the look at the class:\n"
              "\n                 class chef_class2(chef_class1):"
              "\n                           def make_pizza(self):"
              "\n                               print(\"The chef makes pizza\")\n"

              )
        continue_lesson()
        title()

        print("  Step 2 - Now we have to import the class we just made:"
              "\n                   from C_1_1_1_Class_file import chef_class\n"
              "\n\n   Step 3 - Now here is the code we used to use the class:"
              "\n                   mychef = chef_class2()"
              "\n                   mychef.make_chicken()"
              "\n                   mychef.make_salad()"
              "\n                   mychef.make_special_dish()\n"
              "\n                   mychef.make_pizza()"
              "\n\n   Step 4 - Now lets run the code:"
              )
        mychef = chef_class2()
        mychef.make_chicken()
        mychef.make_salad()
        mychef.make_special_dish()
        mychef.make_pizza()
        print()


    def EX3():
        title()
        print(
            "                              Exercise 3 - Overriding Attribute in Inheritance Class")
        print(
            "\n      Another powerful item we can do is override an attribute.  in this exercise we are going to override "
            "\n     chef1's special (\"The chef makes a BBQ ribs\") , with a new dish for chef2.  We'll say hamburger."
            "\n\n       So lets first recap the class for chef1:"
            "\n                 class chef_class1:"
            "\n                           def make_chicken(self):"
            "\n                               print(\"The chef makes a chicken\")"
            "\n                           def make_salad(self):"
            "\n                               print(\"The chef makes a salad\")"
            "\n                           def make_special_dish(self):"
            "\n                               print(\"The chef makes BBQ ribs\"\n)")
        continue_lesson()
        title()
        print("        So lets look at the existing class for chef2 (before the change)"
            "\n                  class chef_class2(chef_class1):"
           "\n                           def make_pizza(self):"
           "\n                               print(\"The chef makes pizza\")"
              
           "\n\n        Now lets look at the override code:"
            "\n                  class chef_class2(chef_class1):"
            "\n                           def make_pizza(self):"
            "\n                               print(\"The chef makes pizza\")"
            "\n                           def make_special_dish(self):"
            "\n                               print(\"The chef makes hamburger\")\n"
            )
        continue_lesson()
        title()

        print("  Step 3 - Now here is the code we used to use the class:"
              "\n                   mychef = chef_class2()"
              "\n                   mychef.make_chicken()"
              "\n                   mychef.make_salad()"
              "\n                   mychef.make_special_dish()"
              "\n                   mychef.make_pizza()\n"
              "\n   NOTE - it overrode make_special_dish() from bbq to hamburger"
       
              "\n\n   Step 4 - Now lets run the code:"
              )
        mychef = chef_class2()
        mychef.make_chicken()
        mychef.make_salad()
        mychef.make_special_dish()
        mychef.make_pizza()

        print()


    def end():
        print("                                                                                  Lesson Menu")
        a = input("\n Please Select:  "
                  "\n  (D)   Description of Lesson "
                  "\n  (R)   Run all Lessons "
                  "\n  (1) Exercise 1 - Building a common class   "
                  "\n  (2) Exercise 2 - Using the Common Class and adding Inheritance        "
                  "\n  (3) Exercise 3 - Overriding Attribute in Inheritance Class    "


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
            continue_lesson()
            end()

        if str(a) == "2":
            EX2()
            continue_lesson()
            end()

        if str(a) == "3":
            EX3()
            continue_lesson()
            end()

        else:
            import P_1_1_Python_Main_Menu
            P_1_1_Python_Main_Menu.main_menu_1

    definition()



