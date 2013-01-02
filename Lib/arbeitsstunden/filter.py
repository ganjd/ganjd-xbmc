# -*- coding: utf-8 -*-

from PyQt4.QtCore import QObject
from PyQt4.QtCore import QVariant
from PyQt4.QtCore import QString
from PyQt4.QtCore import SIGNAL

from Lib.tools import Tools
from Lib.loadSettings import LoadSettings
from Orm.db.models import *



_fromUtf8 = QString.fromUtf8


class Filter(QObject):
    def __init__(self):
        QObject.__init__(self)
        
        self.tools = Tools()
        self.settings = LoadSettings()
        self.setFilter()


    def loadFilter(self):
        
        a_tag = A_Tag.objects.filter(datum__year=self.settings.currentYear()).order_by('datum')
        projektList = a_tag.values_list('projekt')
        projekte = Projekte.objects.filter(id__in=projektList).values_list('kunde')
        kunden = Kunde.objects.filter(id__in=projekte).distinct().order_by('nachname')
        
        self.emit(SIGNAL('addFilterItem'), 'Alle', QVariant('Alle'))
        for entry in kunden:
            self.emit(SIGNAL('addFilterItem'), self.tools.formatKunde(entry), QVariant(entry))



    def getResult(self):
        a_tag = A_Tag.objects.filter(datum__year=self.settings.currentYear()).order_by('datum')
        
        if self.filter_art == 'Alle':
            a_tag = a_tag

        if self.filter_art == 'Kunde':
            projekte = Projekte.objects.filter(kunde=self.filter_string)
            a_tag = a_tag.filter(projekt__in=projekte)
            
            
        return a_tag



    def getDetailResult(self, ak):
        a_tag = A_Tag.objects.filter(datum__year=self.settings.currentYear()).order_by('datum')
        
        detailResult = []
        
        if self.filter_art == 'Alle':
            detailResult = AK.objects.filter(a_tag__in=a_tag).filter(ak__in=ak)


        if self.filter_art == 'Kunde':
            projekte = Projekte.objects.filter(kunde=self.filter_string)
            a_tag = a_tag.filter(projekt__in=projekte)
            detailResult = AK.objects.filter(a_tag__in=a_tag).filter(ak__in=ak)
            
        
        if self.filter_art == 'Projekt':
            a_tag = a_tag.filter(projekt=self.filter_string)
            detailResult = AK.objects.filter(a_tag__in=a_tag).filter(ak__in=ak)
            
            
            
        return detailResult
            



    def getArbeiter(self):
        a_tag = A_Tag.objects.filter(datum__year=self.settings.currentYear()).order_by('datum')
        
        if self.filter_art == 'Alle':
            arbeiterList = AK.objects.filter(a_tag__in=a_tag).values_list('ak').distinct().order_by('ak')

        if self.filter_art == 'Kunde':
            projekte = Projekte.objects.filter(kunde=self.filter_string)
            a_tag = a_tag.filter(projekt__in=projekte)
            arbeiterList = AK.objects.filter(a_tag__in=a_tag).values_list('ak').distinct().order_by('ak')
            
        if self.filter_art == 'Projekt':
            a_tag = a_tag.filter(projekt=self.filter_string)
            arbeiterList = AK.objects.filter(a_tag__in=a_tag).values_list('ak').distinct().order_by('ak')
            


        return arbeiterList
        
        

    
    def setFilter(self, filter_art='Alle', filter_string='Alle'):
        self.filter_art = filter_art
        self.filter_string = filter_string
        
    

