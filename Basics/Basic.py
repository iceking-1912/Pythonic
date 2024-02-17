
class pen(__name__):
    def __init__(self,name):
        self.__name__ = name

    def doesitwrite(self,ink):
        print(self.__name__)
        if (ink > 0) and (ink >5):
            print("Ink- "+str(ink)+"ml")
            print("Writing")
        else :
            # ink += "ml"
            print("Ink- "+str(ink)+"ml")
            print("Not Writing")

fountain = pen("fountain")

refil = 4

fountain.doesitwrite("fountain",refil)


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

