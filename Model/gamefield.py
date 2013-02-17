__author__ = 'Lain'

class gamefield:
    def __init__(self, x, y):
        self.__x = x;
        self.__y = y;

        self.__fallenBlocks = [];

        for i in range(0, x):
            temp = [];
            for j in range(0, y):
                temp.append(0);
            self.__fallenBlocks.append(temp);

    @property
    def x(self):
        return self.__x;

    @property
    def y(self):
        return self.__y;

    @property
    def CurrentFigure(self):
        return self.__CurrentFigure;
    @CurrentFigure.setter
    def CurrentFigure(self, CurrentFigure):
        self.__CurrentFigure = CurrentFigure;

    __fallenBlocks = [];

    def GetBlock(self, x, y):
        return self.__fallenBlocks[x][y];

    def GetGrid(self):
        return self.__fallenBlocks;