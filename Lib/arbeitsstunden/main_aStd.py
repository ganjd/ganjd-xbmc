# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtCore import SIGNAL

from Ui.Arbeitsstunden.aStd import AStd_Ui

from Lib.arbeitsstunden.filter import Filter
from Lib.tools import Tools
from signalReceiver import Signal
from Ui.messageBox import MessageBox
from Lib.sorting import Sort


_fromUtf8 = QtCore.QString.fromUtf8


class AStd_Main(AStd_Ui):
    
    def __init__(self):
        AStd_Ui.__init__(self)
        
        self.messageBox = MessageBox(self)
        
        self.initialize_Threads()

        self.loadArbeiterWidget()
        

    def initialize_Threads(self):
        #Thread Instance fuer A_Tag
        self.loadA_Tag = Load_A_Tag()
        self.connect(self.loadA_Tag, SIGNAL('addItem'), self.addItem)
        self.connect(self.loadA_Tag.filter, SIGNAL('addFilterItem'), self.addFilterItem)
        self.connect(self.loadA_Tag, SIGNAL('connect_error'), self.connect_error)
        self.connect(self.loadA_Tag, SIGNAL('error'), self.error)

    

        
    def loadTreeWidget(self):
        #Leere TreeWidget
        self.treeWidget.clear()

        #Konfiguriere Header fuer Sortierung
        self.treeWidget.setSortingEnabled(False)
        header = self.treeWidget.header()
        header.setSortIndicatorShown(True)
        header.setClickable(True)
        self.sort = Sort(self.treeWidget)
        self.connect(header, QtCore.SIGNAL('sectionClicked(int)'), self.sort.byColumn)
        
        #Fuelle TreeWidget in extra Thread
        self.loadA_Tag.start()


    def addItem(self, item):
        self.treeWidget.addTopLevelItem(item)
        
    
    def addFilterItem(self, text, data):
        if text == 'Alle':
            self.comboBox_filter.clear()
        self.comboBox_filter.addItem(text, data)
        
        
    
    def loadArbeiterWidget(self):
        from Ui.Arbeiter.arbeiter import Arbeiter
        self.ak = Arbeiter()
        self.verticalLayout.addWidget(self.ak)
        
        
    def runArbeiter(self):
        self.ak.run()
        
        
    def refresh(self):
        self.show()
        self.loadTreeWidget()
        self.runArbeiter()
        
        

    def loadFilter(self, filter_art, filter_string='Alle'):   
        
        self.loadA_Tag.setFilter(filter_art, filter_string)
        self.ak.setFilter(filter_art, filter_string)
        self.treeWidget.clear()
        self.refresh()


        

    def connect_error(self, sender):
        reply = self.messageBox.connect_error()
        if reply:
            sender.start()


    def error(self, sender, err):
        reply = self.messageBox.error({'err': err, 'sender': sender})





class Load_A_Tag(QtCore.QThread):
    
    def __init__(self):
        QtCore.QThread.__init__(self)
        
        self.signal = Signal()
        self.signal.registerLoading(self)
        
        self.filter = Filter()
        self.tools = Tools()
        
        self.bLoadFilterOnly = False
        self.bLoadFilter = True
        
    
    def setFilter(self, filter_art, filter_string):
        if self.filter.filter_art != filter_art:
            if self.filter.filter_string == filter_string:
                self.bLoadFilterOnly = True
            else:
                self.bLoadFilter = True
                
        self.filter.setFilter(filter_art, filter_string)


    
    def run(self):
        try:
            self.signal.startLoading(self)
            
            #Filter 
            if self.bLoadFilterOnly:
                self.bLoadFilterOnly = False
                self.filter.loadFilter()
                self.signal.finishedLoading(self)
                return
                
            if self.bLoadFilter:
                self.bLoadFilter = False
                self.filter.loadFilter()
                
            #Lade Inhalte
            sqlResult = self.filter.getResult()
            

            for entry in sqlResult:
    
                item= QtGui.QTreeWidgetItem()
                item.setData(0, 32, QtCore.QVariant(entry))
                
                item.setText(0, self.tools.formatDatum(entry.datum))
                item.setText(1, self.tools.formatKunde(entry.projekt.kunde))
                item.setText(2, entry.projekt.name)
                item.setText(3, str(entry.anzahl_ak))
                item.setText(4, entry.get_status_display())
                for i in range(0, 5):
                    item.setFont(i, QtGui.QFont('Helvetica', 10))
                    
                self.emit(SIGNAL('addItem'), item)
            
            self.signal.finishedLoading(self)
            
        except Exception, err:
            self.signal.killLoading(self)
            if err.__class__.__name__ == 'OperationalError':
                self.emit(SIGNAL('connect_error'), self)
            else:
                self.emit(SIGNAL('error'), self, err)

        
        
        
