# -*- coding: utf-8 -*-

import os
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtCore import QSettings

from Ui_datenbank import Ui_Form

from Lib.loadSettings import LoadSettings
from createDB.createDB import CreateDB


IDENTIFYER = 'Datenbank'

_fromUtf8 = QtCore.QString.fromUtf8


class Settings_Datenbank(QWidget, Ui_Form):

    def __init__(self, parent = None):

        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.identifyer = IDENTIFYER
        
        self.setWerte()
    
    @pyqtSignature("QString")
    def on_lineEdit_textChanged(self, path):
        self.DB_Path = path

    
    @pyqtSignature("")
    def on_toolButton_clicked(self):
        
        dir = QtGui.QFileDialog.getExistingDirectory(self, "Open Directory", os.getcwd(), QtGui.QFileDialog.ShowDirsOnly| QtGui.QFileDialog.DontResolveSymlinks)
        if len(dir) > 0:
            self.lineEdit.setText(dir)
        
        
    def setWerte(self):
        self.loadWerte()
        
        self.label_2.hide()
        self.lineEdit_path_new.hide()
        self.toolButton_2.hide()
        self.commandLinkButton_create.hide()
        self.toolButton_hide.hide()
        
        self.lineEdit.setText(self.DB_Path)
        
        
    def getWerte(self):
        werte = {'path': self.DB_Path}
        return werte
        
        
    def loadWerte(self):
        self.DB_Path = LoadSettings().db_path()
    
    @pyqtSignature("")
    def on_commandLinkButton_neu_clicked(self):
        self.commandLinkButton_neu.hide()
        
        self.label_2.show()
        self.lineEdit_path_new.show()
        self.toolButton_2.show()
        self.commandLinkButton_create.show()
        self.commandLinkButton_create.setEnabled(False)
        self.toolButton_hide.show()
        

    @pyqtSignature("QString")
    def on_lineEdit_path_new_textChanged(self, path):
        self.DB_Path_Neu = path

    
    @pyqtSignature("")
    def on_toolButton_2_clicked(self):
        dir = QtGui.QFileDialog.getExistingDirectory(self, "Open Directory", os.getcwd(), QtGui.QFileDialog.ShowDirsOnly| QtGui.QFileDialog.DontResolveSymlinks)
        if len(dir) > 0:
            self.lineEdit_path_new.setText(dir)
            self.commandLinkButton_create.setEnabled(True)
        

    
    @pyqtSignature("")
    def on_commandLinkButton_create_clicked(self):
        
        settings = QSettings("GanjD-Soft", "GalaBau")
        settings.beginGroup("MainWindow")
        jahr = settings.value('jahr', 2011).toString()
        settings.endGroup()
        
        if os.path.isfile(os.path.join(str(self.DB_Path_Neu), str(jahr), 'project.sqlite')):
            QtGui.QMessageBox.information(self, _fromUtf8('Hinweis'), _fromUtf8('Datenbank schon vorhanden !\n\nWähle ein anderes Verzeichnis!\n'), 'OK') 
            return
            
        elif os.path.isfile(os.path.join(str(self.DB_Path_Neu), 'kunden.sqlite')):
            QtGui.QMessageBox.information(self, _fromUtf8('Hinweis'), _fromUtf8('Datenbank schon vorhanden !\n\nWähle ein anderes Verzeichnis!\n'), 'OK') 
            return
        
        elif os.path.isfile(os.path.join(str(self.DB_Path_Neu), str(jahr), 'position.sqlite')):
            QtGui.QMessageBox.information(self, _fromUtf8('Hinweis'), _fromUtf8('Datenbank schon vorhanden !\n\nWähle ein anderes Verzeichnis!\n'), 'OK')
            
        else:
            try:
                os.mkdir(os.path.join(str(self.DB_Path_Neu), str(jahr)))
            except:
                pass
            self.createDB = CreateDB()
            self.createDB.createProjekt(os.path.join(str(self.DB_Path_Neu), str(jahr)))
            self.createDB.createKunden(str(self.DB_Path_Neu))
            self.createDB.createPosition(os.path.join(str(self.DB_Path_Neu), str(jahr)))
            
            reply = QtGui.QMessageBox.question(self, _fromUtf8('Verzeichnis Wechseln'), _fromUtf8('Soll die neue Datenbank jetzt verwendet werden\n'), 'Ja', 'Nein')
            if reply == 0:
                self.lineEdit.setText(self.DB_Path_Neu)

            self.commandLinkButton_neu.show()

            self.label_2.hide()
            self.lineEdit_path_new.hide()
            self.toolButton_2.hide()
            self.commandLinkButton_create.hide()
            self.toolButton_hide.hide()
    

    
    @pyqtSignature("")
    def on_toolButton_hide_clicked(self):
        self.commandLinkButton_neu.show()
        
        self.label_2.hide()
        self.lineEdit_path_new.hide()
        self.toolButton_2.hide()
        self.commandLinkButton_create.hide()
        self.toolButton_hide.hide()

