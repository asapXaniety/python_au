import sys
from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Triangle:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.A = sqrt((x.x - y.x)**2+(x.y - y.y)**2)
        self.B = sqrt((y.x - z.x)**2+(y.y - z.y)**2)
        self.C = sqrt((x.x - z.x)**2+(x.y - z.y)**2)

    def check_triangle(self):
        if (self.B >= self.A + self.C) or (self.A >= self.B + self.C) or (self.C >= self.A + self.B):
            return 0
        else:
            return 1
    def check_on_the_line(self):
        if self.A == self.B or self.A == self.C or self.B == self.C:
            return 1
        else:
            return 0

    def get_square(self):
        P = (self.A + self.B + self.C) / 2
        return sqrt(P * (P - self.A) * (P - self.B) * (P - self.C))

class FileUtils:
    def __init__(self, file_from):
        self.read = open(file_from)

    def get_all_lines(self):
        all_triangle = self.read.readlines()
        for i in range(len(all_triangle)):
            all_triangle[i] = all_triangle[i].split()
        return all_triangle

    def __del__(self):
       self.read.close()

def Write_to_file(file_to, text):
    text = str(text)
    f = open(file_to, 'w')
    f.write(text)
    f.close()

def main(file_from, file_to):
    Points = FileUtils(file_from)
    Points = Points.get_all_lines()
    Default = 0
    for i in range(len(Points)):
        for j in range(len(Points[i])):
            Points[i][j] = float(Points[i][j])
        x = Point(Points[i][0], Points[i][1])
        y = Point(Points[i][2], Points[i][3])
        z = Point(Points[i][4], Points[i][5])
        Triangle = Triangle(x, y, z)
        if Triangle.check_triangle() and Triangle.check_on_the_line():
            if Triangle.get_square() > Default:
                Default = Triangle.get_square()

    Write_to_file(file_to, M)

if __name__ == "__main__":
     files = sys.argv
     main(files[1], files[2])
