class Triangle(object):
    number_of_sides = 3
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    def check_angles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        else:
            return False       
x=int(input("Enter Angle 1"))
y=int(input("Enter Angle 2"))
z=int(input("Enter Angle 3"))
my_triangle = Triangle(x,y,z)
print (my_triangle.number_of_sides)
print (my_triangle.check_angles())
