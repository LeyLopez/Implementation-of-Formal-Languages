from ABC import SuperClass
class Alphabet(SuperClass):

  def __init__(self):
    self.alphabet1=set()
    self.alphabet2=set()

  def enter_alphabets(self):
    alphabet_one=input("Enter A: ")
    alphabet_two= input("B: ")

    self.alphabet1 = set(alphabet_one.split(', '))
    self.alphabet2 = set(alphabet_two.split(', '))

  def show(self):
    print(f"A: {{{', '.join(self.alphabet1)}}} B: {{{', '.join(self.alphabet2)}}}")   

  def union(self):
    pass

  def interception(self):
    pass
  
  def difference(self):
    pass    
    
my_alphabet = Alphabet()
my_alphabet.enter_alphabets()
my_alphabet.show()

