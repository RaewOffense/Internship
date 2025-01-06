from abc import ABC, abstractmethod

class Animal(ABC):
     
    @abstractmethod
    def eat(self):
          pass
    @abstractmethod
    def makeSound(self):
        pass


class Dog (Animal):
    def eat(self):
        print("Dog eats Dog Feeds.")

    def makeSound(self):
        print("Dog Bark")

dog =Dog()
dog.eat()
dog.makeSound()