# -*- coding: utf-8 -*-

from PyQt4.QtCore import QThread
from PyQt4.QtCore import QString
from PyQt4.QtGui import QWizardPage
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtCore import SIGNAL
from PyQt4.QtCore import QVariant


from Ui_wizardStartPage import Ui_WizardPage

from Lib.tools import Tools
from Orm.db.models import *

from Lib.loadSettings import LoadSettings
from signalReceiver import Signal
from Ui.messageBox import MessageBox


_fromUtf8 = QString.fromUtf8



class WizardStartPage(QWizardPage, Ui_WizardPage):

    def __init__(self, parent = None):

        QWizardPage.__init__(self, parent)
        self.setupUi(self)
        
        self.tools = Tools()
        self.messageBox = MessageBox(self)
        self.fillStatus()
        self.setStyle()

        

    def initializePage(self):
        self.initialize_Threads()
        
        if self.option == False:
            self.loadWerte.start()
            
        else:
            self.identifyOption()
            
            
    def initialize_Threads(self):
        self.loadWerte = Load_Werte()
        self.connect(self.loadWerte, SIGNAL('addWerte'), self.addWerte)
        self.connect(self.loadWerte, SIGNAL('connect_error'), self.connect_error)
        self.connect(self.loadWerte, SIGNAL('error'), self.error)
        
        self.loadEditWerte = Load_EditWerte()
        self.connect(self.loadEditWerte, SIGNAL('addEditWerte'), self.addEditWerte)
        self.connect(self.loadEditWerte, SIGNAL('connect_error'), self.connect_error)
        self.connect(self.loadEditWerte, SIGNAL('error'), self.error)
        
        
    def setOption(self, option):
        self.option = option
        
        
    def identifyOption(self):
        for identifier in self.option.keys():
        
            if identifier == 'Edit':
                self.loadEditWerte.setValues(self.option[identifier])
                self.loadEditWerte.start()



    def register(self):
        self.registerField('Projektnr', self.input_Projektnr)
        self.registerField('Projektname', self.input_Projektname)
        self.registerField('Status', self.input_Status, 'currentText', SIGNAL('activated()'))

        

    def isComplete(self):
        check = False
        
        if len(self.input_Projektname.text()) > 0:
            check = True
        else:
            return False
        if len(self.input_Kunde.text()) > 0:
            check = True
        else:
            return False
            
        return check
        
    
    @pyqtSignature("")
    def on_input_Beschreibung_textChanged(self):
        self.wizard().beschreibung = self.input_Beschreibung.toPlainText()
        
#    @pyqtSignature('int')
#    def on_input_Status_activated(self, index):
#        self.wizard().status = self.input_Status.itemData(index).toString()
        

    @pyqtSignature("QString")
    def on_input_Projektname_textChanged(self, p0):
        self.emit(SIGNAL('completeChanged()'))
    
    @pyqtSignature("QString")
    def on_input_Kunde_textChanged(self, p0):
        self.emit(SIGNAL('completeChanged()'))
    
    @pyqtSignature("")
    def on_toolButton_clicked(self):
        from Ui.Kunden.searchWindow import Contacts
        self.contact = Contacts(self)
        self.contact.show()
        
        
    def setContact(self, kunde):
        self.input_Kunde.setText(kunde.vorname+ ' '+kunde.nachname)
        self.wizard().kunde = kunde
        
    
    
    def addWerte(self, werte):
        self.input_Projektnr.setText(self.tools.formatProjektNr(werte))
        

        
    def addEditWerte(self, dict):
        
        self.input_Projektnr.setText(self.tools.formatProjektNr(str(dict['nr'])))
        self.input_Projektname.setText(dict['name'])
        self.input_Kunde.setText(self.tools.formatKunde(dict['kunde']))
        self.input_Status.setCurrentIndex(self.getIndexFromStatus(dict['status']))
        self.input_Beschreibung.setPlainText(dict['beschreibung'])
        
        self.wizard().kunde = dict['kunde']
        self.wizard().beschreibung = QString(dict['beschreibung'])
        self.wizard().status = dict['status']

    
    def fillStatus(self):
        status = [['O', 'Offen'], ['A', 'Abgerechnet'], ['G', 'Geld erhalten']]
        self.input_Status.clear()
        for entry in status:
            self.input_Status.addItem(entry[1], QVariant(entry[0]))


    
    def getIndexFromStatus(self, status):
        for i in range(0, self.input_Status.count()+1):
            if self.input_Status.itemData(i).toString() == status:
                return i
        
        

    def setStyle(self):
        from PyQt4 import QtGui
        a = QtGui.QStyleFactory.keys()[5]
        b = QtGui.QStyleFactory.create(a)
        self.input_Status.setStyle(b)
        
        
    def connect_error(self, sender):
        reply = self.messageBox.connect_error()
        if reply:
            sender.start()


    def error(self, sender, err):
        reply = self.messageBox.error({'err': err, 'sender': sender})
        
        

class Load_Werte(QThread):
    
    def __init__(self):
        QThread.__init__(self)

        self.signal = Signal()
        self.signal.registerLoading(self)
        
        
    def run(self):
        try:
            self.signal.startLoading(self)
            
            from django.db.models import Max
            maxNr = Projekte.objects.filter(beginn__year=2012).aggregate(Max('nr'))
            newNr = maxNr['nr__max']+1
            self.emit(SIGNAL('addWerte'), newNr)
            
            self.signal.finishedLoading(self)
            
        except Exception, err:
            self.signal.killLoading(self)
            if err.__class__.__name__ == 'OperationalError':
                self.emit(SIGNAL('connect_error'), self)
            else:
                self.emit(SIGNAL('error'), self, err)



class Load_EditWerte(QThread):
    
    def __init__(self):
        QThread.__init__(self)

        self.signal = Signal()
        self.signal.registerLoading(self)
        
    
    def setValues(self, projekt_object):
        self.projekt_object = projekt_object
        
        
    def run(self):
        try:
            self.signal.startLoading(self)
            q = self.projekt_object
            
            self.emit(
                SIGNAL('addEditWerte'), 
                {
                    'nr': q.nr, 
                    'name': q.name,
                    'kunde': q.kunde, 
                    'status': q.status, 
                    'beschreibung': q.beschreibung, 
                }
                )

            self.signal.finishedLoading(self)
            
        except Exception, err:
            self.signal.killLoading(self)
            if err.__class__.__name__ == 'OperationalError':
                self.emit(SIGNAL('connect_error'), self)
            else:
                self.emit(SIGNAL('error'), self, err)
        
        

