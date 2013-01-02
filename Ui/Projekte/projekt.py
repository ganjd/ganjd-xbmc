# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QWidget
from PyQt4.QtCore import pyqtSignature

from Ui_projekt import Ui_Form
from Lib.contextMenu import ContextMenu



class Projekt_Ui(QWidget, Ui_Form):

    def __init__(self):

        QWidget.__init__(self)
        self.setupUi(self)

        
        
    @pyqtSignature("QPoint")
    def on_treeWidget_customContextMenuRequested(self, pos):
        self.menu = ContextMenu(self.treeWidget)
        self.connect(self.menu.contextMenu, QtCore.SIGNAL("triggered(QAction *)"), self.contextMenuActions)
        
        if len(self.treeWidget.selectedItems()) > 0:
            self.menu.ak()
        else:
            self.menu.noSelection()
        self.menu.show(pos)
    
    @pyqtSignature("QTreeWidgetItem*, int")
    def on_treeWidget_itemDoubleClicked(self, item, column):
        self.openDetails(item)
    
    @pyqtSignature("")
    def on_toolButton_clicked(self):
        self.runWizard()

    

