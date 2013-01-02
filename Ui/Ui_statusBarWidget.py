# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'L:\Python Projekte\Galabau-2\Ui\statusBarWidget.ui'
#
# Created: Thu Oct 11 00:38:06 2012
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
        Form.resize(548, 38)
        Form.setMaximumSize(QtCore.QSize(16777215, 38))
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_info = QtGui.QLabel(Form)
        self.label_info.setObjectName(_fromUtf8("label_info"))
        self.horizontalLayout.addWidget(self.label_info)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_jahr = QtGui.QLabel(Form)
        self.label_jahr.setObjectName(_fromUtf8("label_jahr"))
        self.horizontalLayout.addWidget(self.label_jahr)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_user = QtGui.QLabel(Form)
        self.label_user.setObjectName(_fromUtf8("label_user"))
        self.horizontalLayout.addWidget(self.label_user)
        spacerItem2 = QtGui.QSpacerItem(40, 15, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label_online = QtGui.QLabel(Form)
        self.label_online.setMaximumSize(QtCore.QSize(15, 15))
        self.label_online.setText(_fromUtf8(""))
        self.label_online.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/res/Status-user-online-icon.png")))
        self.label_online.setScaledContents(True)
        self.label_online.setObjectName(_fromUtf8("label_online"))
        self.horizontalLayout.addWidget(self.label_online)
        self.label_offline = QtGui.QLabel(Form)
        self.label_offline.setMaximumSize(QtCore.QSize(15, 15))
        self.label_offline.setText(_fromUtf8(""))
        self.label_offline.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/res/Status-user-offline-icon.png")))
        self.label_offline.setScaledContents(True)
        self.label_offline.setObjectName(_fromUtf8("label_offline"))
        self.horizontalLayout.addWidget(self.label_offline)
        self.label_text = QtGui.QLabel(Form)
        self.label_text.setObjectName(_fromUtf8("label_text"))
        self.horizontalLayout.addWidget(self.label_text)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_info.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_jahr.setText(QtGui.QApplication.translate("Form", "Jahr:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_user.setText(QtGui.QApplication.translate("Form", "Benutzer:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_text.setText(QtGui.QApplication.translate("Form", "Verbunden", None, QtGui.QApplication.UnicodeUTF8))

import res_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

