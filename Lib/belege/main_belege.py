# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import SIGNAL


from Ui.Wizard.wizard import Wizard
from Ui.Belege.belege import Belege_Ui

from Lib.belege.filter import Filter
from Lib.tools import Tools
from Ui.messageBox import MessageBox
from Lib.loadSettings import LoadSettings
from signalReceiver import Signal
from Lib.sorting import Sort


_fromUtf8 = QtCore.QString.fromUtf8


class Belege(Belege_Ui):
    
    def __init__(self):
        Belege_Ui.__init__(self)
        
        self.settings = LoadSettings()
        self.messageBox = MessageBox(self)
        self.tools = Tools()
        
        self.initialize_Threads()
        
        

    def initialize_Threads(self):
        self.loadBelege = Load_Belege()
        self.connect(self.loadBelege, SIGNAL('addItem'), self.addItem)
        self.connect(self.loadBelege, SIGNAL('setSummen'), self.setSummen)
        self.connect(self.loadBelege, SIGNAL('connect_error'), self.connect_error)
        self.connect(self.loadBelege, SIGNAL('error'), self.error)
        


    def loadTreeWidget(self):
        self.treeWidget.clear()
        
        #Konfiguriere Header fuer Sortierung
        self.treeWidget.setSortingEnabled(False)
        header = self.treeWidget.header()
        header.setSortIndicatorShown(True)
        header.setClickable(True)
        self.sort = Sort(self.treeWidget)
        self.connect(header, QtCore.SIGNAL('sectionClicked(int)'), self.sort.byColumn)
        
        self.loadBelege.start()


        
    def addItem(self, item):
        self.treeWidget.addTopLevelItem(item)    
    
    
    def setSummen(self, gesamt):
        self.label_summe.setText(_fromUtf8(str(gesamt)+' €'))        
        

    def contextMenuActions(self, action):
        action = action.data().toString()
        
        if action == 'Refresh':
            self.refresh()
            
        if action == 'Edit':
            wizard = Wizard('Beleg', {'Edit': self.getBelegObject()})
            if wizard.result == 1:
                self.refresh()


        if action == 'Del':
            reply = self.messageBox.del_question(self.getBelegObject())
            if reply == 1:
                self.getBelegObject().delete()
                self.refresh()


            
        
    def getBelegObject(self):
        return self.treeWidget.currentItem().data(0, 32).toPyObject()
        

        
    def refresh(self):
        self.show()
        self.loadTreeWidget()
        

    def selectItem(self, beleg_detail_object):
        nr = self.tools.formatBelegNr(beleg_detail_object.nr.nr)
        item = self.ui.treeWidget.findItems(nr, QtCore.Qt.MatchExactly, 0)[0]
        self.ui.treeWidget.setItemSelected(item, True)
        self.ui.treeWidget.setCurrentItem(item)
        
        
    def connect_error(self, sender):
        reply = self.messageBox.connect_error()
        if reply:
            sender.start()


    def error(self, sender, err):
        reply = self.messageBox.error({'err': err, 'sender': sender})
        



class Load_Belege(QtCore.QThread):
    
    def __init__(self):
        QtCore.QThread.__init__(self)
        
        self.signal = Signal()
        self.signal.registerLoading(self)
        
        self.settings = LoadSettings()
        self.filter = Filter()
        self.tools = Tools()
        
        self.bLoadFilterOnly = False
        self.bLoadFilter = True
        
    
    def run(self):
        try:
            self.signal.startLoading(self)
            
            sqlResult = self.filter.getResult()

            summe = float(0)
            for entry in sqlResult:
                item= QtGui.QTreeWidgetItem()
                item.setData(0, 32, QtCore.QVariant(entry))
                
                item.setText(0, self.tools.formatBelegNr(entry.nr))
                item.setText(1, self.tools.formatDatum(entry.datum))
                item.setText(2, entry.lieferant)
                item.setText(3, entry.zahlungsart)
                item.setText(4, str(entry.brutto))
                
                for i in range(0, 5):
                    item.setFont(i, QtGui.QFont('Helvetica', 10))
                
                self.emit(SIGNAL('addItem'), item)
                summe = summe+entry.brutto
            
            self.emit(SIGNAL('setSummen'), summe)
            self.signal.finishedLoading(self)

        except Exception, err:
            self.signal.killLoading(self)
            if err.__class__.__name__ == 'OperationalError':
                self.emit(SIGNAL('connect_error'), self)
            else:
                self.emit(SIGNAL('error'), self, err)
