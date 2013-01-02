# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QWidget
from PyQt4.QtCore import pyqtSignature

from Ui_start import Ui_Form

from Lib.saveSettings import SaveSettings
from Ui.Setting_Widgets.datenbank import Settings_Datenbank

_fromUtf8 = QtCore.QString.fromUtf8


class Start(QWidget, Ui_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QWidget.__init__(self, parent)
        self.setupUi(self)
        
        self.loadUI()
        
        
    def loadUI(self):
        self.identifyerDict = {}
        self.restart = False
        QtGui.QMessageBox.information(self, _fromUtf8('Hinweis'), _fromUtf8('Keine Datenbank gefunden !\n\nWähle erst eine Datenbank aus oder erstelle eine neue !\n'), 'OK')  
        self.db_widget = Settings_Datenbank()
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.addWidget(self.db_widget)
        
    
    @pyqtSignature("")
    def on_pushButton_ok_clicked(self):
        self.identifyerDict[self.db_widget.identifyer] = self.db_widget.getWerte()
        SaveSettings().save(self.identifyerDict)
        self.restart = True
        self.close()
        

    
    @pyqtSignature("")
    def on_pushButton_abbrechen_clicked(self):
        self.close()

