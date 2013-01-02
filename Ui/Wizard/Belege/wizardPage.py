# -*- coding: utf-8 -*-


from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QThread
from PyQt4.QtGui import QWizardPage
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtCore import SIGNAL

from Ui_wizardPage import Ui_WizardPage

from Lib.loadSettings import LoadSettings
from Lib.tools import Tools
from Orm.db.models import *
from signalReceiver import Signal
from Ui.messageBox import MessageBox


_fromUtf8 = QtCore.QString.fromUtf8


class WizardPage(QWizardPage, Ui_WizardPage):

    def __init__(self, parent = None):

        QWizardPage.__init__(self, parent)
        self.setupUi(self)
        
        self.messageBox = MessageBox(self)
        self.loadSettings = LoadSettings()
        self.tools = Tools()
        
        self.visited = False
        self.bruttoCent = ''
        self.bruttoEuro =''
        self.nettoCent = ''
        self.nettoEuro =''
        
        self.connect(self, SIGNAL('Brutto'), self.calcNetto)
        self.connect(self, SIGNAL('Netto'), self.calcBrutto)
        
        
    def nextId(self):
        
        if int(self.field('AnzahlPos').toString()) == self.wizard().currentId():
            return 11
        else:
            return self.wizard().currentId() + 1
            
            
    def cleanupPage(self):
        self.visited = True


            
    def initializePage(self):
        self.initialize_Threads()
        
        if self.option == False:
            if self.visited == False:
                self.loadComboBox.start()

        else:
            self.identifyOption()
        self.setPageTitle()
        
        
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
                self.loadComboBox.start()
                self.loadWerte.setValues(self.option[identifier])
                self.loadWerte.start()
                
                
            if identifier == 'Edit':
                self.loadComboBox.start()
                self.loadEditWerte.setValues(self.option[identifier], self.wizard().currentId())
                self.loadEditWerte.start()



    def validatePage(self):
        
        betragBrutto = float(0)
        betragNetto = float(0)
        
        if int(self.field('AnzahlPos').toString()) == self.wizard().currentId():
            
            for i in range(1, int(self.field('AnzahlPos').toString())+1):
                count = str(i)
                betragBrutto = betragBrutto + float(self.field('Betrag_Brutto_E_'+count).toString()+'.'+self.field('Betrag_Brutto_C_'+count).toString())
                betragNetto = betragNetto + float(self.field('Betrag_Netto_E_'+count).toString()+'.'+self.field('Betrag_Netto_C_'+count).toString())
                
            print betragBrutto
            print betragNetto
            
            if betragNetto == float(self.field('Betrag_Netto_E').toString()+'.'+self.field('Betrag_Netto_C').toString()):
                return True
                
            elif betragBrutto == float(self.field('Betrag_Brutto_E').toString()+'.'+self.field('Betrag_Brutto_C').toString()):
                return True
                
            else:
                QtGui.QMessageBox.information(self, _fromUtf8('Hinweis'), _fromUtf8(
                '''Die Summe aller Beträge entspricht nicht dem Gesamtbetrag !\n\nBitte Beträge prüfen !'''
                ), 'OK')
                return False
        
        else:
        
            return True


    def register(self, count):
        self.registerField('Bezeichnung_'+count, self.input_Bezeichnung, 'currentText', SIGNAL('editTextChanged()'))
        self.registerField('Betrag_Netto_E_'+count, self.input_Betrag_Netto_E, 'text', SIGNAL('textChanged()'))
        self.registerField('Betrag_Netto_C_'+count, self.input_Betrag_Netto_C, 'text', SIGNAL('textChanged()'))
        self.registerField('Betrag_Brutto_E_'+count, self.input_Betrag_Brutto_E, 'text', SIGNAL('textChanged()'))
        self.registerField('Betrag_Brutto_C_'+count, self.input_Betrag_Brutto_C, 'text', SIGNAL('textChanged()'))
        self.registerField('Menge_'+count, self.input_Menge, 'text', SIGNAL('textChanged()'))
        self.registerField('Einheit_'+count, self.input_Einheit, 'currentText', SIGNAL('editTextChanged()'))
        self.registerField('Status_'+count, self.input_Status, 'currentText', SIGNAL('activated()'))


        
    def setProject(self, projekt):
        self.input_Projekt.setText(projekt.name)
        self.wizard().projekt = projekt
        
 
    def addWerte(self, werte):
        self.setProject(werte)
        
        

    def addComboBoxItem(self, item):
        if item[0] == 'bezeichnung':
            self.input_Bezeichnung.addItem(item[1])
        if item[0] == 'einheit':
            self.input_Einheit.addItem(item[1])
            


    def addEditWerte(self, dict):
        self.input_Bezeichnung.setEditText(dict['bezeichnung'])
        self.input_Menge.setText(str(dict['menge']))
        self.input_Einheit.setEditText(dict['einheit'])
        self.input_Betrag_Brutto_E.setText(str(dict['brutto']).split('.')[0])
        self.input_Betrag_Brutto_C.setText(str(dict['brutto']).split('.')[1])
        self.input_Betrag_Netto_E.setText(str(dict['netto']).split('.')[0])
        self.input_Betrag_Netto_C.setText(str(dict['netto']).split('.')[1])
        self.setProject(dict['projekt'])
        self.input_Status.setCurrentIndex(self.getStatus(dict['status']))
        

        
    def getStatus(self, status):
        if status == 'Offen':
            return 0
        if status == 'Abgerechnet':
            return 1
        if status == 'Geld erhalten':
            return 2
        
    
    def setPageTitle(self):
        self.setTitle(_fromUtf8('Artikel '+str(self.wizard().currentId())))
        self.label_artikelnr.setText(_fromUtf8('Artikel  '  +str(self.wizard().currentId())))
        
        
    def isComplete(self):
        check = False
        
        if len(self.input_Bezeichnung.currentText()) > 0:
            check = True
        else:
            return False
            
        if len(self.input_Menge.text()) > 0:
            check = True
        else:
            return False
            
        if len(self.input_Einheit.currentText()) > 0:
            check = True
        else:
            return False
            
        if len(self.input_Projekt.text()) > 0:
            check = True
        else:
            return False
            
        if len(self.input_Status.currentText()) > 0:
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
    def on_input_Bezeichnung_editTextChanged(self, p0):
        self.emit(SIGNAL('completeChanged()'))

        
    @pyqtSignature("QString")
    def on_input_Einheit_editTextChanged(self, p0):
        self.emit(SIGNAL('completeChanged()'))
        
    @pyqtSignature("QString")
    def on_input_Menge_textChanged(self, p0):
        self.emit(SIGNAL('completeChanged()'))
        
    @pyqtSignature("QString")
    def on_input_Projekt_textChanged(self, p0):
        self.emit(SIGNAL('completeChanged()'))
        
    @pyqtSignature("QString")
    def on_input_Bezeichnung_activated(self, p0):
        self.emit(SIGNAL('completeChanged()'))
        
        
    @pyqtSignature("")
    def on_toolButton_Projekt_clicked(self):
        from Ui.Projekte.searchWindow import SearchProject
        self.projects = SearchProject(self)
        self.projects.show()
    
#--------------------------------------------------------------------------------------------------
#ENDE
#--------------------------------------------------------------------------------------------------

    def calcNetto(self):
        
        if len(self.bruttoCent) > 0 and len(self.bruttoEuro) > 0:
            brutto = self.bruttoEuro+'.'+self.bruttoCent
            brutto = float(brutto)
            netto = round(float(brutto/119*100), 2)
            netto = str(netto).split('.')
            self.nettoEuro= netto[0]
            self.nettoCent= netto[1]
            
            self.input_Betrag_Netto_E.setText(self.nettoEuro)
            self.input_Betrag_Netto_C.setText(self.nettoCent)
            self.emit(SIGNAL('completeChanged()'))

    def calcBrutto(self):
        
        if len(self.nettoCent) > 0 and len(self.nettoEuro) > 0:
            netto = self.nettoEuro+'.'+self.nettoCent
            netto = float(netto)
            brutto = round(float(netto/100*119), 2)
            brutto = str(brutto).split('.')
            self.bruttoEuro= brutto[0]
            self.bruttoCent= brutto[1]
            
            self.input_Betrag_Brutto_E.setText(self.bruttoEuro)
            self.input_Betrag_Brutto_C.setText(self.bruttoCent)
            self.emit(SIGNAL('completeChanged()'))
            
            
            
#--------------------------------------------------------------------------------------------------
#Style Optionen
#--------------------------------------------------------------------------------------------------
            
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
        
    def setValues(self, projekt_object):
        self.projekt_object = projekt_object
        
        
    def run(self):
        try:
            self.signal.startLoading(self)
            
            self.emit(SIGNAL('addWerte'), self.projekt_object)
            
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
        
    
    def setValues(self, beleg_object, currentId):
        self.beleg_object = beleg_object
        self.currentId = currentId
        
        
    def run(self):
        try:
            self.signal.startLoading(self)
            
            q = Belege_Details.objects.filter(nr=self.beleg_object)

            beleg_detail = q[self.currentId-1]
 
            
            self.emit(
                SIGNAL('addEditWerte'), 
                {
                    'bezeichnung': beleg_detail.bezeichnung, 
                    'menge': beleg_detail.menge,
                    'einheit': beleg_detail.einheit, 
                    'brutto': beleg_detail.brutto, 
                    'netto': beleg_detail.netto, 
                    'projekt': beleg_detail.projekt, 
                    'status': beleg_detail.get_status_display(), 
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
            
            belege_details = Belege_Details.objects.all()
            
            bezeichnungList = belege_details.values_list('bezeichnung').distinct().order_by('bezeichnung')
            einheitList = belege_details.values_list('einheit').distinct().order_by('einheit')
            
            for entry in bezeichnungList:
                self.emit(SIGNAL('addComboBoxItem'), ['bezeichnung', entry[0]])
    
            for entry in einheitList:
                self.emit(SIGNAL('addComboBoxItem'), ['einheit', entry[0]])
                
            self.signal.finishedLoading(self)
            
        except Exception, err:
            self.signal.killLoading(self)
            if err.__class__.__name__ == 'OperationalError':
                self.emit(SIGNAL('connect_error'), self)
            else:
                self.emit(SIGNAL('error'), self, err)




