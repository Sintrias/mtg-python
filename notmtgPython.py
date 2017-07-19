import random
import sys
import os
#
# long_string = "it works 100% of the times that it worked"
#
# print(long_string[0:8])
# #last 9
# print(long_string[-9:])
# #except last 9
# print(long_string[:-9])
# #replace what comes after [26]
# print(long_string[:26]+" in where it worked all")
#
# print("%c is my letter and my number is %d my floating number is %.5f"%("y",24,2.5212152))
#
# print(long_string.capitalize())
# #returns the index of first instance of the word in starting index
# print(long_string.find("work"))
# print(long_string.isalpha())
# print(long_string.isnumeric())
# print(long_string.replace("100%","0%"))
# quote_list = long_string.split(" ")
# print(quote_list)
#wb => write binary, +ab => append binary just like in c++
# test_file= open("text.txt", "wb")
#
# print(test_file.mode)
# print(test_file.name)
#
# test_file.write(bytes("write me to the file\n", "UTF-8"))
#
# test_file.close()
#
# test_file = open("text.txt", "r+")
#
# text_in_file = test_file.read()
# print(text_in_file)
#
# os.remove("text.txt")
#

class Animal:
    __name = None
    __height = 0
    __weight = 0
    __sound = 0
    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    #"__" means class privates are private
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def get_type(selfs):
        print("Animal")
    def toString(self):
        return "{} is {} cm tall and {} kg and says {}".format(self.__name,
                                                               self.__height,
                                                               self.__weight,
                                                               self.__sound)

cat = Animal("Whiskers", 33, 10, "Meow")
print(cat.toString())

#equivalent to class Dog : Animal
class Dog(Animal):
    __owner = None
    def __init__(self):