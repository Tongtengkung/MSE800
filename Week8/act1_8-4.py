class Animal:                                           # Animal class
    def make_sound(self):
        print("Animal makes a sound")

class Dog(Animal):                                      # Dog class inherits from Animal
    def bark(self):
        print("Dog barks!")

class Cat(Animal):                                      # Cat class inherits from Animal
    def meow(self):
        print("Cat meows!")


dog = Dog()     # Create an instance of Dog
cat = Cat()     # Create an instance of Cat

dog.make_sound()    # Call the method from Animal class
dog.bark()          # Call the method from Dog class

cat.make_sound()    # Call the method from Animal class
cat.meow()          # Call the method from Cat class

# both Dog and Cat classes can use the make_sound method from Animal class