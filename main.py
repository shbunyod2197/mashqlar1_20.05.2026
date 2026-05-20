# 1
class Student:
    def __init__(self, fullname, grade):
        self.fullname = fullname
        self.__grade = grade

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, nw):
        self.__grade = nw

s1 = Student("bunyod", 99.999)
print(s1.grade)

s = s1.grade
print(s)

s1.grade = 99.9999999
print(s1.grade)

# 2
class Car:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, nw_price):
        self.__price = nw_price

c = Car('Toyota', 20000)
print(c.price)

s = c.price
print(s)

c.price = 999
print(c.price)

# 3
class Phone:
    def __init__(self, model, battareya):
        self.model = model
        self.__battareya = battareya

    @property
    def battareya(self):
        return self.__battareya

    @battareya.setter
    def battareya(self, nw_battareya):
        self.__battareya = nw_battareya

k = Phone('Iphone', 45)
s = k.battareya
print(s)

k.batareya = 91929394959
print(k.batareya)

# 4
class Teacher:
    def __init__(self, fullname, salary):
        self.fullname = fullname
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, nw_salary):
        self.__salary = nw_salary

t1 = Teacher('Karimov Aziz', 500)
print(t1.fullname)

s = t1.salary
print(s)

t1.salary = 7777
print(t1.salary)


# 5
class Loptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.__ram = ram

    @property
    def ram(self):
        return self.__ram

    @ram.setter
    def ram(self, ram):
        self.__ram = ram

l1 = Loptop('HP', 8)
print(l1.brand)

s = l1.ram
print(s)

l1.ram = 9888
print(l1.ram)

# 6
class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, nw_password):
        self.__password = nw_password

u1 = User('admin', 12345)
print(u1.password)

s = u1.password
print(s)

u1.password = 54321
print(u1.password)

# 7
class Universitet:
    def __init__(self, name, student_count):
        self.name = name
        self.__student_count = student_count


    @property
    def student_count(self):
        return self.__student_count

    @student_count.setter
    def student_count(self, nw_student_count):
        self.__students = nw_student_count

u1 = Universitet('TATU', 12000)
print(u1)


s = u1.student_count
print(s)

u1.student_count = 99.9999999
print(u1.student_count)

# 8
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

a1 = Animal('Sher', 5)
print(a1.age)

s = a1.age
print(s)

a1.age = 8761234876
print(a1.age)

# 9
class Game:
    def __init__(self, title, level):
        self.title = title
        self.__level = level\

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, level):

g1 = Game('Minecraft', 10)
print(g1.level)

g1.level = 10
print(g1.level)

# 10
class Hospital:
    def __init__(self, name, rooms):
        self.name = name
        self.__rooms = rooms

    @property
    def rooms(self):
        return self.__rooms

    @rooms.setter
    def rooms(self, rooms):
        self.__rooms = rooms

h1 = Hospital('Shifo', 50)
print(h1.rooms)

h1.rooms = 100
print(h1.rooms)

# 11
class Market:
    def __init__(self, name, income):
        self.name = name
        self.__income = income

    @property
    def income(self):
        return self.__income

    @income.setter
    def income(self, value):
        self.__income = value

m1 = Market('Korzinka', 100000)
print(m1)

m1.income = 100
print(m1)

# 12
class Employee:
    def __init__(self, fullname, experience):
        self.fullname = fullname
        self.__experience = experience

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, value):
        self.__experience = value

e1 = Employee('Rustam Aliyev', 3)
print(e1.fullname)

e1.experience = 5
print(e1.fullname)

# 13
class School:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

s1 = School('45-maktab', 800)
print(s1.age)

s1.age = 200
print(s1.age)

# 14
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.__pages = pages

    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, value):
        self.__pages = value

b1 = Book('Python asoslari', 250)
print(b1.pages)

b1.pages = 10
print(b1.pages)

# 15
class Book:
    def __init__(self, company_name,workers):
        self.company_name = company_name
        self.__workers = workers

    @property
    def workers(self):
        return self.__pages

    @workers.setter
    def workers(self, value):
        self.__pages = value

b1 = Book('Python asoslari', 250)
print(b1.workers)

b1.workers = 10
print(b1.workers)
