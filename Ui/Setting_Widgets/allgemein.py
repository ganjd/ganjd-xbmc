# -*- coding: utf-8 -*-


from PyQt4 import QtGui
from PyQt4.QtGui import QWidget
from PyQt4.QtCore import pyqtSignature

from Ui_allgemein import Ui_Form

from Lib.loadSettings import LoadSettings

IDENTIFYER = 'Allgemein'

class Settings_Allgemein(QWidget, Ui_Form):

    def __init__(self):

        QWidget.__init__(self)
        self.setupUi(self)
        
        self.identifyer = IDENTIFYER
        
        self.setWerte()
        
        
        
    def setWerte(self):
        
        self.loadWerte()
        
        styles= QtGui.QStyleFactory.keys()
        
        for i, style in enumerate(styles):
           self.comboBox.addItem(style)
           if style == self.style:
               index = i
        self.comboBox.setCurrentIndex(index)
        
        self.lineEdit_user.setText(self.user)
        
        

    
    @pyqtSignature("QString")
    def on_comboBox_activated(self, p0):
        self.style = p0
        
    @pyqtSignature("QString")
    def on_lineEdit_user_textChanged(self, user):
        self.user = user

       
       
    def getWerte(self):
        werte = {'style': self.style, 'user': self.user}
        return werte
        
        
    def loadWerte(self):
        self.style = LoadSettings().style()
        self.user = LoadSettings().user()
    

