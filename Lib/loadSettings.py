# -*- coding: utf-8 -*-

import os

from Lib.saveSettings import SaveSettings
from PyQt4.QtCore import QSettings
from PyQt4.QtCore import QVariant
from PyQt4 import QtCore

SETTINGS_PATH = os.getcwd()
SETTINGS_FILENAME = 'settings'
print SETTINGS_PATH


class LoadSettings:
    
    def __init__(self):
        pass
        


        
    def style(self):
        
        default = 'Cleanlooks'
        
        settings = QSettings("GanjD-Soft", "GalaBau")
        settings.beginGroup("MainWindow")
        style = settings.value("style", default).toString()
        settings.endGroup()
        
        return style
        
        
    def user(self):
        default = 'David'
        
        settings = QSettings("GanjD-Soft", "GalaBau")
        settings.beginGroup("MainWindow")
        user = settings.value("user", default).toString()
        settings.endGroup()
        
        return user
        
    
    def currentYear(self):
        default = 2012
        
        settings = QSettings("GanjD-Soft", "GalaBau")
        settings.beginGroup("MainWindow")
        jahr = settings.value("jahr", default).toInt()[0]
        settings.endGroup()
        
        return jahr
        
        

    
        
    #TODO: Settings Arbeiter ändern
    def arbeiter(self):
        arbeiterList = []
        return arbeiterList
        
        

        
        
        
        
    
    
