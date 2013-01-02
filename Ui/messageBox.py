# -*- coding: utf-8 -*-


from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature


from Ui_messageBox import Ui_Dialog

from Lib.tools import Tools


_fromUtf8 = QtCore.QString.fromUtf8

class MessageBox(QDialog, Ui_Dialog):

    def __init__(self, parent):

        QDialog.__init__(self)
        self.setupUi(self)
        
        self.name = parent.__class__.__name__
        self.tools = Tools()
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(':/newPrefix/res/Users Folder.png')), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        
#        self.setSizeGripEnabled(True)
        self.setWindowFlags(QtCore.Qt.SplashScreen)
        self.clear()
        
        
        
    def del_question(self, data=False):
        self.clear()
        msg = self.getMessage('question', data)

        self.setIcon(':/newPrefix/res/question_mark_blue.png')

        self.addButton('Ja', 'Accept')
        self.addButton('Nein', 'Reject')
        
        self.setTitle(msg[0])
        self.setInfoText(msg[1])

        self.exec_()
        return self.result()
        
        
    def del_error(self, data=False):
        self.clear()
        msg = self.getMessage('error', data)
        
        self.setWindowTitle(_fromUtf8('Löschen'))
        self.setIcon(':/newPrefix/res/1326055942_emblem-nowrite.png')

        self.addButton('OK', 'Reject')
        
        self.setTitle(msg[0])
        self.setInfoText(msg[1])

        self.exec_()
        return self.result()
        
    
    def connect_error(self, data=False):
        self.clear()
        msg = self.getMessage('connect_error', data)
        
        self.setWindowTitle(_fromUtf8('Verbindungsfehler'))
        self.setIcon(':/newPrefix/res/1326055942_emblem-nowrite.png')
        
        self.addButton('Wiederholen', 'Accept')
        self.addButton('Abbrechen', 'Reject')
        
        self.setTitle(msg[0])
        self.setInfoText(msg[1])
        self.exec_()
        return self.result()
        
    
    def error(self, data=False):
        
        self.clear()
        msg = self.getMessage('connect_error', data)
        
        self.setWindowTitle(_fromUtf8('Verbindungsfehler'))
        self.setIcon(':/newPrefix/res/1326055942_emblem-nowrite.png')
        
        self.addButton('Ok', 'Reject')
        
        self.setTitle(u'Es ist ein Fehler aufgetreten !')
        print data['sender'], data['err'], data['err']
        self.setInfoText('Class:  %s\nType:   %s\nFehler: %s'%(data['sender'], type(data['err']), data['err']))
        self.exec_()
        return self.result()
        
        
        
    def getMessage(self, id, data):
        msg = ''
        msg_i = ''
        
        if id == 'connect_error':
            msg = u'Zugriff auf Datenbank nicht möglich !'
            msg_i = u'Möglicherweise besteht keine Internetverbindung\nbzw. Remotehost ist offline !'
            return [msg, msg_i]
        
        #Kunden
        if self.name == 'Kunden':
            
            if id == 'question':
                msg = u'Soll dieser Kunde wirklich gelöscht werden ?'
                msg_i = u'Der Kunde: "%s" wird unwiederruflich gelöscht !'%self.tools.formatKunde(data)
                
                
            if id == 'error':
                msg = u'Kunde kann nicht gelöscht werden !'
                msg_i = u'Dem Kude: "%s" ist mindestens noch ein Projekt zugeordnet !\nSolange kann dieser Kunde nicht gelöscht werden !'%self.tools.formatKunde(data)
        
        #Projekte
        if self.name == 'Projekt':
            if id == 'question':
                msg = u'Soll dieses Projekt wirklich gelöscht werden ?'
                msg_i = u'Das Projekt: "%s" wird unwiederruflich gelöscht !'%data.name
            
            if id == 'error':
                msg = u'Projekt kann nicht gelöscht werden !'
                msg_i = u'Dem Projekt: "%s" ist mindestens noch ein Material bzw. Arbeitstag zugeordnet !\nSolange kann das Projekt nicht gelöscht werden !'%data.name
                
        
        #Arbeitsstunden
        if self.name == 'Projekt_Details':
            if data.__class__.__name__ == 'A_Tag':
                if id == 'question':
                    msg = u'Soll dieser Arbeitstag wirklich gelöscht werden ?'
                    msg_i = u'Der Arbeitstag am "%s" wird unwiederruflich gelöscht !'%self.tools.formatDatum(data.datum)
                    
        
        if self.name == 'Belege':
            if id == 'question':
                msg = u'Soll dieser Beleg wirklich gelöscht werden ?'
                msg_i = u'Der Belge "%s" am "%s" wird unwiederruflich gelöscht !\nDas kann Auswirkung auf die Materialausgaben in verschiedenen Projekten haben !'%(data.nr, self.tools.formatDatum(data.datum))
        
        return [msg, msg_i] 
        
        
        
    
    def addButton(self, text, role):
        if role == 'Accept':
            self.pushButton.setText(_fromUtf8(text))
            self.pushButton.show()
        
        if role == 'Reject':
            self.pushButton_2.setText(_fromUtf8(text))
            self.pushButton_2.show()
        
        if role == 'Custom':
            self.pushButton_3.setText(_fromUtf8(text))
            self.pushButton_3.show()
            
    
    def setTitle(self, text=''):
        self.label.setText(_fromUtf8(text))
        
    
    def setInfoText(self, text=''):
        self.label_2.setText(_fromUtf8(text))
        
    
    def setIcon(self, path=False):
        if not path:
            self.label_3.hide()
        else:
            self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8(path)))
            self.label_3.show()
        
        

    
    def clear(self):
        self.pushButton.hide()
        self.pushButton_2.hide()
        self.pushButton_3.hide()
        self.setTitle()
        self.setInfoText()
        self.setIcon()
        self.resize(self.minimumSize())
        
        
    
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        self.close()
        self.setResult(1)
    
    @pyqtSignature("")
    def on_pushButton_2_clicked(self):
        self.close()
        self.setResult(0)
    
    @pyqtSignature("")
    def on_pushButton_3_clicked(self):
        self.close()
        self.setResult(2)
