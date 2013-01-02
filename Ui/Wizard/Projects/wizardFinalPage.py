# -*- coding: utf-8 -*-

from PyQt4.QtCore import QThread
from PyQt4.QtCore import QString
from PyQt4.QtGui import QWizardPage
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtCore import SIGNAL

from Ui_wizardFinalPage import Ui_WizardPage

from Orm.db.models import *
from Lib.tools import Tools
from signalReceiver import Signal
from Ui.messageBox import MessageBox
import datetime


_fromUtf8 = QString.fromUtf8

class WizardFinalPage(QWizardPage, Ui_WizardPage):


    def __init__(self, parent = None):

        QWizardPage.__init__(self, parent)
        self.setupUi(self)
        self.tools = Tools()
        self.messageBox = MessageBox(self)
    
        self.initialize_Threads()
        self.validate = False

        self.dict = {}
        

    def initialize_Threads(self):
        self.saveProjekt= Save_Projekt()
        self.connect(self.saveProjekt, SIGNAL('savingFinished'), self.savingFinished)
        self.connect(self.saveProjekt, SIGNAL('connect_error'), self.connect_error)
        self.connect(self.saveProjekt, SIGNAL('error'), self.error)

        
    def initializePage(self):
        
        prjoktnr = self.field('Projektnr').toString()
        prjoktname = self.field('Projektname').toString()
        status = self.field('Status').toString()
        beschreibung = self.wizard().beschreibung
        kunde = self.wizard().kunde
        
        self.label_Projektnr.setText('Projektnummer:   '+prjoktnr)
        self.label_Projektname.setText('Projektname:   '+prjoktname)
        self.label_Kunde.setText('Kunde:   '+kunde.nachname)
        self.label_Status.setText('Status:   '+status)
        self.plainTextEdit_Beschreibung.setPlainText(beschreibung)

        self.dict['Projektnr'] = prjoktnr
        self.dict['Projektname'] = prjoktname.toUtf8()
        self.dict['Kunde'] = kunde
        self.dict['Status'] = self.tools.shortStatusName(status)
        self.dict['Beschreibung'] = beschreibung.toUtf8()
        self.dict['Beginn'] = datetime.date(2012, 1, 1)
        self.dict['Ende'] = datetime.date(2012, 12, 31)

        

    def setOption(self, option):
        self.option = option
    
        
    def savingFinished(self):
        self.validate = True
        self.wizard().next()
        
    
    def validatePage(self):
        if not self.validate:
            self.saveProjekt.setValues(self.dict, self.option)
            self.saveProjekt.start()
        return self.validate


    def connect_error(self, sender):
        reply = self.messageBox.connect_error()
        if reply:
            sender.start()

    def error(self, sender, err):
        reply = self.messageBox.error({'err': err, 'sender': sender})
    
    

class Save_Projekt(QThread):
    
    def __init__(self):
        QThread.__init__(self)
        
        self.signal = Signal()
        self.signal.registerLoading(self)
        
        
    def setValues(self, input, option):
        self.input = input 
        self.option = option
        
    def run(self):
        try:
            self.signal.startLoading(self)
            
            input = self.input
            update = False
            
            if self.option != False:
                for identifier in self.option.keys():
                    if identifier == 'Edit':
                        projekt = self.option[identifier]
                        
                        projekt.nr = input['Projektnr']
                        projekt.name = input['Projektname']
                        projekt.kunde = input['Kunde']
                        projekt.status = input['Status']
                        projekt.beschreibung = input['Beschreibung']
                        projekt.beginn = input['Beginn']
                        projekt.ende = input['Ende']
                        
                        update = True
                
                
            if not update:
                
                projekt = Projekte(
                    nr = input['Projektnr'], 
                    name = input['Projektname'], 
                    kunde = input['Kunde'], 
                    status = input['Status'], 
                    beschreibung = input['Beschreibung'], 
                    beginn = input['Beginn'], 
                    ende = input['Ende'], 
                    )
            
            projekt.save()
            
            self.signal.finishedLoading(self)
            self.emit(SIGNAL('savingFinished'))
            
        except Exception, err:
            self.signal.killLoading(self)
            if err.__class__.__name__ == 'OperationalError':
                self.emit(SIGNAL('connect_error'), self)
            else:
                self.emit(SIGNAL('error'), self, err)
    

