class Dog:
    species = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_biggest_number(*args):  # принимает любое количество возрастов
        the_most_adult = args[0]
        for age in args:
            if age > the_most_adult:
                the_most_adult = age
        return the_most_adult


Rex = Dog("Rex", 2)
Max = Dog("Max", 1.5)
Jake = Dog("Jake", 2.5)
print(f"The oldest dog is {Dog.get_biggest_number(Rex.age, Max.age, Jake.age)} years old.")

