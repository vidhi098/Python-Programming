from abc import ABC, abstractmethod


class Polygon(ABC):  # base class / super class

    @abstractmethod
    def roof(self):
        pass


class Triangle(Polygon):  # subclass

    # overriding abstract method
    def roof(self):
        print("Triangle: I have 3 sides")


class Pentagon(Polygon, ABC):  # subclass

    # overriding abstract method
    def roof(self):
        print("Pentagon: I have 5 sides")


class Hexagon(Polygon, ABC):  # subclass

    # overriding abstract method
    def roof(self):
        print("Hexagon: I have 6 sides")


class Quadrilateral(Polygon, ABC):  # subclass

    # overriding abstract method
    def roof(self):
        print("Quadrilateral: I have 4 sides")


# Driver code
# Creating the objects to call the abstract method.
R = Triangle()
R.roof()

K = Quadrilateral()
K.roof()

R = Pentagon()
R.roof()

K = Hexagon()
K.roof()
