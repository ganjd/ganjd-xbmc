# -*- coding: utf-8 -*-

from PyQt4.QtCore import QThread
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWizardPage
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtCore import SIGNAL

from Ui_wizardFinalPage import Ui_WizardPage
from artikel_Final import Artikel_Final

from Orm.db.models import *
from Lib.tools import Tools
from signalReceiver import Signal
from Ui.messageBox import MessageBox


_fromUtf8 = QtCore.QString.fromUtf8


class WizardFinalPage(QWizardPage, Ui_WizardPage):

    def __init__(self, parent = None):

        QWizardPage.__init__(self, parent)
        self.setupUi(self)
        
        self.tools = Tools() 
        self.messageBox = MessageBox(self)
    
        self.initialize_Threads()
        self.validate = False
        
        self.dict_Main = {}
        

    def initialize_Threads(self):
        self.saveBeleg = Save_Beleg()
        self.connect(self.saveBeleg, SIGNAL('savingFinished'), self.savingFinished)
        self.connect(self.saveBeleg, SIGNAL('connect_error'), self.connect_error)
        self.connect(self.saveBeleg, SIGNAL('error'), self.error)


    def initializePage(self):
        self.clear()
        
        self.dict_Main['Belegnr'] = self.field('Belegnr').toInt()[0]
        self.dict_Main['Datum'] = self.field('Datum').toDate().toPyDate()
        self.dict_Main['Lieferant'] = self.field('Lieferant').toString().toUtf8()
        self.dict_Main['Zahlungsart'] = self.field('Zahlungsart').toString().toUtf8()
        self.dict_Main['Betrag_Netto'] = float(self.field('Betrag_Netto_E').toString()+'.'+self.field('Betrag_Netto_C').toString())
        self.dict_Main['Betrag_Brutto'] = float(self.field('Betrag_Brutto_E').toString()+'.'+self.field('Betrag_Brutto_C').toString())
        self.dict_Main['AnzahlPos'] = self.field('AnzahlPos').toInt()[0]
        
        
        self.list_Details = []
        for i in range(1, int(self.field('AnzahlPos').toString())+1):
            count = str(i)
            
            dict_Details = {}
            dict_Details['Bezeichnung'] = self.field('Bezeichnung_'+count).toString().toUtf8()
            dict_Details['Projekt'] = self.wizard().projekt
            dict_Details['Betrag_Brutto'] = float(self.field('Betrag_Brutto_E_'+count).toString() + '.' + self.field('Betrag_Brutto_C_'+count).toString())
            dict_Details['Betrag_Netto'] = float(self.field('Betrag_Netto_E_'+count).toString() + '.' + self.field('Betrag_Netto_C_'+count).toString())
            dict_Details['Menge'] = self.field('Menge_'+count).toFloat()[0]
            dict_Details['Einheit'] = self.field('Einheit_'+count).toString().toUtf8()
            dict_Details['Status'] = self.tools.shortStatusName(self.field('Status_'+count).toString().toUtf8())
            

            self.list_Details.append(dict_Details)
            self.addArtikelWidget(count, dict_Details)
            
        self.setWerte()
        
        print self.dict_Main
        print self.list_Details
        

    def setWerte(self):
        
        self.label_belegnr.setText(_fromUtf8('Beleg Nr.:   '+self.tools.formatBelegNr(self.dict_Main['Belegnr'])))
        self.label_datum.setText(_fromUtf8('Datum:   '+self.tools.formatDatum(self.dict_Main['Datum'])))
        self.label_Lieferant.setText(_fromUtf8('Lieferant:   '+self.dict_Main['Lieferant']))
        self.label_Zahlungsart.setText(_fromUtf8('Zahlungsart:   '+self.dict_Main['Zahlungsart']))
        self.label_Gesamtbetrag_Netto.setText(_fromUtf8('Gesamtbetrag Netto:   '+str(self.dict_Main['Betrag_Netto'])+'  €'))
        self.label_Gesamtbetrag_Brutto.setText(_fromUtf8('Gesamtbetrag Brutto:   '+str(self.dict_Main['Betrag_Brutto'])+'  €'))
        


    def addArtikelWidget(self, artikelnr, dict_Details):

        self.ak = Artikel_Final(artikelnr, dict_Details)
        self.verticalLayout_4.addWidget(self.ak)
        
        
    def clear(self):
        
        self.scrollAreaWidgetContents.close()
        
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 754, 391))

        self.verticalLayout_4 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        

    def setOption(self, option):
        self.option = option
    
        
    def savingFinished(self):
        self.validate = True
        self.wizard().next()
        
    
    def validatePage(self):
        if not self.validate:
            self.saveBeleg.setValues(self.dict_Main, self.list_Details, self.option)
            self.saveBeleg.start()
        return self.validate


    def connect_error(self, sender):
        reply = self.messageBox.connect_error()
        if reply:
            sender.start()

    def error(self, sender, err):
        reply = self.messageBox.error({'err': err, 'sender': sender})
        

class Save_Beleg(QThread):
    
    def __init__(self):
        QThread.__init__(self)
        
        self.signal = Signal()
        self.signal.registerLoading(self)
        
    
    def setValues(self, input_main, input_details, option):
        self.input_main = input_main
        self.input_details = input_details
        self.option = option
        
    def run(self):
        try:
            self.signal.startLoading(self)
            
            input_main = self.input_main
            input_details = self.input_details
            update = False
            
            #Save or Update A_Tag
            if self.option != False:
                for identifier in self.option.keys():
                    if identifier == 'Edit':
                        beleg = self.option[identifier]
                        beleg.nr = input_main['Belegnr']
                        beleg.datum = input_main['Datum']
                        beleg.lieferant = input_main['Lieferant']
                        beleg.zahlungsart = input_main['Zahlungsart']
                        beleg.brutto = input_main['Betrag_Brutto']
                        beleg.netto = input_main['Betrag_Netto']
                        beleg.anzahl_artikel = anzahl_artikel = input_main['AnzahlPos']
                        update = True
            
    
            if not update:
                beleg = Belege(
                    nr = input_main['Belegnr'], 
                    datum = input_main['Datum'], 
                    lieferant = input_main['Lieferant'], 
                    zahlungsart = input_main['Zahlungsart'], 
                    brutto = input_main['Betrag_Brutto'], 
                    netto = input_main['Betrag_Netto'], 
                    anzahl_artikel = input_main['AnzahlPos'], 
                    )
            
            beleg.save()
            
            if update:
                for entry in Belege_Details.objects.filter(nr=beleg):
                    entry.delete()
            
    
            for i, details in enumerate(input_details):
    
                beleg_detail = Belege_Details(
                    nr = beleg, 
                    bezeichnung = details['Bezeichnung'], 
                    menge = details['Menge'], 
                    einheit = details['Einheit'], 
                    brutto = details['Betrag_Brutto'], 
                    netto = details['Betrag_Netto'], 
                    projekt = details['Projekt'], 
                    status = details['Status'], 
                    )
                    
                beleg_detail.save()
            
            self.signal.finishedLoading(self)
            self.emit(SIGNAL('savingFinished'))
                
        except Exception, err:
            self.signal.killLoading(self)
            if err.__class__.__name__ == 'OperationalError':
                self.emit(SIGNAL('connect_error'), self)
            else:
                self.emit(SIGNAL('error'), self, err)
        
        
        

