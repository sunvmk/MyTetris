from __future__ import print_function

__author__ = 'Lain'

from Tkinter import *

from View.TetrisWidget import *
from View.TetrisTipWidget import *

if __name__ == "__main__":
    print("Main...");
    root = Tk();

    root.title("Python Tetris");
    controller = TetrisController(gameFieldWidth = 10, gameFieldHeight = 20)

    mainWidget = TetrisWidget(root, controller);
    mainWidget.grid(row = 0, column = 0);

    tipWidget = TetrisTipWidget(root, controller);
    tipWidget.grid(row = 0, column = 1, sticky=S);
    root.mainloop();


