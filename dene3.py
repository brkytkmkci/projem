from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
import sys

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        yer = QVBoxLayout(self)
        self.gir = QLineEdit(self)
        dugme = QPushButton('Tıkla', self)
        self.yazi = QLabel(self)

        yer.addWidget(self.gir)
        yer.addWidget(dugme)
        yer.addWidget(self.yazi)

        dugme.clicked.connect(self.gecir)

    def gecir(self):
        self.yazi.setText(self.gir.text())

uyg = QApplication(sys.argv)
pen = Pencere()
pen.show()
uyg.exec_()
    