class Human:
    default_name = 'Alice'
    default_age = 30

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = ''

    def info(self):
        print(f'{self.name}\n{self.age}\n'
              f'{self.__money}\n{self.__house}')

    @staticmethod
    def default_info(default_name=default_name, default_age=default_age):
        print(default_name)
        print(default_age)

    def __make_deal(self, price_house, object_house):
        self.home_price = self.__money - price_house
        self.home_object = object_house

    def earn_money(self, earn):
        self.__money = self.__money + earn

    def __add__(self, other):
        return self + other

    def buy_house(self, price_house):
        if self.__money >= price_house:
            print("Сделка совершена")
        else:
            print(Exception("Денег слишком мало для покупки дома."))


class House:
    def __init__(self, _area, _price):
        self._area = _area
        self._price = _price

    def final_price(self, discount):
        self._price = self._price - discount

    @property
    def price(self):
        return self._price


class SmallHouse(House):
    def __init__(self, _price):
        _area = 40
        super().__init__(_area, _price)


Human.default_info()

people = Human()

Human.default_info('Alena', 30)

dacha = SmallHouse(100000)

# people.buy_house(dacha.price)

people.earn_money(500000)

people.buy_house(dacha.price)
