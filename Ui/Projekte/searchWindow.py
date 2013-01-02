# -*- coding: utf-8 -*-

import os
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget
from PyQt4.QtCore import pyqtSignature

from Ui_searchWindow import Ui_Form



from Lib.loadSettings import LoadSettings


_fromUtf8 = QtCore.QString.fromUtf8


class SearchProject(QWidget, Ui_Form):

    def __init__(self, Parent):
        QWidget.__init__(self)
        self.setupUi(self)
        self.parent = Parent
        
        self.loadSettings = LoadSettings()
        self.loadTreeWidget()
        self.pushButton_apply.setEnabled(False)
        
    
    @pyqtSignature("")
    def on_pushButton_newProject_clicked(self):
        from Ui.Wizard.wizard import Wizard
        self.wizard = Wizard('Project')

    
    @pyqtSignature("")
    def on_pushButton_apply_clicked(self):
        self.parent.setProject(self.projectString, self.projektData)
        self.close()


    
    @pyqtSignature("")
    def on_pushButton_cancel_clicked(self):
        self.close()


    
    @pyqtSignature("QTreeWidgetItem*, int")
    def on_treeWidget_itemDoubleClicked(self, item, column):
        projektData = item.text(0)
        projectString = item.text(1)
        self.parent.setProject(projectString, projektData)
        self.close()


    
    @pyqtSignature("QTreeWidgetItem*, QTreeWidgetItem*")
    def on_treeWidget_currentItemChanged(self, current, previous):
        self.pushButton_apply.setEnabled(True)
        self.projektData = current.text(0)
        self.projectString = current.text(1)

    
        
    def loadTreeWidget(self):
        self.treeWidget.clear()
        
        self.sqllite.connect(self.loadSettings.db_Projekt())
        self.sqllite.execute('SELECT rowId,* FROM mainprojects')
        sqlResult = self.sqllite.fetchall()
        self.sqllite.close()

        for entry in sqlResult:
            item= QtGui.QTreeWidgetItem()
            item.setData(0, 32, QtCore.QVariant(entry[0]))

            for i in range(0, 5):
                if i == 2:
                    kunde = self.getKunde(entry[i+1])
                    item.setText(i, _fromUtf8(kunde))
                    item.setFont(i, QtGui.QFont('Helvetica', 10))
                else:
                    item.setText(i, _fromUtf8(entry[i+1]))
                    item.setFont(i, QtGui.QFont('Helvetica', 10))
                    
                self.treeWidget.addTopLevelItem(item)
                
                
    def getKunde(self, kundenNr):
        kundenString = ''
        
        self.sqllite.connect(self.loadSettings.db_Kunde())
        self.sqllite.execute('SELECT sFirma,sNachname,sVorname FROM kunden WHERE sKundennr=?', (kundenNr, ))
        sqlResult = self.sqllite.fetchall()[0]
        self.sqllite.close()

        if len(sqlResult[0]) > 0:
            kundenString = kundenString+sqlResult[0]
        else:
            if len(sqlResult[2]) > 0:
                kundenString = kundenString+sqlResult[2]+' '
            if len(sqlResult[1]) > 0:
                kundenString = kundenString+sqlResult[1]

        return kundenString

