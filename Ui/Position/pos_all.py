# -*- coding: utf-8 -*-

import os
from PyQt4 import QtGui, QtCore

from PyQt4.QtGui import QWidget
from PyQt4.QtCore import pyqtSignature

from Ui_pos_all import Ui_Form

from Lib.datenbankHandler import ConnectDB
from Lib.tools import Tools

from Lib.loadSettings import LoadSettings


_fromUtf8 = QtCore.QString.fromUtf8


class Pos_All(QWidget, Ui_Form):

    def __init__(self, Projektnr):

        QWidget.__init__(self)
        self.setupUi(self)
        
        self.loadSettings = LoadSettings()
        self.sqllite = ConnectDB()
        self.tools = Tools() 
        self.projektnr = Projektnr
        
        self.loadTreeWidget()
        
        
        
    
    def loadTreeWidget(self):
        self.treeWidget.header().resizeSection(0, 400)
        self.setPosHeader()
        
        self.addTopLevelItem()
        

    def addTopLevelItem(self):
        
        pos_beschreibung = self.getPos_Beschreibung()
        
        if pos_beschreibung == False:
            self.status = False
            return

        for entry in pos_beschreibung:
            stunden_gesamt = self.getPos_Stunden(entry)
            
            item= QtGui.QTreeWidgetItem()
            item.setData(0, 32, QtCore.QVariant('False'))

            for i in range(0, 2):
                if i == 1:
                    item.setText(i, _fromUtf8(stunden_gesamt))
                else:
                    item.setText(i, _fromUtf8(entry))
                item.setFont(i, QtGui.QFont('Helvetica', 10))
                    
                self.treeWidget.addTopLevelItem(item)
                
            self.addChildItem(entry, item)

            
    def addChildItem(self, beschreibung, topLevelItem):
        
        self.sqllite.connect(self.loadSettings.db_Position())
        self.sqllite.execute('SELECT sId FROM pos WHERE sProjekt=? AND sBeschreibung=?', (self.projektnr, beschreibung))
        sqlResult = self.sqllite.fetchall()
        self.sqllite.close()
        
        lst = []
        for entry in sqlResult:
            lst.append(entry[0])

        lst_Clean = list(set(lst))

        
        for entry in lst_Clean:
        
            child = QtGui.QTreeWidgetItem(topLevelItem)
            child.setData(0, 32, QtCore.QVariant(entry))
            
            child.setText(0, _fromUtf8(entry.split(':')[0]))
            child.setFont(0, QtGui.QFont('Helvetica', 8))
            child.addChild(child)
        
        
 
    def getPos_Beschreibung(self):
        
        self.sqllite.connect(self.loadSettings.db_Position())
        self.sqllite.execute('SELECT sBeschreibung FROM pos WHERE sProjekt=?', (self.projektnr, ))
        sqlResult = self.sqllite.fetchall()
        self.sqllite.close()
        
        if len(sqlResult) > 0:
            self.status = True
            
            lst = []
            for entry in sqlResult:
                lst.append(entry[0])
                
            lst_Clean = list(set(lst))
            
            return lst_Clean
        
        else:
            return False
            
    
    def getPos_Stunden(self, beschreibung):
        
            self.sqllite.connect(self.loadSettings.db_Position())
            self.sqllite.execute('SELECT sStunden,sMinuten FROM pos WHERE sProjekt=? AND sBeschreibung=?', (self.projektnr, beschreibung))
            sqlResult = self.sqllite.fetchall()
            self.sqllite.close()
            
            stunden_gesamt = float(0)
            
            for entry in sqlResult:
                stunden = entry[0]+'.'+entry[1]
                stunden = float(stunden)
                stunden_gesamt = stunden_gesamt + stunden
                
            return str(stunden_gesamt)
            
    
    def setPosHeader(self):
        self.sqllite.connect(self.loadSettings.db_Projekt())
        self.sqllite.execute('SELECT sKunde,sProjektname FROM mainprojects WHERE sProjektNr=?', (self.projektnr, ))
        sqlResult = self.sqllite.fetchall()[0]
        self.sqllite.close()
        
        projektname = sqlResult[1]
        kunde = self.tools.getKundeFromNr(sqlResult[0])
        
        self.label_projekt.setText(_fromUtf8('Projekt:   '+projektname))
        self.label_kunde.setText(_fromUtf8('Kunde:   '+kunde))

            
    
    @pyqtSignature("QTreeWidgetItem*, int")
    def on_treeWidget_itemDoubleClicked(self, item, column):
        posid = str(item.data(0, 32).toString())
        
        if posid == 'False':
            return
        else:
            from Ui.Position.pos import Positionen
            
            self.pos = Positionen('posid|'+posid)
            self.pos.show()


