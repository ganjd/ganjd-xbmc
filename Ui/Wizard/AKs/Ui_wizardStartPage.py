# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'L:\Python Projekte\Galabau-2\Ui\Wizard\AKs\wizardStartPage.ui'
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

class Ui_WizardPage(object):
    def setupUi(self, WizardPage):
        WizardPage.setObjectName(_fromUtf8("WizardPage"))
        WizardPage.resize(675, 411)
        self.verticalLayout = QtGui.QVBoxLayout(WizardPage)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame_2 = QtGui.QFrame(WizardPage)
        self.frame_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_Datum = QtGui.QLabel(self.frame_2)
        self.label_Datum.setMinimumSize(QtCore.QSize(100, 0))
        self.label_Datum.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_Datum.setFont(font)
        self.label_Datum.setObjectName(_fromUtf8("label_Datum"))
        self.horizontalLayout.addWidget(self.label_Datum)
        self.input_Datum = QtGui.QDateEdit(self.frame_2)
        self.input_Datum.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"selection-color: rgb(0, 0, 0);"))
        self.input_Datum.setWrapping(False)
        self.input_Datum.setFrame(True)
        self.input_Datum.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.input_Datum.setAccelerated(False)
        self.input_Datum.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToPreviousValue)
        self.input_Datum.setCalendarPopup(True)
        self.input_Datum.setCurrentSectionIndex(0)
        self.input_Datum.setObjectName(_fromUtf8("input_Datum"))
        self.horizontalLayout.addWidget(self.input_Datum)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_Kunde = QtGui.QLabel(self.frame_2)
        self.label_Kunde.setMinimumSize(QtCore.QSize(100, 0))
        self.label_Kunde.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_Kunde.setFont(font)
        self.label_Kunde.setObjectName(_fromUtf8("label_Kunde"))
        self.horizontalLayout_2.addWidget(self.label_Kunde)
        self.input_Kunde = QtGui.QLineEdit(self.frame_2)
        self.input_Kunde.setReadOnly(True)
        self.input_Kunde.setObjectName(_fromUtf8("input_Kunde"))
        self.horizontalLayout_2.addWidget(self.input_Kunde)
        self.toolButton_kunde = QtGui.QToolButton(self.frame_2)
        self.toolButton_kunde.setObjectName(_fromUtf8("toolButton_kunde"))
        self.horizontalLayout_2.addWidget(self.toolButton_kunde)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_Kunde_2 = QtGui.QLabel(self.frame_2)
        self.label_Kunde_2.setMinimumSize(QtCore.QSize(100, 0))
        self.label_Kunde_2.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_Kunde_2.setFont(font)
        self.label_Kunde_2.setObjectName(_fromUtf8("label_Kunde_2"))
        self.horizontalLayout_3.addWidget(self.label_Kunde_2)
        self.input_Projekt = QtGui.QLineEdit(self.frame_2)
        self.input_Projekt.setReadOnly(True)
        self.input_Projekt.setObjectName(_fromUtf8("input_Projekt"))
        self.horizontalLayout_3.addWidget(self.input_Projekt)
        self.toolButton_projekt = QtGui.QToolButton(self.frame_2)
        self.toolButton_projekt.setObjectName(_fromUtf8("toolButton_projekt"))
        self.horizontalLayout_3.addWidget(self.toolButton_projekt)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_AKs = QtGui.QLabel(self.frame_2)
        self.label_AKs.setMinimumSize(QtCore.QSize(100, 0))
        self.label_AKs.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_AKs.setFont(font)
        self.label_AKs.setObjectName(_fromUtf8("label_AKs"))
        self.horizontalLayout_4.addWidget(self.label_AKs)
        self.input_AKs = QtGui.QComboBox(self.frame_2)
        self.input_AKs.setObjectName(_fromUtf8("input_AKs"))
        self.input_AKs.addItem(_fromUtf8(""))
        self.input_AKs.addItem(_fromUtf8(""))
        self.input_AKs.addItem(_fromUtf8(""))
        self.input_AKs.addItem(_fromUtf8(""))
        self.input_AKs.addItem(_fromUtf8(""))
        self.input_AKs.addItem(_fromUtf8(""))
        self.input_AKs.addItem(_fromUtf8(""))
        self.input_AKs.addItem(_fromUtf8(""))
        self.input_AKs.addItem(_fromUtf8(""))
        self.input_AKs.addItem(_fromUtf8(""))
        self.horizontalLayout_4.addWidget(self.input_AKs)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_Status = QtGui.QLabel(self.frame_2)
        self.label_Status.setMinimumSize(QtCore.QSize(100, 0))
        self.label_Status.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_Status.setFont(font)
        self.label_Status.setObjectName(_fromUtf8("label_Status"))
        self.horizontalLayout_5.addWidget(self.label_Status)
        self.input_Status = QtGui.QComboBox(self.frame_2)
        self.input_Status.setObjectName(_fromUtf8("input_Status"))
        self.input_Status.addItem(_fromUtf8(""))
        self.input_Status.addItem(_fromUtf8(""))
        self.input_Status.addItem(_fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.input_Status)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(WizardPage)
        QtCore.QMetaObject.connectSlotsByName(WizardPage)

    def retranslateUi(self, WizardPage):
        WizardPage.setWindowTitle(QtGui.QApplication.translate("WizardPage", "WizardPage", None, QtGui.QApplication.UnicodeUTF8))
        WizardPage.setTitle(QtGui.QApplication.translate("WizardPage", "Arbeitsstunden", None, QtGui.QApplication.UnicodeUTF8))
        WizardPage.setSubTitle(QtGui.QApplication.translate("WizardPage", "Erfassen von Arbeitsstunden", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Datum.setText(QtGui.QApplication.translate("WizardPage", "Datum", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Kunde.setText(QtGui.QApplication.translate("WizardPage", "Kunde", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_kunde.setText(QtGui.QApplication.translate("WizardPage", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Kunde_2.setText(QtGui.QApplication.translate("WizardPage", "Projekt", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_projekt.setText(QtGui.QApplication.translate("WizardPage", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_AKs.setText(QtGui.QApplication.translate("WizardPage", "Anzahl AKs", None, QtGui.QApplication.UnicodeUTF8))
        self.input_AKs.setItemText(0, QtGui.QApplication.translate("WizardPage", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.input_AKs.setItemText(1, QtGui.QApplication.translate("WizardPage", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.input_AKs.setItemText(2, QtGui.QApplication.translate("WizardPage", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.input_AKs.setItemText(3, QtGui.QApplication.translate("WizardPage", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.input_AKs.setItemText(4, QtGui.QApplication.translate("WizardPage", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.input_AKs.setItemText(5, QtGui.QApplication.translate("WizardPage", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.input_AKs.setItemText(6, QtGui.QApplication.translate("WizardPage", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.input_AKs.setItemText(7, QtGui.QApplication.translate("WizardPage", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.input_AKs.setItemText(8, QtGui.QApplication.translate("WizardPage", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.input_AKs.setItemText(9, QtGui.QApplication.translate("WizardPage", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Status.setText(QtGui.QApplication.translate("WizardPage", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.input_Status.setItemText(0, QtGui.QApplication.translate("WizardPage", "Offen", None, QtGui.QApplication.UnicodeUTF8))
        self.input_Status.setItemText(1, QtGui.QApplication.translate("WizardPage", "Abgerechnet", None, QtGui.QApplication.UnicodeUTF8))
        self.input_Status.setItemText(2, QtGui.QApplication.translate("WizardPage", "Geld erhalten", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    WizardPage = QtGui.QWizardPage()
    ui = Ui_WizardPage()
    ui.setupUi(WizardPage)
    WizardPage.show()
    sys.exit(app.exec_())

