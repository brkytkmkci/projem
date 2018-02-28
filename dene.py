from PyQt5.QtWidgets import QApplication, QWidget, QButtonGroup, QLabel, QVBoxLayout, QRadioButton, QPushButton
import sys

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.yerlesim = QVBoxLayout(self)
        self.radyo1 = QRadioButton("Kadın", self)
        self.radyo2 = QRadioButton("Erkek", self)
        self.dugme = QPushButton("Tamam", self)
        self.yazi = QLabel("Erkek cinsiyetini seçtiniz.", self)

        self.dugmeGrubu = QButtonGroup(self)
        self.dugmeGrubu.addButton(self.radyo1)
        self.dugmeGrubu.addButton(self.radyo2)

        self.yerlesim.addWidget(self.radyo1)
        self.yerlesim.addWidget(self.radyo2)
        self.yerlesim.addWidget(self.dugme)
        self.yerlesim.addWidget(self.yazi)

        self.dugme.clicked.connect(self.tiklandi)

    def tiklandi(self):
        if self.dugmeGrubu.checkedButton():
            metin = self.dugmeGrubu.checkedButton().text() + " cinsiyetini seçtiniz."
            self.yazi.setText(metin)
        

uygulama = QApplication(sys.argv)
pencere1 = Pencere()

pencere1.show()
uygulama.exec_()