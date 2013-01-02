# -*- coding: utf-8 -*-

from PyQt4.QtCore import QObject
from PyQt4.QtCore import QVariant
from PyQt4.QtCore import QString
from PyQt4.QtCore import SIGNAL

from Lib.tools import Tools
from Orm.db.models import *



class Filter(QObject):
    
    def __init__(self):
        QObject.__init__(self)
        
        self.loadFilter()
        
        
        
    def loadFilter(self):
        self.setFilter()



    def getResult(self):
        
        if self.filter_id == 'Alle':
            q = Kunde.objects.all()
            return q




    def setFilter(self, filter_id='Alle', filter_string='Alle'):
        self.filter_id = filter_id
        self.filter_string = filter_string
