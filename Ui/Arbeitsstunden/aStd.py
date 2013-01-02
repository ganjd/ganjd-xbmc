# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QWidget
from PyQt4.QtCore import pyqtSignature

from Ui_aStd import Ui_Form

from Lib.tools import Tools
from Lib.contextMenu import ContextMenu


class AStd_Ui(QWidget, Ui_Form):
    def __init__(self):

        QWidget.__init__(self)
        self.setupUi(self)
        
        self.tools = Tools()
        
        self.groupBox.setTitle('Alle')
        self.toolButton_show.hide()
        self.toolButton_show_2.hide()
        self.setStyle()
        
        
    @pyqtSignature("int")
    def on_comboBox_filter_activated(self, index):
        filter_string = self.comboBox_filter.itemData(index).toPyObject()
        if filter_string == 'Alle':
            self.loadFilter('Alle')
        else:
            self.loadFilter('Kunde', filter_string)
        self.groupBox.setTitle(self.comboBox_filter.itemText(index))


    
    @pyqtSignature("")
    def on_toolButton_show_clicked(self):
        self.groupBox.show()
        self.toolButton_show.hide()
        self.toolButton_hide.show()
        self.toolButton_hide_2.show()

    
    @pyqtSignature("")
    def on_toolButton_hide_clicked(self):
        self.groupBox.hide()
        self.toolButton_show.show()
        self.toolButton_hide.hide()
        self.toolButton_hide_2.hide()
        
        
    def setStyle(self):
        a = QtGui.QStyleFactory.keys()[5]
        b = QtGui.QStyleFactory.create(a)
        self.comboBox_filter.setStyle(b)
        
    
    @pyqtSignature("")
    def on_toolButton_show_2_clicked(self):
        self.treeWidget.show()
        self.toolButton_show_2.hide()
        self.toolButton_hide_2.show()
        self.toolButton_hide.show()

    
    @pyqtSignature("")
    def on_toolButton_hide_2_clicked(self):
        self.treeWidget.hide()
        self.toolButton_show_2.show()
        self.toolButton_hide_2.hide()
        self.toolButton_hide.hide()

