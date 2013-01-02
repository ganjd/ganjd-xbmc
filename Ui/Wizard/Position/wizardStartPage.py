# -*- coding: utf-8 -*-

import os
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QWizardPage
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtCore import SIGNAL

from Ui_wizardStartPage import Ui_WizardPage

from Lib.datenbankHandler import ConnectDB
from Lib.tools import Tools

from Lib.loadSettings import LoadSettings



_fromUtf8 = QtCore.QString.fromUtf8



class WizardStartPage(QWizardPage, Ui_WizardPage):

    def __init__(self, parent = None):

        QWizardPage.__init__(self, parent)
        self.setupUi(self)
        
        self.loadSettings = LoadSettings()
        self.sqllite = ConnectDB()
        self.tools = Tools() 
        self.setStyle()
        
        
    def initializePage(self):
        
        if self.option == False:
            self.getProjektNr()
        else:
            self.identifyOption()
        
        
    def setOption(self, option):
        self.option = option
        
        
    def identifyOption(self):
        option = self.option.split('|')
        
        if option[0] == 'pos':
            self.getWerte(option[1])
            self.wizard().editStatus = False
            
        if option[0] == 'edit':
            self.editWerte(option[1], option[2])
            self.wizard().editStatus = [option[1], option[2]]
            
            
            
    def register(self):
        self.registerField('AnzahlPos', self.input_anzahlPos, 'currentText', SIGNAL('activated()'))
        
        

    def getWerte(self, rowid):
        
        self.sqllite.connect(self.loadSettings.db_Projekt())
        self.sqllite.execute('SELECT * FROM mainas WHERE rowId=?', (rowid, ))
        sqlResult = self.sqllite.fetchall()[0]
        self.sqllite.close()
        
        self.setValues(sqlResult)
        
        self.label_datum.setText(_fromUtf8('Datum:   '+sqlResult[2]))
        self.label_anzahlak.setText(_fromUtf8('Anzahl der Arbeiter:   '+sqlResult[4]))
        self.label_kunde.setText(_fromUtf8('Kunde:   '+self.tools.getKundeFromNr(sqlResult[1])))
        self.label_projekt.setText(_fromUtf8('Projekt:   '+self.tools.getProjektFromNr(sqlResult[0])))
        
        self.sqllite.connect(self.loadSettings.db_Projekt())
        self.sqllite.execute('SELECT rowId FROM as_ak WHERE sProjekt=? and sDatum=?', (sqlResult[0], sqlResult[2]))
        sqlResult = self.sqllite.fetchall()
        self.sqllite.close()
        
        self.wizard().ak_asRowId = sqlResult
        
        
    def setValues(self, werte):
        self.wizard().datum = werte[2]
        self.wizard().projekt = werte[0]
        self.wizard().anzahlak = werte[4]
        self.wizard().kunde = werte[1]
        
        
    def editWerte(self, rowid, posId):
        self.getWerte(rowid)
        self.sqllite.connect(self.loadSettings.db_Position())
        self.sqllite.execute('SELECT sAnzahlpos FROM pos WHERE sId=?', (posId, ))
        sqlResult = self.sqllite.fetchall()[0][0]
        self.sqllite.close()
        
        anzahlpos = int(sqlResult)
        self.input_anzahlPos.setCurrentIndex(anzahlpos-1)
        self.wizard().old_anzahlpos = anzahlpos
        
        
    def setStyle(self):
        a = QtGui.QStyleFactory.keys()[5]
        b = QtGui.QStyleFactory.create(a)
        self.input_anzahlPos.setStyle(b)

        
    

