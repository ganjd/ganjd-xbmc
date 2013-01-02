# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QThread
from PyQt4.QtCore import QString
from PyQt4.QtGui import QWizardPage
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtCore import SIGNAL

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
        self.registerField('Kundennr', self.input_kundennr, 'text', SIGNAL('textChanged()'))
        self.registerField('Matchcode', self.input_matchcode, 'text', SIGNAL('textChanged()'))
        self.registerField('Anrede', self.input_anrede,'currentText', SIGNAL('activated()'))
        self.registerField('Firma', self.input_firma, 'text', SIGNAL('textChanged()'))
        self.registerField('Nachname', self.input_nachname, 'text', SIGNAL('textChanged()'))
        self.registerField('Vorname', self.input_vorname, 'text', SIGNAL('textChanged()'))
        self.registerField('Plz', self.input_plz, 'text', SIGNAL('textChanged()'))
        self.registerField('Ort', self.input_ort, 'text', SIGNAL('textChanged()'))
        self.registerField('Str', self.input_str, 'text', SIGNAL('textChanged()'))
        self.registerField('Telefon', self.input_tel, 'text', SIGNAL('textChanged()'))
        self.registerField('Mobil', self.input_mobil, 'text', SIGNAL('textChanged()'))
        self.registerField('Fax', self.input_fax, 'text', SIGNAL('textChanged()'))
        self.registerField('Email', self.input_email, 'text', SIGNAL('textChanged()'))
        
        
    def addWerte(self, werte):
        self.input_kundennr.setText(str(werte))
        
        
    def addEditWerte(self, dict):
        self.input_kundennr.setText(str(dict['nr']))
        self.input_matchcode.setText(dict['matchcode'])
        self.input_anrede.setEditText(dict['anrede'])
        self.input_firma.setText(dict['firma'])
        self.input_nachname.setText(dict['nachname'])
        self.input_vorname.setText(dict['vorname'])
        self.input_plz.setText(str(dict['plz']))
        self.input_ort.setText(dict['ort'])
        self.input_str.setText(dict['strasse'])
        self.input_tel.setText(dict['telefon'])
        self.input_mobil.setText(dict['mobil'])
        self.input_fax.setText(dict['fax'])
        self.input_email.setText(dict['email'])
        
        
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
            maxNr = Kunde.objects.all().aggregate(Max('nr'))
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
        
    
    def setValues(self, kunde_object):
        self.kunde_object = kunde_object
        
        
    def run(self):
        try:
            self.signal.startLoading(self)
            q = self.kunde_object
            
            self.emit(
                SIGNAL('addEditWerte'), 
                {
                    'nr': q.nr, 
                    'matchcode': q.matchcode,
                    'anrede': q.anrede, 
                    'firma': q.firma, 
                    'vorname': q.vorname, 
                    'nachname': q.nachname, 
                    'plz': q.plz, 
                    'ort': q.ort, 
                    'strasse': q.strasse, 
                    'telefon': q.telefon, 
                    'mobil': q.mobil, 
                    'fax': q.fax, 
                    'email': q.email, 
                }
                )

            self.signal.finishedLoading(self)
            
        except Exception, err:
            self.signal.killLoading(self)
            if err.__class__.__name__ == 'OperationalError':
                self.emit(SIGNAL('connect_error'), self)
            else:
                self.emit(SIGNAL('error'), self, err)
        


