from ClassAlphabet import Alphabet
from ABC import SuperClass
from ClassLanguages import Languages

def main():
    my_alphabet=Alphabet()
    my_alphabet.enter_alphabets()
    my_alphabet.show()
    my_alphabet.union()
    my_language = Languages()
    my_language.enter_num_words()  
    my_language.union()


main()
