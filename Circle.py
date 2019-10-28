class Circle():
    # class object attribute
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius*radius*Circle.pi

    def get_circumference(self):
        return self.radius * Circle.pi * 2


c = Circle(30)
print(c.pi)
print(c.radius)
print(c.get_circumference())
print(c.area)

# print('Radius is: ',c.radius)
# print('Area is: ',c.area)
# print('Circumference is: ',c.getCircumference())
#
# c = Circle(2)
#
# print('Radius is: ',c.radius)
# print('Area is: ',c.area)
# print('Circumference is: ',c.getCircumference())