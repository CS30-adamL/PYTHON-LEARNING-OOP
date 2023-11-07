
"""
OBJECTS

Objects are the building blocks of an OOP program. An object is a combination of data (properties/state) and methods (functions/behaviour). 

For example, a player object may have data to store properties of the player such as: x, y, width, height, color, speed, etc. and methods to define the behaviour of the player such as : move, draw, jump, teleport, etc.. 

In Python, we have already learned how to create dictionaries that can store data:
"""

#Create a block dictionary
block = {
    "x": 200,
    "y": 300,
    "w": 100,
    "h": 50,
    "color": "blue",
}


"""CLASSES & OBJECTS

In an OOP program, we create objects. These objects store data in properties and provide functionality with methods.  A class may be used to create an object with properties and methods.

There are two steps in creating an object with a class:
Define a class. A class is a template for an object. It is a blueprint which describes the properties and behaviour that the objects of the class all share. A class can be used to create many objects. Objects created from a class are called instances of that particular class.
Use class to create an object. Once a class is defined, we can use the class to create objects that follow the blueprint/template of the class. To create an object from a class we need to use the name of the class followed by parentheses: this will create an object and run the class’s constructor method. (Note: by convention a class name should be capitalized. This is to help distinguish it from a regular function)
"""

"""CONSTRUCTOR METHOD

A constructor is a special method of a class that will automatically run when an object is created. In Python, the constructor must be called __init__ and the first parameter is commonly called self and is a reference to the object being created.

Example - RandomCircle Class
"""

import random


# Create a Random Circle class
class RandomCircle:
    # Define constructor method
    def __init__(self):
        # Add properties to empty self object
        self.x = random.randrange(0, 400)
        self.y = random.randrange(0, 400)
        self.r = random.randrange(0, 50)


        print(f"New Random Circle Created: {self.x}, {self.y}, {self.r}")




# Use RandomCircle class to create two RandomCircle objects
circle1 = RandomCircle()
circle2 = RandomCircle()


"""CONSTRUCTOR ARGUMENTS

You may provide arguments for the class constructor when you create a new object.  Define parameters for the constructor method and then pass in arguments when you create a new object.

Example - Circle class
"""


# Create a Circle class
class Circle:
    # Define constructor method with parameters
    def __init__(self, initX, initY, initR):
        # Add properties to empty self object
        self.x = initX
        self.y = initY
        self.r = initR


        print(f"New Circle Created: {self.x}, {self.y}, {self.r}")




# Use Circle class to create two Circle objects
# with the provided arguments.
circle1 = Circle(50, 100, 20)
circle2 = Circle(200, 400, 75)


"""METHODS

Methods are functions defined inside the body of a class. They are used to define the behaviour of the objects created with that class.

We define methods the same way we would a regular function, except all methods must use the first parameter to store a reference to the object calling the method. This first parameter is commonly called self.

A common error is to forget to put self as the first parameter in your function definition.

You can invoke methods using dot notation. Use the name of the object followed by a dot and then the method name followed by parentheses and any required arguments placed inside the parentheses. 

Example - Circle Class with Methods
"""
import math


# Create a Circle class
class Circle:
    # Define constructor method with parameters
    def __init__(self, initX, initY, initR):
        # Add properties to empty self object
        self.x = initX
        self.y = initY
        self.r = initR


        print(f"New Circle Created: {self.x}, {self.y}, {self.r}")


    # Methods (Functions / Behaviour)
    def setCenter(self, newX, newY):
        self.x = newX
        self.y = newY
        print(f"Center is now: ({self.x}, {self.y})")


    def setRadius(self, newR):
        self.r = newR
        print(f"Radius is now: {self.r}")


    def getArea(self):
        return math.pi * (self.r ** 2)




# Use Circle class to create two Circle objects
# with the provided arguments.
print("\nCIRCLE 1")
circle1 = Circle(50, 100, 10)
circle1.setCenter(500, 50)
print(f"Circle 1's area is: {circle1.getArea()}.")


print("\n CIRCLE 2")
circle2 = Circle(200, 400, 100)
print(f"Circle 2's area is: {circle2.getArea()}.")
circle2.setRadius(10)
print(f"Circle 2's area is: {circle2.getArea()}.")


