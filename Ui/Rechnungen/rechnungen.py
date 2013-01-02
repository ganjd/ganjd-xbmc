# -*- coding: utf-8 -*-

from PyQt4.QtGui import QWidget
from PyQt4.QtCore import pyqtSignature

from Ui_rechnungen import Ui_Form

class Rechnungen_Ui(QWidget, Ui_Form):

    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
    
    
    @pyqtSignature("")
    def on_toolButton_clicked(self):
        print 'Neue Rechnung'

