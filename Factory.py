# https://www.youtube.com/watch?v=-a1PFtooGo4&list=PL7yh-TELLS1FuqLSjl5bgiQIEH25VEmIc&index=7&ab_channel=NeuralNine

from abc import ABCMeta, abstractstaticmethod
from time import perf_counter

class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def person_method():
        """ Interface Method"""
    
class Student(IPerson):

    def __int__(self):
        self.name = "Basid student name"
    
    def person_method(self):
        print(" I am a student")


class Teacher(IPerson):

    def __int__(self):
        self.name = "Basid Teacher name"
    def person_method(self):
        print(" I am a teacher")

class PersonFactory:

    @staticmethod
    def build_person(person_type):
        if person_type == 'Student':
            return Student()
        if person_type == 'Teacher':
            return Teacher()
        print("invalid type")
        return -1

if __name__ =="__main__":
    choice = input("What type of person do you want to create?\n")
    person = PersonFactory.build_person(choice)
    person.person_method()

# s1 = Student()
# s1.person_method()

# t1 = Teacher()
# t1.person_method()
