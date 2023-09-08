
from PC_1_1_Tools import *

from PC_1_1_1_Class_file import student
from PC_1_1_1_Class_file import Car

student1 = student("Jim", "Business", "3.1", False)
student2 = student("Pam", "Art", "2.3", True)

Car1 = Car("Ford", "Mustang", "2008", True)
Car2 = Car("Fod", "Mustang", "2008", True)
Car3 = Car("Frd", "Mustang", "2008", True)
Car4 = Car("Fd", "Mustang", "2008", True)
Car5 = Car("a", "Mustang", "2008", True)

elt = Car1.getModel()

print(student1.name)
print(student1.gpa)

print(student2.name)
print(student2.gpa)

print(Car1.Make)
print(Car1.Model)
print(Car1.Year)
print(Car1.Would_you_buy)

print(Car2.getModel())










def lesson_27():

    def title():
        new_page()
        print(
            "\n                                   -----------------------------------    Lesson 27  - Classes and Objects  -----------------------------\n")

    def definition():
            title()
            print("\nWhat is an object:"
                  "\n  *    Python is an object oriented programming language. "
                  "\n  *    Almost everything in Python is an object, with its properties and methods."
                  "\n  *    Objects have member variables and have behaviour associated with them. In python a class is created by the keyword class . An object is created using the constructor of the class."
            
                  "\n\nWhat is a Class"        
                  "\n   *  A Class is like an object constructor, or a \"blueprint\" for creating objects."
                  "\n   *  A class is a code template for creating objects. "
                  " \n   *   In python a class is created by the keyword class."
                  "\n   *   Class is another datatype we can use in python.\n\n"
                  )


            enter_lesson_menu()
            end()


    def run_all():
        print("Run All")
        continue_lesson()
        end()

    def EX1():
        title()
        print("                                                                  Exercise 1 - Creating a Class")
        print("\nStep 1 - Create a new file Python file (.py).  I called it \"PC_1_1_1_Class_file.py\""
              "\n\nStep 2 - Create a class within that new python file  "
              "\n     *   It begins with \"class\" ."
              "\n     *   Followed by the name of the class then a colon \":\"."
              "\n     *   I called mine  \"class Car:\""
              "\n\nStep 3 -  Create an initialized function."
              "\n     *     Use \"def\" space, two underscores \"__\" the word \"init\" two more underscores \"__\" then \"(self) followed by colon\":\""
              "\n     *     Here is the full command:    def __init__(self):\n"

              )
        continue_lesson()
        title()
        print("                                                                  Exercise 1 - Creating a Class")
        print("\n\nStep 4 - Assign the attributes of the class you can you use Strings, Numbers and Booleans.  How you do this is:"
        "\n         * Add in Attributes after \"Self,\")  These can be anything you want.  I used Make, Model, Year, Would I buy"
        "\n         * Here is what it looks like  \"def __init__(self, Make, Model, Year, Would_you_buy):\" \n " \
        "")


        print("\nStep 5 - Now we have to assign some Values.  In order to do this we have to assign the attribute with a variable."
              "\n         *   The format is: \"self.\" the name of the attribute, followed by the name of the variable (you can use any name for the variable"
              "\n         *   Here is an example of the one i created:"
              "\n                      -      self.Make  = Make"
              "\n                      -      self.Model = Model"
              "\n                      -      self.Year    = Year"
              "\n                      -      Would_you_buy = Would_you_buy \n"
              )
        continue_lesson()
        title()
        print("                                                                  Exercise 1 - Creating a Class")
        print("\nHere is the full file:"
              "\n                           1   class Car:"
              "\n                           2      def __init__(self, Make, Model, Year, Would_you_buy):"
              "\n                           3       self.Make = Make"
              "\n                           4       self.Model = Model"
              "\n                           5       self.Year = Year"
              "\n                           6       self.Would_you_buy = Would_you_buy\n"
              "\n\n And that is how you create a class."
              )


    def EX2():
        title()
        print("                                                                       Exercise 2 - Assigning the Attributes in the class")
        print("\n In the Python file you are working in (not the class file) you assign must:"
              "\n Step 1 - import the file.  Your code \"from\" name of the Class Python File \"import\" then the name of the class"
              "\n                                                                1   from C_1_1_1_Class_file import Car "
              "\n \nStep 2 - Assign the attributes."
              "\n * New Variable, \"=\" Class name \"(\"attrubute 1\",\" attrubute 2\" followed by all the (attributes assigned)  \")\". "
              "\n * Here is what I used                             2   Car1 = Car(\"Ford\", \"Mustang\" \"2008\", True)"
              "\n\n Step 3 - Now we can print any attrubute we want:"
              "\n       If we want to print the Make -          3   print(Car1.Make)  "
              "\n       If we want to print the Make -          4   print(Car1.Model)  "
               "\n       If we want to print the Year -           5   print(Car1.Year)  "
              "\n       If we want to print the Make -          6   print(Car1.Would_you_buy)  "
                )

    def EX3():
        title()
        print("                                                                             Exercise 3 - Printing the Attrubutes in the Class")
        print("\n At this point, I'll show you the code followed by the output"
              "\n           Code used:"
              "\n                              1         from C_1_1_1_Class_file import Car "
              "\n                              2        Car1 = Car(\"Ford\", \"Mustang\" \"2008\", True)"
              "\n                              3        print(Car1.Make)  "
              "\n                              4        print(Car1.Model)  "
              "\n                              5        print(Car1.Year)  "
              "\n                              6        print(Car1.Would_you_buy)  " 
              "\n\n           Output:"
              "")
        Car1 = Car("Ford", "Mustang", "2008", True)
        print(Car1.Make)
        print(Car1.Model)
        print(Car1.Year )
        print(Car1.Would_you_buy )
        print("")
        continue_lesson()
        title()
        print(
            "                                                                             Exercise 3 - Printing the Attrubutes in the Class")
        print("\n Lets enter another input.  Note we are using Car2 this time"
              "\n           Code used:"
              "\n                              1         from C_1_1_1_Class_file import Car "
              "\n                              2        Car1 = Car(\"GMC\", \"Hummer\" \"2008\", True)"
              "\n                              3        print(Car1.Make)  "
              "\n                              4        print(Car1.Model)  "
              "\n                              5        print(Car1.Year)  "
              "\n                              6        print(Car1.Would_you_buy)  "
              "\n\n           Output:"
              "")
        Car1 = Car("GMC", "Hummer H3", "2008", True)
        print(Car1.Make)
        print(Car1.Model)
        print(Car1.Year)
        print(Car1.Would_you_buy)
        print("")


    def run_all_lessons():
        EX1()
        continue_lesson()
        EX2()
        continue_lesson()
        EX3()
        continue_lesson()
        end()


    def end():
        title()
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




