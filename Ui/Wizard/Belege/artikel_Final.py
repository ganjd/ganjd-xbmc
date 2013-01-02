# -*- coding: utf-8 -*-

from PyQt4 import QtCore
from PyQt4.QtGui import QWidget
from PyQt4.QtCore import pyqtSignature

from Ui_artikel_Final import Ui_Form


from Lib.tools import Tools


_fromUtf8 = QtCore.QString.fromUtf8


class Artikel_Final(QWidget, Ui_Form):

    def __init__(self, artikelnr, dict_Details):

        QWidget.__init__(self)
        self.setupUi(self)
        
        self.tools = Tools()
        
        self.dict_Details = dict_Details
        
        self.groupBox.setTitle('Artikel '+artikelnr)
        
        self.setWerte()
        
        
        
    def setWerte(self):
        self.label_Bezeichnung.setText(_fromUtf8(u'Bezeichnung:   '+self.dict_Details['Bezeichnung']))
        self.label_Kunde.setText(_fromUtf8('Kunde:   '+self.tools.formatKunde(self.dict_Details['Projekt'].kunde)))
        self.label_Projekt.setText(_fromUtf8('Projekt:   '+str(self.dict_Details['Projekt'].nr)))
        self.label_Menge.setText(_fromUtf8('Menge:   '+str(self.dict_Details['Menge'])+'  '+self.dict_Details['Einheit']))
        self.label_Betrag_Netto.setText(_fromUtf8('Betrag Netto:   '+str(self.dict_Details['Betrag_Netto'])+'  €'))
        self.label_Betrag_Brutto.setText(_fromUtf8('Betrag Brutto:   '+str(self.dict_Details['Betrag_Brutto'])+'  €'))
        self.label_Status.setText(_fromUtf8('Status:   '+self.longStatusName(self.dict_Details['Status'])))
        
    
    def longStatusName(self, status):
        if status == 'O':
            return 'Offen'
        if status == 'A':
            return 'Abgerechnet'
        if status == 'G':
            return 'Geld erhalten'
            
        return ''

        
