# http://megarobot.club/задачи-2-неделя-ооп-python/
# Задача 2. Написать программу, в которой есть главный класс Games со статическим полем Year,
# опишите конструктор присваивающий значение полю Year, также опишите метод getName, который возвращает имя игры.
# На основе главного класса путем наследования опишите четыре класса PCGames, PS4Games, XboxGames, MobileGames.
# Добавьте каждому классу дополнительные поля и переопределите у всех классов метод getName.

class Games:
    year = "Default year"

    def __init__(self, year, name):
        self.year = year
        self.name = name

    def get_name(self, name):
        return self.name


class PCGames(Games):
    def __init__(self, year, name, download_location):
        super().__init__(year, name)
        self.download_location = download_location

    def get_name(self, name):
        self.name = 'PCGames'
        return self.name


class PS4Games(Games):
    def __init__(self, year, name, type_of_games):
        super().__init__(year, name)
        self.type_of_games = type_of_games

    def get_name(self, name):
        self.name = 'PS4Games'
        return self.name


class XboxGames(Games):
    def __init__(self, year, name, type_of_games):
        super().__init__(year, name)
        self.type_of_games = type_of_games

    def get_name(self, name):
        self.name = 'XboxGames'
        return self.name


class MobileGames(Games):
    def __init__(self, year, name, shop):
        super().__init__(year, name)
        self.shop = shop

    def get_name(self, name):
        self.name = 'MobileGames'
        return self.name


# Задача 3. Напишите программу с пустым классом Country.
# Опишите наследуемые от класса Country классы Russia, Canada, Germany.
# Добавьте каждому классу поле population и опишите метод setPopulation и getPopulation.

class Country:
    def __init__(self, population):
        self.population = population

    def set_population(self, population):
        self.population = population

    def get_population(self):
        return self.population


class Russia(Country):
    def __init__(self, area, population):
        super().__init__(population)
        self.area = area


class Canada(Country):
    def __init__(self, capital, population):
        super().__init__(population)
        self.capital = capital


class Germany(Country):
    def __init__(self, gdp, population):
        super().__init__(population)
        self.gdp = gdp


g = Germany(4200, 84318653)
print(g.get_population())
g.set_population(84320000)
print(g.get_population())


# Задача 4. Напишите программу в которой есть главный класс с текстовым полем.
# В главное классе должен быть метод для присваивания значения полю: без аргументов и с одним текстовым аргументом.
# Объект главного класса создаётся передачей одного текстового аргумента конструктору.
# На основе главного класса создается класса потомок. В классе-потомке нужно добавить числовое поле.
# У конструктора класса-потомка два аргумента.


class Home:
    type_of_foundation = "Plate"

    def __init__(self, roof_material):
        self.roof_material = roof_material

    def set_type_of_foundation(self, type_of_foundation):
        self.type_of_foundation = type_of_foundation

    @staticmethod
    def start():
        print("Стройка идет")


class Private(Home):
    def __init__(self, roof_material, number_of_rooms, type_of_heating):
        super().__init__(roof_material)
        self.number_of_rooms = number_of_rooms
        self.type_of_heating = type_of_heating


# http://megarobot.club/задачи-3-неделя-ооп-python/
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
