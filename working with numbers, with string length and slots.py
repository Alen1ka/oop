# https://smartiqa.ru/python-workbook/class#5
# Задача 2. Базовый уровень.
# Николаю требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник.
# Для этого он решил создать класс TriangleChecker, принимающий только положительные числа.
# С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):
# – Ура, можно построить треугольник!;
# – С отрицательными числами ничего не выйдет!;
# – Нужно вводить только числа!;
# – Жаль, но из этого треугольник не сделать.

class TriangleChecker:
    def __init__(self, length):
        self.length = length

    def is_triangle(self):
        for i in range(len(self.length)):
            if not str(self.length[i]).isdigit():
                if str(self.length[i])[:1] == '-':
                    return '– С отрицательными числами ничего не выйдет!;'
                else:
                    return '– Нужно вводить только числа!;'

            elif int(self.length[i]) < 0:
                return '– С отрицательными числами ничего не выйдет!;'

        if self.length[0] + self.length[1] <= self.length[2] or self.length[0] + self.length[2] <= self.length[1] or \
                self.length[1] + self.length[2] <= self.length[0]:
            return '– Жаль, но из этого треугольник не сделать.'

        elif int(self.length[0]) > 0 and int(self.length[1]) > 0 and int(self.length[2]) > 0:
            return '– Ура, можно построить треугольник!;'


segment1 = TriangleChecker([3, -2, 5])
print(segment1.is_triangle())
segment2 = TriangleChecker([3, 2, 5])
print(segment2.is_triangle())
segment3 = TriangleChecker([3, 'Два', 5])
print(segment3.is_triangle())
segment1 = TriangleChecker([2, 3, 4])
print(segment1.is_triangle())


# Задача 3. Базовый уровень.
# Евгения создала класс KgToPounds с параметром kg, куда передается определенное количество килограмм,
# а с помощью метода to_pounds() они переводятся в фунты.
# Чтобы закрыть доступ к переменной “kg” она реализовала методы set_kg() - для задания нового значения килограммов,
# get_kg()  - для вывода текущего значения кг. Из-за этого возникло неудобство:
# нам нужно теперь использовать эти 2 метода для задания и вывода значений.
# Помогите ей переделать класс с использованием функции property() и свойств-декораторов. Код приведен ниже.

# Вариант 1 со свойством декоратора
class KgToPounds:
    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.205

    @property
    def working_with_kg(self):
        return self.__kg

    @working_with_kg.setter
    def working_with_kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError('Килограммы задаются только числами')


kg1 = KgToPounds(1)
print(kg1.working_with_kg)
kg1.working_with_kg = 5
print(kg1.working_with_kg)


# kg1.working_with_kg = 'two'
# print(kg1.working_with_kg) # выдает ValueError: Килограммы задаются только числами


# Вариант 2 с функцией property()
class Kg:
    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.205

    def set_kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError('Килограммы задаются только числами')

    def get_kg(self):
        return self.__kg

    property(to_pounds, set_kg, get_kg)


kg3 = Kg(1)
print(kg3.get_kg())
kg3.set_kg(5)
print(kg3.get_kg())


# kg3.set_kg('two')
# print(kg3.get_kg()) # выдает ValueError: Килограммы задаются только числами

# Задача 4. Базовый уровень.
# Николай – оригинальный человек.
# Он решил создать класс Nikola, принимающий при инициализации 2 параметра: имя и возраст. Но на этом он не успокоился.
# Не важно, какое имя передаст пользователь при создании экземпляра, оно всегда будет содержать “Николая”.
# В частности - если пользователя на самом деле зовут Николаем, то с именем ничего не произойдет, а если его зовут,
# например, Максим, то оно преобразуется в “Я не Максим, а Николай”.
# Более того, никаких других атрибутов и методов у экземпляра не может быть добавлено, даже если кто-то и вздумает
# так поступить (т.е. если некий пользователь решит прибавить к экземпляру свойство «отчество» или метод «приветствие»,
# то ничего у такого хитреца не получится).

class Nikola:
    __slots__ = ['name', 'age']  # не позволяют создать surname вне конструктора класса

    def __init__(self, name, age):
        if name == "Николай":
            self.name = name
        else:
            self.name = f"Я не {name}, а Николай"
        self.age = age


name1 = Nikola('Алёна', 23)
print(name1.name)

# name1.surname = "Иванов"
# print(name1.surname)
