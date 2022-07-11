# Задача 1. Необходимо реализовать код, показанный в примерах выше. Создать класс Rectangle и класс ToyClass.
# Для ToyClass необходимо добавить три атрибута, и метод который устанавливает их.

class Rectangle:
    pass


class ToyClass:
    def __init__(self, color, weight, price):
        self.color = color
        self.weight = weight
        self.price = price


# Задача 2. Напишите программу с классом Student, в котором есть три атрибута: name, groupNumber и age.
# По умолчанию name = Ivan, age = 18, groupNumber = 10A.
# Необходимо создать пять методов: getName, getAge, getGroupNumber, setNameAge, setGroupNumber.
# Метод getName нужен для получения данных об имени конкретного студента, метод getAge нужен для получения данных
# о возрасте конкретного студента, метод setGroupNumber нужен для получения данных о номере группы конкретного студента.
# Метод SetNameAge позволяет изменить данные атрибутов установленных по умолчанию,
# метод setGroupNumber позволяет изменить номер группы установленный по умолчанию.
# В программе необходимо создать пять экземпляров класса Student, установить им разные имена, возраст и номер группы.

class Student:
    def __init__(self, name='Ivan', age=18, group_number='10А'):
        self.name = name
        self.age = age
        self.groupNumber = group_number

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_group_number(self):
        return self.groupNumber

    def set_name_age(self, name, age):
        self.name = name
        self.age = age
        return self.age, self.name

    def set_group_number(self, group_number):
        self.groupNumber = group_number
        return self.groupNumber


student1 = Student()
student2 = Student('Ann', 21, '7А')
student3 = Student('Kate', 19, '9А')
student4 = Student('Tom', 20, '8А')
student5 = Student('Nick', 19, '10А')

student1.set_name_age('Maria', 22)
print(student1.age)  # 22


# Задача 3. Напишите программу с классом Math. Создайте два атрибута — a и b.
# Напишите методы addition — сложение, multiplication — умножение, division — деление, subtraction — вычитание.
# При передаче в методы параметров a и b с ними нужно производить соответствующие действия и печатать ответ.

class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print(self.a + self.b)

    def multiplication(self):
        print(self.a * self.b)

    def division(self):
        print(self.a / self.b)

    def subtraction(self):
        print(self.a - self.b)


example1 = Math(1, 2)
example1.addition()


# Задача 4. Напишите программу с классом Car. Создайте конструктор класса Car.
# Создайте атрибуты класса Car — color (цвет), type (тип), year (год). Напишите пять методов.
# Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен».
# Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен». Третий — присвоение автомобилю года выпуска.
# Четвертый метод — присвоение автомобилю типа. Пятый — присвоение автомобилю цвета.

class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    @staticmethod
    def starting_the_car():
        print("Автомобиль заведен")

    @staticmethod
    def turning_off_the_car():
        print("Автомобиль заглушен")

    def assignment_of_the_year(self, year):
        self.year = year

    def assignment_of_the_type(self, type):
        self.type = type

    def assignment_of_the_color(self, color):
        self.color = color
