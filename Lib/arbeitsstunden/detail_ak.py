## -*- coding: utf-8 -*-
#
#import os
#from PyQt4 import QtGui, QtCore
#
#from Lib.tools import Tools
#from Lib.contextMenu import ContextMenu
#from Lib.datenbankHandler import ConnectDB
#from Lib.project.getsummen import Get_Summen
#
#
#_fromUtf8 = QtCore.QString.fromUtf8
#
#
#class AK_Detail:
#    
#    def __init__(self, Main, Ui):
#        
#        self.AkMemberList = ['Max', 'Johannes', 'David', 'Elias']
#        self.main = Main
#        self.ui = Ui
#        self.tools = Tools()
#        self.sqllite = ConnectDB()
#
#        self.loadUi()
#        self.ui.connect(self.ui.tabWidget, QtCore.SIGNAL("currentChanged (int)"), self.tabWidgetRequest)
#       
#    
#
#    def loadUi(self):
#
#        self.ui.tabWidget.clear()
#        self.ui.tabWidget.setCurrentIndex(0)
#        
#        for ak in self.AkMemberList:
#
#            self.tab = QtGui.QWidget()
#            self.verticalLayout = QtGui.QVBoxLayout(self.tab)
#
#            
#            exec 'self.treeWidget_'+ak+' = QtGui.QTreeWidget(self.tab)'
#
#            exec 'self.treeWidget = self.treeWidget_'+ak
#
#            self.treeWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
#            self.treeWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
#            self.treeWidget.header().setDefaultSectionSize(200)
#            self.treeWidget.setSortingEnabled(True)
#            self.treeWidget.setFrameShape(QtGui.QFrame.NoFrame)
#
#            self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Datum", None, QtGui.QApplication.UnicodeUTF8))
#            self.treeWidget.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Projekt", None, QtGui.QApplication.UnicodeUTF8))
#            self.treeWidget.headerItem().setText(2, QtGui.QApplication.translate("MainWindow", "Kunde", None, QtGui.QApplication.UnicodeUTF8))
#            self.treeWidget.headerItem().setText(3, QtGui.QApplication.translate("MainWindow", "Arbeitsbeginn", None, QtGui.QApplication.UnicodeUTF8))
#            self.treeWidget.headerItem().setText(4, QtGui.QApplication.translate("MainWindow", "Arbeitsende", None, QtGui.QApplication.UnicodeUTF8))
#            self.treeWidget.headerItem().setText(5, QtGui.QApplication.translate("MainWindow", "Pause", None, QtGui.QApplication.UnicodeUTF8))
#            self.treeWidget.headerItem().setText(6, QtGui.QApplication.translate("MainWindow", "Stunden", None, QtGui.QApplication.UnicodeUTF8))
#            self.treeWidget.headerItem().setText(7, QtGui.QApplication.translate("MainWindow", "Status", None, QtGui.QApplication.UnicodeUTF8))
#            
#            self.verticalLayout.addWidget(self.treeWidget)
#            self.ui.tabWidget.addTab(self.tab, _fromUtf8(ak))
#            
#            self.loadTreeWidget(ak)
#            self.ui.connect(self.treeWidget, QtCore.SIGNAL("customContextMenuRequested(QPoint)"), self.contextMenuRequest)
#            
#        self.setCurrentTreeWidget()
#
#        
#        
#    def loadTreeWidget(self, ak):
#        self.summe = Get_Summen()
#        exec 'self.treeWidget_'+ak+'.clear()'
#        
#        sqlResult = self.main.filter.getDetailResult(ak)
#
#        for entry in sqlResult:
#            stunden = str(self.tools.getTimeDifference(entry.beginn, entry.ende, entry.pause))
#            
#            item= QtGui.QTreeWidgetItem()
#            item.setData(0, 32, QtCore.QVariant(entry))
#            
#            item.setText(0, self.tools.formatDatum(entry.a_tag.datum))
#            item.setText(1, self.tools.formatKunde(entry.projekt.kunde))
#            item.setText(2, entry.projekt.name)
#            item.setText(3, self.tools.formatZeit(entry.beginn))
#            item.setText(4, self.tools.formatZeit(entry.ende))
#            item.setText(5, str(entry.pause))
#            item.setText(6, entry.get_status_display())
#            
#
#            for i in range(0, 5):
#                item.setFont(i, QtGui.QFont('Helvetica', 10))
#                    
#            
#            exec 'self.treeWidget_'+ak+'.addTopLevelItem(item)'
#                
#            #---------Hole Summen-------------------------------------
#            
#            stunden = float(stunden)
#            self.summe.stunden_Gesamt(stunden)
#            self.summe.stunden_Offen(stunden, entry[4])
#            self.summe.stunden_Abgerechnet(stunden, entry[4])
#            #---------Ende----------------------------------------------
#        
#        #-------------Setze Summen Label-----------------------------------------------------------------------------    
#        self.ui.label.setText('Gesamt:   '+str(self.summe.stundenGesamt)+' Stunden')
#        self.ui.label_2.setText('Offen:   '+str(self.summe.stundenOffen)+' Stunden')
#        self.ui.label_3.setText('Abgerechnet:   '+str(self.summe.stundenAbgerechnet)+' Stunden')
#        #-------------Ende-----------------------------------------------------------------------------------------------
#                
#
#
#    def contextMenuRequest(self, pos):
#
#        self.menu = ContextMenu(self.treeWidget)
#        self.ui.connect(self.menu.contextMenu, QtCore.SIGNAL("triggered(QAction *)"), self.contextMenuActions)
#        
#        if len(self.treeWidget.selectedItems()) > 0:
#            self.menu.ak()
#        else:
#            self.menu.noSelection()
#        self.menu.show(pos)
#        
#
#        
#    def contextMenuActions(self, action):
#        action = self.tools.getEncodedString(action.text())
#        print action
#        
#        if action ==  'Löschen':
#            self.sqllite.connect(os.getcwd() + '\\db\\project.sqlite')
#            self.sqllite.delete('as_ak', self.getRowId())
#            self.refresh()
#            
#        if action == 'Aktualisieren':
#            self.refresh()
#        
#        
#    def tabWidgetRequest(self):
#        self.setCurrentTreeWidget()
#        
#        
#    def setCurrentTreeWidget(self):
#        ak = self.getCurrentAK()
#        if ak == False:
#            return
#        exec 'self.treeWidget = self.treeWidget_'+ak
#        
#        
#    def getCurrentAK(self):
#        print self.ui.tabWidget.currentIndex()
#        if self.ui.tabWidget.currentIndex() == -1:
#            return False
#        return str(self.ui.tabWidget.tabText(self.ui.tabWidget.currentIndex()))
#        
#        
#    def getRowId(self):
#        return str(self.treeWidget.currentItem().data(0, 32).toString())
#        
#    
#    def refresh(self):
#        self.loadUi()
#        
#        
#
