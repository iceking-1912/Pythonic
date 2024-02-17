# tuple
# coordinator = [5, 7]
# coordinator[0] = 13
# print(coordinator[0])

# functions
# def print_coordinates(x):
#     x = int(x)
#     coordinator = (12, 17, 223)
#     print(coordinator[x])
#
#
# x = input("x(0)or y(1) or z(2) ")
#
# print_coordinates(x)

#
# def greetings(name, age):
#     print("Hey " + name + " you are " + age + " years old.")
#
# greetings("Steven Maverick ","39")


# def greetings(name, yob):
#     yob = int(yob)
#     age = 2023 - yob
#     print("Hey " + name + " you are " + str(age) + " years old.")
#
#
# greetings("Steven Maverick ", "1979")


# better calculator
#
# num1 = float(input("Enter first Number: "))
# op = input("Enter the Operation: ")
# num2 = float(input("Enter Second Number: "))
#
# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "*":
#     print(num1 * num2)
# elif op == "/":
#     print(num1/num2)
# else:
#     print("Invalid Operation")
#


# # Dictionary
# month_converter = {
#     "jan": "January",
#     "feb": "February",
#     "mar": "March",
#     "apr": "April",
#     "may": "May",
#     "jun": "June",
#     "jul": "July",
#     "aug": "August",
#     "sep": "September",
#     "oct": "October",
#     "nov": "November",
#     "dec": "December"
# }
# month = input("Enter the KeyWord ")
#
# print(month_converter.get(month, "Not a Valid Key"))

# while i am doing that
# i = 1
# while i <= 20:
#     print("Hi Himanshu")
#     i += 1
# print("Done")

# Guess my Game

# import random
# import openai
#
# openai.api_key = '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'
# secret_word = "denji"
# guess = ""
#
# while guess != secret_word:
#     guess = input("Enter Guess = ")
#     clue_dict = ["it starts with a 'd'. ", "it ends with an 'i'. ", "it is a character from Chainsaw man"]
#     rand_int = random.randint(0, 2)
#
#     if guess != secret_word:
#         print("incorrect")
#         print(clue_dict[rand_int])
#
# print("Correct")
#
# x = 1
# while x <= 10:
#     print("meow")
#     x += 1


# class pen(__name__):
#     def __init__(self, name):
#         self.__name__ = name
#
#     def doesitwrite(self, ink):
#         print(self.__name__)
#         if (ink > 0) and (ink > 5):
#             print("Ink- " + str(ink) + "ml")
#             print("Writing")
#         else:
#             # ink += "ml"
#             print("Ink- " + str(ink) + "ml")
#             print("Not Writing")
#
#
# fountain = pen("fountain")
#
# refil = 4
#
# fountain.doesitwrite("fountain", refil)

# ball = pen()

# ball.doesitwrite(refil)


# class animal:
# def walk(self):
#     print("walking")

# class dog(animal):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def bark(self):
#         print("woof!!")

# husky = dog("husky",10)

# print(husky.name)
# print(husky.age)
# husky.bark()
# husky.walk()
