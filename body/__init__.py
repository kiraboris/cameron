"""A PC body as a QT application."""

from PySide2 import QtWidgets
from .window import TheWindow

class C:
    def __init__(self):
        self._app = QtWidgets.QApplication()
        self._win = TheWindow()

    def life_loop(self, mind):
        self._win.show()
        self._app.exec_()

def create():
    return C()