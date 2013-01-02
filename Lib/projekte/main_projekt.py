# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QObject
from PyQt4.QtCore import SIGNAL

from Ui.Wizard.wizard import Wizard
from Ui.Projekte.projekt import Projekt_Ui
from Lib.projekte.details_projekt import Projekt_Details

from Lib.tools import Tools
from Orm.db.models import *
from Lib.loadSettings import LoadSettings
from Ui.messageBox import MessageBox
from signalReceiver import Signal



_fromUtf8 = QtCore.QString.fromUtf8



class Projekt(Projekt_Ui):
    
    def __init__(self):
        Projekt_Ui.__init__(self)
        
        self.settings = LoadSettings()
        self.tools = Tools()
        self.messageBox = MessageBox(self)
        
        self.initialize_Threads()
        self.loadTabWidget()
        
        
        
    def initialize_Threads(self):
        self.loadProjekte = Load_Projekte()
        self.connect(self.loadProjekte, SIGNAL('addItem'), self.addItem)
        self.connect(self.loadProjekte, SIGNAL('connect_error'), self.connect_error)
        self.connect(self.loadProjekte, SIGNAL('error'), self.error)
        

    def loadTabWidget(self):

        self.tabWidget = QtGui.QTabWidget()
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(True)
#        self.tabWidget.setMovable(True)
        self.connect(self.tabWidget, SIGNAL("tabCloseRequested (int)"), self.tabCloseRequest)
        
        
        self.addTab(self, u'Übersicht')
        

    
    def addTab(self, widget, tabTitle):
        self.tab = QtGui.QWidget()
        self.verticalLayout = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout.addWidget(widget)
        self.tabWidget.addTab(self.tab, tabTitle)
        self.tabWidget.setCurrentIndex(self.tabWidget.count()-1)

    
    def tabCloseRequest(self, int):
        if int > 0:
            self.tabWidget.removeTab(int)
            
            
    
    def loadTreeWidget(self):
        self.treeWidget.clear()
        self.loadProjekte.start()
        

    def addItem(self, item):
        self.treeWidget.addTopLevelItem(item)
        
        
    
    def openDetails(self, content):
        projekt_object = content.data(0, 32).toPyObject()
        projekt_name = content.text(1)
        
        details = Projekt_Details(projekt_object)
        self.addTab(details, projekt_name)



    def contextMenuActions(self, action):
        action = self.tools.getEncodedString(action.text())
        
        if action == 'Aktualisieren':
            self.refresh()
            
            
        if action == 'Status ändern':
            print 'Status ändern'
            
            
        if action == 'Bearbeiten':
            self.runWizard({'Edit': self.getProjektObject()})
            
            
        if action == 'Löschen':
            reply = self.messageBox.del_question(self.getProjektObject())
            if reply == 1:
                try:
                    self.getProjektObject().delete()
                    self.refresh()
                except Exception, err:
                    print err
                    self.messageBox.del_error(self.getProjektObject())
                    



    def getProjektObject(self):
        return self.treeWidget.currentItem().data(0, 32).toPyObject()
        
        
        
    def refresh(self):        
        self.tabWidget.show()
        self.loadTreeWidget()

        
    def close(self):
        self.tabWidget.close()
        
        
    def runWizard(self, option=False):
        wizard = Wizard('Projekt', option)
        if wizard.result == 1:
            self.refresh()
        

    def connect_error(self, sender):
        reply = self.messageBox.connect_error()
        if reply:
            sender.start()


    def error(self, sender, err):
        reply = self.messageBox.error({'err': err, 'sender': sender})
        
        

class Load_Projekte(QtCore.QThread):
    
    def __init__(self):
        QtCore.QThread.__init__(self)
        
        self.signal = Signal()
        self.signal.registerLoading(self)
        
        self.settings = LoadSettings()
        
        self.bLoadFilterOnly = False
        self.bLoadFilter = True
        
    
    def run(self):
        try:
            self.signal.startLoading(self)
            
            q = Projekte.objects.filter(beginn__year=self.settings.currentYear()).order_by('nr')
            
            for entry in q:
                item= QtGui.QTreeWidgetItem()
                item.setData(0, 32, QtCore.QVariant(entry))
    
                item.setText(0, str(entry.nr))
                item.setText(1, entry.name)
                item.setText(2, entry.kunde.nachname)
                item.setText(3, entry.get_status_display())
                
                for i in range(0, 4):
                    item.setFont(i, QtGui.QFont('Verdana', 10))
                
                self.emit(SIGNAL('addItem'), item)
                    
            self.signal.finishedLoading(self)

        except Exception, err:
            self.signal.killLoading(self)
            if err.__class__.__name__ == 'OperationalError':
                self.emit(SIGNAL('connect_error'), self)
            else:
                self.emit(SIGNAL('error'), self, err)

