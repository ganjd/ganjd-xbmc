# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'L:\Python Projekte\Galabau-2\Ui\Projekte\details.ui'
#
# Created: Tue Oct 16 12:17:26 2012
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
        Form.resize(873, 617)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.toolButton = QtGui.QToolButton(Form)
        self.toolButton.setMinimumSize(QtCore.QSize(110, 50))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/res/1318969217_stock_new-window.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(40, 25))
        self.toolButton.setPopupMode(QtGui.QToolButton.DelayedPopup)
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton.setAutoRaise(True)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.horizontalLayout.addWidget(self.toolButton)
        self.toolButton_ansicht = QtGui.QToolButton(Form)
        self.toolButton_ansicht.setMinimumSize(QtCore.QSize(110, 50))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/res/1318972409_view_detailed.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_ansicht.setIcon(icon1)
        self.toolButton_ansicht.setIconSize(QtCore.QSize(40, 25))
        self.toolButton_ansicht.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_ansicht.setAutoRaise(True)
        self.toolButton_ansicht.setObjectName(_fromUtf8("toolButton_ansicht"))
        self.horizontalLayout.addWidget(self.toolButton_ansicht)
        self.toolButton_pos = QtGui.QToolButton(Form)
        self.toolButton_pos.setMinimumSize(QtCore.QSize(110, 50))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/res/1318968719_x-office-spreadsheet.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_pos.setIcon(icon2)
        self.toolButton_pos.setIconSize(QtCore.QSize(40, 25))
        self.toolButton_pos.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_pos.setAutoRaise(True)
        self.toolButton_pos.setObjectName(_fromUtf8("toolButton_pos"))
        self.horizontalLayout.addWidget(self.toolButton_pos)
        self.toolButton_ak = QtGui.QToolButton(Form)
        self.toolButton_ak.setMinimumSize(QtCore.QSize(110, 50))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/res/group.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_ak.setIcon(icon3)
        self.toolButton_ak.setIconSize(QtCore.QSize(40, 25))
        self.toolButton_ak.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_ak.setAutoRaise(True)
        self.toolButton_ak.setObjectName(_fromUtf8("toolButton_ak"))
        self.horizontalLayout.addWidget(self.toolButton_ak)
        self.toolButton_beleg = QtGui.QToolButton(Form)
        self.toolButton_beleg.setMinimumSize(QtCore.QSize(110, 50))
        self.toolButton_beleg.setIcon(icon3)
        self.toolButton_beleg.setIconSize(QtCore.QSize(40, 25))
        self.toolButton_beleg.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_beleg.setAutoRaise(True)
        self.toolButton_beleg.setObjectName(_fromUtf8("toolButton_beleg"))
        self.horizontalLayout.addWidget(self.toolButton_beleg)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.toolButton_switch = QtGui.QToolButton(Form)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/res/1318968775_stock_mail-filters-apply.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_switch.setIcon(icon4)
        self.toolButton_switch.setIconSize(QtCore.QSize(16, 16))
        self.toolButton_switch.setCheckable(False)
        self.toolButton_switch.setChecked(False)
        self.toolButton_switch.setAutoRepeat(False)
        self.toolButton_switch.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_switch.setAutoRaise(True)
        self.toolButton_switch.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_switch.setObjectName(_fromUtf8("toolButton_switch"))
        self.horizontalLayout.addWidget(self.toolButton_switch)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_3.addWidget(self.line)
        self.widget_main = QtGui.QWidget(Form)
        self.widget_main.setObjectName(_fromUtf8("widget_main"))
        self.verticalLayout_main = QtGui.QVBoxLayout(self.widget_main)
        self.verticalLayout_main.setSpacing(0)
        self.verticalLayout_main.setMargin(0)
        self.verticalLayout_main.setMargin(0)
        self.verticalLayout_main.setObjectName(_fromUtf8("verticalLayout_main"))
        self.frame_material = QtGui.QFrame(self.widget_main)
        self.frame_material.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_material.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_material.setObjectName(_fromUtf8("frame_material"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_material)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_2 = QtGui.QLabel(self.frame_material)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_4.addWidget(self.label_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.toolButton_filter = QtGui.QToolButton(self.frame_material)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/res/filter_data.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_filter.setIcon(icon5)
        self.toolButton_filter.setCheckable(True)
        self.toolButton_filter.setAutoExclusive(False)
        self.toolButton_filter.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_filter.setAutoRaise(True)
        self.toolButton_filter.setObjectName(_fromUtf8("toolButton_filter"))
        self.horizontalLayout_7.addWidget(self.toolButton_filter)
        self.frame_filter = QtGui.QFrame(self.frame_material)
        self.frame_filter.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_filter.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_filter.setObjectName(_fromUtf8("frame_filter"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.frame_filter)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.label_3 = QtGui.QLabel(self.frame_filter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_6.addWidget(self.label_3)
        self.comboBox_filter_art = QtGui.QComboBox(self.frame_filter)
        self.comboBox_filter_art.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBox_filter_art.setObjectName(_fromUtf8("comboBox_filter_art"))
        self.comboBox_filter_art.addItem(_fromUtf8(""))
        self.comboBox_filter_art.addItem(_fromUtf8(""))
        self.comboBox_filter_art.addItem(_fromUtf8(""))
        self.comboBox_filter_art.addItem(_fromUtf8(""))
        self.horizontalLayout_6.addWidget(self.comboBox_filter_art)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.label_10 = QtGui.QLabel(self.frame_filter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_6.addWidget(self.label_10)
        self.comboBox_filter_string = QtGui.QComboBox(self.frame_filter)
        self.comboBox_filter_string.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBox_filter_string.setObjectName(_fromUtf8("comboBox_filter_string"))
        self.horizontalLayout_6.addWidget(self.comboBox_filter_string)
        self.horizontalLayout_7.addWidget(self.frame_filter)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.treeWidget_2 = QtGui.QTreeWidget(self.frame_material)
        self.treeWidget_2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeWidget_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.treeWidget_2.setRootIsDecorated(False)
        self.treeWidget_2.setObjectName(_fromUtf8("treeWidget_2"))
        self.treeWidget_2.headerItem().setText(3, _fromUtf8("Lieferant"))
        self.treeWidget_2.header().setDefaultSectionSize(250)
        self.treeWidget_2.header().setSortIndicatorShown(True)
        self.verticalLayout_2.addWidget(self.treeWidget_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_7 = QtGui.QLabel(self.frame_material)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_3.addWidget(self.label_7)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.label_8 = QtGui.QLabel(self.frame_material)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_3.addWidget(self.label_8)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.label_9 = QtGui.QLabel(self.frame_material)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_3.addWidget(self.label_9)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_main.addWidget(self.frame_material)
        self.line_3 = QtGui.QFrame(self.widget_main)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout_main.addWidget(self.line_3)
        self.frame_as = QtGui.QFrame(self.widget_main)
        self.frame_as.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_as.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_as.setObjectName(_fromUtf8("frame_as"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frame_as)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label = QtGui.QLabel(self.frame_as)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_5.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.treeWidget = QtGui.QTreeWidget(self.frame_as)
        self.treeWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeWidget.setFrameShape(QtGui.QFrame.NoFrame)
        self.treeWidget.setRootIsDecorated(False)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.headerItem().setText(0, _fromUtf8("Datum"))
        self.treeWidget.header().setDefaultSectionSize(200)
        self.treeWidget.header().setSortIndicatorShown(True)
        self.verticalLayout.addWidget(self.treeWidget)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_4 = QtGui.QLabel(self.frame_as)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.label_5 = QtGui.QLabel(self.frame_as)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_2.addWidget(self.label_5)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.label_6 = QtGui.QLabel(self.frame_as)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_2.addWidget(self.label_6)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_main.addWidget(self.frame_as)
        self.verticalLayout_3.addWidget(self.widget_main)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton.setText(QtGui.QApplication.translate("Form", "      Neu      ", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_ansicht.setText(QtGui.QApplication.translate("Form", "Ansicht", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_pos.setText(QtGui.QApplication.translate("Form", "Positionen anzeigen", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_ak.setText(QtGui.QApplication.translate("Form", "Arbeiter", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_beleg.setText(QtGui.QApplication.translate("Form", "Belege", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_switch.setText(QtGui.QApplication.translate("Form", "Material", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Material", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_filter.setText(QtGui.QApplication.translate("Form", "Filtern", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "nach:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_filter_art.setItemText(0, QtGui.QApplication.translate("Form", "Datum", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_filter_art.setItemText(1, QtGui.QApplication.translate("Form", "Lieferant", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_filter_art.setItemText(2, QtGui.QApplication.translate("Form", "Zahlungsart", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_filter_art.setItemText(3, QtGui.QApplication.translate("Form", "Bezeichnung", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Form", "Datum", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_2.headerItem().setText(0, QtGui.QApplication.translate("Form", "Datum", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_2.headerItem().setText(1, QtGui.QApplication.translate("Form", "Bezeichnung", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_2.headerItem().setText(2, QtGui.QApplication.translate("Form", "Menge", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_2.headerItem().setText(4, QtGui.QApplication.translate("Form", "Zahlungsart", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_2.headerItem().setText(5, QtGui.QApplication.translate("Form", "Betrag", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_2.headerItem().setText(6, QtGui.QApplication.translate("Form", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Arbeitsstunden", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(1, QtGui.QApplication.translate("Form", "Anzahl Arbeiter", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(2, QtGui.QApplication.translate("Form", "Stunden", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(3, QtGui.QApplication.translate("Form", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

import res_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

