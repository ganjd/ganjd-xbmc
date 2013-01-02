# -*- coding: utf-8 -*-

import os
from PyQt4 import QtCore
from Lib.loadSettings import LoadSettings



class Tools:
    
    def __init__(self):
        self.loadSettings = LoadSettings()

    def formatText(self, sString):
        sString = str(sString.toLatin1())
        sString = sString.strip()
        sString = sString.replace('<br><br>', '')
        sString = QtCore.QString.fromUtf8(sString)
        return sString
        
        
    def getEncodedString(self, sString):
        sString = (QtCore.QTextCodec.codecForName("UTF-8").fromUnicode(sString))
        sString = str(sString)
        sString = sString.strip()
        return str(sString)
        
    
    def getTimeDifference(self, startTime, endTime, pause='30'):
        try:
            pause = float(pause)
        except:
            pause = 0.0
        
        if pause == '':
            pause = 0
            
        import datetime
        
        timedelta_start = datetime.timedelta(hours=startTime.hour, minutes=startTime.minute)
        timedelta_end = datetime.timedelta(hours=endTime.hour, minutes=endTime.minute)

        timedelta = timedelta_end-timedelta_start
        seconds = timedelta.total_seconds()
        minute = round(float(seconds)/60, 2)
        stunde = round(float(minute)/60, 2)
        diffrence = stunde - round(float(1)/60*pause, 2)
        return diffrence
        
        
        
    def formatDatum(self, datum):
        datum = datum.strftime('%d.%m.%Y')
        return datum
        
        
    def formatZeit(self, zeit):
        zeit = zeit.strftime('%H : %M')
        return zeit
        
    
    def formatProjektNr(self, nr):
        format = '000'
        return '%s%s'%(format, nr)
        
    
    def formatBelegNr(self, nr):
        null_count = 3
        if int(nr) < 10:
            format = '0'*(null_count)
        elif int(nr) < 100:
            format = '0'*(null_count-1)
        else:
            format = '0'*(null_count-2)
            
        return '%s%s'%(format, nr)
        
    
    def formatKunde(self, kunde):
        kundenString = ''
        
        if len(kunde.firma) == 0:
            if len(kunde.vorname) == 0:
                kundenString = kunde.nachname
            else:
                if len(kunde.nachname) == 0:
                    kundenString = kunde.vorname
                else:
                    kundenString = '%s %s'%(kunde.vorname, kunde.nachname)
        else:
            
            if len(kunde.vorname) == 0:
                kundenString = '%s, %s'%(kunde.firma, kunde.nachname)
            else:
                if len(kunde.nachname) == 0:
                    kundenString = '%s, %s'%(kunde.firma, kunde.vorname)
                else:
                    kundenString = '%s, %s %s'%(kunde.firma, kunde.vorname, kunde.nachname)
        
        return kundenString
        
        
        
    def shortStatusName(self, status):
        if status == 'Geld erhalten':
            return 'G'
        if status == 'Abgerechnet':
            return 'A'
        if status == 'Offen':
            return 'O'
            
        return 'O'
        
        
        
    def shortStatusName_AK(self, status):
        if status == 'Ausgezahlt':
            return 'A'
            
        return 'O'
            
        




