# -*- coding: utf-8 -*-

import os
from PyQt4 import QtGui, QtCore

from Lib.tools import Tools
from Lib.contextMenu import ContextMenu
from Lib.datenbankHandler import ConnectDB

from Lib.loadSettings import LoadSettings


_fromUtf8 = QtCore.QString.fromUtf8


class AK_Detail:
    
    def __init__(self, Main, Ui):
        
        self.AkMemberList = ['Max', 'Johannes', 'David', 'Elias']
        self.main = Main
        self.ui = Ui
        self.tools = Tools()
        
        self.loadSettings = LoadSettings()
        self.sqllite = ConnectDB()

        self.loadUi()
        self.ui.connect(self.ui.tabWidget, QtCore.SIGNAL("currentChanged (int)"), self.tabWidgetRequest)
       
    

    def loadUi(self):

        self.ui.tabWidget.clear()
        self.ui.tabWidget.setCurrentIndex(0)
        
        for ak in self.AkMemberList:

            self.tab = QtGui.QWidget()
            self.verticalLayout = QtGui.QVBoxLayout(self.tab)

            
            exec 'self.treeWidget_'+ak+' = QtGui.QTreeWidget(self.tab)'

            exec 'self.treeWidget = self.treeWidget_'+ak

            self.treeWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
            self.treeWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
            self.treeWidget.header().setDefaultSectionSize(200)
            self.treeWidget.setSortingEnabled(True)
            self.treeWidget.setFrameShape(QtGui.QFrame.NoFrame)

            self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Datum", None, QtGui.QApplication.UnicodeUTF8))
            self.treeWidget.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Projekt", None, QtGui.QApplication.UnicodeUTF8))
            self.treeWidget.headerItem().setText(2, QtGui.QApplication.translate("MainWindow", "Kunde", None, QtGui.QApplication.UnicodeUTF8))
            self.treeWidget.headerItem().setText(3, QtGui.QApplication.translate("MainWindow", "Arbeitsbeginn", None, QtGui.QApplication.UnicodeUTF8))
            self.treeWidget.headerItem().setText(4, QtGui.QApplication.translate("MainWindow", "Arbeitsende", None, QtGui.QApplication.UnicodeUTF8))
            self.treeWidget.headerItem().setText(5, QtGui.QApplication.translate("MainWindow", "Pause", None, QtGui.QApplication.UnicodeUTF8))
            self.treeWidget.headerItem().setText(6, QtGui.QApplication.translate("MainWindow", "Stunden", None, QtGui.QApplication.UnicodeUTF8))
            self.treeWidget.headerItem().setText(7, QtGui.QApplication.translate("MainWindow", "Status", None, QtGui.QApplication.UnicodeUTF8))
            
            self.verticalLayout.addWidget(self.treeWidget)
            self.ui.tabWidget.addTab(self.tab, _fromUtf8(ak))
            
            self.loadTreeWidget(ak)
            self.ui.connect(self.treeWidget, QtCore.SIGNAL("customContextMenuRequested(QPoint)"), self.contextMenuRequest)
            
        self.setCurrentTreeWidget()

        
        
    def loadTreeWidget(self, ak):
        exec 'self.treeWidget_'+ak+'.clear()'
        
        sqlResult = self.main.filter.getDetailResult(ak)

        for entry in sqlResult:
            stunden = str(self.tools.getTimeDifference(entry[5], entry[6], entry[7]))
            
            item= QtGui.QTreeWidgetItem()
            item.setData(0, 32, QtCore.QVariant(entry[0]))
            
            sortList = [2, 3, 4, 5, 6, 7, 'x', 8]
            for i, number in enumerate(sortList):
                if i == 1:
                    item.setText(i, _fromUtf8(self.tools.getProjektFromNr(entry[number])))
                elif i == 2:
                    item.setText(i, _fromUtf8(self.tools.getKundeFromNr(entry[number])))
                elif number == 'x':
                    item.setText(i, _fromUtf8(stunden))
                else:
                    item.setText(i, _fromUtf8(entry[number]))
                item.setFont(i, QtGui.QFont('Helvetica', 10))
                    
                exec 'self.treeWidget_'+ak+'.addTopLevelItem(item)'
                


    def contextMenuRequest(self, pos):

        self.menu = ContextMenu(self.treeWidget)
        self.ui.connect(self.menu.contextMenu, QtCore.SIGNAL("triggered(QAction *)"), self.contextMenuActions)
        
        if len(self.treeWidget.selectedItems()) > 0:
            self.menu.ak()
        else:
            self.menu.noSelection()
        self.menu.show(pos)
        

        
    def contextMenuActions(self, action):
        action = self.tools.getEncodedString(action.text())
        print action
        
        if action ==  'Löschen':
            self.sqllite.connect(self.loadSettings.db_Projekt())
            self.sqllite.delete('as_ak', self.getRowId())
            self.refresh()
            
        if action == 'Aktualisieren':
            self.refresh()
        
        
    def tabWidgetRequest(self):
        self.setCurrentTreeWidget()
        
        
    def setCurrentTreeWidget(self):
        ak = self.getCurrentAK()
        if ak == False:
            return
        exec 'self.treeWidget = self.treeWidget_'+ak
        
        
    def getCurrentAK(self):
        print self.ui.tabWidget.currentIndex()
        if self.ui.tabWidget.currentIndex() == -1:
            return False
        return str(self.ui.tabWidget.tabText(self.ui.tabWidget.currentIndex()))
        
        
    def getRowId(self):
        return str(self.treeWidget.currentItem().data(0, 32).toString())
        
    
    def refresh(self):
        self.loadUi()
        
        

