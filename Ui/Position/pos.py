# -*- coding: utf-8 -*-

import os
from PyQt4 import QtGui, QtCore

from PyQt4.QtGui import QWidget
from PyQt4.QtCore import pyqtSignature

from Ui_pos import Ui_Form
from pos_content import Pos_Content

from Lib.datenbankHandler import ConnectDB

from Lib.loadSettings import LoadSettings


_fromUtf8 = QtCore.QString.fromUtf8


class Positionen(QWidget, Ui_Form):

    def __init__(self, Option):

        QWidget.__init__(self)
        self.setupUi(self)
        
        self.loadSettings = LoadSettings()
        self.sqllite = ConnectDB()
        
        self.identify(Option)
        
        

    def identify(self, option):
        option = option.split('|')
        
        if option[0] == 'rowid':
            self.getPosId(option[1])
            self.loadUi()
            
        if option[0] == 'posid':
            self.posId = option[1]
            self.loadUi()
        
        
    def getPosId(self, rowId):
        self.sqllite.connect(self.loadSettings.db_Projekt())
        self.sqllite.execute('SELECT sDatum,sProjekt,sAnzahl_AK FROM mainas WHERE rowId=?', (rowId, ))
        sqlResult = self.sqllite.fetchall()[0]
        self.sqllite.close()

        if len(sqlResult) > 0:
            self.posId = sqlResult[0]+':'+sqlResult[1]+':'+sqlResult[2]
        else:
            return False
            
            
    def loadUi(self):
        
        self.tabWidget = QtGui.QTabWidget(self.groupBox)
        self.tabWidget.setDocumentMode(True)
#        self.tabWidget.setTabsClosable(True)
#        self.tabWidget.setMovable(True)
#        self.MainWindow.connect(self.tabWidget, QtCore.SIGNAL("tabCloseRequested (int)"), self.tabCloseRequest)
        self.verticalLayout_2.addWidget(self.tabWidget)
        
        self.sqllite.connect(self.loadSettings.db_Position())
        self.sqllite.execute('SELECT sAnzahlpos FROM pos WHERE sId=?', (self.posId, ))
        sqlResult = self.sqllite.fetchall()
        self.sqllite.close()
        
        if len(sqlResult) > 0:
            self.status = True
            sqlResult = sqlResult[0]
            
            anzahlpos = sqlResult[0]
            for i in range(0, int(anzahlpos)):
                posnr = str(i+1)
                
                self.ui = Pos_Content()
                self.loadTreeWidget(posnr)
                self.addTab(self.ui, 'Postion Nr. '+posnr)
        
        else:
            self.status = False
        

    
    def addTab(self, widget, tabTitle):
        self.tab = QtGui.QWidget()
        self.verticalLayout = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.addWidget(widget)
        self.tabWidget.addTab(self.tab, _fromUtf8(tabTitle))
        self.tabWidget.setCurrentIndex(self.tabWidget.count()-1)
        
    
    
    def loadTreeWidget(self, posnr):
        self.ui.treeWidget.clear()
        
        self.sqllite.connect(self.loadSettings.db_Position())
        self.sqllite.execute('SELECT rowId,* FROM pos WHERE sPosnr=? AND sId=?', (posnr, self.posId))
        sqlResult = self.sqllite.fetchall()
        self.sqllite.close()

        for entry in sqlResult:
            self.ui.plainTextEdit.setPlainText(_fromUtf8(entry[5]))
            
            item= QtGui.QTreeWidgetItem()
            item.setData(0, 32, QtCore.QVariant(entry[0]))
            stunden = entry[7]+':'+entry[8]

            for i in range(0, 2):
                if i == 1:
                    item.setText(i, _fromUtf8(stunden))
                else:
                    item.setText(i, _fromUtf8(entry[i+6]))
                item.setFont(i, QtGui.QFont('Helvetica', 10))
                    
                self.ui.treeWidget.addTopLevelItem(item)
