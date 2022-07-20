import string


class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print(self.letters)

    def letters_num(self):
        print(len(self.letters))


class EngAlphabet(Alphabet):
    __letters_num = len(string.ascii_uppercase)

    def __init__(self):
        super().__init__('En', f'{string.ascii_uppercase}')

    def is_en_letter(self, letter):
        if letter in self.letters:
            return f"Буква {letter} относится к английскому алфавиту."
        return f"Буква {letter} не относится к английскому алфавиту."

    def letters_num(self):
        return self.__letters_num

    @staticmethod
    def example():
        return "MY CAT IS FUNNY"


if __name__ == '__main__':
    A = EngAlphabet()
    A.print()
    print(A.letters_num())
    print(A.is_en_letter('F'))
    print(A.is_en_letter('Щ'))
    print(A.example())
