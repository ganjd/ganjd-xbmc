# -*- coding: utf-8 -*-

#Django specific settings
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")


# Import your models for use in your script
from db.models import *

from datenbankHandler import ConnectDB


#Einige Funktionen zur Konvertierung

def getStatus(status):
    if status == 'Geld erhalten':
        return 'G'
    if status == 'Abgerechnet':
        return 'A'
    if status == 'Offen':
        return 'O'
        
    return 'O'
    
    
def getStatusAk(status):
    if status == 'Ausgezahlt':
        return 'A'
        
    return 'O'
    

def getDatum(datum):
    import time
    import datetime
    
    c = time.strptime(datum, "%d.%m.%Y")
    day = int(time.strftime("%d", c))
    month = int(time.strftime('%m', c))
    year= int(time.strftime('%Y', c))

    return datetime.date(year, month, day)
    
    
def getTime(zeit):
    import datetime
    zeit = zeit.split(':')
    hour = int(zeit[0])
    minute = int(zeit[1])
    return datetime.time(hour, minute)
    
    
def getPause(pause):
    if pause == '':
        return 0
        
    return pause
    
    
def getBetrag(betrag):
    betrag = betrag.replace(',', '.')
    betrag = float(betrag)
    return betrag


def getMenge(menge):
    menge_new = menge.split(',')
    if menge_new[0] == 'o':
        menge = '0.%s'%menge_new[1]
    return menge.replace(',', '.')
    

def getProjektBeginn():
    import datetime
    date = datetime.date(w_year, 1, 1)
    return date
    
#--------------------------------------------------------------------------------------------------------------------------


#Datenbank Pfade
w_year = 2012
sql_kunden = os.path.join(os.getcwd(), 'kunden.sqlite')
sql_projekt = os.path.join(os.getcwd(), str(w_year), 'project.sqlite')


#-----------------------------------------------------------------------------------------------------------------------------


#Kunden
def importKunden():
    sql = ConnectDB()
    sql.connect(sql_kunden)
    sql.execute('SELECT * FROM kunden')
    sqlResult = sql.fetchall()
    print sqlResult
    
    for entry in sqlResult:
        try:
            Kunde.objects.get(nr__exact=entry[0])
            print 'Kunde schon vorhanden'
        except:
            print 'Import Kunde'
            kunde = Kunde(
                nr=entry[0], 
                matchcode = entry[1], 
                anrede=entry[2], 
                firma=entry[3], 
                nachname=entry[4], 
                vorname=entry[5],
                plz=entry[6], 
                ort=entry[7], 
                strasse=entry[8], 
                telefon=entry[9], 
                mobil=entry[10], 
                fax=entry[11], 
                email=entry[12], 
                )
            kunde.save()
        
    print 'Alle Kunden importiert'

#---------------------------------------------------------------------------------

#Projekte
def importProjekte():
    sql = ConnectDB()
    sql.connect(sql_projekt)
    sql.execute('SELECT * FROM mainprojects')
    sqlResult = sql.fetchall()
    print sqlResult
    
    for entry in sqlResult:
        
        q = Projekte.objects.filter(nr__exact=entry[0])
        q = q.filter(beginn__exact=getProjektBeginn())
        
        if len(q) <= 0:
            print 'Import Projekt'
            projekt = Projekte(
                nr=entry[0], 
                name=entry[1], 
                kunde=Kunde.objects.get(nr__exact=entry[2]), 
                status=getStatus(entry[3]), 
                beschreibung=entry[4], 
                beginn=getProjektBeginn()
                )
            projekt.save()
        else:
            print 'Projekt schon Vorhanden'
    
    print 'Alle Projekte importiert'

#------------------------------------------------------------------------------

#A_Tag
def importA_Tag():
    sql = ConnectDB()
    sql.connect(sql_projekt)
    sql.execute('SELECT * FROM mainas')
    sqlResult = sql.fetchall()
    print sqlResult
    
    for entry in sqlResult:
    
        q = A_Tag.objects.filter(projekt=Projekte.objects.get(nr__exact=entry[0]))
        q = q.filter(datum__exact=getDatum(entry[2]))
        
        if len(q) <=0:
            print 'Import A_Tag'
            a_tag = A_Tag(
                projekt=Projekte.objects.get(nr__exact=entry[0]), 
                datum=getDatum(entry[2]), 
                status=getStatus(entry[3]), 
                anzahl_ak=entry[4], 
                )
            a_tag.save()
        else:
            print 'A_Tag schon vorhanden'
            
    print 'Alle A_Tage importiert'


#---------------------------------------------------------------------------------------------

#AK
def importAK():
    sql = ConnectDB()
    sql.connect(sql_projekt)
    sql.execute('SELECT * FROM as_ak')
    sqlResult = sql.fetchall()
    print sqlResult
    
    for entry in sqlResult:
    
        q = A_Tag.objects.filter(projekt=Projekte.objects.get(nr__exact=entry[1]))
        q_1 = q.filter(datum__exact=getDatum(entry[3]))
    
        q = AK.objects.filter(a_tag__exact=q_1[0])
        q = q.filter(ak__exact=entry[0])
        
        if len(q) <=0:
            print 'Import AK'
            ak_1 = AK(
                a_tag=q_1[0], 
                ak=entry[0], 
                beginn=getTime(entry[5]), 
                ende=getTime(entry[6]), 
                pause=getPause(entry[7]), 
                status=getStatusAk(entry[8]), 
                )
            ak_1.save()
        
        else:
            print 'AK schon vorhanden'
            
    print 'Alle AKs importiert'


#------------------------------------------------------------------------------------------------------------------------------

#Belege
def importBelege():
    sql = ConnectDB()
    sql.connect(sql_projekt)
    sql.execute('SELECT * FROM belege_main')
    sqlResult = sql.fetchall()
    print sqlResult
    
    for entry in sqlResult:
    
        q = Belege.objects.filter(nr__exact=entry[0])
        q = q.filter(datum__exact=getDatum(entry[1]))
        
        if len(q) <= 0:
            print 'Import Beleg'
            belege = Belege(
                nr=entry[0], 
                datum=getDatum(entry[1]), 
                lieferant=entry[2], 
                zahlungsart=entry[3], 
                brutto=getBetrag(entry[4]), 
                netto=getBetrag(entry[5]), 
                anzahl_artikel=entry[6], 
                )
            belege.save()
            
        else:
            print 'Beleg schon vorhanden'
            
    print 'Alle Belege importiert'

#------------------------------------------------------------------------------------------------------------------------------------

#Beleg_Detail
def importBelege_Details():
    sql = ConnectDB()
    sql.connect(sql_projekt)
    sql.execute('SELECT * FROM belege_details')
    sqlResult = sql.fetchall()
    print sqlResult
    
    for entry in sqlResult:
        
        q_b = Belege.objects.filter(nr__exact=entry[0])
        for q_i in q_b:
            q = Belege_Details.objects.filter(nr__exact=q_i)
            q = q.filter(bezeichnung__exact=entry[1])
            q = q.filter(brutto__exact=getBetrag(entry[4]))
    #        q = q.filter(projekt__exact=Projekte.objects.get(nr__exact=entry[6]))
            if len(q) > 0:
                print 'Found Entry:'
                break
            
        q_projekt = Projekte.objects.filter(nr__exact=entry[6])
        q_projekt = q_projekt.filter(beginn__exact=getProjektBeginn())
        
        q_beleg = Belege.objects.filter(nr__exact=entry[0])
        
        for q_beleg_i in q_beleg:
            print q_beleg_i.datum
            if q_beleg_i.datum.year == w_year:
                q_beleg_match = q_beleg_i
                break
        
        if len(q) <= 0:
            print 'Import Beleg_Detail'
            print entry
            beleg_detail = Belege_Details(
                nr=q_beleg_match, 
                bezeichnung=entry[1], 
                menge=getMenge(entry[2]), 
                einheit=entry[3], 
                brutto=getBetrag(entry[4]), 
                netto=getBetrag(entry[5]), 
                projekt=q_projekt[0], 
                status=getStatus(entry[7]), 
                )
            beleg_detail.save()
        else:
            print 'Beleg_Detail schon vorhanden'
            
    print 'Alle Belege_Details importiert'

#-----------------------------------------------------------------------------------------------------------------------------------

    
#importKunden()
#importProjekte()
#importA_Tag()
#importAK()
#importBelege()
#importBelege_Details()
import datetime
date_from = datetime.date(2011, 1, 1)
date_til = datetime.date(2011, 12, 31)

q =Belege.objects.filter(datum__year=2011).order_by('nr')


for entry in q:
    beleg_detail = Belege_Details.objects.filter(nr=entry)
    print entry.nr, entry.datum, entry.lieferant
    for entry in beleg_detail:
        print entry.bezeichnung





