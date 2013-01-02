# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QWizard
from PyQt4.QtCore import QObject
from PyQt4.QtCore import QThread

from Orm.db.models import *

from Lib.tools import Tools

from Lib.loadSettings import LoadSettings


_fromUtf8 = QtCore.QString.fromUtf8



class Wizard(QObject):

    def __init__(self, identifyer=False, option=False):
        
        QObject.__init__(self)
        
        self.Identifyer = identifyer
        self.option = option
        self.identify()
        self.wizardProperties()

        
    def wizardProperties(self):
        if self.Identifyer == False:
            return
            
        self.wizard.setWizardStyle(QtGui.QWizard.ModernStyle)
        self.wizard.setButtonText(0, _fromUtf8('Zurück'))
        self.wizard.setButtonText(1, _fromUtf8('Weiter'))
        self.wizard.setButtonText(4, _fromUtf8('Abbrechen'))
        self.wizard.setButtonText(3, _fromUtf8('Fertig'))
        
        self.wizard.addPages()
        self.wizard.restart()
        self.wizard.exec_()
        self.result = self.wizard.result
        

    
    def identify(self):

        if self.Identifyer == 'AS':
            self.wizard = AS_Wizard(self.option)
            self.wizard.resize(772, 505)
            self.wizard.setWindowTitle(_fromUtf8('Arbeitsstunden - Wizard'))
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/res/1318969250_gnome-planner.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.wizard.setWindowIcon(icon)
                
            
        elif self.Identifyer == 'Material':
            self.wizard = Material_Wizard(self.option)
            self.wizard.resize(772, 505)
            self.wizard.setWindowTitle(_fromUtf8('Material - Wizard'))
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/res/1318969228_applications-development.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.wizard.setWindowIcon(icon)
            
        elif self.Identifyer == 'Projekt':
            self.wizard = Project_Wizard(self.option)
            self.wizard.resize(772, 505)
            self.wizard.setWindowTitle(_fromUtf8('Projekt - Wizard'))
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/res/1318968798_add-folder-to-archive.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.wizard.setWindowIcon(icon)
            
        elif self.Identifyer == 'Kunde':
            self.wizard = Kunden_Wizard(self.option)
            self.wizard.resize(850, 505)
            self.wizard.setWindowTitle(_fromUtf8('Kunden - Wizard'))
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/res/1318968748_human-folder-public.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.wizard.setWindowIcon(icon)
            
        elif self.Identifyer == 'Position':
            self.wizard = Position_Wizard(self.option)
            self.wizard.resize(930, 650)
            self.wizard.setWindowTitle(_fromUtf8('Positionen - Wizard'))
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/res/1318968719_x-office-spreadsheet.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.wizard.setWindowIcon(icon)
            
        elif self.Identifyer == 'Beleg':
            self.wizard = Beleg_Wizard(self.option)
            self.wizard.resize(850, 550)
            self.wizard.setWindowTitle(_fromUtf8('Belege - Wizard'))
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/res/1318968719_x-office-spreadsheet.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.wizard.setWindowIcon(icon)
            
        else:
            self.Identifyer = False
            print 'Falscher Identifyer'
    
    
    

class AS_Wizard(QWizard):
    

    
    def __init__(self, option):
        QWizard.__init__(self)
        self.option = option


    def addPages(self):
        from AKs.wizardPage import WizardPage
        from AKs.wizardStartPage import WizardStartPage
        from AKs.wizardFinalPage import WizardFinalPage
        from wizardLastPage import WizardLastPage
        
        self.startPage = WizardStartPage()
        self.startPage.register()
        self.startPage.setOption(self.option)
        self.setPage(0, self.startPage)
        
        for i in range(1, 11):
            self.page = WizardPage()
            self.page.register(str(i))
            self.page.setOption(self.option)
            self.setPage(i, self.page)
            
        self.finalPage = WizardFinalPage()
        self.finalPage.setOption(self.option)
        self.addPage(self.finalPage)
        
        self.lastPage = WizardLastPage()
        self.addPage (self.lastPage)
    
    
    def done(self, result):
        self.hide()
        self.result = result
        


class Project_Wizard(QWizard):
    
    def __init__(self, option):
        QWizard.__init__(self)
        self.option= option
        
        self.beschreibung = ''
        self.status = ''
        self.kunde = None


    def addPages(self):
        from Projects.wizardStartPage import WizardStartPage
        from Projects.wizardFinalPage import WizardFinalPage
        from wizardLastPage import WizardLastPage
        
        self.startPage = WizardStartPage()
        self.startPage.register()
        self.startPage.setOption(self.option)
        self.setPage(0, self.startPage)
        
        self.finalPage = WizardFinalPage()
        self.finalPage.setOption(self.option)
        self.addPage(self.finalPage)
        
        self.lastPage = WizardLastPage()
        self.addPage(self.lastPage)
        

    def done(self, result):
        self.hide()
        self.result = result
        
        


class Kunden_Wizard(QWizard):
    
    def __init__(self, option):
        QWizard.__init__(self)
        self.option= option

    def addPages(self):
        from Kunde.wizardStartPage import WizardStartPage
        from Kunde.wizardFinalPage import WizardFinalPage
        from wizardLastPage import WizardLastPage
        
        self.startPage = WizardStartPage()
        self.startPage.register()
        self.startPage.setOption(self.option)
        self.setPage(0, self.startPage)
        
        self.finalPage = WizardFinalPage()
        self.finalPage.setOption(self.option)
        self.addPage(self.finalPage)
        
        self.lastPage = WizardLastPage()
        self.addPage(self.lastPage)
        
        
    def done(self, result):
        self.hide()
        self.result = result




class Beleg_Wizard(QWizard):
    
    def __init__(self, option):
        QWizard.__init__(self)
        self.option = option
        
        self.betragNetto = float(0)
        self.betragBrutto = float(0)


    def addPages(self):
        from Belege.wizardPage import WizardPage
        from Belege.wizardStartPage import WizardStartPage
        from Belege.wizardFinalPage import WizardFinalPage
        from wizardLastPage import WizardLastPage
        
        self.editStatus = False
        
        self.startPage = WizardStartPage()
        self.startPage.register()
        self.startPage.setOption(self.option)
        self.setPage(0, self.startPage)
        
        for i in range(1, 11):
            self.page = WizardPage()
            self.page.register(str(i))
            self.page.setOption(self.option)
            self.setPage(i, self.page)
            
        self.finalPage = WizardFinalPage()
        self.finalPage.setOption(self.option)
        self.addPage(self.finalPage)
        
        self.lastPage = WizardLastPage()
        self.addPage(self.lastPage)
    
    
    def done(self, result):
        self.hide()
        self.result = result
        




#class Position_Wizard(QWizard):
#    
#    def __init__(self, option):
#        QWizard.__init__(self)
#        
#        self.loadSettings = LoadSettings()
#        self.option= option
#        self.sqllite = ConnectDB()
#        self.tools = Tools()
#        self.resize(900, 700)
#
#
#    def addPages(self):
#        
#        from Position.wizardStartPage import WizardStartPage
#        from Position.wizardPage import WizardPage
#        from Position.wizardFinalPage import WizardFinalPage
#        
#        self.startPage = WizardStartPage()
#        self.startPage.register()
#        self.startPage.setOption(self.option)
#        self.setPage(0, self.startPage)
#        
#        for i in range(1, 11):
#            self.page = WizardPage()
##            self.page.register(str(i))
#            self.setPage(i, self.page)
#            
#        self.finalPage = WizardFinalPage()
#        self.addPage(self.finalPage)
#        
#
#    def done(self, result):
#        if result == 1:
#            self.getWizardInput()
#            
#        self.hide()
#        
#    def getWizardInput(self):
#        
#        input_main = self.finalPage.posDict_Main
#        input_details = self.finalPage.posList_Details
#        
#        
#        id = self.tools.getEncodedString(input_main['Id'])
#        projektnr = self.tools.getEncodedString(input_main['Projektnr'])
#        anzahlpos = self.tools.getEncodedString(input_main['AnzahlPos'])
#
#        
#        for entry in input_details:
#            posnr = self.tools.getEncodedString(entry['Posnr'])
#            for entry in entry['Details']:
#                beschreibung = self.tools.getEncodedString(entry[0])
#                ak = self.tools.getEncodedString(entry[1])
#                stunden = self.tools.getEncodedString(entry[2])
#                minuten = self.tools.getEncodedString(entry[3])
#                rowId = entry[4]
#                
#                if rowId != False:
#                    posWerte = (id, projektnr, anzahlpos, posnr, beschreibung, ak, stunden, minuten, rowId)
#                    self.writeToPositionen(posWerte, update=True)
#                else:
#                    posWerte = (id, projektnr, anzahlpos, posnr, beschreibung, ak, stunden, minuten)
#                    self.writeToPositionen(posWerte)
#                    
#                
#        if self.editStatus != False:
#            if int(self.old_anzahlpos) > int(anzahlpos):
#    
#                for i in range(int(anzahlpos), int(self.old_anzahlpos)):
#                    del_posnr = str(i + 1)
#                    self.deletePos(id, del_posnr)
#                
#                
#    def writeToPositionen(self, posWerte, update=False):
#        
#        self.sqllite.connect(self.loadSettings.db_Position())
#        
#        if update != False:
#            self.sqllite.execute('''UPDATE pos SET 
#            sId=?,
#            sProjekt=?,
#            sAnzahlpos=?,
#            sPosnr=?,
#            sBeschreibung=?,
#            sAk=?,
#            sStunden=?,
#            sMinuten=?
#            WHERE rowId=?''', posWerte)
#            
#        else:
#            
#            self.sqllite.execute('INSERT INTO pos VALUES(?,?,?,?,?,?,?,?)', posWerte)
#        
#        self.sqllite.commit()
#        self.sqllite.close()
#        
#    def deletePos(self, id, posnr):
#        self.sqllite.connect(self.loadSettings.db_Position())
#        self.sqllite.execute('DELETE FROM pos WHERE sId=? AND sPosnr=?', (id, posnr))
#        self.sqllite.commit()
#        self.sqllite.close()
        


