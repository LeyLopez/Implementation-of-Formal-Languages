from ABC import SuperClass
from ClassAlphabet import Alphabet
import random
import itertools


class Languages(SuperClass): 

    def __init__(self, alphabets):
        self.language1 = []
        self.language2 = []
        self.alphabets = alphabets


    def generate_laguages(self):
        words_languages_one = int(input("Enter the number of words in Language A: "))
        words_languages_two = int(input("Enter the number of words in Language B: "))

        alphabet1 = self.alphabets.alphabet1
        alphabet2 = self.alphabets.alphabet2

        self.language1 = list(itertools.product(alphabet1,alphabet2))
        self.language2 = list(itertools.product(alphabet1,alphabet2))

        self.language1 = random.sample(self.language1, words_languages_one)
        self.language2 = random.sample(self.language2, words_languages_two)


    def show_languages(self):
        
        formatted_language1= [f"{elem[0]}{elem[1]}" for elem in self.language1]
        formatted_language2= [f"{elem[0]}{elem[1]}" for elem in self.language2]

        print("Language A: {" + ", ".join(formatted_language1) + "}")
        print("Language B: {" + ", ".join(formatted_language2) + "}")
    

    def union(self):
        Languages_union = self.language1 + self.language2
        formatted_language_union=[f"{elem[0]}{elem[1]}"for elem in Languages_union]
        print("The Languages union (A∪B) is: {" + ", ".join(formatted_language_union) + "}")

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


