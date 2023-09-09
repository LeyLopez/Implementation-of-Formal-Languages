from ABC import SuperClass
class Alphabet(SuperClass):

  def __init__(self):
    self.alphabet1=set()
    self.alphabet2=set()

  def enter_alphabets(self):
    alphabet_one=input("Enter alphabet A: ")
    alphabet_two= input("alphabet B: ")

    self.alphabet1 = set(alphabet_one.split(','))
    self.alphabet2 = set(alphabet_two.split(','))

  def show(self):
    print(f"A: {{{', '.join(self.alphabet1)}}} B: {{{', '.join(self.alphabet2)}}}")   

  def union(self):
    alphabets_union = self.alphabet1.union(self.alphabet2)
    print("The alphabets union (A∪B)is: ", alphabets_union)

  def interception(self):
    alphabets_interception = self.alphabet1.intersection(self.alphabet2)
    print(f"The alphabets interception (A∩B) is : ", alphabets_interception)
  
  def difference(self):
    alphabet_difference1 = self.alphabet1.difference(self.alphabet2)
    alphabet_difference2 = self.alphabet2.difference(self.alphabet1)
    print(f"The first alphabets difference (A-B) is: {alphabet_difference1}  and the second alphabets difference(B-A) is: {alphabet_difference2}")    
    
my_alphabet = Alphabet()
my_alphabet.enter_alphabets()
my_alphabet.show()
my_alphabet.union()
my_alphabet.interception()
my_alphabet.difference()

