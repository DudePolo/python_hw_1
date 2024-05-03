# Watto needs a new system for organizing his inventory of podracers. 
# Help him do this by implementing an Object Oriented solution according to the following criteria.

# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes. 
class Podracer:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

  # Define a repair() method that will update the condition of the podracer to "repaired".
  def repair(self):
    self.condition = "repaired"
    
# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
class AnakinsPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super().__init__(max_speed, condition, price)
  
  def boost(self):
    self.max_speed *= 2
    
# Define another class that inherits Podracer and call this one SebulbasPod. 
# This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
class SebulbasPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super().__init__(max_speed, condition, price)
  
  def flame_jet(self,other):
    other.condition = "trashed"



pod = Podracer(100, "damaged", 1000)
pod.repair()

print("Pod Condition after repair:", pod.condition)


new_pod = AnakinsPod(2, "new", 500)
new_pod.boost()

print("New Pod Max Speed after boost:", new_pod.max_speed)


third_pod = SebulbasPod(150, "new", 1500)
third_pod.flame_jet(new_pod)

print("Third Pod Condition after flame_jet:", new_pod.condition) 


'''
Make sure to answer the following prompts about your coding experience:

How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
    -Encapsulation: Each class encapsulates its own data and behavior
    -Inheritance: AnakinsPod and SebulbasPod inherit from the Podracer class
    -Polymorphism: AnakinsPod class defines a 'boost' method and SebulbasPod has 'flame-jet' method
    -Abstraction: Classes abstract away the details of their implementation from the outside world

Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
    -OOP is well suited for this as it allows for the creation of reusable and modular code by organizing related data and functions into classes and objects

How in particular did Object Oriented Programming assist in the solving of this problem?
    -OOP provides a natural and intuitive way to model the entities involved and their relationships a.k.a podracers -> inheritance
'''