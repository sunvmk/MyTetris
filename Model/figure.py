__author__ = 'Lain'

class figure:
    def __init__(self, x=0, y=0, state=0, template=[]):
        self.__x = x
        self.__y = y
        self._state = 0
        self.__template = template

    def rotate(self):
        if self._state < len(self.__template)-1:
            self._state = self._state+1
        else:
            self._state = 0
        return self.__template[self._state]

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
    def template(self):
        return self.__template
    @template.setter
    def template(self, t):
        self.__template = t

    @property
    def state(self):
        return self._state

    @property
    def height(self):
        return len(self.__template[self._state][0])

    @property
    def width(self):
        return len(self.__template[self._state])

    @property
    def shape(self):
        return self.__template[self._state]


