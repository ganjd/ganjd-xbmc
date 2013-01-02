# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'L:\Python Projekte\Galabau-2\Ui\Arbeitsstunden\aStd.ui'
#
# Created: Mon Oct 15 11:09:40 2012
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
        Form.resize(577, 439)
        Form.setAutoFillBackground(False)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Impact"))
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setWordWrap(True)
        self.label.setMargin(0)
        self.label.setIndent(5)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.comboBox_filter = QtGui.QComboBox(Form)
        self.comboBox_filter.setMinimumSize(QtCore.QSize(150, 0))
        self.comboBox_filter.setObjectName(_fromUtf8("comboBox_filter"))
        self.horizontalLayout_3.addWidget(self.comboBox_filter)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.toolButton_show_2 = QtGui.QToolButton(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/res/1314482878_br_up.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_show_2.setIcon(icon)
        self.toolButton_show_2.setIconSize(QtCore.QSize(16, 10))
        self.toolButton_show_2.setObjectName(_fromUtf8("toolButton_show_2"))
        self.horizontalLayout_2.addWidget(self.toolButton_show_2)
        self.toolButton_hide_2 = QtGui.QToolButton(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/res/1314470636_br_down.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_hide_2.setIcon(icon1)
        self.toolButton_hide_2.setIconSize(QtCore.QSize(16, 10))
        self.toolButton_hide_2.setObjectName(_fromUtf8("toolButton_hide_2"))
        self.horizontalLayout_2.addWidget(self.toolButton_hide_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.treeWidget = QtGui.QTreeWidget(Form)
        self.treeWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.treeWidget.setRootIsDecorated(False)
        self.treeWidget.setItemsExpandable(False)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.header().setCascadingSectionResizes(True)
        self.treeWidget.header().setDefaultSectionSize(250)
        self.treeWidget.header().setSortIndicatorShown(True)
        self.verticalLayout_2.addWidget(self.treeWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.toolButton_show = QtGui.QToolButton(Form)
        self.toolButton_show.setIcon(icon)
        self.toolButton_show.setIconSize(QtCore.QSize(16, 10))
        self.toolButton_show.setObjectName(_fromUtf8("toolButton_show"))
        self.horizontalLayout.addWidget(self.toolButton_show)
        self.toolButton_hide = QtGui.QToolButton(Form)
        self.toolButton_hide.setIcon(icon1)
        self.toolButton_hide.setIconSize(QtCore.QSize(16, 10))
        self.toolButton_hide.setObjectName(_fromUtf8("toolButton_hide"))
        self.horizontalLayout.addWidget(self.toolButton_hide)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_2.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Arbeitsstunden", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_show_2.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_hide_2.setStatusTip(QtGui.QApplication.translate("Form", "Verstecken", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_hide_2.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.setSortingEnabled(True)
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("Form", "Datum", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(1, QtGui.QApplication.translate("Form", "Kunde", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(2, QtGui.QApplication.translate("Form", "Projekt", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(3, QtGui.QApplication.translate("Form", "Anzahl Arbeiter", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(4, QtGui.QApplication.translate("Form", "Stunden", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(5, QtGui.QApplication.translate("Form", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_show.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_hide.setStatusTip(QtGui.QApplication.translate("Form", "Verstecken", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_hide.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "GroupBox", None, QtGui.QApplication.UnicodeUTF8))

import res_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

