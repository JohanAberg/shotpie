__author__ = 'aberg'

from manifest import QtGui, QtCore


class View(QtGui.QGraphicsView):
    def __init__(self):
        super(View, self).__init__()
        self.setRenderHint(QtGui.QPainter.Antialiasing)
        #self.setStyleSheet("border-width: 0px; border-style: solid; background-color:rgba(0,0,0,11) ")
        #self.setStyleSheet("background-color:rgba(33,0,0,0) ")
        self.setStyleSheet("background: transparent; border: transparent;")
        #self.setStyleSheet("background: transparent;")

        #self.setBackgroundRole(QtGui.QPalette.Window)
        #self.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(122, 122, 122, 122)))
        #self.setAutoFillBackground(False)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground);
        #p = self.palette()
        #p.setColor(QtGui.QPalette.Window, QtCore.Qt.transparent)
        #self.setPalette(p)