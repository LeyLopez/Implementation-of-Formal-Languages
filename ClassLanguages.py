from ABC import SuperClass
import random
from ClassAlphabet import Alphabet

class Languages(SuperClass):

    def __init__(self, alphabet1, alphabet2):
        self.alphabet1 = alphabet1
        self.alphabet2 = alphabet2
        self.words1 = []
        self.words2 = []

    def enter_num_words(self):
        num_words_one = int(input("Enter the number of words in Language A:"))
        num_words_two = int(input("Enter the number of words in Language B:"))

        for _ in range(num_words_one):
            word = " "
            for _ in range(random.randint(1, len(alphabet_handler.alphabet1))):
                word += random.choice(alphabet_handler.alphabet1)
            self.words1.append(word)

        for _ in range(num_words_two):
            word = " "
            for _ in range(random.randint(1, len(alphabet_handler.alphabet2))):
                word += random.choice(alphabet_handler.alphabet2)
            self.words2.append(word)
            
        return self.words1, self.words2

    def union(self):
        return self.words1 | self.words2

    def interception(self):
        return self.words1 & self.words2

    def difference(self):
        return self.words1 - self.words2


if __name__ == "__main__":
    alphabet_handler = Alphabet()
    alphabet_handler.enter_alphabets()

    my_Languages = Languages(alphabet_handler.alphabet1, alphabet_handler.alphabet2)
    words1, words2 = my_Languages.enter_num_words()

    print("\nGenerated words for Language A:")
    for word in words1:
        print(word)

    print("\nGenerated words for Language B:")
    for word in words2:
        print(word)

    my_Languages = Languages(alphabet1, alphabet2)
    my_Languages.enter_num_words()
