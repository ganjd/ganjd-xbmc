# -*- coding: utf-8 -*-

from PyQt4.QtCore import QThread
from PyQt4.QtCore import QString
from PyQt4.QtGui import QWizardPage
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtCore import SIGNAL

from Ui_wizardFinalPage import Ui_WizardPage

from Orm.db.models import *
from signalReceiver import Signal
from Ui.messageBox import MessageBox

_fromUtf8 = QString.fromUtf8

class WizardFinalPage(QWizardPage, Ui_WizardPage):

    def __init__(self, parent = None):

        QWizardPage.__init__(self, parent)
        self.setupUi(self)
        
        self.messageBox = MessageBox(self)
    
        self.initialize_Threads()
        self.validate = False
        
        self.dict = {}


    def initialize_Threads(self):
        self.saveKunde = Save_Kunde()
        self.connect(self.saveKunde, SIGNAL('savingFinished'), self.savingFinished)
        self.connect(self.saveKunde, SIGNAL('connect_error'), self.connect_error)
        self.connect(self.saveKunde, SIGNAL('error'), self.error)
        
        
        
    def initializePage(self):
        
        kundennr = self.field('Kundennr').toString()
        matchcode = self.field('Matchcode').toString()
        anrede = self.field('Anrede').toString()
        firma = self.field('Firma').toString()
        nachname = self.field('Nachname').toString()
        vorname = self.field('Vorname').toString()
        plz = self.field('Plz').toString()
        ort = self.field('Ort').toString()
        str = self.field('Str').toString()
        telefon = self.field('Telefon').toString()
        mobil = self.field('Mobil').toString()
        fax = self.field('Fax').toString()
        email = self.field('Email').toString()
        
        self.label_kundennr.setText('Kundennummer:   '+kundennr)
        self.label_matchcode.setText('Matchcode:   '+matchcode)
        self.label_anrede.setText('Anrede:   '+anrede)
        self.label_firma.setText('Firma:   '+firma)
        self.label_nachname.setText('Nachname:   '+nachname)
        self.label_vorname.setText('Vorname:   '+vorname)
        self.label_str.setText(_fromUtf8('Straße:   ')+str)
        self.label_ort.setText('Ort:   '+plz+' '+ort)
        self.label_telefon.setText('Telefon:   '+telefon)
        self.label_mobil.setText('Mobil:   '+mobil)
        self.label_fax.setText('Fax:   '+fax)
        self.label_email.setText('E-Mail:   '+email)
        
        
        self.dict['Kundennr'] = kundennr
        self.dict['Matchcode'] = matchcode
        self.dict['Anrede'] = anrede
        self.dict['Firma'] = firma
        self.dict['Nachname'] = nachname
        self.dict['Vorname'] = vorname
        self.dict['Plz'] = plz
        self.dict['Ort'] = ort
        self.dict['Str'] = str
        self.dict['Telefon'] = telefon
        self.dict['Mobil'] = mobil
        self.dict['Fax'] = fax
        self.dict['Email'] = email
        

    def setOption(self, option):
        self.option = option
        

    def savingFinished(self):
        self.validate = True
        self.wizard().next()
    
    def validatePage(self):
        if not self.validate:
            self.saveKunde.setValues(self.dict, self.option)
            self.saveKunde.start()
        print self.validate
        return self.validate

        

    def connect_error(self, sender):
        reply = self.messageBox.connect_error()
        if reply:
            sender.start()

    def error(self, sender, err):
        reply = self.messageBox.error({'err': err, 'sender': sender})



class Save_Kunde(QThread):
    
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
                        kunde = self.option[identifier]
                        kunde.nr = input['Kundennr']
                        kunde.matchcode = input['Matchcode']
                        kunde.anrede = input['Anrede']
                        kunde.firma= input['Firma']
                        kunde.nachname = input['Nachname']
                        kunde.vorname = input['Vorname']
                        kunde.plz = input['Plz']
                        kunde.ort = input['Ort']
                        kunde.strasse = input['Str']
                        kunde.telefon = input['Telefon']
                        kunde.mobil = input['Mobil']
                        kunde.fax = input['Fax']
                        kunde.email = input['Email']
                        
                        update = True
    
            if not update:
                kunde = Kunde(
                    nr = input['Kundennr'], 
                    matchcode = input['Matchcode'], 
                    anrede = input['Anrede'], 
                    firma = input['Firma'], 
                    nachname = input['Nachname'], 
                    vorname = input['Vorname'], 
                    plz = input['Plz'], 
                    ort = input['Ort'], 
                    strasse = input['Str'], 
                    telefon = input['Telefon'], 
                    mobil = input['Mobil'], 
                    fax = input['Fax'], 
                    email = input['Email'], 
                    )
                    
            kunde.save()
            
            self.signal.finishedLoading(self)
            self.emit(SIGNAL('savingFinished'))
            
        except Exception, err:
            self.signal.killLoading(self)
            if err.__class__.__name__ == 'OperationalError':
                self.emit(SIGNAL('connect_error'), self)
            else:
                self.emit(SIGNAL('error'), self, err)
