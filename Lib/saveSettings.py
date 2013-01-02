# -*- coding: utf-8 -*-


from PyQt4.QtCore import QSettings
from PyQt4.QtCore import QVariant
from PyQt4 import QtCore



class SaveSettings:
    
    def __init__(self):

        self.wiederherstellen = False


    def create(self):
        self.allgemein()
        self.datenbank()
        self.arbeiter()
        

    def setStandard(self):
        self.wiederherstellen = True
        self.create()
        
        
    def save(self, identifyerDict):
        
        for identifyer in identifyerDict:
            werte = identifyerDict[identifyer]
        
            if identifyer == 'Allgemein':
                self.allgemein(werte)
            if identifyer == 'Datenbank':
                self.datenbank(werte)
            if identifyer == 'Arbeiter':
                self.arbeiter(werte)
                
        
        
    def allgemein(self, werte=False):

        
        if werte == False:
            style = 'Cleanlooks'
            user = 'David'

            
        else:
            style = werte['style']
            user = werte['user']
            

        settings = QSettings("GanjD-Soft", "GalaBau")
        settings.beginGroup("MainWindow")
        settings.setValue("style", style)
        settings.setValue('user', user)
        settings.endGroup()
        
        
        
    def datenbank(self, werte=False):
        
        if werte == False:
            # Default Values
            path = os.path.join(os.getcwd(), 'db')
            
        else:
            path = werte['path']
        
        settings = QSettings("GanjD-Soft", "GalaBau")
        settings.beginGroup("Datenbank")
        settings.setValue("path", path)
        settings.endGroup()
        
        
        
    def arbeiter(self, werte=False):
        pass

