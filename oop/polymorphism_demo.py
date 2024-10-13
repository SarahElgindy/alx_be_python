class Shape:
    def area(self):
        raise NotImplementedError("Derived classes must override this method.")

class Rectangle(Shape):
    def __init__(self, lenght, width):
        self.lenght=lenght
        self.width=width
    def area(self):
        return self.lenght * self.width
        
class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius
    def area(self):
        return (self.radius **2)