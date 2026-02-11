from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self, sides):
        super().__init__()
        self.sides = sides
    
    @abstractmethod
    def perimeter(self,side_length):
        self.side_length = side_length
        return self.sides * self.side_length
    
    @abstractmethod
    def area(self):
        pass    

class Triangle(Shape):
    def __init__(self):
        super().__init__(3)

    def __str__(self):
        return "This is a triangle of side length {}".format(self.side_length)
    
    def perimeter(self, side_length):
        return "perimeter is " + str(super().perimeter(side_length))
    
    def area(self):
        return math.sqrt(3) / 4 * (self.side_length ** 2)



#shape = Shape(4)  # This will raise an error because Shape is abstract

shape1 = Triangle()

print(shape1, shape1.perimeter(5))  # Output: This is a triangle



