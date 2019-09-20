"""A PC body as a QT application."""

from PySide2 import QtWidgets

from . import window

class C:
    def __init__(self):
        self._app = QtWidgets.QApplication()
        self._win = window.ChatWindow()

    def life_loop(self, mind):
        self._win.show()
        self._app.exec_()

def create():
    return C()