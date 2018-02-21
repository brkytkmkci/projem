from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit
from PyQt5.QtCore import QSize, QPoint
from PyQt5.QtGui import QIcon, QPixmap
import sys

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(QSize(400,100))
        self.move(QPoint(0,0))
        self.setWindowTitle("Python ve PyQt5 ile Görsel Programlama Öğreniyoruz")
        self.setWindowIcon(QIcon('a.png'))

        etiket = QLabel(self)
        etiket.setText("Deneme")
        etiket.setPixmap(QPixmap("b.png"))
        etiket.resize(100,100)

        lineedit = QLineEdit(self)
        lineedit.setReadOnly(True)

uygulama = QApplication(sys.argv)
pencere1 = Pencere()

pencere1.show()
uygulama.exec_()