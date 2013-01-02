# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import SIGNAL

from Ui.Wizard.wizard import Wizard
from Ui.Projekte.details import Projekt_Details_Ui

from Lib.projekte.filter_belege import Filter_Belege
from Lib.projekte.filter_as import Filter_AS
from Lib.getsummen import Get_Summen
from Lib.tools import Tools
from Orm.db.models import *
from Lib.loadSettings import LoadSettings
from signalReceiver import Signal
from Ui.messageBox import MessageBox
from Lib.sorting import Sort


_fromUtf8 = QtCore.QString.fromUtf8



class Projekt_Details(Projekt_Details_Ui):
    
    def __init__(self, projekt_object):

        Projekt_Details_Ui.__init__(self)
        
        self.settings = LoadSettings()
        self.messageBox = MessageBox(self)

        self.projekt_object = projekt_object
        
        self.initialize_Threads()
        



    def initialize_Threads(self):
        
        self.loadAS = Load_AS(self.projekt_object)
        self.connect(self.loadAS, SIGNAL('addItem_AS'), self.addItem_AS)
        self.connect(self.loadAS, SIGNAL('setSummen'), self.setSummen_AS)
        self.connect(self.loadAS, SIGNAL('connect_error'), self.connect_error)
        self.connect(self.loadAS, SIGNAL('error'), self.error)
        self.connect(self.loadAS.filter, SIGNAL('addFilterItem'), self.addFilterItem_AS)
        
        
        self.loadMaterial = Load_Material(self.projekt_object)
        self.connect(self.loadMaterial, QtCore.SIGNAL('addItem_Material'), self.addItem_Material)
        self.connect(self.loadMaterial, SIGNAL('setSummen'), self.setSummen_Material)
        self.connect(self.loadMaterial, SIGNAL('connect_error'), self.connect_error)
        self.connect(self.loadMaterial, SIGNAL('error'), self.error)
        self.connect(self.loadMaterial.filter, SIGNAL('addFilterItem'), self.addFilterItem_Material)
        
        
        self.loadTreeWidget_AS()
        self.loadTreeWidget_Material()
        


    #TreeWidget
    def loadTreeWidget_AS(self):
        self.treeWidget.clear()
        
        self.treeWidget.setSortingEnabled(False)
        header = self.treeWidget.header()
 
        header.setSortIndicatorShown(True)
        header.setClickable(True)
        self.sort_AS = Sort(self.treeWidget)
        self.connect(header, QtCore.SIGNAL('sectionClicked(int)'), self.sort_AS.byColumn)
        
        self.loadAS.start()

    def loadTreeWidget_Material(self):
        self.treeWidget_2.clear()
        
        self.treeWidget_2.setSortingEnabled(False)
        header = self.treeWidget_2.header()
 
        header.setSortIndicatorShown(True)
        header.setClickable(True)
        self.sort_Material = Sort(self.treeWidget_2)
        self.connect(header, QtCore.SIGNAL('sectionClicked(int)'), self.sort_Material.byColumn)
        
        self.loadMaterial.start()
    
    
    
    #Add TreeWidgetItems
    def addItem_AS(self, item):
        self.treeWidget.addTopLevelItem(item)
        self.sort_AS.byColumn(0)
        
    def addItem_Material(self, item):
        self.treeWidget_2.addTopLevelItem(item)
        self.sort_Material.byColumn(0)
        
        
        
    #Summen
    def setSummen_AS(self, gesamt, offen, abgerechnet):
        print gesamt
    
    def setSummen_Material(self, gesamt, offen, abgerechnet):
        self.label_7.setText(_fromUtf8('Gesamt:   '+str(gesamt)+' €'))
        self.label_8.setText(_fromUtf8('Offen:   '+str(offen)+' €'))
        self.label_9.setText(_fromUtf8('Abgerechnet:   '+str(abgerechnet)+' €'))
        
        
        
    #Add Filter Items
    def addFilterItem_AS(self, text, data):
        pass
    
    def addFilterItem_Material(self, text, data):
        if text == 'Alle':
            self.comboBox_filter_string.clear()
        self.comboBox_filter_string.addItem(text, data)
        


    #Contextmenu 
    def contextMenuActions_AS(self, action):
        action = action.data().toString()
        
        if action == 'PosAdd':
            self.wizard = Wizard('Position', 'pos|'+self.getRowId_AS())
            self.upload()
            self.refresh_AS()
            
        if action == 'PosEdit':
            self.wizard = Wizard('Position', 'edit|'+self.getRowId_AS()+'|'+self.getPosId())
            self.upload()
            self.refresh_AS()
            
        if action == 'PosShow':
            self.runPos()
        
        if action == 'PosDel':
            reply = QtGui.QMessageBox.question(self.parent.MainWindow, _fromUtf8('Löschen'), _fromUtf8('Sollen alle zugeordneten Positionen wirklich gelöscht werden?'), 'Ja', 'Nein')
            if reply == 0:
                self.sqllite.connect(self.loadSettings.db_Position())
                self.sqllite.execute('DELETE FROM pos WHERE sId=?', (self.getPosId(),))
                self.sqllite.commit()
                self.sqllite.close()
            
        if action == 'update':
            self.refresh_AS()
            
        if action == 'edit':
            self.runWizard_AS({'Edit': self.getA_TagObject()})
 
        if action == 'Status ändern':
            print 'Status ändern'
            
        if action == 'delete':
            reply = self.messageBox.del_question(self.getA_TagObject())
            if reply == 1:
                self.getA_TagObject().delete()
                self.refresh_AS()
                

        
    def contextMenuActions_Material(self, action):
        action = action.data().toString()
        
        if action == 'Refresh':
            print 'Refresh'
            self.refresh_Material()
            
        if action == 'StatusEdit':
            QtGui.QMessageBox.question(self, _fromUtf8('Info'), _fromUtf8('Funktion noch nicht implementiert !'), 'OK')
            
        if action == 'ZuBeleg':
            pass
#            self.runBelege()
#            self.belege.selectItem(self.getBeleg_DetailObject())

        if action == 'Löschen':
            reply = QtGui.QMessageBox.question(self.parent.MainWindow, _fromUtf8('Löschen'), _fromUtf8('Soll dieser Eintrag wirklich gelöscht werden?'), 'Ja', 'Nein')
            if reply == 0:
                print 'Loeschen'



    #Toolbutton Actions Neu
    def toolButtonActions(self, action):
        action = action.text()
        if action == 'Arbeitsstunden':
            self.runWizard_AS({'Projekt_Object': self.projekt_object})

            
        if action == 'Beleg':
            self.runWizard_Material({'Projekt_Object': self.projekt_object})


        
    #Get Model Objekte
    def getA_TagObject(self):
        return self.treeWidget.currentItem().data(0, 32).toPyObject()

    def getBeleg_DetailObject(self):
        return self.treeWidget_2.currentItem().data(0, 32).toPyObject()
        
        

    #Refresh
    def refresh_AS(self):
        self.loadTreeWidget_AS()   
        
    def refresh_Material(self):
        self.loadTreeWidget_Material()
        
        
        
    #Wizard
    def runWizard_AS(self, option=False):
        wizard = Wizard('AS', option)
        if wizard.result == 1:
            self.refresh_Material() 
            
    def runWizard_Material(self, option):
        wizard = Wizard('Beleg', option)
        if wizard.result == 1:
            self.refresh_Material() 



    #Filter
    def loadFilter_AS(self, filter_art, filter_string='Alle'):
        pass
        
    def loadFilter_Material(self, filter_art, filter_string='Alle'):
        if filter_string != self.loadMaterial.filter.filter_string:        
            self.treeWidget_2.clear()
        self.loadMaterial.setFilter(filter_art, filter_string)
        
        

#    def getPosId(self):
#        from Ui.Position.pos import Positionen
#        self.pos = Positionen('rowid|'+self.getRowId_AS())
#        return str(self.pos.posId) 
        

#    def checkPosExsist(self):
#        from Ui.Position.pos import Positionen
#        
#        self.pos = Positionen('rowid|'+self.getRowId_AS())
#        if self.pos.status == False:
#            return False
#        else:
#            return True
            
        
#    def runPos(self):
#        from Ui.Position.pos import Positionen
#        
#        self.pos = Positionen('rowid|'+self.getRowId_AS())
#        if self.pos.status == False:
#            QtGui.QMessageBox.information(self.parent.MainWindow, _fromUtf8('Hinweis'), _fromUtf8('Es wurden noch keine Positionen zugeordnet'), 'OK')
#        else:
#            self.pos.show()
#            
#        
#    def runPos_All(self):
#        from Ui.Position.pos_all import Pos_All
#        
#        self.pos_all = Pos_All(self.projektnr)
#        if self.pos_all.status == False:
#            QtGui.QMessageBox.information(self.parent.MainWindow, _fromUtf8('Hinweis'), _fromUtf8('Keine Positionen vorhanden !'), 'OK')
#        else:
#            self.pos_all.show()
    

            
    
    def runArbeiter(self):
        from Ui.Arbeiter.arbeiter import Arbeiter
        self.ak = Arbeiter()
        self.ak.setFilter('Projekt', self.projekt_object)
        self.ak.run()
        
    
    def showRechnungen(self):
        from Ui.Rechnungen.rechnungen import Rechnungen_Ui
        self.rechnungen = Rechnungen_Ui()
        self.verticalLayout_main.addWidget(self.rechnungen)
        
        


    def connect_error(self, sender):
        reply = self.messageBox.connect_error()
        if reply:
            sender.start()


    def error(self, sender, err):
        reply = self.messageBox.error({'err': err, 'sender': sender})



class Load_AS(QtCore.QThread):
    
    def __init__(self, projekt_object):
        QtCore.QThread.__init__(self)
        
        self.signal = Signal()
        self.signal.registerLoading(self)
        
        self.filter = Filter_AS(projekt_object)
        self.tools = Tools()
        self.summe = Get_Summen()
        
    
    def run(self):
        
        try:
            self.signal.startLoading(self)
            
            self.summe.clear()
            sqlResult = self.filter.getResult()
            
            for entry in sqlResult:
                stunden = self.getStundenFromAK(entry)
                
                item= QtGui.QTreeWidgetItem()
                item.setData(0, 32, QtCore.QVariant(entry))
                
                item.setText(0, self.tools.formatDatum(entry.datum))
                item.setText(1, str(entry.anzahl_ak))
                item.setText(2, str(stunden))
                item.setText(3, entry.get_status_display())
                
                for i in range(0, 4):
                    item.setFont(i, QtGui.QFont('Helvetica', 10))
    
                self.emit(SIGNAL('addItem_AS'), item)
     
                #---------Hole Summen-------------------------------------
                self.summe.stunden_Gesamt(stunden)
                self.summe.stunden_Offen(stunden, entry.status)
                self.summe.stunden_Abgerechnet(stunden, entry.status)
                #---------Ende----------------------------------------------
            
            #-------------Setze Summen Label-----------------------------------------------------------------------------    
            self.emit(SIGNAL('setSummen'),self.summe.stundenGesamt, self.summe.stundenOffen, self.summe.stundenAbgerechnet)
    
            self.signal.finishedLoading(self)
        
        except Exception, err:
            self.signal.killLoading(self)
            if err.__class__.__name__ == 'OperationalError':
                self.emit(SIGNAL('connect_error'), self)
            else:
                self.emit(SIGNAL('error'), self, err)


  
    def getStundenFromAK(self, a_tag):
        q_ak = AK.objects.filter(a_tag=a_tag)
        
        stunden = float(0)
        for entry in q_ak:
            stunden = stunden + self.tools.getTimeDifference(entry.beginn, entry.ende, entry.pause)
        
        return stunden



    

class Load_Material(QtCore.QThread):
    
    def __init__(self, projekt_object):
        QtCore.QThread.__init__(self)
        
        self.signal = Signal()
        self.signal.registerLoading(self)
        
        self.filter = Filter_Belege(projekt_object)
        self.tools = Tools()
        self.summe = Get_Summen()
        
        self.bLoadFilterOnly = False
        self.bLoadFilter = True
        
        
    
    def setFilter(self, filter_art, filter_string):
        
        if self.filter.filter_art != filter_art:
            if self.filter.filter_string == filter_string:
                self.bLoadFilterOnly = True
            else:
                self.bLoadFilter = True
                
        self.filter.setFilter(filter_art, filter_string)
        self.start()
        
    
    def run(self):
        
        try:
            self.signal.startLoading(self)
            
            #Filter 
            if self.bLoadFilterOnly:
                self.bLoadFilterOnly = False
                self.filter.loadFilter()
                self.signal.finishedLoading(self)
                return
                
            if self.bLoadFilter:
                self.bLoadFilter = False
                self.filter.loadFilter()
            
            #Lade Inhalte
            self.summe.clear()
            sqlResult = self.filter.getResult()
    
            for entry in sqlResult:
                item= QtGui.QTreeWidgetItem()
                item.setData(0, 32, QtCore.QVariant(entry))
                
                item.setText(0, self.tools.formatDatum(entry.nr.datum))
                item.setText(1, entry.bezeichnung)
                item.setText(2, str(entry.menge))
                item.setText(3, entry.nr.lieferant)
                item.setText(4, entry.nr.zahlungsart)
                item.setText(5, str(entry.brutto))
                item.setText(6, entry.get_status_display())
                
                for i in range(0, 7):
                    item.setFont(i, QtGui.QFont('Verdana', 10))
                    
                self.emit(SIGNAL('addItem_Material'), item)
            
                #---------Hole Summen-------------------------------------
                self.summe.betrag_Gesamt(entry.brutto)
                self.summe.betrag_Offen(entry.brutto, entry.status)
                self.summe.betrag_Abgerechnet(entry.brutto, entry.status)
                #---------Ende----------------------------------------------
            
            #Setze Summen
            self.emit(SIGNAL('setSummen'),self.summe.betragGesamt, self.summe.betragOffen, self.summe.betragAbgerechnet)
    
            self.signal.finishedLoading(self)
            
        except Exception, err:
            self.signal.killLoading(self)
            if err.__class__.__name__ == 'OperationalError':
                self.emit(SIGNAL('connect_error'), self)
            else:
                self.emit(SIGNAL('error'), self, err)
    
