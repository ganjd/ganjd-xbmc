# -*- coding: utf-8 -*-

import sqlite3


class ConnectDB():
    
    def __init__(self):
        pass

    def connect(self, sDatenbank):
        
        self.connection = sqlite3.connect(sDatenbank)
        self.connection.text_factory = str
        self.cursor = self.connection.cursor()
        
        
    def close(self):
        self.connection.close()
        
        
    def commit(self):
        self.connection.commit()
        

    def execute(self, sStatment, sParam=False):
        if sParam == False:
            self.cursor.execute(sStatment)
        else:
            self.cursor.execute(sStatment, sParam)

        
    def fetchall(self):
        return self.cursor.fetchall()
        
        
    
    def delete(self, sTabel, delString):
        
        try:
            self.cursor.execute('DELETE FROM '+sTabel+' WHERE rowid=?', (delString, ))
        except:
            print 'Fehler beim löschen von Details'
            
        self.connection.commit()
        self.connection.close()
        print 'Eintrag gelöscht'
        
    
        
