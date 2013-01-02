# -*- coding: utf-8 -*-


from PyQt4 import QtGui
from PyQt4.QtCore import QString
from PyQt4.QtGui import QWidget
from PyQt4.QtCore import pyqtSignature

from Ui_ak_Final import Ui_Form

_fromUtf8 = QString.fromUtf8


class Ak_Final(QWidget, Ui_Form):

    def __init__(self, GroupBoxTitle, Detail_List):

        QWidget.__init__(self)
        self.setupUi(self)
        
        self.groupBoxTitle = GroupBoxTitle
        self.detail_List = Detail_List
        
        self.setUi()
        
    
    def setUi(self):
        self.groupBox.setTitle(_fromUtf8('Position Nr. '+ self.groupBoxTitle))
        
        for entry in self.detail_List:

            self.plainTextEdit.setPlainText(_fromUtf8(entry[0]))
            
            font_label = QtGui.QFont()
            font_label.setPointSize(10)
            font_label.setBold(False)
            
            horizontalLayout = QtGui.QHBoxLayout()
            label = QtGui.QLabel(self.frame)
            label.setText(_fromUtf8(entry[1]))
            label.setFont(font_label)
            horizontalLayout.addWidget(label)
            label_zeit = QtGui.QLabel(self.frame)
            label_zeit.setText(_fromUtf8(entry[2]+':'+entry[3]+'  Stunden'))
            label_zeit.setFont(font_label)
            horizontalLayout.addWidget(label_zeit)
            self.verticalLayout.addLayout(horizontalLayout)
            
