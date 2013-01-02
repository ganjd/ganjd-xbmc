# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'L:\Python Projekte\Galabau-2\Ui\Wizard\Projects\wizardFinalPage.ui'
#
# Created: Thu Oct 11 00:38:18 2012
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
        WizardPage.resize(772, 505)
        self.verticalLayout_3 = QtGui.QVBoxLayout(WizardPage)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.frame = QtGui.QFrame(WizardPage)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_Projektnr = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_Projektnr.setFont(font)
        self.label_Projektnr.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_Projektnr.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_Projektnr.setObjectName(_fromUtf8("label_Projektnr"))
        self.verticalLayout_2.addWidget(self.label_Projektnr)
        self.label_Projektname = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_Projektname.setFont(font)
        self.label_Projektname.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_Projektname.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_Projektname.setObjectName(_fromUtf8("label_Projektname"))
        self.verticalLayout_2.addWidget(self.label_Projektname)
        self.label_Kunde = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_Kunde.setFont(font)
        self.label_Kunde.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_Kunde.setObjectName(_fromUtf8("label_Kunde"))
        self.verticalLayout_2.addWidget(self.label_Kunde)
        self.label_Status = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_Status.setFont(font)
        self.label_Status.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_Status.setObjectName(_fromUtf8("label_Status"))
        self.verticalLayout_2.addWidget(self.label_Status)
        self.verticalLayout_3.addWidget(self.frame)
        self.line = QtGui.QFrame(WizardPage)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_3.addWidget(self.line)
        self.scrollArea = QtGui.QScrollArea(WizardPage)
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 754, 310))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.groupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.plainTextEdit_Beschreibung = QtGui.QPlainTextEdit(self.groupBox)
        self.plainTextEdit_Beschreibung.setFrameShape(QtGui.QFrame.NoFrame)
        self.plainTextEdit_Beschreibung.setTabChangesFocus(False)
        self.plainTextEdit_Beschreibung.setDocumentTitle(_fromUtf8(""))
        self.plainTextEdit_Beschreibung.setReadOnly(True)
        self.plainTextEdit_Beschreibung.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.plainTextEdit_Beschreibung.setBackgroundVisible(False)
        self.plainTextEdit_Beschreibung.setCenterOnScroll(False)
        self.plainTextEdit_Beschreibung.setObjectName(_fromUtf8("plainTextEdit_Beschreibung"))
        self.verticalLayout.addWidget(self.plainTextEdit_Beschreibung)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)

        self.retranslateUi(WizardPage)
        QtCore.QMetaObject.connectSlotsByName(WizardPage)

    def retranslateUi(self, WizardPage):
        WizardPage.setWindowTitle(QtGui.QApplication.translate("WizardPage", "WizardPage", None, QtGui.QApplication.UnicodeUTF8))
        WizardPage.setTitle(QtGui.QApplication.translate("WizardPage", "Zusammenfassung", None, QtGui.QApplication.UnicodeUTF8))
        WizardPage.setSubTitle(QtGui.QApplication.translate("WizardPage", "Alles Richtig ?", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Projektnr.setText(QtGui.QApplication.translate("WizardPage", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Projektname.setText(QtGui.QApplication.translate("WizardPage", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Kunde.setText(QtGui.QApplication.translate("WizardPage", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Status.setText(QtGui.QApplication.translate("WizardPage", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("WizardPage", "Beschreibung", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    WizardPage = QtGui.QWizardPage()
    ui = Ui_WizardPage()
    ui.setupUi(WizardPage)
    WizardPage.show()
    sys.exit(app.exec_())

