
from PySide2 import QtWidgets, QtGui, QtCore


class ChatLineEdit(QtWidgets.QLineEdit):

    sigMessage = QtCore.Signal(str)

    def keyReleaseEvent(self, event: QtGui.QKeyEvent):
        if event.key() == QtGui.Qt.Key_Return:
            self.selectAll()
            self.sigMessage.emit(self.text())


class ChatWindow(QtWidgets.QMainWindow):

    sigUserMessage = QtCore.Signal(str)

    def __init__(self):
        super().__init__()
        cw = QtWidgets.QWidget()
        self.txt = QtWidgets.QTextEdit()
        self.line = ChatLineEdit()
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.txt)
        layout.addWidget(self.line)
        self.line.sigMessage.connect(self.on_user_message)
        cw.setLayout(layout)
        self.setCentralWidget(cw)

        # default annotations
        self._partner_name = "They"
        self._user_name = "You"
        self.txt.setReadOnly(True)

    def showEvent(self, event: QtGui.QShowEvent):
        self.line.setFocus()

    def set_partner_name(self, name: str):
        self._partner_name = name

    def set_user_name(self, name: str):
        self._user_name = name

    def on_user_message(self, msg: str):
        self.txt.append(self._user_name + ": " + msg + "\n")
        self.sigUserMessage.emit(msg)

    def on_partner_message(self, msg: str):
        self.txt.append(self._partner_name + ": " + msg + "\n")