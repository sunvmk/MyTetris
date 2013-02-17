__author__ = 'Lain'

from Model.figure import *
from Model.gamefield import *
from Settings.Settings import *

class TetrisController:
    def __init__(self, gameFieldWidth = 10, gameFieldHeight = 10, figureSize = FIGURE_TEMPLATE_SIZE):

        self.__templateFigureSize = figureSize;
        self.__figure = figure(self.__templateFigureSize, self.__templateFigureSize);
        self.__gamefield = gamefield(gameFieldWidth, gameFieldHeight);

    def GetCurrentFigure(self):
        return self.__figure

    def GetGameField(self):
        return self.__gamefield

    def GetNextFigure(self):
        return figure(self.__templateFigureSize, self.__templateFigureSize);