from PyQt5.QtWidgets import *
import sys

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.lineEdit = QLineEdit(self)
        self.buton = QPushButton(self)
        self.buton.setText("Tamam")
        self.label = QLabel(self)
        self.label.setText("Burası değişecek!")

        layout.addWidget(self.lineEdit)
        layout.addWidget(self.buton)
        layout.addWidget(self.label)

        self.lineEdit.returnPressed.connect(self.rengiDegistir)
        self.lineEdit.textChanged.connect(self.labeleYaz)

    def rengiDegistir(self):
        self.buton.animateClick()
        self.label.setStyleSheet("color:red")

    def labeleYaz(self, metin):
        self.label.setText(metin)

uygulama = QApplication(sys.argv)
pencere = Pencere()
pencere.show()
uygulama.exec_()