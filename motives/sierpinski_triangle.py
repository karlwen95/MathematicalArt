# %% imports
import numpy as np
import random
import matplotlib.pyplot as plt
from tqdm import tqdm
import decimal as dec
import plotly.graph_objects as go


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
        self.current_point = None
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

    def __area(self, leave_out_point=0):
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
        return random.choice(self.get_points())

    def rule1(self):
        """
        Choose one of the three corner points to start in
        :return:
        """
        self.current_point = self.random_corner()

    def rule2(self):
        """
        Choose one of the three corner points
        :return:
        """
        next_corner = self.random_corner()
        self.middle_point(next_corner)

    def rule3(self):
        """Mark the point, i.e. store in memory (or draw)"""
        pass

    def middle_point(self, point1):
        """
        Get the point in the middle of two points.
        :param point1:
        :param point2:
        :return: Point object with coordinates in the middle of input points
        """
        point2 = self.current_point

        # find new x value
        delta_x = np.abs(point1.x - point2.x)
        new_x = point1.x + delta_x/2 if point1.x < point2.x else point1.x - delta_x/2

        # find new y value
        delta_y = np.abs(point1.y - point2.y)
        new_y = point1.y + delta_y / 2 if point1.y < point2.y else point1.y - delta_y / 2

        # go to the next point
        self.current_point = Point(new_x, new_y)

    def algorithm(self, n: int):
        """
        The algorithm creating the Sierpinsky triangle
        :param n: Number of iterations
        :return:
        """
        # choose starting corner
        self.rule1()

        for _ in tqdm(range(n)):
            # find next point
            self.rule2()

            # add the middle point
            self.added_points.append(self.current_point)

    def plot_points(self, plot_type: str, dpi: int, figure_width_inch: float, figure_height_inch: float):
        if plot_type == 'plt':
            fig = plt.figure(figsize=(figure_width_inch, figure_height_inch), dpi=dpi)
        elif plot_type == 'go':
            fig = go.Figure()

        # plot corner points
        if plot_type == 'plt':
            plt.scatter(x=self.__corner1.x, y=self.__corner1.y, c='k', s=0.001)
            plt.scatter(x=self.__corner2.x, y=self.__corner2.y, c='k', s=0.001)
            plt.scatter(x=self.__corner3.x, y=self.__corner3.y, c='k', s=0.001)
        elif plot_type == 'go':
            fig.add_trace(go.Scatter(x=[self.__corner1.x], y=[self.__corner1.y], mode='markers', marker=dict(size=5, color='black')))
            fig.add_trace(go.Scatter(x=[self.__corner2.x], y=[self.__corner2.y], mode='markers', marker=dict(size=5, color='black')))
            fig.add_trace(go.Scatter(x=[self.__corner3.x], y=[self.__corner3.y], mode='markers', marker=dict(size=5, color='black')))

        # plot the added points
        if plot_type == 'plt':
            plt.scatter(x=[p.x for p in self.added_points], y=[p.y for p in self.added_points], c='k', s=0.001)
            plt.title(f'Sierpinsky Triangle after {len(self.added_points)} iterations')
            plt.show()
        elif plot_type == 'go':
            fig.add_trace(go.Scatter(x=[p.x for p in self.added_points], y=[p.y for p in self.added_points], mode='markers',marker=dict(size=2, color='black')))
            fig.update_layout(title=f'Sierpinsky Triangle after {self.added_points} iterations',
                              xaxis_title='X Axis',
                              yaxis_title='Y Axis')
            fig.show()
        return fig

# %% main

if __name__ == '__main__':
    dec.getcontext().prec = 6  # precision
    p1 = Point(1, 1)
    p2 = Point(2, np.sqrt(3))
    p3 = Point(3, 1)
    st = Sierpinski(p1, p2, p3)
    st.algorithm(n=int(1e8))

    # Figure size,
    poster_width = 80  # cm
    poster_height = 120  # cm
    cm_per_inch = 2.54
    poster_width_inch = poster_width / cm_per_inch
    poster_height_inch = poster_height / cm_per_inch

    fig_width = poster_width_inch / 2
    fig_height = poster_height_inch / 6


    fig = st.plot_points(plot_type='plt', dpi=300, figure_width_inch=6.4, figure_height_inch=4.8)

    # remove all spines
    ax = fig.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    ax.set_title('')
    fig.savefig('triangle_manySmallPoints.png', format='png')

