# https://chel-center.ru/python-yfc/2020/03/11/obektno-orientirovannoe-programmirovanie-v-python-3/
# Используя тот же класс Dog, создайте три новые собаки, каждая из которых имеет свой возраст. Затем напишите функцию с
# именем get_biggest_number(), которая принимает любое количество возрастов (*args) и возвращает самый старый из них.
# Затем выведите возраст самой старой собаки примерно так: The oldest dog is 7 years old.

# Создайте класс Pets, который содержит экземпляры собак; этот класс полностью отделен от класса Dog. Другими словами,
# класс Dog не наследуется от класса Pets. Затем назначьте три экземпляра собаки экземпляру класса Pets.

# Используя тот же файл, добавьте атрибут экземпляра is_hungry = True в класс Dog. Затем добавьте метод с именем eat(),
# который при вызове изменяет значение is_hungry на False. Выясните, как лучше кормить каждую собаку, а затем выведите
# «Мои собаки голодны». если все голодны или «Мои собаки не голодны». если все не голодны.

# Затем добавьте метод walk() к классам Pets и Dog, чтобы при вызове метода для Pets, каждый экземпляр собаки,
# назначенный классу Pets, будет walk().

class Dog:
    species = "mammal"
    is_hungry = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_biggest_number(*args):  # принимает любое количество возрастов
        return max(args)

    # Метод класса
    def description(self):
        return "{} is {}.".format(self.name, self.age)

    # Метод класса
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

    def eat(self):
        self.is_hungry = False

    def walk(self):
        print("{} is walking!".format(self.name))


# Дочерний класс (наследник класса Dog)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# Дочерний класс (наследник класса Dog)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


class Pets:
    all_pets = []

    def __init__(self, *args):
        for arg in args:
            self.all_pets.append(arg)

    def num(self):
        return len(self.all_pets)

    def is_mammals(self):
        for pet in self.all_pets:
            if pet.species != "mammal":
                return "Not all animals are mammals."
        return "And they're all mammals, of course."

    def walk(self):
        for pet in self.all_pets:
            pet.walk()


if __name__ == "__main__":
    Rex = Dog("Rex", 2)
    Max = Dog("Max", 1.5)
    Jake = Dog("Jake", 2.5)
    print(f"The oldest dog is {Dog.get_biggest_number(Rex.age, Max.age, Jake.age)} years old.")

    pets = Pets(Rex, Max, Jake)
    print(f"I have {pets.num()} dogs.")

    print(Rex.description())
    print(Max.description())
    print(Jake.description())

    print(pets.is_mammals())

    for dog in pets.all_pets:
        dog.eat()

    if all(dog.is_hungry is False for dog in pets.all_pets):
        print("My dogs are not hungry.")
    else:
        print("My dogs are hungry.")

    pets.walk()
