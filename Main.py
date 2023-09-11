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

    my_languages.generate_laguages_one()
    my_languages.generate_language_two()
    my_languages.show_languages()
    my_languages.union()
    my_languages.difference()



main()
