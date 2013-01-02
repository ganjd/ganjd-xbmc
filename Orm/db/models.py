import sys

try:
    from django.db import models
except  Exception, err:
    print err
    print "There was an error loading django modules. Do you have django installed?"
    sys.exit()


    
    
class Kunde(models.Model):
    nr = models.IntegerField()
    matchcode = models.CharField(max_length=255)
    anrede = models.CharField(max_length=20)
    firma = models.CharField(max_length=255)
    nachname = models.CharField(max_length=255)
    vorname = models.CharField(max_length=255)
    plz = models.CharField(max_length=10)
    ort = models.CharField(max_length=255)
    strasse = models.CharField(max_length=255)
    telefon= models.CharField(max_length=20)
    mobil = models.CharField(max_length=20)
    fax = models.CharField(max_length=20)
    email =  models.EmailField(max_length=254)
    
    
    

class Projekte(models.Model):
    STATUS = (
        ('O', 'Offen'), 
        ('A', 'Abgerechnet'), 
        ('G', 'Geld erhalten'), 
        )
        
    nr = models.IntegerField()
    name = models.CharField(max_length=255)
    kunde = models.ForeignKey(Kunde, on_delete=models.PROTECT)
    status = models.CharField(max_length=2, choices=STATUS)
    beschreibung = models.TextField()
    beginn = models.DateField(null=True)
    ende = models.DateField(null=True)
    
    
    

class A_Tag(models.Model):
    STATUS = (
        ('O', 'Offen'), 
        ('A', 'Abgerechnet'), 
        ('G', 'Geld erhalten'), 
        )
        
    projekt = models.ForeignKey(Projekte, on_delete=models.PROTECT)
    datum = models.DateField()
    status = models.CharField(max_length=2, choices=STATUS)
    anzahl_ak = models.IntegerField()
    
    


class AK(models.Model):
    STATUS = (
        ('O', 'Offen'), 
        ('A', 'Ausgezahlt'),  
        )
       
    a_tag = models.ForeignKey(A_Tag)
    ak = models.CharField(max_length=255)
    beginn = models.TimeField()
    ende = models.TimeField()
    pause = models.IntegerField()
    status = models.CharField(max_length=2, choices=STATUS)
    
    
    
    
class Belege(models.Model):
    nr = models.IntegerField()
    datum = models.DateField()
    lieferant = models.CharField(max_length=255)
    zahlungsart = models.CharField(max_length=255)
    brutto = models.FloatField()
    netto = models.FloatField()
    anzahl_artikel = models.IntegerField()
    



class Belege_Details(models.Model):
    STATUS = (
        ('O', 'Offen'), 
        ('A', 'Abgerechnet'), 
        ('G', 'Geld erhalten'), 
        )
    nr = models.ForeignKey(Belege)
    bezeichnung = models.CharField(max_length=255)
    menge = models.FloatField()
    einheit = models.CharField(max_length=100)
    brutto = models.FloatField()
    netto = models.FloatField()
    projekt = models.ForeignKey(Projekte)
    status = models.CharField(max_length=2, choices=STATUS)
    
    
    
    
    
    
    
    
    
    
        
    
