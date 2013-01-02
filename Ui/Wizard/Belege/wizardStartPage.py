# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QThread
from PyQt4.QtGui import QWizardPage
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtCore import SIGNAL
from PyQt4.QtCore import QDate

from Ui_wizardStartPage import Ui_WizardPage

from Lib.tools import Tools
from Orm.db.models import *

from Lib.loadSettings import LoadSettings
from signalReceiver import Signal
from Ui.messageBox import MessageBox



_fromUtf8 = QtCore.QString.fromUtf8



class WizardStartPage(QWizardPage, Ui_WizardPage):

    def __init__(self, parent = None):

        QWizardPage.__init__(self, parent)
        self.setupUi(self)
        
        self.messageBox = MessageBox(self)
        self.settings = LoadSettings()
        self.tools = Tools() 
        
        self.setStyle()
        
        self.bruttoCent = ''
        self.bruttoEuro =''
        self.nettoCent = ''
        self.nettoEuro =''
        
        self.connect(self, SIGNAL('Brutto'), self.calcNetto)
        self.connect(self, SIGNAL('Netto'), self.calcBrutto)
        
        
    def initializePage(self):
        self.initialize_Threads()
        
        if self.option == False:
            self.input_Datum.setDate(QDate.currentDate())
            self.loadWerte.start()
            self.loadComboBox.start()

        else:
            self.identifyOption()
            

    def initialize_Threads(self):
        self.loadWerte = Load_Werte()
        self.connect(self.loadWerte, SIGNAL('addWerte'), self.addWerte)
        self.connect(self.loadWerte, SIGNAL('connect_error'), self.connect_error)
        self.connect(self.loadWerte, SIGNAL('error'), self.error)
        
        self.loadComboBox = Load_ComboBox()
        self.connect(self.loadComboBox, SIGNAL('addComboBoxItem'), self.addComboBoxItem)
        self.connect(self.loadComboBox, SIGNAL('connect_error'), self.connect_error)
        self.connect(self.loadComboBox, SIGNAL('error'), self.error)
        
        self.loadEditWerte = Load_EditWerte()
        self.connect(self.loadEditWerte, SIGNAL('addEditWerte'), self.addEditWerte)
        self.connect(self.loadEditWerte, SIGNAL('connect_error'), self.connect_error)
        self.connect(self.loadEditWerte, SIGNAL('error'), self.error)
        
        
    def setOption(self, option):
        self.option = option
        
        
    def identifyOption(self):
        for identifier in self.option.keys():
            if identifier == 'Projekt_Object':
                self.input_Datum.setDate(QDate.currentDate())
                self.loadWerte.start()
                self.loadComboBox.start()

            
            if identifier == 'Edit':
                self.loadEditWerte.setValues(self.option[identifier])
                self.loadEditWerte.start()


            
            
    def register(self):
        self.registerField('Belegnr', self.input_Belegnr, 'text', SIGNAL('textChanged()'))
        self.registerField('Datum', self.input_Datum, 'date')
        self.registerField('Lieferant', self.input_Lieferant, 'currentText', SIGNAL('editTextChanged()'))
        self.registerField('Zahlungsart', self.input_Zahlungsart, 'currentText', SIGNAL('editTextChanged()'))
        self.registerField('Betrag_Netto_E', self.input_Betrag_Netto_E, 'text', SIGNAL('textChanged()'))
        self.registerField('Betrag_Netto_C', self.input_Betrag_Netto_C, 'text', SIGNAL('textChanged()'))
        self.registerField('Betrag_Brutto_E', self.input_Betrag_Brutto_E, 'text', SIGNAL('textChanged()'))
        self.registerField('Betrag_Brutto_C', self.input_Betrag_Brutto_C, 'text', SIGNAL('textChanged()'))
        self.registerField('AnzahlPos', self.input_anzahlPos, 'currentText', SIGNAL('activated()'))
        
        
    def addWerte(self, wert):
        self.input_Belegnr.setText(self.tools.formatBelegNr(wert))
        

#    def setValues(self, werte):
#        self.wizard().datum = werte[2]
#        self.wizard().projekt = werte[0]
#        self.wizard().anzahlak = werte[4]
#        self.wizard().kunde = werte[1]
        
        
    def addComboBoxItem(self, item):
        if item[0] == 'lieferant':
            self.input_Lieferant.addItem(item[1])
        if item[0] == 'zahlungsart':
            self.input_Zahlungsart.addItem(item[1])
            


    def addEditWerte(self, dict):
        self.input_Belegnr.setText(self.tools.formatBelegNr(dict['nr']))
        self.input_Datum.setDate(dict['datum'])
        self.input_Lieferant.setEditText(dict['lieferant'])
        self.input_Zahlungsart.setEditText(dict['zahlungsart'])
        self.input_Betrag_Brutto_E.setText(str(dict['brutto']).split('.')[0])
        self.input_Betrag_Brutto_C.setText(str(dict['brutto']).split('.')[1])
        self.input_Betrag_Netto_E.setText(str(dict['netto']).split('.')[0])
        self.input_Betrag_Netto_C.setText(str(dict['netto']).split('.')[1])
        self.input_anzahlPos.setCurrentIndex(dict['anzahl_artikel']-1)
        
        self.emit(SIGNAL('completeChanged()'))



    def isComplete(self):
        check = False
        
        if len(self.input_Lieferant.currentText()) > 0:
            check = True
        else:
            return False
        if len(self.input_Zahlungsart.currentText()) > 0:
            check = True
        else:
            return False
        if len(self.input_Betrag_Netto_E.text()) > 0:
            check = True
        else:
            return False
        if len(self.input_Betrag_Netto_C.text()) > 0:
            check = True
        else:
            return False
        if len(self.input_Betrag_Brutto_E.text()) > 0:
            check = True
        else:
            return False
        if len(self.input_Betrag_Brutto_C.text()) > 0:
            check = True
        else:
            return False
            
        return check
        
        
#--------------------------------------------------------------------------------------------------
#SIGNALS
#--------------------------------------------------------------------------------------------------
    @pyqtSignature("QString")
    def on_input_Betrag_Netto_C_textEdited(self, p0):
        self.emit(SIGNAL('completeChanged()'))
        
        if len(p0) == 0:
            self.nettoCent = ''
            return
        try:
            int(p0)
            self.nettoCent = p0
        except:
            self.input_Betrag_Netto_C.setText(self.nettoCent)
        
        self.emit(SIGNAL('Netto'))
            
    
    @pyqtSignature("QString")
    def on_input_Betrag_Netto_E_textEdited(self, p0):
        self.emit(SIGNAL('completeChanged()'))
        
        if len(p0) == 0:
            self.nettoEuro = ''
            return
        try:
            int(p0)
            self.nettoEuro = p0
        except:
            self.input_Betrag_Netto_E.setText(self.nettoEuro)
            
        self.emit(SIGNAL('Netto'))
            
    @pyqtSignature("QString")
    def on_input_Betrag_Brutto_C_textEdited(self, p0):
        self.emit(SIGNAL('completeChanged()'))
        
        if len(p0) == 0:
            self.bruttoCent = ''
            return
        try:
            int(p0)
            self.bruttoCent = p0
        except:
            self.input_Betrag_Brutto_C.setText(self.bruttoCent)
        
        self.emit(SIGNAL('Brutto'))
    
    @pyqtSignature("QString")
    def on_input_Betrag_Brutto_E_textEdited(self, p0):
        self.emit(SIGNAL('completeChanged()'))
        
        if len(p0) == 0:
            self.bruttoEuro = ''
            return
        try:
            int(p0)
            self.bruttoEuro = p0
        except:
            self.input_Betrag_Brutto_E.setText(self.bruttoEuro)
        
        self.emit(SIGNAL('Brutto'))

    
    @pyqtSignature("QString")
    def on_input_Lieferant_editTextChanged(self, p0):
        self.emit(SIGNAL('completeChanged()'))

        
    @pyqtSignature("QString")
    def on_input_Zahlungsart_editTextChanged(self, p0):
        self.emit(SIGNAL('completeChanged()'))
    
#--------------------------------------------------------------------------------------------------
#ENDE
#--------------------------------------------------------------------------------------------------
        
        
    def calcNetto(self):
        
        if len(self.bruttoCent) > 0 and len(self.bruttoEuro) > 0:
            brutto = self.bruttoEuro+'.'+self.bruttoCent
            brutto = float(brutto)
            netto = round(float(brutto/119*100), 2)
            netto = str(netto).split('.')
            nettoEuro= netto[0]
            nettoCent= netto[1]
            
            self.input_Betrag_Netto_E.setText(nettoEuro)
            self.input_Betrag_Netto_C.setText(nettoCent)

    def calcBrutto(self):
        
        if len(self.nettoCent) > 0 and len(self.nettoEuro) > 0:
            netto = self.nettoEuro+'.'+self.nettoCent
            netto = float(netto)
            brutto = round(float(netto/100*119), 2)
            brutto = str(brutto).split('.')
            bruttoEuro= brutto[0]
            bruttoCent= brutto[1]
            
            self.input_Betrag_Brutto_E.setText(bruttoEuro)
            self.input_Betrag_Brutto_C.setText(bruttoCent)
            
            
        
    def setStyle(self):
        a = QtGui.QStyleFactory.keys()[5]
        b = QtGui.QStyleFactory.create(a)
        self.input_anzahlPos.setStyle(b)
        
        
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
            maxNr = Belege.objects.filter(datum__year=2012).aggregate(Max('nr'))
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
        
    
    def setValues(self, beleg_object):
        self.beleg_object = beleg_object
        
        
    def run(self):
        try:
            self.signal.startLoading(self)
            
            self.emit(
                SIGNAL('addEditWerte'), 
                {
                    'nr': self.beleg_object.nr, 
                    'datum': self.beleg_object.datum,
                    'lieferant': self.beleg_object.lieferant, 
                    'zahlungsart': self.beleg_object.zahlungsart, 
                    'brutto': self.beleg_object.brutto, 
                    'netto': self.beleg_object.netto, 
                    'anzahl_artikel': self.beleg_object.anzahl_artikel, 
                }
                )

            self.signal.finishedLoading(self)
            
        except Exception, err:
            self.signal.killLoading(self)
            if err.__class__.__name__ == 'OperationalError':
                self.emit(SIGNAL('connect_error'), self)
            else:
                self.emit(SIGNAL('error'), self, err)
    



class Load_ComboBox(QThread):
    
    def __init__(self):
        QThread.__init__(self)
        
        self.signal = Signal()
        self.signal.registerLoading(self)
        
        
    def run(self):
        try:
            self.signal.startLoading(self)
            
            belege = Belege.objects.all()
            
            lieferantList = belege.values_list('lieferant').distinct().order_by('lieferant')
            zahlungsartList = belege.values_list('zahlungsart').distinct().order_by('zahlungsart')
            
            for entry in lieferantList:
                self.emit(SIGNAL('addComboBoxItem'), ['lieferant', entry[0]])
    
            for entry in zahlungsartList:
                self.emit(SIGNAL('addComboBoxItem'), ['zahlungsart', entry[0]])
                
            self.signal.finishedLoading(self)
            
        except Exception, err:
            self.signal.killLoading(self)
            if err.__class__.__name__ == 'OperationalError':
                self.emit(SIGNAL('connect_error'), self)
            else:
                self.emit(SIGNAL('error'), self, err)


        
    

