import math
'''
0 4 5
1 7 6
0 5 9
1 7 2

8.19
'''
class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    # 因為後面x,y也都是物件，所以__sub__與__cross計算完之後也要實體化成物件返回，而dot absolute都是scalar，所以返回值就好
    def __sub__(self, no):
        return Points(self.x - no.x, self.y - no.y, self.z - no.z)

    def dot(self, no):
        return self.x * no.x+ self.y * no.y+ self.z * no.z

    def cross(self, no):
        return Points(self.y*no.z - self.z*no.y, self.z*no.x - self.x*no.z, self.x*no.y-self.y*no.x)

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
