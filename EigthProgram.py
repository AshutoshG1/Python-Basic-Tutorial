# class Student: 
#     name = "Ashutosh"

# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s1.name)

# class Car:
#     color = "blue"
#     brand = "mercedes"

# car1 = Car()
# print(car1.color)
# print(car1.brand)
# car2 = Car()

# class Student: 
#     name = "Ashutosh"
#     colloge_name = "ABC"
#     def __init__():
#         print("default constructor")
    
#     def __init__(self, fullname):
#         self.name = fullname
#         print("creating new student in database")

#     def hello(self):
#         print("hello method")

    

# s1 = Student("karan")
# print(s1.name)
# print(s1.colloge_name)
# print(Student.colloge_name)
# s1.hello()

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     def getAvg(self):
#         sum = 0
#         for val in self.marks:
#             sum +=val
#         print("hi",self.name,"your avg score is : ",sum/3)

# s1 = Student("tony",[99,98,97])
# s1.getAvg()

# class Student:
#     def __init__(self, name):
#         self.name = name
     
    

#     @staticmethod
#     def college():
#         print("static method")


# s1 = Student("Techie")
# s1.college()

# #Abstraction
# class Car:
#     def __init__(self):
#         self.accelerator = False
#         self.brk = False
#         self.clutch = False
#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("car started...")
# car1 = Car()
# car1.start()


# class Account:
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.account_no = acc
    
#     #debit method
#     def debit(self,amount):
#         self.balance -= amount
#         print("Rs. ", amount, "was debited")
#         print("total balance = ",self.getBalance())

#     #credit method
#     def credit(self,amount):
#         self.balance += amount
#         print("Rs. ", amount, "was credited")
#         print("total balance = ",self.getBalance())

#     def getBalance(self):
#         return self.balance


# acc1 = Account(10000,12345)
# print(acc1.balance)
# print(acc1.account_no)
# acc1.credit(2000)
# acc1.debit(500)

# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("Ashu")
# del s1
# print(s1)

# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass

#     def reset_pass(self):
#         print(self.__acc_pass)

# acc1 = Account("12345","abcde")
# print(acc1.acc_no)
# #print(acc1.acc_pass)
# acc1.reset_pass()

# class Person:
#     __name = "ashu"

#     def __hello(self):
#         print("hello method")
    
#     def welcome(self):
#         self.__hello()

# p1 = Person()
# #print(p1.__name)
# print(p1.welcome())

# #Inheritance
# class Car:
#     @staticmethod
#     def start():
#         print("car started")

#     @staticmethod
#     def stop():
#         print("car stopped")

# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name

# car1 = ToyotaCar("fortuner")
# car2 = ToyotaCar("prius")

# print(car1.name)
# print(car1.start())


# #Multi-level Inheritance 
# class Car:
#     @staticmethod
#     def start():
#         print("car started")

#     @staticmethod
#     def stop():
#         print("car stopped")

# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name

# class Fortuner(ToyotaCar):
#     def __init__(self, type):
#         self.type = type
    

# car1 = Fortuner("diesel")
# car1.start()

# #Multiple Inheritance 
# class A:
#     varA = "welcome to class A"
# class B:
#     varB = "welcome to class B"

# class C(A, B):
#     varC = "welcome to class C"

# c1 = C()
# print(c1.varA)
# print(c1.varB)
# print(c1.varC)

#super keyword
# class Car:
#     def __init__(self, type):
#         self.type = type
#     @staticmethod
#     def start():
#         print("car started")

#     @staticmethod
#     def stop():
#         print("car stopped")

# class ToyotaCar(Car):
#     def __init__(self, name, type):
#         super().__init__(type)
#         self.name = name
        

# car1 = ToyotaCar("prius","electric")
# print(car1.type)

#class method 

# class Person:
#     name = "anonymous"

#     def changeName(self, name):
#         self.name = name

# p1 = Person()
# p1.changeName("rahul kumar")
# print(p1.name)
# print(Person.name)

# class Person:
#     name = "anonymous"

#     # def changeName(self, name):
#     #     self.__class__.name = "Rahul"

#     @classmethod
#     def changeName(cls, name):
#         cls.name = name


# p1 = Person()
# p1.changeName("rahul kumar")
# print(p1.name)
# print(Person.name)

# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#         #self.percentage = str((self.phy+self.chem+self.math)/3)+"%"

#     # def calcPercentage(self):
#     #     self.percentage = str((self.phy+self.chem+self.math)/3)+"%"
#     @property
#     def percentage(self):
#         return str((self.phy+self.chem+self.math)/3)+"%"     

# stu1 = Student(98,99,97)
# print(stu1.percentage)
# stu1.phy = 90
# print(stu1.percentage)


#Polymorphism 
# print(1+2)
# print("Techie"+"Ashutosh")
# print([1,2,3]+[4,5,6])

# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img
#     def showNumber(self):
#         print(self.real,"i +",self.img,"j")
    
#     def __add__(self, num2): #dunder function
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal, newImg)
# num1 = Complex(1,3)
# num1.showNumber()

# num2 = Complex(2,4)
# num2.showNumber()

# #num3 = num1.add(num2)
# num3 = num1 + num2
# num3.showNumber()