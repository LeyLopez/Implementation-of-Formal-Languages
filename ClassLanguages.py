from ABC import SuperClass
from ClassAlphabet import Alphabet

class Languages(SuperClass): 

    def __init__(self):
        self.language1 = set()
        self.language2 = set()
        self.alphabet = Alphabet

    def enter_num_words(self):
        num_words_one = int(input("Enter the number of words in Language A: "))
        num_words_two = int(input("Enter the number of words in Language B: "))
        

    def union(self):
        pass

    def interception(self):
        pass

    def difference(self):
        pass


my_language = Languages()
my_language.enter_num_words()  
