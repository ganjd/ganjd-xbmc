# -*- coding: utf-8 -*-


from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWizardPage
from PyQt4.QtCore import pyqtSignature

from Ui_wizardFinalPage import Ui_WizardPage
from ak_Final import Ak_Final

from Lib.tools import Tools


_fromUtf8 = QtCore.QString.fromUtf8


class WizardFinalPage(QWizardPage, Ui_WizardPage):

    def __init__(self, parent = None):

        QWizardPage.__init__(self, parent)
        self.setupUi(self)
        
        self.tools = Tools() 
        
        self.posDict_Main = {}


    def initializePage(self):
        self.clear()
        
        projektnr = self.wizard().projekt
        posid = self.wizard().datum+':'+self.wizard().projekt+':'+self.wizard().anzahlak
        anzahlpos = self.field('AnzahlPos').toString()
        
        self.posDict_Main['Projektnr'] = projektnr
        self.posDict_Main['Id'] = posid
        self.posDict_Main['AnzahlPos'] = anzahlpos
        
        
        self.posList_Details = []
        for i in range(0, int(self.field('AnzahlPos').toString())):
            count = str(i)
            
            exec 'posnr = self.wizard().posnr_' + count
            exec 'posDict_Details = self.wizard().posDict_' + str(posnr)
            
            posDict_Details['Posnr'] = str(posnr)
            
            self.posList_Details.append(posDict_Details)
            self.addAkWidget(posnr, posDict_Details)
            
        self.getWerte(projektnr, anzahlpos)
        
            
            
    def getWerte(self, projektnr, anzahlpos):
        
        self.label_datum.setText(_fromUtf8('Datum:   '+self.wizard().datum))
        self.label_anzahlpos.setText(_fromUtf8('Anzahl der Positionen:   '+anzahlpos))
        self.label_kunde.setText(_fromUtf8('Kunde:   '+self.tools.getKundeFromNr(self.wizard().kunde)))
        self.label_projekt.setText(_fromUtf8('Projekt:   '+self.tools.getProjektFromNr(projektnr)))
        

        
    def addAkWidget(self, posnr, posDict_Details):

        self.ak = Ak_Final(str(posnr), posDict_Details['Details'])
        self.verticalLayout_4.addWidget(self.ak)
        
    def clear(self):
        
        self.scrollAreaWidgetContents.close()
        
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 754, 391))

        self.verticalLayout_4 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)




        

        

        
        
