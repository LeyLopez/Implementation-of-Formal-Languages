from ABC import SuperClass
from ClassAlphabet import Alphabet
import random
import itertools


class Languages(SuperClass): 

    def __init__(self, alphabets):
        self.language1 = []
        self.language2 = []
        self.alphabets = alphabets


    def generate_laguages_one(self):
        words_languages_one = int(input("Enter the number of words in Language A: "))

        alphabet1 = self.alphabets.alphabet1
        alphabet2 = self.alphabets.alphabet2

        self.language1 = list(itertools.product(alphabet1,alphabet2))
        
        self.language1 = random.sample(self.language1, words_languages_one)

        
    def generate_language_two(self):
        words_languages_two = int(input("Enter the number of words in Language B: "))

        alphabet1 = self.alphabets.alphabet1
        alphabet2 = self.alphabets.alphabet2

        self.language2 = list(itertools.product(alphabet1,alphabet2))

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

    def difference(self):
       Languages_difference = set(self.language1) - set(self.language2)
       formatted_language_difference = ["".join(elem) for elem in Languages_difference]
       print("The difference between Language A and Language B is: {" + ", ".join(formatted_language_difference) + "}")
                
    def intersection(self):
        Languages_intersection = set(self.language1) & set(self.language2)
        formatted_language_intersection = ["".join(elem) for elem in Languages_intersection]
        print("The intersection between Language A and Language B is: {" + ", ".join(formatted_language_intersection) + "}")


    def concatenation(self):
        Languages_concatenation = []
        for word_one in self.language1:
            for word_two in self.language2:
                word_concatenation = word_one + word_two
                Languages_concatenation.append(word_concatenation)

                formatted_concatenation = [''.join(word) for word in Languages_concatenation]

        print("The concatenation of Language A and Language B is: {" + ", ".join(formatted_concatenation) + "}")


    def exponentiation(self):
        choose_power = int(input("Enter the number of power: "))
        random_language = random.choice([self.language1, self.language2])
        Language_exponentiation = random_language * choose_power
    
        print(f"The language was chosen: {random_language} \nRaised to the power: {choose_power} \nResult: {Language_exponentiation}") 


    def reverse_language(self):
        random_language = random.choice([self.language1, self.language2])
        reversed_language = ' '.join([''.join(reversed(t)) for t in random_language])
        
        # Mostrar el lenguaje original y su versión invertida
        original_language_str = ' '.join([''.join(t) for t in random_language])
        print(f"The original language: {original_language_str}")
        print(f"The reversed language: {reversed_language}")


    def cardinality(self):
        pass


