# -*- coding: utf-8 -*-


from PyQt4.QtCore import QObject
from PyQt4.QtCore import QVariant
from PyQt4.QtCore import QString

from Lib.tools import Tools
from Orm.db.models import *

from Lib.loadSettings import LoadSettings


_fromUtf8 = QString.fromUtf8


class Filter_AS(QObject):
    
    def __init__(self, projekt_object):
        QObject.__init__(self)
        
        self.settings = LoadSettings()
        self.tools = Tools()
        
        self.projekt_object = projekt_object
        self.setFilter()

        
        
    def loadFilter(self):
        pass
        


    def getResult(self):
        q = A_Tag.objects.filter(projekt__exact=self.projekt_object).order_by('datum')
        return q
        



    def setFilter(self, filter_art='Alle', filter_string='Alle'):
        self.filter_art = self.tools.getEncodedString(filter_art)
        self.filter_string = self.tools.getEncodedString(filter_string)
        
        
        
        

