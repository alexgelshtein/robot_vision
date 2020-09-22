import sys
from PyQt5 import QtCore, QtWidgets

class Example(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        lcd = QtWidgets.QLCDNumber(self)
        sld = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal & slot')
        self.show()


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())