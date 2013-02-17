__author__ = 'Lain'

from Settings.Settings import *

class figure:
    def __init__(self, x, y, type = 0, color = DEFAULT_FIGURE_COLOR):
        self.__x = x;
        self.__y = y;
        self.__color = color;
        self.__templateGrid = [];

    @property
    def x(self):
        return self.__x;
    @x.setter
    def x(self, x):
        self.__x = x;

    @property
    def y(self):
        return self.__y;
    @y.setter
    def y(self, y):
        self.__y = y;

    @property
    def templateGrid(self):
        return self.__templateGrid;
    @templateGrid.setter
    def templateGrid(self, t):
        self.__templateGrid= t;

    @property
    def color(self):
        return self.__color;
    @y.setter
    def y(self, color):
        self.__color = color;