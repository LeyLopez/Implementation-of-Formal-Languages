from ClassAlphabet import Alphabet
from ABC import SuperClass
from ClassLanguages import Languages

def main():
    my_alphabet=Alphabet()
    my_languages=Languages(my_alphabet)
    my_alphabet.enter_alphabets()
    my_alphabet.show()
    my_alphabet.union()
    my_alphabet.interception()
    my_alphabet.star_closure()

    my_languages.enter_laguages()
    my_languages.generate_languages()



main()
