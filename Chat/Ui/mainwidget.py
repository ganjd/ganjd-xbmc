# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QWidget
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtCore import SIGNAL

from Chat.Ui.Ui_mainwidget import Ui_Form

from Chat.chatClient import Client
from Chat.Ui.status import Status_Widget



_fromUtf8 = QtCore.QString.fromUtf8


class MainWidget(QWidget, Ui_Form):
    

    def __init__(self, username, server=False):

        QWidget.__init__(self)
        self.setupUi(self)
        

        self.user_historie = {}
        self.user_offline = {}
        self.chat_partner = 'Alle'
        self.chat_partner_status = False
        self.current_user = False
        self.username = username
        self.password = '1234'
        
        self.startClient()
        self.widget.hide()
        
        if self.username != 'David':
            self.treeWidget.hide()
            self.toolButton.hide()
        

        
    def startClient(self):
        
        self.client = Client()
        self.client.setUser(self.username, self.password)
        
        self.connect(self.client, SIGNAL('Incoming'), self.incoming)
        self.connect(self.client, SIGNAL('Userlist'), self.userlist)
        self.connect(self.client, SIGNAL('Written'), self.written)
        self.connect(self.client, SIGNAL('State'), self.state)
        self.connect(self.client, SIGNAL('closeReady'), self.closeReady)
        
        self.client.connectClient()
            
            
            
    def openChatPartner(self, partner, status):
        self.treeWidget.setMinimumSize(QtCore.QSize(0, 90))
        self.treeWidget.setMaximumSize(QtCore.QSize(16777215, 90))
        
        self.label_chat_partner.setText(partner+' - '+status)
        self.chat_partner = partner
        self.chat_partner_status = status
        
        self.user_historie[self.current_user] = self.plainTextEdit.toPlainText()
        self.plainTextEdit.clear()
        try:
            self.plainTextEdit.appendPlainText(self.user_historie[partner])
        except:
            print 'NoHistorie'
        self.widget.show()
        self.current_user = partner
        
        
        
    def send(self):
        
        msg = self.getEncodedString(self.lineEdit.text())
        send_an = self.getEncodedString(self.chat_partner)
        if len(msg) > 0:
            self.client.send(msg, send_an)
        
        
        
    def incoming(self, msg, user):

        if self.current_user != user:
            self.openChatPartner(_fromUtf8(user), 'online')
            
        if self.widget.isHidden() == True:
            self.widget.show()
            self.treeWidget.setMinimumSize(QtCore.QSize(0, 90))
            self.treeWidget.setMaximumSize(QtCore.QSize(16777215, 90))

        text = str(user)+'>> '+str(msg)
        self.plainTextEdit.appendPlainText(text)
        
        
        
    def userlist(self, user, status):
        if user == False:
            self.treeWidget.clear()
        else:
            if user != self.username:
                item= QtGui.QTreeWidgetItem()
                item.setText(0, _fromUtf8(user))
                item.setText(1, _fromUtf8(status))
                self.treeWidget.addTopLevelItem(item)
                if self.current_user != False:
                    self.label_chat_partner.setText(self.current_user+' - '+status)
                if user == 'David':#
                    self.openChatPartner(_fromUtf8(user), status)
                    
        
        
    def written(self):
        self.plainTextEdit.appendPlainText(self.username+'>> '+self.lineEdit.text())
        self.lineEdit.setText('')
        
        
    def state(self, state):
        
        if state == 0:
            text = 'Nicht mit Chatserver verbunden'
            self.treeWidget.clear()
#            self.client.connectClient()

        if state == 1:
            text = 'Hostname Lookup'
            
        if state == 2:
            text = 'Verbindung zum Chatserver wird hergestellt ...'
        
        if state == 3:
            text = 'Verbunden mit Chatserver'
            
        if state == 6:
            text = 'Verbindung wird getrennt ...'
            
        self.label.setText(text)
        


    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            if self.lineEdit.hasFocus() == True:
                self.send()

    
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        self.send()


            
    def getEncodedString(self, sString):
        sString = (QtCore.QTextCodec.codecForName("UTF-8").fromUnicode(sString))
        sString = str(sString)
        sString = sString.strip()
        return str(sString)
        
    
    @pyqtSignature("QTreeWidgetItem*, int")
    def on_treeWidget_itemDoubleClicked(self, item, column):
        self.openChatPartner(item.text(0), item.text(1))


    def logout(self):
        self.client.logout()    
     
     
    
            
    def startStatusWidget(self):
        self.statusWidget = Status_Widget(self.pos(), self.size())
        self.statusWidget.show()
        
        
        
    def closeReady(self):
        self.emit(SIGNAL('closeReady')) 
        
        
        
    def closeEvent(self, event):
        print 'Close Event'
        ret = self.client.logout()
        
        if ret == True:
            event.accept()
            if self.client.state() == 3:
                print 'Warten auf Beenden'
                self.isClosing = True
            else:                
                print 'Direkt Beenden'
                self.closeReady()
                


    
    @pyqtSignature("")
    def on_toolButton_clicked(self):
        self.widget.hide()
        self.treeWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.treeWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        
