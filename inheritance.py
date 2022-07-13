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
    def __init__(self, area,  population):
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
