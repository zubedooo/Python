import cmath
class Circle():
    def __init__(self, radius):
        self.setRadius(radius)
    def getRadius(self):
        return self.__radius
    def setRadius(self, radius):
        if radius < 0:
            raise RuntimeError("Negative radius Disallowed")
        if radius ==0:
            raise RuntimeError("No 0 Please")
        if type(radius)!=int:
            raise RuntimeError("Character Disallowed")
        else:
            self.__radius = radius
    def getArea(self):
        return self.__radius * self.__radius * cmath.pi
    def printCircle(self):
        print(self.__str__() + " radius: " + str(self.__radius))

n=int(input("Enter Radius: "))
try:
  c= Circle(n)
  print("c's area is: ",c.getArea())
except RuntimeError as ex:
  print("Invalid radius,", ex)
