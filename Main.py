from ClassAlphabet import Alphabet
from ABC import SuperClass
from ClassLanguages import Languages

def main():
    my_alphabet=Alphabet()
    my_languages=Languages(my_alphabet)
    my_alphabet.generate_alphabets()
    my_alphabet.show()
    my_alphabet.show_union()
    my_alphabet.show_intersection()
    my_alphabet.show_difference()
    my_alphabet.show_star_closure()

    my_languages.generate_language_one()
    my_languages.generate_language_two()
    my_languages.show_languages()
    my_languages.show_union()
    my_languages.show_difference()
    my_languages.show_intersection()
    my_languages.concatenation()
    my_languages.show_cardinality()
    my_languages.reverse_language()
    my_languages.power_language()
    
    

main()
