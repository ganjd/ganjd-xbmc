# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QWidget
from PyQt4.QtCore import pyqtSignature

from Ui_kunden import Ui_Form
from Lib.contextMenu import ContextMenu


class Kunden_Ui(QWidget, Ui_Form):

    def __init__(self):

        QWidget.__init__(self)
        self.setupUi(self)
        
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 100, 500))

        
    
    @pyqtSignature("QString")
    def on_comboBox_filter_activated(self, p0):
        pass

    
    @pyqtSignature("QPoint")
    def on_treeWidget_customContextMenuRequested(self, pos):
        self.menu = ContextMenu(self.treeWidget)
        self.connect(self.menu.contextMenu, QtCore.SIGNAL("triggered(QAction *)"), self.contextMenuActions)
        
        if len(self.treeWidget.selectedItems()) > 0:
            self.menu.kunden()
        else:
            self.menu.noSelection()
        self.menu.show(pos)

    
    @pyqtSignature("")
    def on_toolButton_show_clicked(self):
        self.widget_2.show()
        self.toolButton_show.hide()
        self.toolButton_hide.show()
    
    @pyqtSignature("")
    def on_toolButton_hide_clicked(self):
        self.widget_2.hide()
        self.toolButton_show.show()
        self.toolButton_hide.hide()
        
    
#    @pyqtSignature("QTreeWidgetItem*, int")
#    def on_treeWidget_itemClicked(self, item, column):
#        self.setDetails(item)
#        self.setAuftrag(item)
    
    
#    @pyqtSignature("")
#    def on_treeWidget_itemSelectionChanged(self):    
#        self.setDetails(item)
#        self.setAuftrag(item)
        
        
    @pyqtSignature("")
    def on_toolButton_new_clicked(self):
        self.runWizard()
    
    @pyqtSignature("QTreeWidgetItem*, QTreeWidgetItem*")
    def on_treeWidget_currentItemChanged(self, current, previous):
        if current != None:
            self.setDetails(current)
            self.setAuftrag(current)

