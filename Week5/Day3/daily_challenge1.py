# class Circle():
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         print(self.radius)

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"The area of this circle is {3.14*self.radius**2}") 

    def printPattern(self):
        import math
        # dist represents distance to the center
        # for horizontal movement
        for i in range((2 * self.radius)+1):
    
            # for vertical movement
            for j in range((2 * self.radius)+1):
                
                dist = math.sqrt((i - self.radius) * (i - self.radius) +
                    (j - self.radius) * (j - self.radius))

                if (dist > self.radius - 0.5 and dist < self.radius + 0.5):
                    print("*",end="")
                else:
                    print(" ",end="")     
        
    
            print()

    def add_circles(self,other_circle):
        new_radius=self.radius+other_circle.radius
        print(f"The new circle has a radius of {new_radius}")


    def compare_circles(self,other_circle):
        radius1=self.radius
        radius2=other_circle.radius
        if radius1>radius2:
            print(f"circle with radius of {radius1} is larger")
        if radius2>radius1:
            print(f"circle with radius of {radius2} is larger")
        if radius1==radius2:
            print("The circles are the same size")

    def add_to_list(self,other_circle):
        circle_list=[]
        circle_list.append(self.radius)
        circle_list.append(other_circle.radius)
        circle_list.sort()
        print(circle_list)

        

circle1=Circle(30)
circle2=Circle(20)

circle1.area()

circle1.add_circles(circle2)
circle1.compare_circles(circle2)
circle1.add_to_list(circle2)
# circle1.printPattern()

# print(Circle.area(2))
        