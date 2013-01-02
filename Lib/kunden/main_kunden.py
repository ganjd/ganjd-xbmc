# -*- coding: utf-8 -*-


from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import SIGNAL

from Ui.Kunden.kunden import Kunden_Ui
from Ui.Wizard.wizard import Wizard

from Lib.kunden.filter import Filter
from Lib.tools import Tools
from Ui.messageBox import MessageBox
from Lib.loadSettings import LoadSettings
from Orm.db.models import *
from signalReceiver import Signal


_fromUtf8 = QtCore.QString.fromUtf8


class Kunden(Kunden_Ui):
    
    def __init__(self):
        Kunden_Ui.__init__(self)


        self.settings = LoadSettings()
        self.tools = Tools()
        self.messageBox = MessageBox(self)
        
        self.initialize_Threads()
        


    def initialize_Threads(self):
        self.loadKunden = Load_Kunden()
        self.connect(self.loadKunden, SIGNAL('addItem'), self.addItem)
        self.connect(self.loadKunden, SIGNAL('connect_error'), self.connect_error)
        self.connect(self.loadKunden, SIGNAL('error'), self.error)
        
        self.loadDetails = Load_Details()
        self.connect(self.loadDetails, SIGNAL('addDetails'), self.addDetails)
        self.connect(self.loadDetails, SIGNAL('connect_error'), self.connect_error)
        self.connect(self.loadDetails, SIGNAL('error'), self.error)
        
        self.loadAuftrag = Load_Auftrag()
        self.connect(self.loadAuftrag, SIGNAL('addAuftrag'), self.addAuftrag)
        self.connect(self.loadAuftrag, SIGNAL('connect_error'), self.connect_error)
        self.connect(self.loadAuftrag, SIGNAL('error'), self.error)
        

    
    def loadTreeWidget(self):
        self.treeWidget.clear()
        self.loadKunden.start()
        
        
    def addItem(self, item):
        self.treeWidget.addTopLevelItem(item)
        
        
    def setDetails(self, item):
        self.loadDetails.setValues(item)
        self.loadDetails.start()


    def addDetails(self, dict):
        
        self.label_anrede.setText(dict['anrede'])
        self.label_firma.setText(dict['firma'])
        
        if len(dict['vorname']) > 0 and len(dict['nachname']) > 0:
            self.label_vornachname.setText(dict['vorname']+' '+dict['nachname'])
        else:
            if len(dict['vorname']) > 0:
                self.label_vornachname.setText(dict['vorname'])
            else:
                self.label_vornachname.setText(dict['nachname'])
            
        if len(dict['plz']) > 0 and len(dict['ort']) > 0:
            self.label_plzort.setText(dict['plz']+' '+dict['ort'])
        else:
            if len(dict['plz']) > 0:
                self.label_plzort.setText(dict['plz'])
            else:
                self.label_plzort.setText(dict['ort'])

        self.label_strasse.setText(dict['strasse'])
        self.label_telefon.setText(dict['telefon'])
        self.label_mobil.setText(dict['mobil'])
        self.label_fax.setText(dict['fax'])
        self.label_email.setText(dict['email'])
        
        
        
    def setAuftrag(self, item):
        self.treeWidget_2.clear()
        self.loadAuftrag.setValues(item)
        self.loadAuftrag.start()
        

    def addAuftrag(self, item):
        self.treeWidget_2.addTopLevelItem(item)



    def refresh(self):
        self.show()
        self.loadTreeWidget()

        
        
    def runWizard(self, option=False):
        wizard = Wizard('Kunde', option)
        if wizard.result == 1:
            self.refresh()

        
        
        
    def getKundenObjekt(self):
        return self.treeWidget.currentItem().data(0, 32).toPyObject()
        
        
    
    def contextMenuActions(self, action):
        action = self.tools.getEncodedString(action.text())
        print action
        if action == 'Aktualisieren':
            self.refresh()
            
        if action == 'Bearbeiten':
            self.runWizard({'Edit': self.getKundenObjekt()})
            
        if action == 'Löschen':
            reply = self.messageBox.del_question(self.getKundenObjekt())
            if reply == 1:
                try:
                    self.getKundenObjekt().delete()
                except Exception, err:
                    self.messageBox.del_error(self.getKundenObjekt())
                self.refresh()



    def connect_error(self, sender):
        reply = self.messageBox.connect_error()
        if reply:
            sender.start()
            
    
    def error(self, sender, err):
        reply = self.messageBox.error({'err': err, 'sender': sender})




class Load_Kunden(QtCore.QThread):
    
    def __init__(self):
        QtCore.QThread.__init__(self)
        
        self.signal = Signal()
        self.signal.registerLoading(self)
        
        self.filter = Filter()

    
    def run(self):
        try:
            self.signal.startLoading(self)
            
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
                
                self.emit(SIGNAL('addItem'), item)
                
            self.signal.finishedLoading(self)
            
        except Exception, err:
            self.signal.killLoading(self)
            if err.__class__.__name__ == 'OperationalError':
                self.emit(SIGNAL('connect_error'), self)
            else:
                self.emit(SIGNAL('error'), self, err)

        
        
        

class Load_Details(QtCore.QThread):
    
    def __init__(self):
        QtCore.QThread.__init__(self)
        
        self.signal = Signal()
        self.signal.registerLoading(self)

        

    def setValues(self, item):
        self.item = item


    
    def run(self):
        try:
            self.signal.startLoading(self)
            
            kunde= self.item.data(0, 32).toPyObject()
            kunde_fields = kunde._meta.fields
            
            dict = {}
            for entry in kunde_fields:
                dict[entry.name] = entry.value_to_string(kunde)
                
            self.emit(SIGNAL('addDetails'), dict)
            
            self.signal.finishedLoading(self)
            
        except Exception, err:
            self.signal.killLoading(self)
            if err.__class__.__name__ == 'OperationalError':
                self.emit(SIGNAL('connect_error'), self)
            else:
                self.emit(SIGNAL('error'), self, err)
        


class Load_Auftrag(QtCore.QThread):
    
    def __init__(self):
        QtCore.QThread.__init__(self)
        
        self.signal = Signal()
        self.signal.registerLoading(self)
        


    def setValues(self, item):
        self.item = item

        
    def run(self):
        try:
            self.signal.startLoading(self)
            
            kunde = self.item.data(0, 32).toPyObject()
            
            sqlResult = Projekte.objects.filter(kunde=kunde)
            
            for entry in sqlResult:
                item= QtGui.QTreeWidgetItem()
                item.setData(0, 32, QtCore.QVariant(entry))
                
                item.setText(0, str(entry.nr))
                item.setText(1, entry.name)
                item.setText(2, entry.get_status_display())
    
                for i in range(0, 3):
                    item.setFont(i, QtGui.QFont('Helvetica', 10))
                        
                self.emit(SIGNAL('addAuftrag'), item)
    
            self.signal.finishedLoading(self)
            
        except Exception, err:
            self.signal.killLoading(self)
            if err.__class__.__name__ == 'OperationalError':
                self.emit(SIGNAL('connect_error'), self)
            else:
                self.emit(SIGNAL('error'), self, err)
        
        
