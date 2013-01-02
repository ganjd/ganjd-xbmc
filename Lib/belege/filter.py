# -*- coding: utf-8 -*-

import os
from PyQt4.QtCore import QVariant
from PyQt4.QtCore import QString

from Lib.tools import Tools
from Orm.db.models import *

from Lib.loadSettings import LoadSettings



_fromUtf8 = QString.fromUtf8


class Filter:
    def __init__(self):
        

        self.settings = LoadSettings()

        self.tools = Tools()

        self.loadFilter()
        
        
        
    def loadFilter(self):
        self.setFilter()



    def getResult(self):
        
        if self.filter_art == 'Alle':
            q = Belege.objects.filter(datum__year=self.settings.currentYear()).order_by('nr')
            return q


            
          
    
    def setFilter(self, filter_art='Alle', filter_string='Alle'):
        self.filter_art = filter_art
        self.filter_string = filter_string
