import math

class Line():

    def __init__(self, cord1, cord2):
        self.cord1 = cord1
        self.cord2 = cord2

    def distance(self):
        # Algorithm
        # Square root of (X2 - X1)^2 + (Y2 - Y1)^2
        total = 0

        total = math.sqrt(math.pow(self.cord2[0] - self.cord1[0], 2) + math.pow(self.cord2[1] - self.cord1[1], 2))
        print("The distance is: %.2f\n" % total)


    def slope(self):
        # Algorithm
        # Y2 - Y1 / X2 -X1
        total = 0

        total = ( self.cord2[1] - self.cord1[1] ) / ( self.cord2[0] - self.cord1[0] )
        print("The slope is: %.1f\n" % total)



coordinate1 = (3, 2)
coordinate2 = (8, 10)

line = Line(coordinate1, coordinate2) # Creates an instance of the Line class

line.distance() # Call the distance function and print the result
line.slope() # Call the slope function and print the result