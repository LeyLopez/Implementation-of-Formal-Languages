from ABC import SuperClass
from ClassAlphabet import Alphabet
import random
import itertools


class Languages(SuperClass): 

    def __init__(self, alphabets):
        self.language1 = set()
        self.language2 = set()
        self.alphabets = alphabets


    def enter_laguages_one(self):
        words_languages_one = int(input("Enter the number of words in Language A: "))
        return words_languages_one
        
    def generate_language_one(self):
        alphabet1 = self.alphabets.alphabet1
        alphabet2 = self.alphabets.alphabet2

        self.language1 = list(itertools.product(alphabet1,alphabet2))
        language_one_list=list(self.language1)
        
        self.language1 = set(random.sample(language_one_list, self.enter_laguages_one()))

        
    def enter_language_two(self):
        words_languages_two = int(input("Enter the number of words in Language B: "))
        return words_languages_two

    def generate_language_two(self):
        alphabet1 = self.alphabets.alphabet1
        alphabet2 = self.alphabets.alphabet2

        self.language2 = set(itertools.product(alphabet1,alphabet2))
        language_two_list= list(self.language2)

        self.language2 = set(random.sample(language_two_list, self.enter_language_two()))


    def show_languages(self):
        
        formatted_language1= [f"{elem[0]}{elem[1]}" for elem in self.language1]
        formatted_language2= [f"{elem[0]}{elem[1]}" for elem in self.language2]

        print("Language A: {" + ", ".join(formatted_language1) + "}")
        print("Language B: {" + ", ".join(formatted_language2) + "}")



    def union(self):
        Languages_union = self.language1.union(self.language2)
        return Languages_union

    def show_union(self):
        language_union_list =list(self.union())
        formatted_language_union=[f"{elem[0]}{elem[1]}"for elem in language_union_list]
        print("The Languages union (A∪B) is: {" + ", ".join(formatted_language_union) + "}")

    def difference_one(self):
       Languages_difference1 = list(self.language1.difference(self.language2))
       return Languages_difference1

    def difference_two(self):
        Languages_difference2 = list(self.language2.difference(self.language1))
        return Languages_difference2

    def show_difference(self):
        language_difference1_list = self.difference_one()
        language_difference2_list = self.difference_two()
        formatted_language_difference1 = [f"{elem[0]}{elem[1]}"for elem in language_difference1_list]
        formatted_language_difference2 = [f"{elem[0]}{elem[1]}"for elem in language_difference2_list]
        print("The first alphabets difference (A-B) is: {" + ", ".join(formatted_language_difference1) + "}  and the second alphabets difference(B-A) is: {" + ", ".join(formatted_language_difference2 ) + "}")
                
    def intersection(self):
        Languages_intersection = self.language1.intersection(self.language2)
        return Languages_intersection
    
    def show_intersection(self):
        language_intersection_list = list(self.intersection())
        formatted_language_intersection = [f"{elem[0]}{elem[1]}"for elem in language_intersection_list]
        print("The intersection between Language A and Language B is: {" + ", ".join(formatted_language_intersection) + "}")


    def concatenation(self):
        Languages_concatenation = []
        for word_one in self.language1:
            for word_two in self.language2:
                word_concatenation = word_one + word_two
                Languages_concatenation.append(word_concatenation)

                formatted_concatenation = [''.join(word) for word in Languages_concatenation]

        print("The concatenation of Language A and Language B is: {" + ", ".join(formatted_concatenation) + "}")


    def power_language(self):
        choose_power = int(input("Enter the number of power: "))
        random_language = random.choice([self.language1, self.language2])

        language_exponentiation = ""
        for i in range(choose_power):
            language_exponentiation += str(random_language)
        print(f"The language was chosen: {random_language} \nRaised to the power: {choose_power} \nResult: {language_exponentiation}")
        
    def reverse_language_one(self):
        language_one = list(self.language1)
        language_one.reverse()
        print("The reverse of language one is: ", language_one)

    def reverse_language_two(self):
        language_two = list(self.language2)
        language_two.reverse()
        print("The reverse of language two is: ", language_two)

    def choise_language_cardinality(self):
        random_language = random.choice([self.language1,self.language2])
        return random_language
    
    def cardinality(self):
        Language_cardinality = len(self.choise_language_cardinality())
        return Language_cardinality
    
    def show_cardinality(self):
        random_language = self.choise_language_cardinality()
        formatted_random_language = [f"{elem[0]}{elem[1]}"for elem in random_language]
        print("Language choose for the cardinality: {" + ", ".join(formatted_random_language) + "}")
        print(f"The cardinality of the randomly chosen language is: {self.cardinality()}")


