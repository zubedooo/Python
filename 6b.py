import math
class Circle():
    def __init__(self, radius):
        self.setRadius(radius)
    def getRadius(self):
        return self.radius
    def setRadius(self, radius):
        if int(radius) < 0:
            raise RuntimeError("Negative radius Disallowed")
        elif int(radius) ==0:
            raise RuntimeError("No 0 Please")
        else:
            self.radius = radius
    def getArea(self):
        return self.radius * self.radius * math.pi
try:
    n=input("Enter Radius: ")
except:
    print 'Invalid radius', RuntimeError('No characters Please',)
else:    
    try:
        c= Circle(n)
        print "c's area is: ",c.getArea()
    except RuntimeError as ex:
        print "Invalid radius,", ex
