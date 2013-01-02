# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget
from PyQt4.QtCore import pyqtSignature

from Ui_searchWindow import Ui_Form
from Lib.kunden.filter import Filter
from Lib.tools import Tools

_fromUtf8 = QtCore.QString.fromUtf8


class Contacts(QWidget, Ui_Form):

    def __init__(self, Parent):

        QWidget.__init__(self)
        self.setupUi(self)
        self.parent = Parent
        self.tools = Tools()
        self.loadTreeWidget()
        
        
    
    @pyqtSignature("QString")
    def on_lineEdit_textChanged(self, p0):
        print p0

    
    @pyqtSignature("QTreeWidgetItem*, int")
    def on_treeWidget_itemDoubleClicked(self, item, column):
        kunde = item.data(0, 32).toPyObject()
        self.parent.setContact(kunde)
        self.close()

        
    @pyqtSignature("QTreeWidgetItem*, QTreeWidgetItem*")
    def on_treeWidget_currentItemChanged(self, current, previous):
        self.kunde = current.data(0, 32).toPyObject()

        

    
    @pyqtSignature("")
    def on_pushButton_apply_clicked(self):
        self.parent.setContact(self.kunde)
        self.close()
        
    
    @pyqtSignature("")
    def on_pushButton_cancel_clicked(self):
        self.close()
        
    @pyqtSignature("")
    def on_pushButton_newKunde_clicked(self):
        from Ui.Wizard.wizard import Wizard
        self.wizard = Wizard('Kunde')

 

    def loadTreeWidget(self):
        self.treeWidget.clear()
        
        self.filter = Filter()
        sqlResult = self.filter.getResult()

        for entry in sqlResult:
            item= QtGui.QTreeWidgetItem()
            item.setData(0, 32, QtCore.QVariant(entry))

            item.setText(0, str(entry.nr))
            item.setText(1, entry.firma)
            item.setText(2, entry.nachname)
            item.setText(3, entry.vorname)
            item.setText(4, entry.strasse)
            item.setText(5, entry.plz+' '+entry.ort)
    
            for i in range(0, 6):
                    item.setFont(i, QtGui.QFont('Helvetica', 10))
                
            self.treeWidget.addTopLevelItem(item)

