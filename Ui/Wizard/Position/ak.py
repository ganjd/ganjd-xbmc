# -*- coding: utf-8 -*-

from PyQt4.QtCore import QString
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QWidget
from PyQt4.QtCore import pyqtSignature

from Ui_ak import Ui_Form

_fromUtf8 = QString.fromUtf8


class Arbeiter(QWidget, Ui_Form):

    def __init__(self, Parent, GroupBoxTitle, Id):

        QWidget.__init__(self)
        self.setupUi(self)
        self.parent = Parent
        self.groupBox.setTitle(_fromUtf8(GroupBoxTitle))
        
        self.id = str(Id)
        self.setStyle()
        

    
    @pyqtSignature("QString")
    def on_comboBox_activated(self, p0):
        exec 'self.parent.stunden_' + self.id + '= p0'

    
    @pyqtSignature("QString")
    def on_comboBox_2_activated(self, p0):
        exec 'self.parent.minuten_' + self.id + '= p0'

        
        
    def setStyle(self):
        a = QtGui.QStyleFactory.keys()[5]
        b = QtGui.QStyleFactory.create(a)
        self.comboBox.setStyle(b)
        self.comboBox_2.setStyle(b)
