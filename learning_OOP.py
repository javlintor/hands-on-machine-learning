
# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade

#     def get_grade(self):
#         return self.grade

# class Course:
#     def __init__(self, name, max_students):
#         self.name = name
#         self.max_students = max_students
#         self.students = []

#     def add_student(self, student):
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             return True
#         return False
    
#     def get_average_grade(self):
#         value = 0 
#         for student in self.students:
#             value += student.get_grade()
#         return value/len(self.students)

# s1 = Student("Tim", 19, 95)
# s2 = Student("Bill", 19, 75)
# s3 = Student("Jill", 19, 65)

# course = Course("Scince", 2)
# course.add_student(s1)
# course.add_student(s2)
# print(course.get_average_grade())


# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def speak(self):
#         print("Meow")

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def speak(self):
#         print("Bark")

# class Pet:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age 

#     def show(self):
#         print("I am {} and I am {} years old".format(self.name, self.age))

#     def speak(self):
#         print("I am a pet")   
        
# class Cat(Pet):
#     def __init__(self, name, age, color):
#         super().__init__(name, age)
#         self.color = color

#     def speak(self):
#         print("Meow")

#     def show(self):
#         print("I am {} and I am {} years old and I am {}".format(self.name, self.age, self.color))

# class Dog(Pet):
#     def speak(self):
#         print("Bark")

# p = Pet("Tim", 19)
# p.speak()
# c = Cat("Bill", 34, "Brown")
# c.speak()   # derive class methods are  considered first
# d = Dog("Jill", 32)
# d.speak()



# class Person:
#     number_of_people = 0     # class attribute
#     gravity = -9.8

#     def __init__(self, name):
#         self.name = name
#         Person.add_person()
    
#     # class methods
#     @classmethod              
#     def number_of_people_(cls):
#         return cls.number_of_people 

#     @classmethod 
#     def add_person(cls):
#         cls.number_of_people += 1
    
# p1 = Person("tim")
# p2 = Person("jill")
# print(Person.number_of_people_())


# static methods
# classes that organized functions

class Math:

    @staticmethod 
    def add5(x):
        return x + 5

    @staticmethod 
    def add10(x):
        return x + 10


print(Math.add5(5)) 


