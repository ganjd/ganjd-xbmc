# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'L:\Python Projekte\Galabau-2\Ui\Wizard\AKs\wizardFinalPage.ui'
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
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_Kunde = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_Kunde.setFont(font)
        self.label_Kunde.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_Kunde.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_Kunde.setObjectName(_fromUtf8("label_Kunde"))
        self.horizontalLayout_2.addWidget(self.label_Kunde)
        self.label_Projekt = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_Projekt.setFont(font)
        self.label_Projekt.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_Projekt.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_Projekt.setObjectName(_fromUtf8("label_Projekt"))
        self.horizontalLayout_2.addWidget(self.label_Projekt)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_Datum = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_Datum.setFont(font)
        self.label_Datum.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_Datum.setObjectName(_fromUtf8("label_Datum"))
        self.horizontalLayout.addWidget(self.label_Datum)
        self.label_Status = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_Status.setFont(font)
        self.label_Status.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_Status.setObjectName(_fromUtf8("label_Status"))
        self.horizontalLayout.addWidget(self.label_Status)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 754, 374))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.groupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_Start = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Start.setFont(font)
        self.label_Start.setObjectName(_fromUtf8("label_Start"))
        self.horizontalLayout_3.addWidget(self.label_Start)
        self.label_Ende = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Ende.setFont(font)
        self.label_Ende.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Ende.setObjectName(_fromUtf8("label_Ende"))
        self.horizontalLayout_3.addWidget(self.label_Ende)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label_Pause = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Pause.setFont(font)
        self.label_Pause.setObjectName(_fromUtf8("label_Pause"))
        self.verticalLayout.addWidget(self.label_Pause)
        self.label_Status_AK = QtGui.QLabel(self.groupBox)
        self.label_Status_AK.setObjectName(_fromUtf8("label_Status_AK"))
        self.verticalLayout.addWidget(self.label_Status_AK)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)

        self.retranslateUi(WizardPage)
        QtCore.QMetaObject.connectSlotsByName(WizardPage)

    def retranslateUi(self, WizardPage):
        WizardPage.setWindowTitle(QtGui.QApplication.translate("WizardPage", "WizardPage", None, QtGui.QApplication.UnicodeUTF8))
        WizardPage.setTitle(QtGui.QApplication.translate("WizardPage", "Zusammenfassung", None, QtGui.QApplication.UnicodeUTF8))
        WizardPage.setSubTitle(QtGui.QApplication.translate("WizardPage", "Alles Richtig ?", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Kunde.setText(QtGui.QApplication.translate("WizardPage", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Projekt.setText(QtGui.QApplication.translate("WizardPage", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Datum.setText(QtGui.QApplication.translate("WizardPage", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Status.setText(QtGui.QApplication.translate("WizardPage", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("WizardPage", "GroupBox", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Start.setText(QtGui.QApplication.translate("WizardPage", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Ende.setText(QtGui.QApplication.translate("WizardPage", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Pause.setText(QtGui.QApplication.translate("WizardPage", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Status_AK.setText(QtGui.QApplication.translate("WizardPage", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    WizardPage = QtGui.QWizardPage()
    ui = Ui_WizardPage()
    ui.setupUi(WizardPage)
    WizardPage.show()
    sys.exit(app.exec_())

