# -*- coding: utf-8 -*-

from PyQt4 import QtCore
from PyQt4.QtGui import QWidget
from PyQt4.QtCore import pyqtSignature

from Ui_statusBarWidget import Ui_Form

_fromUtf8 = QtCore.QString.fromUtf8

class StatusBar_Widget(QWidget, Ui_Form):

    def __init__(self, parent = None):

        QWidget.__init__(self, parent)
        self.setupUi(self)
        
        self.setOffline()
        
        
    def setText(self, text):
        self.label_text.setText(text)
        
        
    def setOnline(self):
        
        self.label_online.show()
        self.label_offline.hide()
        self.label_text.setText('Verbunden')
        
    def setOffline(self):
        
        self.label_offline.show()
        self.label_online.hide()
        self.label_text.setText('Getrennt')
        
    def setUser(self, user):
        self.label_user.setText(_fromUtf8('Benutzer:  ')+user)
        
    def setJahr(self, jahr):
        self.label_jahr.setText(_fromUtf8('Wirtschaftsjahr:  ')+jahr)
        
    def setInfo(self, info):
        self.label_info.setText(_fromUtf8(info))
        
        
