# -*- coding: utf-8 -*-

from PyQt4 import QtCore
from PyQt4.QtCore import QString
from PyQt4.QtGui import QWizardPage
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtCore import SIGNAL
from PyQt4.QtCore import QDate

from Ui_wizardStartPage import Ui_WizardPage
from Lib.loadSettings import LoadSettings

from signalReceiver import Signal
from Ui.messageBox import MessageBox


_fromUtf8 = QString.fromUtf8


class WizardStartPage(QWizardPage, Ui_WizardPage):

    def __init__(self, parent = None):

        QWizardPage.__init__(self, parent)
        self.setupUi(self)
        
        self.settings = LoadSettings()
        self.messageBox = MessageBox(self)
        self.setStyle()
        

    def initializePage(self):
        if self.option == False:
            self.input_Datum.setDate(QDate.currentDate())
            
        else:
            self.identifyOption()

    def initialize_Threads(self):
        self.loadEditWerte = Load_EditWerte()
        self.connect(self.loadEditWerte, SIGNAL('addEditWerte'), self.addEditWerte)
        self.connect(self.loadEditWerte, SIGNAL('connect_error'), self.connect_error)
        self.connect(self.loadEditWerte, SIGNAL('error'), self.error)

        
        
    def setOption(self, option):
        self.option = option
        
        
    def identifyOption(self):
        self.initialize_Threads()
        for identifier in self.option.keys():
        
            if identifier == 'Projekt_Object':
                self.input_Datum.setDate(QDate.currentDate())
                self.getWerte(self.option[identifier])
            
            if identifier == 'Edit':
                self.loadEditWerte.setValues(self.option[identifier])
                self.loadEditWerte.start()

            
    def register(self):
        self.registerField('Datum', self.input_Datum, 'date')
        self.registerField('AKs', self.input_AKs, 'currentText', SIGNAL('activated()'))
        self.registerField('Kunde', self.input_Kunde)
        self.registerField('Projekt', self.input_Projekt)
        self.registerField('Status', self.input_Status, 'currentText', SIGNAL('activated()'))
            


    def isComplete(self):
        if len(self.input_Kunde.text()) > 0:
            return True
        return False
    
    
    @pyqtSignature("QString")
    def on_input_Kunde_textChanged(self, p0):
        self.emit(SIGNAL('completeChanged()'))
        
    
    @pyqtSignature("")
    def on_toolButton_kunde_clicked(self):
        from Ui.Kunden.searchWindow import Contacts
        self.contact = Contacts(self)
        self.contact.show()

    
    @pyqtSignature("")
    def on_toolButton_projekt_clicked(self):
        from Ui.Projekte.searchWindow import SearchProject
        self.projects = SearchProject(self)
        self.projects.show()
        
        
    def setContact(self, kunde):
        self.input_Kunde.setText(kunde.vorname+ ' '+kunde.nachname)
        self.wizard().kunde = kunde
        
        
    def setProject(self, projekt):
        self.input_Projekt.setText(projekt.name)
        self.wizard().projekt = projekt
        
        
    def getWerte(self, projekt):

        self.setProject(projekt)

        self.setContact(projekt.kunde)
        
        self.toolButton_kunde.setEnabled(False)
        self.toolButton_projekt.setEnabled(False)


    def addEditWerte(self, dict):
        self.input_Datum.setDate(dict['datum'])
        self.input_AKs.setCurrentIndex(int(dict['anzahl_ak'])-1)
        self.input_Status.setCurrentIndex(self.getStatus(dict['status']))
        
        self.setProject(dict['projekt'])
        self.setContact(dict['kunde'])
        
        self.toolButton_kunde.setEnabled(False)
        self.toolButton_projekt.setEnabled(False)
        
        

    def getStatus(self, status):
        if status == 'Offen':
            return 0
        if status == 'Abgerechnet':
            return 1
        if status == 'Geld erhalten':
            return 2
            

    def setStyle(self):
        from PyQt4 import QtGui
        a = QtGui.QStyleFactory.keys()[5]
        b = QtGui.QStyleFactory.create(a)
        self.input_AKs.setStyle(b)
        self.input_Status.setStyle(b)
        
        
    def connect_error(self, sender):
        reply = self.messageBox.connect_error()
        if reply:
            sender.start()


    def error(self, sender, err):
        reply = self.messageBox.error({'err': err, 'sender': sender})



class Load_EditWerte(QtCore.QThread):
    
    def __init__(self):
        QtCore.QThread.__init__(self)
        
        self.signal = Signal()
        self.signal.registerLoading(self)
        

    def setValues(self, a_tag_object):
        self.a_tag_object = a_tag_object
        
    
    def run(self):
        
        try:
            self.signal.startLoading(self)
            self.emit(
                SIGNAL('addEditWerte'), 
                {
                    'datum': self.a_tag_object.datum, 
                    'anzahl_ak': self.a_tag_object.anzahl_ak,
                    'status': self.a_tag_object.get_status_display(), 
                    'projekt': self.a_tag_object.projekt, 
                    'kunde': self.a_tag_object.projekt.kunde, 
                }
                )
    
            self.signal.finishedLoading(self)
        
        except Exception, err:
            self.signal.killLoading(self)
            if err.__class__.__name__ == 'OperationalError':
                self.emit(SIGNAL('connect_error'), self)
            else:
                self.emit(SIGNAL('error'), self, err)

