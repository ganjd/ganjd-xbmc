# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'L:\Python Projekte\Galabau-2\Ui\Wizard\Belege\artikel_Final.ui'
#
# Created: Thu Oct 11 00:38:13 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(595, 198)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox = QtGui.QGroupBox(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.frame = QtGui.QFrame(self.groupBox)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(50, -1, -1, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_Bezeichnung = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_Bezeichnung.setFont(font)
        self.label_Bezeichnung.setObjectName(_fromUtf8("label_Bezeichnung"))
        self.verticalLayout.addWidget(self.label_Bezeichnung)
        self.label_Menge = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_Menge.setFont(font)
        self.label_Menge.setObjectName(_fromUtf8("label_Menge"))
        self.verticalLayout.addWidget(self.label_Menge)
        self.label_Betrag_Brutto = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_Betrag_Brutto.setFont(font)
        self.label_Betrag_Brutto.setObjectName(_fromUtf8("label_Betrag_Brutto"))
        self.verticalLayout.addWidget(self.label_Betrag_Brutto)
        self.label_Betrag_Netto = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_Betrag_Netto.setFont(font)
        self.label_Betrag_Netto.setObjectName(_fromUtf8("label_Betrag_Netto"))
        self.verticalLayout.addWidget(self.label_Betrag_Netto)
        self.label_Kunde = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_Kunde.setFont(font)
        self.label_Kunde.setObjectName(_fromUtf8("label_Kunde"))
        self.verticalLayout.addWidget(self.label_Kunde)
        self.label_Projekt = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_Projekt.setFont(font)
        self.label_Projekt.setObjectName(_fromUtf8("label_Projekt"))
        self.verticalLayout.addWidget(self.label_Projekt)
        self.label_Status = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_Status.setFont(font)
        self.label_Status.setObjectName(_fromUtf8("label_Status"))
        self.verticalLayout.addWidget(self.label_Status)
        self.verticalLayout_2.addWidget(self.frame)
        self.verticalLayout_3.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "David:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Bezeichnung.setText(QtGui.QApplication.translate("Form", "Bezeichnung", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Menge.setText(QtGui.QApplication.translate("Form", "Menge", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Betrag_Brutto.setText(QtGui.QApplication.translate("Form", "Betrag_Brutto", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Betrag_Netto.setText(QtGui.QApplication.translate("Form", "Betrag_Netto", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Kunde.setText(QtGui.QApplication.translate("Form", "Kunde", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Projekt.setText(QtGui.QApplication.translate("Form", "Projekt", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Status.setText(QtGui.QApplication.translate("Form", "Status", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

