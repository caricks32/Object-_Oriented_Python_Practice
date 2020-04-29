import math

class Cylinder():

    # Static variable that does not change when an instance of the class is created
    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        # Algorithm
        # V = pi*r^2*h
        volume = 0

        volume = self.pi * math.pow(self.radius, 2) * self.height
        print("The volume is: {}".format(volume))

    def surface_area(self):
        # Algorithm
        # A = 2*pi*r*h + 2*pi*r^2
        s_area = 0

        s_area = ( 2 * self.pi * self.radius * self.height ) + ( 2 * self.pi * math.pow(self.radius,2))
        print("The volume is: %.2f" % s_area)


my_cylinder = Cylinder(2, 3) # Create an instance of the Cylinder class
my_cylinder.volume() # Call the volume function and print the result
my_cylinder.surface_area() # Call the surface_area function and print the result