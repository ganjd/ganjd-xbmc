# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtCore import SIGNAL

from Ui_arbeiter import Ui_Form
from Ui.Arbeiter.ak_treewidget import AK_TreeWidget

from Lib.arbeitsstunden.filter import Filter
from Lib.tools import Tools
from signalReceiver import Signal
from Ui.messageBox import MessageBox
from Lib.sorting import Sort



_fromUtf8 = QtCore.QString.fromUtf8


class Arbeiter(QWidget, Ui_Form):

    def __init__(self):

        QWidget.__init__(self)
        self.setupUi(self)

        self.tools = Tools() 
        self.messageBox = MessageBox(self)
        
        self.loadTabWidget()
        self.setFilter('Alle', 'Alle')
        
        
    
    def run(self):
        self.clear()
        self.initialize_Threads()
        self.loadArbeiter.start()
        self.show()

        
    def initialize_Threads(self):
        self.loadArbeiter = Load_Arbeiter()
        self.loadArbeiter.setFilter(self.filter_art, self.filter_string)
        self.connect(self.loadArbeiter, SIGNAL('ladeArbeiter'), self.loadTreeWidget_Arbeiter)
        self.connect(self.loadArbeiter, SIGNAL('connect_error'), self.connect_error)
        self.connect(self.loadArbeiter, SIGNAL('error'), self.error)
        
        
    def loadTabWidget(self):
        
        self.tabWidget = QtGui.QTabWidget(self.frame)
        self.tabWidget.setDocumentMode(True)
        self.verticalLayout_3.addWidget(self.tabWidget)
        
    def loadTreeWidget_Arbeiter(self, arbeiter):
        
        self.ui_Arbeiter = AK_TreeWidget(arbeiter)
        self.ui_Arbeiter.loadFilter(self.filter_art, self.filter_string)

        self.tab = QtGui.QWidget()
        
        self.verticalLayout = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout.addWidget(self.ui_Arbeiter)
        
        self.tabWidget.addTab(self.tab, arbeiter[0])
        self.tabWidget.setCurrentIndex(self.tabWidget.count()-1)
        
    
    def setFilter(self, filter_art, filter_string):
        self.filter_art = filter_art
        self.filter_string = filter_string
        
        
    def clear(self):
        for i in range(0, self.tabWidget.count()):
            self.tabWidget.removeTab(0)
        
        

    def connect_error(self, sender):
        reply = self.messageBox.connect_error()
        if reply:
            sender.start()


    def error(self, sender, err):
        reply = self.messageBox.error({'err': err, 'sender': sender})



class Load_Arbeiter(QtCore.QThread):
    
    def __init__(self):
        QtCore.QThread.__init__(self)
        
        self.signal = Signal()
        self.signal.registerLoading(self)
        
        self.filter = Filter()
        self.tools = Tools()
        
        
    
    def setFilter(self, filter_art, filter_string):
        self.filter_art = filter_art
        self.filter_string = filter_string


    def run(self):
        try:
            self.signal.startLoading(self)
            
            #Filter 
            self.filter.setFilter(self.filter_art, self.filter_string)

            #Lade Inhalte
            sqlResult = self.filter.getResult()
            
            arbeiterList = self.filter.getArbeiter()
            for arbeiter in arbeiterList:
                self.emit(SIGNAL('ladeArbeiter'), arbeiter, self.filter.filter_art, self.filter.filter_string)

            self.signal.finishedLoading(self)
            
        except Exception, err:
            self.signal.killLoading(self)
            if err.__class__.__name__ == 'OperationalError':
                self.emit(SIGNAL('connect_error'), self)
            else:
                self.emit(SIGNAL('error'), self, err)

