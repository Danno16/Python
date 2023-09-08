

from PC_1_1_Tools import *

from PC_1_1_1_Class_file import student_object

def lesson_29():
    def title():
        new_page()
        print(
            "\n                                   -----------------------------------    Lesson 29 - Object Function  -----------------------------\n")

    def definition():
        title()
        print("\nWhat is an object:"
              "\n       -   The object() function returns an empty object. You cannot add new properties or methods to this object. "
              "\n       -   This object is the base for all classes, it holds the built-in properties and methods which are default for all classes."
              "\n\n      -     Class Function is a function that we can use inside of a class and it can either modify tthe object of that class"
              "\n                   or give specific information about those objects.\n\n"
              )
        continue_lesson()
        ex1()


    def ex1():
        title()
        print("                                                                  Exercise 1 - Creating a Class")
        print("\nStep 1 - I created a new class in our class file we created earlier.  The class file is calledC_1_1_1_Class_file.py"
              "\n   and the name of the new class I built is called \"class student_object\""
              "\n\nHere is the look at the class:\n"
              "\n                 class student_object:"
              "\n                           def __init__(self, name, major, gpa):"
              "\n                           self.name = name"
              "\n                           self.major = major"
              "\n                           self.gpa = gpa          \n  "
              )
        continue_lesson()
        title()
        print("  Step 2 - Now lets create the inputs for the class we are going to use:"
              "\n\n                   student1 = student_object(\"Micky Mouse\", \"Fun\", 4.0)"
              "\n                   student2 = student_object(\"Donald Duck\", \"Complaining\", 3.5)"
              "\n                   student3 = student_object(\"Goofy\", \"Goofing Around\", 1.7)\n\n"
              )
        continue_lesson()
        title()
        print("  Step 3 - Next steup is to crea a function that will tells us whether or not they are on Honor Roll: "
              "\n                     First thing we have to do is to add function in our class."
              "\n                               Here is the code I used "
              "\n\n                                     def on_honor_roll(self):"
             "\n                                             if (self.gpa) >= 3.5:      )"
             "\n                                                return True"
             "\n                                            else:"
              "\n                                                return False\n\n   "
              )

        continue_lesson()
        title()
        print("     Step 4 - Now lets print the results.\n\n"
        "\n                         print(student1.on_honor_roll())"
        "\n                         print(student1.on_honor_roll())"
        "\n                         print(student1.on_honor_roll())\n"
              )

        student1 = student_object("Micky Mouse", "Fun", 4.0)
        student2 = student_object("Donald Duck", "Complaining", 3.5)
        student3 = student_object("Goofy", "Goofing around", 1.7
                                  )
        print((student1.name) + "is on honor role?  - " + str(student1.on_honor_roll()))
        print((student2.name) + "is on honor role?  - " + str(student2.on_honor_roll()))
        print((student2.name) + "is on honor role?  - " + str(student3.on_honor_roll()))



        a = input("\n\nWould you like to redu the lesson (Y) or press <Enter for Main Menu>?  ")
        if a == "y":
            lesson_29()
        if a == "y":
            lesson_29()
        else:
            import P_1_1_Python_Main_Menu
            P_1_1_Python_Main_Menu.main_menu_1

    definition()
