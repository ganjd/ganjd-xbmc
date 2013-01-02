# -*- coding: utf-8 -*-

from PyQt4.QtGui import QWidget
from PyQt4.QtCore import pyqtSignature
from PyQt4 import QtCore, QtGui

from Ui_status import Ui_Form

import sys



class ShowStatus():
    def __init__(self, pos, size, parent=None):

        
        self.statusWidget = Status_Widget(pos, size)
        
        
    def show(self):

        self.statusWidget.show()

    
    def close(self):
        self.statusWidget.close()
        
    


class Status_Widget(QWidget, Ui_Form):

    def __init__(self, pos, size):

        QWidget.__init__(self)
        self.setupUi(self)

        
        point = QtCore.QPoint(size.width()/2, size.height()/2)
        point_2 = QtCore.QPoint(self.size().width()/2, self.size().height()/2)
        
        pos += point
        pos -= point_2
        
        self.move(pos)
        self.setWindowFlags(QtCore.Qt.SplashScreen)#
        
    
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        self.close()
        
    
    def setStatus(self, status):
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(status)
        


        
