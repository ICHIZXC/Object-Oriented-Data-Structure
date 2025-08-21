class Spherical:
    pi = 3.1415926535897932384626433832795028841
    
    def __init__(self, radius):
        self.radius = radius

    def changeR(self, Radius):
        self.radius = Radius

    def findVolume(self):
        v = (4/3 * Spherical.pi * (self.radius ** 3))
        return v

    def findArea(self):
        a = 4 * Spherical.pi * (self.radius ** 2)
        return a

    def __str__(self):
        return f"Radius ={self.radius} Volumn = {self.findVolume()} Area = {self.findArea()}"

r1, r2 = input("Enter R : ").split()
R1 = Spherical(int(r1))
print(type(R1))
print(dir(R1))
print(R1)
R1.changeR(int(r2))
print(R1)