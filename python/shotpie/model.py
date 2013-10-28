from manifest import QtGui

__author__ = 'aberg'

class Model(QtGui.QGraphicsScene):
    def __init__(self):
        super(Model, self).__init__()
        self.items = [1, 2, 3, 4, 5, 3, 45, 6, 56, 34, 6, 456, 345, 6, 456, 345, 65, 1, 2, 3, 4, 5, 3, 45, 6, 56, 34, 6,
                      456, 345, 6, 456, 345, 65]

    def refresh(self):
        span_angle = 360.0/len(self.items)
        for index, item in enumerate(self.items):
            print index, index * span_angle * 16, span_angle * 16
            item = QtGui.QGraphicsEllipseItem(0, 0, 100, 100)
            item.setStartAngle(index*span_angle*16)
            item.setSpanAngle(span_angle*16)
            self.addItem(item)