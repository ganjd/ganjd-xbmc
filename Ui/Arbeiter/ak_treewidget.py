# -*- coding: utf-8 -*-


from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtCore import SIGNAL

from Ui_ak_treewidget import Ui_Form

from Lib.arbeitsstunden.filter import Filter
from Lib.tools import Tools
from Lib.getsummen import Get_Summen
from Ui.messageBox import MessageBox
from signalReceiver import Signal
from Lib.sorting import Sort


_fromUtf8 = QtCore.QString.fromUtf8



class AK_TreeWidget(QWidget, Ui_Form):

    def __init__(self, arbeiter):

        QWidget.__init__(self)
        self.setupUi(self)
        
        self.arbeiter = arbeiter
        self.messageBox = MessageBox(self)
        
        self.initialize_Threads()
        self.loadTreeWidget()
        
        
        
    def initialize_Threads(self):
        self.loadA_Tag = Load_A_Tag(self.arbeiter)
        self.connect(self.loadA_Tag, SIGNAL('addItem'), self.addItem)
        self.connect(self.loadA_Tag, SIGNAL('setSummen'), self.setSummen)
        self.connect(self.loadA_Tag, SIGNAL('connect_error'), self.connect_error)
        self.connect(self.loadA_Tag, SIGNAL('error'), self.error)
#        self.connect(self.loadAS.filter, SIGNAL('addFilterItem'), self.addFilterItem_AS)
        
        
    def loadTreeWidget(self):

        self.treeWidget.clear()
        
        self.treeWidget.setSortingEnabled(False)
        header = self.treeWidget.header()
        header.setSortIndicatorShown(True)
        header.setClickable(True)
        self.sort = Sort(self.treeWidget)
        self.connect(header, QtCore.SIGNAL('sectionClicked(int)'), self.sort.byColumn)

        self.loadA_Tag.start()

        

    def addItem(self, item):
        self.treeWidget.addTopLevelItem(item)
        self.sort.byColumn(0)
        
        
    def setSummen(self, gesamt, offen, abgerechnet):
        print gesamt, offen, abgerechnet
        self.label.setText('Gesamt:   '+str(gesamt)+' Stunden')
        self.label_2.setText('Offen:   '+str(offen)+' Stunden')
        self.label_3.setText('Abgerechnet:   '+str(abgerechnet)+' Stunden')
        
        
    def loadFilter(self, filter_art, filter_string):
        self.loadA_Tag.filter.setFilter(filter_art, filter_string)

        
    def connect_error(self, sender):
        reply = self.messageBox.connect_error()
        if reply:
            sender.start()


    def error(self, sender, err):
        reply = self.messageBox.error({'err': err, 'sender': sender})

        
        



class Load_A_Tag(QtCore.QThread):
    
    def __init__(self, arbeiter):
        QtCore.QThread.__init__(self)
        
        self.signal = Signal()
        self.signal.registerLoading(self)

        self.arbeiter = arbeiter
        self.filter = Filter()
        self.tools = Tools()
        self.summe = Get_Summen()
        
        
        
    
    def run(self):
        try:
            self.signal.startLoading(self)
            
            self.summe.clear()
            sqlResult = self.filter.getDetailResult(self.arbeiter)
            
            for entry in sqlResult:
                stunden = str(self.tools.getTimeDifference(entry.beginn, entry.ende, entry.pause))
                
                item= QtGui.QTreeWidgetItem()
                item.setData(0, 32, QtCore.QVariant(entry))
                
                item.setText(0, self.tools.formatDatum(entry.a_tag.datum))
                item.setText(1, self.tools.formatKunde(entry.a_tag.projekt.kunde))
                item.setText(2, entry.a_tag.projekt.name)
                item.setText(3, self.tools.formatZeit(entry.beginn))
                item.setText(4, self.tools.formatZeit(entry.ende))
                item.setText(5, str(entry.pause))
                item.setText(6, entry.get_status_display())
                
                for i in range(0, 5):
                    item.setFont(i, QtGui.QFont('Helvetica', 10))
                
                self.emit(SIGNAL('addItem'), item)
                
                #---------Hole Summen-------------------------------------
                stunden = float(stunden)
                self.summe.stunden_Gesamt(stunden)
                self.summe.stunden_Offen(stunden, entry.status)
                self.summe.stunden_Abgerechnet(stunden, entry.status)
                #---------Ende----------------------------------------------
            
            self.emit(SIGNAL('setSummen'),self.summe.stundenGesamt, self.summe.stundenOffen, self.summe.stundenAbgerechnet)
    
            
            self.signal.finishedLoading(self)
        
        except Exception, err:
            self.signal.killLoading(self)
            if err.__class__.__name__ == 'OperationalError':
                self.emit(SIGNAL('connect_error'), self)
            else:
                self.emit(SIGNAL('error'), self, err)

        
        
        
        
        
