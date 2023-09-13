from ABC import SuperClass
import itertools
import random
import re

class Alphabet(SuperClass):

  def __init__(self):
    self.alphabet1=set()
    self.alphabet2=set()

  def enter_alphabets(self):
    print("The way both alphabets should be typed is: {a,l,b,m} {ñ,l,2,+,@}")
    alphabets = input("Enter alphabets A and B: ")
    return alphabets

  def generate_alphabets(self):
    delimiter = " "
    alphabet_one, alphabet_two = re.split(delimiter, self.enter_alphabets())
    self.alphabet1 = set(alphabet_one.strip("{}").split(","))
    self.alphabet2 = set(alphabet_two.strip("{}").split(","))

  def show(self):
    print(f"A: {{{', '.join(self.alphabet1)}}} B: {{{', '.join(self.alphabet2)}}}")   

  def union(self):
    alphabets_union = self.alphabet1.union(self.alphabet2)
    return alphabets_union
  
  def show_union(self):
    print("The alphabets union (A∪B)is: ", self.union())

  def intersection(self):
    alphabets_interception = self.alphabet1.intersection(self.alphabet2)
    return alphabets_interception
  
  def show_intersection(self):
    print(f"The alphabets interception (A∩B) is : ", self.intersection())
  
  def difference_one(self):
    alphabet_difference1 = self.alphabet1.difference(self.alphabet2)
    return alphabet_difference1
    

  def difference_two(self):
    alphabet_difference2 = self.alphabet2.difference(self.alphabet1)
    return alphabet_difference2

  def show_difference(self):
    print(f"The first alphabets difference (A-B) is: {self.difference_one()}  and the second alphabets difference(B-A) is: {self.difference_two()}")


  def enter_simbols_closure(self):
    quantity = int(input("Enter the quantity of simbols for calculate the star closure: "))
    return quantity
  
  def closure(self):
    closure = list(itertools.product(self.alphabet1, self.alphabet2))
    return closure
  
  def generate_closure(self):
    random_closure = random.sample(self.closure(), self.enter_simbols_closure())
    return random_closure
  
  def show_star_closure(self):
    formatted_closure = [f"{elem[0]}{elem[1]}" for elem in self.generate_closure()]
    print("Star Closure: {" + ", ".join(formatted_closure) + "}")







