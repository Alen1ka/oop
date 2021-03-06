# https://smartiqa.ru/courses/python/lesson-6
class Human:
    default_name = 'Alice'
    default_age = 30

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = ''

    def info(self):
        print(f'{self.name}\n{self.age}\n{self.__money}\n{self.__house}')

    @staticmethod
    def default_info():
        print(Human.default_name)
        print(Human.default_age)

    def __make_deal(self, price_house, object_house):
        self.__money -= price_house
        self.__home_object = object_house

    def earn_money(self, earn):
        self.__money += earn

    def buy_house(self, object_house, discount=0):
        price = object_house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(price, object_house)
            print("Сделка совершена.")
        else:
            print("Денег слишком мало для покупки дома.")


class House:
    def __init__(self, _area, _price):
        self._area = _area
        self._price = _price

    def final_price(self, discount):
        final_price = self._price * (100 - discount) / 100
        return final_price


class SmallHouse(House):
    def __init__(self, _price):
        _area = 40
        super().__init__(_area, _price)


if __name__ == '__main__':
    Human.default_info()

    people = Human('Alena', 30)

    people.info()

    dacha = SmallHouse(100000)

    people.buy_house(dacha)

    people.earn_money(95000)

    people.buy_house(dacha, 5)
