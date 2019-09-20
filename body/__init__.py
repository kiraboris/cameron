"""A PC body as a QT application."""

from PySide2 import QtWidgets

from . import window

class C:
    def __init__(self):
        self._app = QtWidgets.QApplication()
        self._win = window.ChatWindow()

    def life_loop(self, mind):
        self._connect(mind)
        self._win.show()
        self._app.exec_()

    def _connect(self, mind):
        ai_name = mind.name()
        self._win.setWindowTitle("Chat with %s" % ai_name)
        self._win.set_partner_name(ai_name)
        self._win.sigUserMessage.connect(mind.admin_input)


def create():
    return C()