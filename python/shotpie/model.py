from PySide import QtGui

__author__ = 'aberg'

class Model(QtGui.QGraphicsScene):
    def __init__(self):
        super(Model, self).__init__()
        self.items = [1, 2, 3, 4, 5]

    def refresh(self):
        span_angle = 360/len(self.items)
        for index, item in enumerate(self.items):
            item = QtGui.QGraphicsEllipseItem(0, 0, 100, 100)
            item.setStartAngle(index*span_angle*16)
            item.setSpanAngle(span_angle*16)
            self.addItem(item)