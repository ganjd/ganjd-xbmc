# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'L:\Python Projekte\Galabau-2\Ui\Setting_Widgets\datenbank.ui'
#
# Created: Thu Oct 11 00:38:12 2012
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
        Form.resize(588, 355)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.widget = QtGui.QWidget(Form)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.line = QtGui.QFrame(self.widget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.verticalLayout_3.addWidget(self.widget)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.toolButton = QtGui.QToolButton(self.groupBox)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.horizontalLayout.addWidget(self.toolButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addWidget(self.groupBox)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.commandLinkButton_neu = QtGui.QCommandLinkButton(Form)
        self.commandLinkButton_neu.setAutoRepeat(False)
        self.commandLinkButton_neu.setAutoDefault(False)
        self.commandLinkButton_neu.setDefault(False)
        self.commandLinkButton_neu.setDescription(_fromUtf8("Erzeugt eine leere Datenbank"))
        self.commandLinkButton_neu.setObjectName(_fromUtf8("commandLinkButton_neu"))
        self.verticalLayout_3.addWidget(self.commandLinkButton_neu)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.toolButton_hide = QtGui.QToolButton(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/res/1326055942_emblem-nowrite.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_hide.setIcon(icon)
        self.toolButton_hide.setIconSize(QtCore.QSize(10, 10))
        self.toolButton_hide.setAutoRaise(True)
        self.toolButton_hide.setObjectName(_fromUtf8("toolButton_hide"))
        self.horizontalLayout_4.addWidget(self.toolButton_hide)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lineEdit_path_new = QtGui.QLineEdit(Form)
        self.lineEdit_path_new.setReadOnly(True)
        self.lineEdit_path_new.setObjectName(_fromUtf8("lineEdit_path_new"))
        self.horizontalLayout_3.addWidget(self.lineEdit_path_new)
        self.toolButton_2 = QtGui.QToolButton(Form)
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.horizontalLayout_3.addWidget(self.toolButton_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.commandLinkButton_create = QtGui.QCommandLinkButton(Form)
        self.commandLinkButton_create.setObjectName(_fromUtf8("commandLinkButton_create"))
        self.horizontalLayout_2.addWidget(self.commandLinkButton_create)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        self.label.setText(QtGui.QApplication.translate("Form", "Datenbank Einstellungen", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "Verzeichnis", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.commandLinkButton_neu.setText(QtGui.QApplication.translate("Form", "Neue Datenbank", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_hide.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Verzeichnis fÃ¼r neue Datenbank wÃ¤hlen:", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_2.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.commandLinkButton_create.setText(QtGui.QApplication.translate("Form", "Erstellen", None, QtGui.QApplication.UnicodeUTF8))

import res_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

