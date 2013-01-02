# -*- coding: utf-8 -*-

from PyQt4.QtGui import QMenu
from PyQt4.QtGui import QAction
from PyQt4 import QtCore

_fromUtf8 = QtCore.QString.fromUtf8

class ContextMenu:
    
    def __init__(self, slot):
        
        self.slot = slot
        self.contextMenu = QMenu(slot)

    
    def ak(self):
        self.contextMenu.addAction(_fromUtf8('Aktualisieren'))
        self.contextMenu.addAction(_fromUtf8('Bearbeiten'))
        self.contextMenu.addAction(_fromUtf8('Status ändern'))
        self.contextMenu.addSeparator()
        self.contextMenu.addAction(_fromUtf8('Löschen'))
        
    def kunden(self):
        self.contextMenu.addAction(_fromUtf8('Aktualisieren'))
        self.contextMenu.addAction(_fromUtf8('Bearbeiten'))
        self.contextMenu.addSeparator()
        self.contextMenu.addAction(_fromUtf8('Löschen'))
        
        
    def projekt_as(self):
        
        action = QAction(_fromUtf8('Aktualisieren'), self.slot)
        action.setDisabled(False)
        action.setData(QtCore.QVariant('update'))
        self.contextMenu.addAction(action) 
        
        self.contextMenu.addSeparator()
        
        submenu = self.contextMenu.addMenu(_fromUtf8('Positionen'))
        
        action = QAction(_fromUtf8('Anzeigen'), self.slot)
        action.setDisabled(True)
        submenu.addAction(action)
        
        submenu.addSeparator()
        
        action = QAction(_fromUtf8('Hinzufügen'), self.slot)
        action.setDisabled(False)
        action.setData(QtCore.QVariant('PosAdd'))
        submenu.addAction(action)
        
        action = QAction(_fromUtf8('Bearbeiten'), self.slot)
        action.setDisabled(True)
        submenu.addAction(action)
        
        action = QAction(_fromUtf8('Löschen'), self.slot)
        action.setDisabled(True)
        submenu.addAction(action)
        
        action = QAction(_fromUtf8('Ändern'), self.slot)
        action.setDisabled(False)
        action.setData(QtCore.QVariant('edit'))
        self.contextMenu.addAction(action)
        
        action = QAction(_fromUtf8('Löschen'), self.slot)
        action.setDisabled(False)
        action.setData(QtCore.QVariant('delete'))
        self.contextMenu.addAction(action)

    
    def projekt_as_PosEdit(self):
        self.contextMenu.addAction(_fromUtf8('Aktualisieren'))        
        self.contextMenu.addSeparator()

        submenu = self.contextMenu.addMenu(_fromUtf8('Positionen'))
        
        action = QAction(_fromUtf8('Anzeigen'), self.slot)
        action.setDisabled(False)
        action.setData(QtCore.QVariant('PosShow'))
        submenu.addAction(action)
        
        submenu.addSeparator()
        
        action = QAction(_fromUtf8('Hinzufügen'), self.slot)
        action.setDisabled(True)
        submenu.addAction(action)
        
        action = QAction(_fromUtf8('Bearbeiten'), self.slot)
        action.setDisabled(False)
        action.setData(QtCore.QVariant('PosEdit'))
        submenu.addAction(action)
        
        action = QAction(_fromUtf8('Löschen'), self.slot)
        action.setDisabled(False)
        action.setData(QtCore.QVariant('PosDel'))
        submenu.addAction(action)
        
    def projekt_material(self):
        action = QAction(_fromUtf8('Aktualisieren'), self.slot)
        action.setDisabled(False)
        action.setData(QtCore.QVariant('Refresh'))
        self.contextMenu.addAction(action)
        
        action = QAction(_fromUtf8('Zu Beleg gehen'), self.slot)
        action.setDisabled(False)
        action.setData(QtCore.QVariant('ZuBeleg'))
        self.contextMenu.addAction(action)
        
        action = QAction(_fromUtf8('Status ändern'), self.slot)
        action.setDisabled(False)
        action.setData(QtCore.QVariant('StatusEdit'))
        self.contextMenu.addAction(action)
        
    
    def belege(self):
        action = QAction(_fromUtf8('Aktualisieren'), self.slot)
        action.setDisabled(False)
        action.setData(QtCore.QVariant('Refresh'))
        self.contextMenu.addAction(action)
        
        action = QAction(_fromUtf8('Ändern'), self.slot)
        action.setDisabled(False)
        action.setData(QtCore.QVariant('Edit'))
        self.contextMenu.addAction(action)
        
        self.contextMenu.addSeparator()
        
        action = QAction(_fromUtf8('Löschen'), self.slot)
        action.setDisabled(False)
        action.setData(QtCore.QVariant('Del'))
        self.contextMenu.addAction(action)
        


    def noSelection(self):
        self.contextMenu.addAction(_fromUtf8('Aktualisieren'))
        
        
    def show(self, Point):
        self.contextMenu.exec_(self.slot.mapToGlobal(Point))
