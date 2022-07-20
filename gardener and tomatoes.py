import textwrap


class Tomato:
    states = {0: "Отсутствует", 1: "Цветение", 2: "Зеленый", 3: "Красный"}

    def __init__(self, index):
        self._index = index
        self._states = Tomato.states[0]

    def grow(self):
        for i, stage in self.states.items():
            if self._states == stage:
                self._states = Tomato.states[i + 1]
                return self._states

    def is_ripe(self):
        if self._states == "Красный":
            print("Томат созрел")


class TomatoBush:
    def __init__(self, num):
        self.num = num
        self.tomatoes = []
        for i in num:
            self.tomatoes.append(Tomato(i))

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        if (tomato != "Красный" for tomato in self.tomatoes):
            return False
        return True

    def give_away_all(self):
        if self.all_are_ripe():
            self.tomatoes = []


class Gardener:
    def __init__(self, name):
        self.name = name
        self._plant = Tomato(1)

    def work(self):
        self._plant.grow()

    def harvest(self):
        tomatobush1 = TomatoBush(1)
        if tomatobush1.all_are_ripe():
            self.tomatoes = []
        else:
            print("Не все плоды созрели.")

    @staticmethod
    def knowledge_base():
        print(textwrap.dedent('''
            Выращивание рассады томатов.\tТомат — культура светолюбивая и теплолюбивая, требовательная к условиям 
            произрастания. Чем ярче, интенсивнее свет, тем быстрее формируется урожай. Затяжная пасмурная погода 
            удлиняет период созревания плодов на 10-15 дней, ухудшает их вкус.\tОптимальная температура для роста и 
            развития растений: 22-24 °С днем, 16-18 °С ночью. При температуре ниже 10 °С приостанавливается рост 
            растений, пыльца не созревает, завязи опадают.\tВ нашем климате урожай томата можно получить, только 
            если высаживать рассаду в весенние теплицы или открытый грунт в возрасте 40-65 суток. Если теплица 
            отапливается, то высокорослые поздние сорта томатов высевают на рассаду в середине февраля, 
            а скороспелые низкорослые, часть из которых будет высажена в открытый грунт, — в первой декаде марта.'''))


if __name__ == '__main__':
    ivan = Gardener("Ivan")
    ivan.knowledge_base()
    ivan.work()
    ivan.harvest()
    while ivan.tomatoes != []:
        ivan.work()
    ivan.harvest()
