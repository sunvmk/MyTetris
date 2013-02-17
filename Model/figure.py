__author__ = 'Lain'

from Settings.Settings import *

class figure:
    def __init__(self, x, y, type = 0, color = DEFAULT_FIGURE_COLOR):
        self.__x = x
        self.__y = y
        self.__color = color
        self.__state = 0 #current figure state
        #range check
        self.__fullTemplate = DEFAULT_FIGURE_TYPE[type]

        self.__templateGrid = self.__fullTemplate[self.__state]



    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def templateGrid(self):
        return self.__templateGrid
    @templateGrid.setter
    def templateGrid(self, t):
        self.__templateGrid= t

    @property
    def color(self):
        return self.__color
    @y.setter
    def y(self, color):
        self.__color = color

    @property
    def height(self):
        return len(self.__templateGrid[0])

    @property
    def width(self):
        return len(self.__templateGrid)


