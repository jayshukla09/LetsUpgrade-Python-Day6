Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
class cone:
    def __init__(self, radius, height):
        self.radius=radius
        self.height=height

    def surfacearea(self):
        return math.pi*(self.radius**2)+math.pi*self.radius*math.sqrt(self.radius**2+self.height**2)
    def volume(self):
        return math.pi*self.radius**2*(self.height%3)

r=int(input("enter radius of cone:"))
h=int(input("enter height of cone:"))
obj=cone(r, h)
print("surface area of cone:", round(obj.surfacearea()))
print("volume of cone:", round(obj.volume()))
