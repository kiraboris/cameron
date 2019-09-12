"""A PC body as a QT application"""

from PySide2 import QtWidgets

class C:
    def __init__(self):
        self._app = QtWidgets.QApplication()
        self._win = QtWidgets.QMainWindow()

    def life_loop(self, mind):
        self._win.show()
        self._app.exec_()

def create():
    return C()