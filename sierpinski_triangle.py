# %% imports
import numpy as np
import random



# %% point class

class Point:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__coordinates = (self.__x, self.__y)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) not in (int, float):
            print('Wrong input type')
        else:
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) not in (int, float):
            print('Wrong input type')
        else:
            self.__y = y

    @property
    def coordinates(self):
        return self.__x, self.__y

    def update_coordinates(self, x, y):
        if type(x) not in (int, float) or type(y) not in (int, float):
            print('Wrong input type')
        else:
            self.__x = x
            self.__y = y


# %% siepinski class

class Sierpinski:

    def __init__(self, corner1: Point, corner2: Point, corner3: Point):
        self.__corner1 = corner1
        self.__corner2 = corner2
        self.__corner3 = corner3
        self.__iter = -1
        self.__middle_point = None
        self.__test_point = None
        self.__added_points = []

    @property
    def corner1(self):
        return self.__corner1

    @property
    def corner2(self):
        return self.__corner2

    @property
    def corner3(self):
        return self.__corner3

    @property
    def added_points(self):
        return self.__added_points

    def get_points(self):
        return self.__corner1, self.__corner2, self.__corner3

    def __area(self, leave_out_point = 0):
        x1, y1 = self.__corner1.coordinates
        x2, y2 = self.__corner1.coordinates
        x3, y3 = self.__corner1.coordinates
        if leave_out_point == 1:
            x1, y1 = self.__test_point.coordinates
        elif leave_out_point == 2:
            x2, y2 = self.__test_point.coordinates
        elif leave_out_point == 3:
            x3, y3 = self.__test_point.coordinates
        return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

    def is_inside_triangle(self):
        A = self.__area(leave_out_point=0)
        A1 = self.__area(leave_out_point=1)
        A2 = self.__area(leave_out_point=2)
        A3 = self.__area(leave_out_point=3)
        return A == A1 + A2 + A3

    # choose random corner point
    def random_corner(self):
        return random.choice(self.get_points()).coordinates

    # choose first point
    def first_point(self):
        min_x = min(self.__corner1.x, self.__corner2.x, self.__corner3.x)
        max_x = max(self.__corner1.x, self.__corner2.x, self.__corner3.x)
        min_y = min(self.__corner1.y, self.__corner2.y, self.__corner3.y)
        max_y = max(self.__corner1.y, self.__corner2.y, self.__corner3.y)
        x = random.uniform(min_x, max_x)
        y = random.uniform(min_y, max_y)
        self.__test_point = Point()



    # get point between previous point and random corner point
    def rule1(self):



# %% main

if __name__ == '__main__':
    p1 = Point(1, 1)
    p2 = Point(2, 2)
    p3 = Point(3, 1)
    st = Sierpinski(p1, p2, p3)
    print(st.random_point())
