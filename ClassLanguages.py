from ABC import SuperClass
from ClassAlphabet import Alphabet
import random

class Languages:
    def __init__(self):
        self.language1 = set()
        self.language2 = set()

    def enter_num_words(self):
        num_words_one = int(input("Enter the number of words in Language A: "))
        num_words_two = int(input("Enter the number of words in Language B: "))    

        self.language1 = self.generate_language(num_words_one)
        self.language2 = self.generate_language(num_words_two)

        print("\nWords for Language A: \n")
        for word in self.language1:
            print(word)

        print("\nWords for Language B: \n")
        for word in self.language2:
            print(word)

    def generate_language(self, num_words):
        language = []
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for _ in range(num_words):
            word = "".join(random.choice(alphabet) for _ in range(random.randint(1, 10)))
            language.append(word)
        return language

    def union(self):
        Languages_union = self.language1.union(self.language2)
        print("The Languages union (A∪B) is: ", Languages_union)

    def interception(self):
        pass

    def difference(self):
        pass

    def concatenation(self):
        pass

    def exponentiation(self):
        pass

    def reverse_language(self):
        pass

    def cardinality(self):
        pass

my_language = Languages()
my_language.enter_num_words()  
