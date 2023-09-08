class student:

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

class Car:

    def __init__(self, Make, Model, Year, Would_you_buy):
        self.Make = Make
        self.Model = Model
        self.Year = Year
        self.Would_you_buy = Would_you_buy

    def getModel(self):
        return self.Model

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


class Pyton_Trivia_Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

class student_object:

    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def on_honor_roll(self):
        if (self.gpa) >= 3.5:
            return True
        else:
            return False

class chef_class1:
    def make_chicken(self):
        print("The chef makes a chicken")
    def make_salad(self):
        print("The chef makes the salad")
    def make_special_dish(self):
        print("The chef makes a BBQ ribs")

class chef_class2(chef_class1):
    def make_pizza(self):
        print("The chef makes pizza")
    def make_special_dish(self):
        print("The chef makes hamburger")