# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'L:\Python Projekte\Galabau-2\Ui\Wizard\Belege\wizardStartPage.ui'
#
# Created: Thu Oct 11 00:38:14 2012
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
        WizardPage.resize(725, 528)
        self.verticalLayout = QtGui.QVBoxLayout(WizardPage)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame_2 = QtGui.QFrame(WizardPage)
        self.frame_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_4 = QtGui.QLabel(self.frame_2)
        self.label_4.setMinimumSize(QtCore.QSize(150, 0))
        self.label_4.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.input_Belegnr = QtGui.QLineEdit(self.frame_2)
        self.input_Belegnr.setMinimumSize(QtCore.QSize(200, 0))
        self.input_Belegnr.setReadOnly(True)
        self.input_Belegnr.setObjectName(_fromUtf8("input_Belegnr"))
        self.horizontalLayout_2.addWidget(self.input_Belegnr)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_datum = QtGui.QLabel(self.frame_2)
        self.label_datum.setMinimumSize(QtCore.QSize(150, 0))
        self.label_datum.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_datum.setFont(font)
        self.label_datum.setObjectName(_fromUtf8("label_datum"))
        self.horizontalLayout.addWidget(self.label_datum)
        self.input_Datum = QtGui.QDateEdit(self.frame_2)
        self.input_Datum.setMinimumSize(QtCore.QSize(300, 0))
        self.input_Datum.setCalendarPopup(True)
        self.input_Datum.setObjectName(_fromUtf8("input_Datum"))
        self.horizontalLayout.addWidget(self.input_Datum)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_5 = QtGui.QLabel(self.frame_2)
        self.label_5.setMinimumSize(QtCore.QSize(150, 0))
        self.label_5.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_5.addWidget(self.label_5)
        self.input_Lieferant = QtGui.QComboBox(self.frame_2)
        self.input_Lieferant.setMinimumSize(QtCore.QSize(200, 0))
        self.input_Lieferant.setEditable(True)
        self.input_Lieferant.setObjectName(_fromUtf8("input_Lieferant"))
        self.horizontalLayout_5.addWidget(self.input_Lieferant)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label = QtGui.QLabel(self.frame_2)
        self.label.setMinimumSize(QtCore.QSize(150, 0))
        self.label.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.input_Zahlungsart = QtGui.QComboBox(self.frame_2)
        self.input_Zahlungsart.setMinimumSize(QtCore.QSize(200, 0))
        self.input_Zahlungsart.setEditable(True)
        self.input_Zahlungsart.setObjectName(_fromUtf8("input_Zahlungsart"))
        self.horizontalLayout_3.addWidget(self.input_Zahlungsart)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(self.frame_2)
        self.label_3.setMinimumSize(QtCore.QSize(150, 0))
        self.label_3.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.input_Betrag_Brutto_E = QtGui.QLineEdit(self.frame_2)
        self.input_Betrag_Brutto_E.setMinimumSize(QtCore.QSize(200, 0))
        self.input_Betrag_Brutto_E.setMaxLength(5)
        self.input_Betrag_Brutto_E.setObjectName(_fromUtf8("input_Betrag_Brutto_E"))
        self.horizontalLayout_4.addWidget(self.input_Betrag_Brutto_E)
        self.label_6 = QtGui.QLabel(self.frame_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_4.addWidget(self.label_6)
        self.input_Betrag_Brutto_C = QtGui.QLineEdit(self.frame_2)
        self.input_Betrag_Brutto_C.setMaxLength(2)
        self.input_Betrag_Brutto_C.setObjectName(_fromUtf8("input_Betrag_Brutto_C"))
        self.horizontalLayout_4.addWidget(self.input_Betrag_Brutto_C)
        self.label_8 = QtGui.QLabel(self.frame_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_4.addWidget(self.label_8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_7 = QtGui.QLabel(self.frame_2)
        self.label_7.setMinimumSize(QtCore.QSize(150, 0))
        self.label_7.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_7.addWidget(self.label_7)
        self.input_Betrag_Netto_E = QtGui.QLineEdit(self.frame_2)
        self.input_Betrag_Netto_E.setMinimumSize(QtCore.QSize(200, 0))
        self.input_Betrag_Netto_E.setMaxLength(5)
        self.input_Betrag_Netto_E.setObjectName(_fromUtf8("input_Betrag_Netto_E"))
        self.horizontalLayout_7.addWidget(self.input_Betrag_Netto_E)
        self.label_9 = QtGui.QLabel(self.frame_2)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_7.addWidget(self.label_9)
        self.input_Betrag_Netto_C = QtGui.QLineEdit(self.frame_2)
        self.input_Betrag_Netto_C.setMaxLength(2)
        self.input_Betrag_Netto_C.setObjectName(_fromUtf8("input_Betrag_Netto_C"))
        self.horizontalLayout_7.addWidget(self.input_Betrag_Netto_C)
        self.label_10 = QtGui.QLabel(self.frame_2)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_7.addWidget(self.label_10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.line = QtGui.QFrame(self.frame_2)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_3.addWidget(self.line)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem6)
        self.frame = QtGui.QFrame(self.frame_2)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.input_anzahlPos = QtGui.QComboBox(self.frame)
        self.input_anzahlPos.setObjectName(_fromUtf8("input_anzahlPos"))
        self.input_anzahlPos.addItem(_fromUtf8(""))
        self.input_anzahlPos.addItem(_fromUtf8(""))
        self.input_anzahlPos.addItem(_fromUtf8(""))
        self.input_anzahlPos.addItem(_fromUtf8(""))
        self.input_anzahlPos.addItem(_fromUtf8(""))
        self.input_anzahlPos.addItem(_fromUtf8(""))
        self.input_anzahlPos.addItem(_fromUtf8(""))
        self.input_anzahlPos.addItem(_fromUtf8(""))
        self.input_anzahlPos.addItem(_fromUtf8(""))
        self.input_anzahlPos.addItem(_fromUtf8(""))
        self.verticalLayout_2.addWidget(self.input_anzahlPos)
        self.verticalLayout_3.addWidget(self.frame)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem7)
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(WizardPage)
        QtCore.QMetaObject.connectSlotsByName(WizardPage)

    def retranslateUi(self, WizardPage):
        WizardPage.setWindowTitle(QtGui.QApplication.translate("WizardPage", "WizardPage", None, QtGui.QApplication.UnicodeUTF8))
        WizardPage.setTitle(QtGui.QApplication.translate("WizardPage", "Belege", None, QtGui.QApplication.UnicodeUTF8))
        WizardPage.setSubTitle(QtGui.QApplication.translate("WizardPage", "Beleg erfassen", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("WizardPage", "Beleg Nr.:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_datum.setText(QtGui.QApplication.translate("WizardPage", "Datum:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("WizardPage", "Lieferant:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("WizardPage", "Zahlungsart:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("WizardPage", "Gesamtbetrag Brutto:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("WizardPage", "â‚¬", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("WizardPage", "Cent", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("WizardPage", "Gesamtbetrag Netto:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("WizardPage", "â‚¬", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("WizardPage", "Cent", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("WizardPage", "Anzahl der Artikel auswÃ¤hlen:", None, QtGui.QApplication.UnicodeUTF8))
        self.input_anzahlPos.setItemText(0, QtGui.QApplication.translate("WizardPage", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.input_anzahlPos.setItemText(1, QtGui.QApplication.translate("WizardPage", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.input_anzahlPos.setItemText(2, QtGui.QApplication.translate("WizardPage", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.input_anzahlPos.setItemText(3, QtGui.QApplication.translate("WizardPage", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.input_anzahlPos.setItemText(4, QtGui.QApplication.translate("WizardPage", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.input_anzahlPos.setItemText(5, QtGui.QApplication.translate("WizardPage", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.input_anzahlPos.setItemText(6, QtGui.QApplication.translate("WizardPage", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.input_anzahlPos.setItemText(7, QtGui.QApplication.translate("WizardPage", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.input_anzahlPos.setItemText(8, QtGui.QApplication.translate("WizardPage", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.input_anzahlPos.setItemText(9, QtGui.QApplication.translate("WizardPage", "10", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    WizardPage = QtGui.QWizardPage()
    ui = Ui_WizardPage()
    ui.setupUi(WizardPage)
    WizardPage.show()
    sys.exit(app.exec_())

