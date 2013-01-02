# -*- coding: utf-8 -*-

import os
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWizardPage
from PyQt4.QtCore import pyqtSignature

from Ui_wizardPage import Ui_WizardPage
from ak import Arbeiter

from Lib.datenbankHandler import ConnectDB
from Lib.tools import Tools

from Lib.loadSettings import LoadSettings



_fromUtf8 = QtCore.QString.fromUtf8


class WizardPage(QWizardPage, Ui_WizardPage):

    def __init__(self, parent = None):

        QWizardPage.__init__(self, parent)
        self.setupUi(self)
        
        self.loadSettings = LoadSettings()
        self.sqllite = ConnectDB()
        self.tools = Tools()
        
        
        
    def nextId(self):
        
        if int(self.field('AnzahlPos').toString()) == self.wizard().currentId():
            return 11
        else:
            return self.wizard().currentId() + 1
            
            
    def initializePage(self):
        self.clear()
        self.setPageTitle()
        self.getWerte()
        self.setPosNr()

        
        
    def validatePage(self):
        
        posList = []
        for i, entry in enumerate(self.wizard().ak_asRowId):
            count = str(i)
            
            
            beschreibung = self.beschreibung
            exec 'ak = self.ak_' + count
            exec 'stunden = self.stunden_' + count
            exec 'minuten = self.minuten_' + count
            exec 'rowId = self.rowId_' + count
            
            lst = [beschreibung, ak, stunden, minuten, rowId]

            posList.append(lst)
            
        print posList
        exec 'self.wizard().posDict_' +  str(self.wizard().currentId()) + ' = {"Details" : posList}'
        
        
        return True
        

        
    def setPosNr(self):
        for i in range(0, int(self.field('AnzahlPos').toString())):
            count = str(i)
            if i+1 == self.wizard().currentId():
                self.currentPosVariable = count
                exec  'self.wizard().posnr_' + count + ' = self.wizard().currentId()'   
                
            
    def getWerte(self):
        
        for i, entry in enumerate(self.wizard().ak_asRowId):
            self.sqllite.connect(self.loadSettings.db_Projekt())
            self.sqllite.execute('SELECT * FROM as_ak WHERE rowId=?', (entry[0], ))
            sqlResult = self.sqllite.fetchall()[0]
            self.sqllite.close()
            
            self.addAkWidget(sqlResult[0], i)
            if self.wizard().editStatus != False:
                rowId = self.editWerte(sqlResult[0])
                self.setVariablen(sqlResult[0], str(i), rowId)
                
            else:
                self.setVariablen(sqlResult[0], str(i))
            
            
    def addAkWidget(self, title, count):
        self.ak = Arbeiter(self, _fromUtf8(title), count)
        self.verticalLayout.addWidget(self.ak)
        self.label_posnr.setText('Position Nr. '+str(self.wizard().currentId()))
        
            
    def setVariablen(self, ak, count, rowId=False):
        exec 'self.ak_' + count + '= ak'
        exec 'self.stunden_' + count + ' = self.ak.comboBox.currentText()'
        exec 'self.minuten_' + count + ' = self.ak.comboBox_2.currentText()'
        exec 'self.rowId_' + count + ' = rowId'
        
        if self.wizard().editStatus == False:
            self.beschreibung = ''
        

            
    def editWerte(self, ak):
        self.sqllite.connect(self.loadSettings.db_Position())
        self.sqllite.execute('SELECT sBeschreibung,sStunden,sMinuten,rowId FROM pos WHERE sId=? AND sAk=? AND sPosnr=?', (self.wizard().editStatus[1], ak, self.wizard().currentId()))
        sqlResult = self.sqllite.fetchall()
        self.sqllite.close()
        print sqlResult
        
        if len(sqlResult) > 0:
            sqlResult = sqlResult[0]
        else:
            self.beschreibung = ''
            return False
        
        beschreibung = sqlResult[0]
        stunden = int(sqlResult[1])
        minuten = int(sqlResult[2])
        rowId = sqlResult[3]

        self.plainTextEdit.setPlainText(sqlResult[0])
        
        if stunden <= 0:
            self.ak.comboBox.setCurrentIndex(0)
        else:
            self.ak.comboBox.setCurrentIndex(stunden)
            
        if minuten <= 0:
            self.ak.comboBox_2.setCurrentIndex(0)
        if minuten == 15:
            self.ak.comboBox_2.setCurrentIndex(1)
        if minuten == 30:
            self.ak.comboBox_2.setCurrentIndex(2)
        if minuten == 45:
            self.ak.comboBox_2.setCurrentIndex(3)
            
        return rowId


    
    @pyqtSignature("")
    def on_plainTextEdit_textChanged(self):
        self.beschreibung = self.plainTextEdit.toPlainText()
        
    
    def setPageTitle(self):
        self.setTitle(_fromUtf8('Position Nr. '+str(self.wizard().currentId())))
        
    
    def clear(self):
        
        self.scrollAreaWidgetContents.close()
        
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 505, 95))

        self.verticalLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setSpacing(15)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        
        
    
        

