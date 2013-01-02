# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget
from PyQt4.QtCore import pyqtSignature

from Ui_arbeiter import Ui_Form

from Lib.loadSettings import LoadSettings

IDENTIFYER = 'Arbeiter'


_fromUtf8 = QtCore.QString.fromUtf8


class Settings_Arbeiter(QWidget, Ui_Form):

    def __init__(self, parent = None):

        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.identifyer = IDENTIFYER
        
        self.setWerte()
        
    def setWerte(self):
        self.loadWerte()
        
        for entry in self.arbeiter:
            item = QtGui.QListWidgetItem()
            item.setText(entry)
            self.listWidget.addItem(item)
        
        
    def getWerte(self):
        arbeiter = ''
        for i in range(0, self.listWidget.count()):
            arbeiter = arbeiter+self.listWidget.item(i).text()+'|'
        arbeiter = arbeiter[:-1]
        
        werte = [arbeiter]
        return werte
        
        
    def loadWerte(self):
        self.arbeiter = LoadSettings().arbeiter()
    
    @pyqtSignature("QString")
    def on_lineEdit_textChanged(self, newArbeiter):
        if len(newArbeiter) > 0:
            self.newArbeiter = newArbeiter
            self.toolButton_add.setEnabled(True)
        else:
            self.toolButton_add.setEnabled(False)

    
    @pyqtSignature("")
    def on_toolButton_add_clicked(self):
        reply = QtGui.QMessageBox.question(self, _fromUtf8('Hinzufügen'), _fromUtf8('Sollen "'+self.newArbeiter+'" zur Arbeiterliste hinzugefügt werden ?'), 'Ja', 'Nein')
        if reply == 0:
            self.listWidget.addItem(QtGui.QListWidgetItem(self.newArbeiter))
        self.lineEdit.setText('')



    
    @pyqtSignature("")
    def on_toolButton_del_clicked(self):
        reply = QtGui.QMessageBox.question(self, _fromUtf8('Hinzufügen'), _fromUtf8('Sollen "'+self.currentArbeiter.text()+'" von der Arbeiterliste gelöscht werden ?'), 'Ja', 'Nein')
        if reply == 0:
            self.listWidget.takeItem(self.listWidget.currentRow())

    
    @pyqtSignature("")
    def on_toolButton_edit_clicked(self):
        print 'edit '
        self.listWidget.openPersistentEditor(self.currentArbeiter)

    
    @pyqtSignature("QListWidgetItem*")
    def on_listWidget_itemClicked(self, item):
        try:
            self.listWidget.closePersistentEditor(self.currentArbeiter)
        except:
            pass
        self.currentArbeiter = item
        self.toolButton_del.setEnabled(True)
        self.toolButton_edit.setEnabled(True)

