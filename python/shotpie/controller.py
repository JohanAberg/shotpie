import sys
from shotpie.model import Model
from shotpie.view import View
from PySide import QtCore
from PySide import QtGui
__author__ = 'aberg'

class Controller(QtCore.QObject):

    def __init__(self):
        super(Controller, self).__init__()
        self.view = View()
        self.view.setWindowTitle('ShotPie')
        self.model = Model()
        self.view.setScene(self.model)
        self.model.refresh()



if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)

    con = Controller()
    con.view.show()

    app.exec_()