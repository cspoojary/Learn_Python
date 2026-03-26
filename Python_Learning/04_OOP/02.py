# ABSTRACTION
'''
Abstraction is the process of hiding the complex internal details of a system and only exposing the essential 
features to the user. It allows you to focus on what an object does instead of how it does it. By creating a simplified 
interface, you make your code easier to use, maintain, and update without breaking other parts of your program.

- The Real-World Analogy:
Think about driving a car. To drive, you interact with the steering wheel, the accelerator, and the brake pedal. 
These controls form the "interface" you use to operate the vehicle. You do not need to understand how the fuel injectors work, how the transmission shifts gears, or how the combustion engine fires to get from point A to point B.

The car's manufacturer has abstracted the complex mechanical reality behind a simple, user-friendly interface.

- Why do we use it in programming?

Reduces Complexity: Developers can use complex logic without having to understand every line of the underlying code.

Increases Reusability: Abstract concepts can be reused across different parts of an application.

Improves Security: By hiding internal implementations, you prevent other parts of the code from accidentally modifying sensitive data or processes.
'''
from abc import ABC, abstractmethod

# 1. This is our Abstract Class
class Shape(ABC):
    
    # This is an abstract method. 
    # It forces any subclass to create its own version of this method.
    @abstractmethod
    def calculate_area(self):
        pass
        
    # Abstract classes can also have normal, fully implemented methods
    def display_shape_type(self):
        print("I am a 2D shape.")

# 2. This is a Concrete Class inheriting from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    # We MUST implement the abstract method here, or Python will throw an error
    def calculate_area(self):
        return 3.14159 * (self.radius ** 2)

# 3. Another Concrete Class inheriting from Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def calculate_area(self):
        return self.width * self.height

# --- Using the Code ---

# If we try to do this: shape = Shape()
# Python throws an error! We cannot instantiate an abstract class.

# Instead, we create instances of the concrete classes:
my_circle = Circle(5)
my_rectangle = Rectangle(4, 6)

# The user just calls 'calculate_area()' without needing to know the math inside.
print(f"Circle Area: {my_circle.calculate_area()}")       # Output: Circle Area: 78.53975
print(f"Rectangle Area: {my_rectangle.calculate_area()}") # Output: Rectangle Area: 24

# Both can use the shared, implemented method from the abstract class
my_circle.display_shape_type() # Output: I am a 2D shape.

'''
In this code, Shape is an abstraction. If another developer is writing a program that needs 
to calculate the area of various shapes, they just need to know that every shape object has a calculate_area() method. 
They don't need to look inside Circle to see the Pi math, or Rectangle to see the multiplication. The complexity is hidden 
behind the simple calculate_area() interface.
'''