
from PySide2 import QtWidgets

class TheWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        cw = QtWidgets.QWidget()
        txt = QtWidgets.QTextEdit()
        line = QtWidgets.QLineEdit()
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(txt)
        layout.addWidget(line)
        cw.setLayout(layout)
        self.setCentralWidget(cw)