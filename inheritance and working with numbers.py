# Задача 2. Необходимо написать программу в которой описать один базовый класс в нем описать конструктор,
# и класс потомок. Описать в классе потомке конструктор с параметрами по умолчанию.
# Затем нужно описать класс для которого класс потомок является базовым классом и в нем переопределить конструктор.
# В каждом классе описать по два поля и методы — show, get, set для каждого поля.

class Furniture:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def show_name(self):
        print(f"Название {self.name}")

    def show_amount(self):
        print(f"Количество {self.amount}")

    def get_name(self):
        return self.name

    def get_amount(self):
        return self.amount

    def set_name(self, name):
        self.name = name

    def set_amount(self, amount):
        self.amount = amount


class Chairs(Furniture):
    def __init__(self, name, amount, back_material='grid', seat_material='cloth'):
        super().__init__(name, amount)
        self.back_material = back_material
        self.seat_material = seat_material

    def show_back_material(self):
        print(self.back_material)

    def get_back_material(self):
        return self.back_material

    def set_back_material(self, back_material):
        self.back_material = back_material

    def show_seat_material(self):
        print(self.seat_material)

    def get_seat_material(self):
        return self.seat_material

    def set_seat_material(self, seat_material):
        self.seat_material = seat_material


class OfficeChair(Chairs):
    def __init__(self, roller_material, weight_restrictions, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.roller_material = roller_material
        self.weight_restrictions = weight_restrictions

    def show_name(self):
        print(f"Название {self.roller_material}")

    def show_amount(self):
        print(f"Количество {self.weight_restrictions}")

    def get_name(self):
        return self.roller_material

    def get_amount(self):
        return self.weight_restrictions

    def set_name(self, roller_material):
        self.roller_material = roller_material

    def set_amount(self, weight_restrictions):
        self.weight_restrictions = weight_restrictions


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
