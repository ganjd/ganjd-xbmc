# -*- coding: utf-8 -*-


from PyQt4 import QtGui, QtCore
from Lib.tools import Tools


_fromUtf8 = QtCore.QString.fromUtf8


class Get_Summen:
    
    def __init__(self):
        
        self.tools = Tools() 
        self.defineParams()
        
        
    def defineParams(self):
        self.stundenGesamt = float(0)
        self.stundenOffen = float(0)
        self.stundenAbgerechnet = float(0)
        
        self.betragGesamt = float(0)
        self.betragOffen = float(0)
        self.betragAbgerechnet = float(0)
        
        
    def stunden_Gesamt(self, stunden):
        self.stundenGesamt = self.stundenGesamt + stunden
        
        
    def stunden_Offen(self, stunden, status):
        if status == 'O':
            self.stundenOffen = self.stundenOffen + stunden
            
    def stunden_Abgerechnet(self, stunden, status):
        if status == 'A':
            self.stundenAbgerechnet = self.stundenAbgerechnet + stunden
            
        
    def betrag_Gesamt(self, betrag):
        self.betragGesamt = self.betragGesamt + betrag
        
    def betrag_Offen(self, betrag, status):
        if status == 'O':

            self.betragOffen = self.betragOffen + betrag
            
    def betrag_Abgerechnet(self, betrag, status):
        if status == 'A':
            self.betragAbgerechnet = self.betragAbgerechnet + betrag
            
    def clear(self):
        self.defineParams()
