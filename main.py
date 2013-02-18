from __future__ import print_function

__author__ = 'Lain'

from Tkinter import *

from View.TetrisWidget import *
from View.TetrisTipWidget import *
import time
import sys

def destroy_window():
    global root
    if root:
        root.destroy()
    #sys.exit(0)

class MainWrapper(TetrisWidget):
    def __init__(self,root, controller):
        TetrisWidget.__init__(self,root, controller)
        root.bind( "<KeyPress>", controller.keypress )

    def update(self):

        TetrisWidget.getController(self).find_full_line()

        if TetrisWidget.getController(self).GetCurrentFigure():#check for None

            if TetrisWidget.getController(self).collisionCheck("down"): #collision check
                #append old figure to the field
                TetrisWidget.getController(self).appendFigure()

                #create new Figure
                TetrisWidget.getController(self).spawnFigure()
                TetrisWidget.setFigureForRender(self)
                TetrisWidget.getRender(self,"figure").Render()
            else:
                TetrisWidget.getRender(self,"figure").move("down")
                action = TetrisWidget.getController(self).getAction()
                if TetrisWidget.getController(self).collisionCheck(action) is False:
                    if action == "rotate":
                        pass
                    else:
                        TetrisWidget.getRender(self,"figure").move(action)
                    TetrisWidget.getController(self).resetAction()


        else:
            #create new Figure
            TetrisWidget.getController(self).spawnFigure()
            TetrisWidget.setFigureForRender(self)
            TetrisWidget.getRender(self,"figure").Render()

        if True:
           TetrisWidget.update(self)


if __name__ == "__main__":
    print("Main...")
    global root
    root = Tk()

    root.title("Python Tetris")
    #root.protocol('WM_DELETE_WINDOW', destroy_window) do not work with update
    controller = TetrisController(gameFieldWidth = 10, gameFieldHeight = 20)

    #mainWidget = TetrisWidget(root, controller)
    #mainWidget.grid(row = 0, column = 0)
    mainXyidget = MainWrapper(root, controller)
    mainXyidget.grid(row = 0, column = 0)

    #tipWidget = TetrisTipWidget(root, controller)
    #tipWidget.grid(row = 0, column = 1, sticky=S)
    while True:
        time.sleep(0.35)
        mainXyidget.update()
        #tipWidget.update()
    #root.mainloop()


