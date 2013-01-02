# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QWidget
from PyQt4.QtCore import pyqtSignature
from chatClient import Client
from PyQt4.QtCore import SIGNAL

from Ui_mainwidget import Ui_Form

_fromUtf8 = QtCore.QString.fromUtf8

class MainWidget(QWidget, Ui_Form):

    def __init__(self, username):

        QWidget.__init__(self)
        self.setupUi(self)
        
        self.username = username
        self.password = '1234'
        
        self.client = Client()
        
        self.connect(self.client, SIGNAL('Incoming'), self.incoming)
        self.connect(self.client, SIGNAL('Userlist'), self.userlist)
        self.connect(self.client, SIGNAL('Written'), self.written)
        self.connect(self.client, SIGNAL('State'), self.state)
        
        self.client.setUser(self.username, self.password)
        self.client.connectClient()
        
        
        
        
    def incoming(self, msg, descriptor):
        text = str(descriptor)+'>>'+str(msg)
        self.plainTextEdit.appendPlainText(text)
        
        
    def userlist(self, user, status):
        if user == False:
            self.treeWidget.clear()
        else:
            item= QtGui.QTreeWidgetItem()
            item.setText(0, _fromUtf8(user))
            item.setText(1, _fromUtf8(status))
            self.treeWidget.addTopLevelItem(item)
        
        
    def written(self):
        self.plainTextEdit.appendPlainText(self.username+'>>'+self.lineEdit.text())
        self.lineEdit.setText('')
        
        
    def state(self, state):
        
        if state == 0:
            text = 'Nicht Verbunden'
            self.treeWidget.clear()
            
        if state == 1:
            text = 'Hostname Lookup'
            
        if state == 2:
            text = 'Verbindung wird hergestellt ...'
        
        if state == 3:
            text = 'Verbunden'
            
        if state == 6:
            text = 'Verbindung wird getrennt ...'
            
        self.label.setText(text)
        
        
        
    
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        msg = self.getEncodedString(self.lineEdit.text())
        if len(msg) > 0:
            self.client.send(msg)
        else:
            self.client.logout()
            
            
    def getEncodedString(self, sString):
        sString = (QtCore.QTextCodec.codecForName("UTF-8").fromUnicode(sString))
        sString = str(sString)
        sString = sString.strip()
        return str(sString)
        
        
    def logout(self):
        self.client.logout()
