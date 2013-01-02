# -*- coding: utf-8 -*-

from PyQt4.QtCore import QObject
from PyQt4.QtCore import QVariant
from PyQt4.QtCore import QString
from PyQt4.QtCore import SIGNAL

from Lib.tools import Tools
from Orm.db.models import *
import datetime

from Lib.loadSettings import LoadSettings


_fromUtf8 = QString.fromUtf8


class Filter_Belege(QObject):
    
    def __init__(self, projekt_object):
        QObject.__init__(self)
        
        self.settings = LoadSettings()
        self.tools = Tools()
        
        self.projekt_object = projekt_object
        self.setFilter()

        
        
    def loadFilter(self):
        
        self.emit(SIGNAL('addFilterItem'), 'Alle', QVariant('Alle'))

        belege_details = Belege_Details.objects.filter(projekt=self.projekt_object)
        belege = Belege.objects.filter(id__in=belege_details.values_list('nr'))
        
        
        if self.filter_art == 'Datum':       
            datumList = belege.values_list('datum').distinct().order_by('datum')
            for entry in datumList:
                self.emit(SIGNAL('addFilterItem'), self.tools.formatDatum(entry[0]), QVariant(entry[0]))
            
        if self.filter_art == 'Lieferant':
            lieferantList = belege.values_list('lieferant').distinct().order_by('lieferant')
            for entry in lieferantList:
                self.emit(SIGNAL('addFilterItem'), entry[0], QVariant(entry[0]))
                
        if self.filter_art == 'Zahlungsart':
            zahlungsartList = belege.values_list('zahlungsart').distinct().order_by('zahlungsart')
            for entry in zahlungsartList:
                self.emit(SIGNAL('addFilterItem'), entry[0], QVariant(entry[0]))
        
        if self.filter_art == 'Bezeichnung':
            bezeichnungList = belege_details.values_list('bezeichnung').distinct().order_by('bezeichnung')
            for entry in bezeichnungList:
                self.emit(SIGNAL('addFilterItem'), entry[0], QVariant(entry[0]))



    def getResult(self):
        q = Belege_Details.objects.filter(projekt=self.projekt_object)
        
        if self.filter_art == 'Datum' and self.filter_string != 'Alle':
            q1 = q.values_list('nr')
            q2 = Belege.objects.filter(id__in=q1)
            q2 = q2.filter(datum=datetime.date(year=int(self.filter_string.split('.')[2]), month=int(self.filter_string.split('.')[1]), day=int(self.filter_string.split('.')[0])))
            q = q.filter(nr__in=q2)

        if self.filter_art == 'Lieferant' and self.filter_string != 'Alle':
            q1 = q.values_list('nr')
            q2 = Belege.objects.filter(id__in=q1)
            q2 = q2.filter(lieferant=self.filter_string)
            q = q.filter(nr__in=q2)
            
        if self.filter_art == 'Zahlungsart' and self.filter_string != 'Alle':
            q1 = q.values_list('nr')
            q2 = Belege.objects.filter(id__in=q1)
            q2 = q2.filter(zahlungsart=self.filter_string)
            q = q.filter(nr__in=q2)
        
        if self.filter_art == 'Bezeichnung' and self.filter_string != 'Alle':
            q = q.filter(bezeichnung=self.filter_string)

        return q



    def setFilter(self, filter_art='Datum', filter_string='Alle'):
        self.filter_art = self.tools.getEncodedString(filter_art)
        self.filter_string = self.tools.getEncodedString(filter_string)
        
        
        
        

