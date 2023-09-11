from ABC import SuperClass
import itertools
import random
import re

class Alphabet(SuperClass):

  def __init__(self):
    self.alphabet1=set()
    self.alphabet2=set()

  def enter_alphabets(self):
    delimiter = " "
    alphabets = input("Enter alphabets A and B: ")
    alphabet_one, alphabet_two = re.split(delimiter, alphabets)

    self.alphabet1 = set(alphabet_one.strip("{}").split(","))
    self.alphabet2 = set(alphabet_two.strip("{}").split(","))

  def show(self):
    print(f"A: {{{', '.join(self.alphabet1)}}} B: {{{', '.join(self.alphabet2)}}}")   

  def union(self):
    alphabets_union = self.alphabet1.union(self.alphabet2)
    print("The alphabets union (A∪B)is: ", alphabets_union)

  def intersection(self):
    alphabets_interception = self.alphabet1.intersection(self.alphabet2)
    print(f"The alphabets interception (A∩B) is : ", alphabets_interception)
  
  def difference(self):
    alphabet_difference1 = self.alphabet1.difference(self.alphabet2)
    alphabet_difference2 = self.alphabet2.difference(self.alphabet1)
    print(f"The first alphabets difference (A-B) is: {alphabet_difference1}  and the second alphabets difference(B-A) is: {alphabet_difference2}")

    


  def star_closure(self):
    quantity = int(input("Enter the quantity of simbols for calculate the star closure: "))
    closure = list(itertools.product(self.alphabet1, self.alphabet2))

    random_closure = random.sample(closure, quantity)

    formatted_closure = [f"{elem[0]}{elem[1]}" for elem in random_closure]

    print("Star Closure: {" + ", ".join(formatted_closure) + "}")







