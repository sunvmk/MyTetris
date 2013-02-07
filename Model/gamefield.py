__author__ = 'Lain'

class gamefield:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

        #self.__fallenBlocks = [[1,0,1,1,0],[1,1,0,1,1],[1,0,0,1,0],[1,0,1,0,0],[0,0,1,0,1]];

        for i in range(0, y):
           temp = []
           for j in range(0, x):
               if i==0:
                    temp.append(0)
               else:
                   temp.append(0)
           self.__fallenBlocks.append(temp)

    def append(self, figure):
        for i in range(0, figure.height):
            for j in range(0, figure.width):
                if figure.shape[j][i] == 1:
                    print figure.x+j, figure.y+i
                    self.__fallenBlocks[figure.y+i][figure.x+j] = 1

        #figure.x
        #figure.y
        #figure.height
        #figure.width

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def CurrentFigure(self):
        return self.__CurrentFigure
    @CurrentFigure.setter
    def CurrentFigure(self, CurrentFigure):
        self.__CurrentFigure = CurrentFigure

    __fallenBlocks = []

    def GetCell(self, x, y):
        return self.__fallenBlocks[x][y]

    def GetGrid(self):
        return self.__fallenBlocks