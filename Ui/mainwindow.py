# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtCore import QSettings
from PyQt4.QtCore import SIGNAL
from PyQt4.QtCore import QThread
from Lib.ftp import Ftp
from Ui.status import ShowStatus
from Ui.statusBarWidget import StatusBar_Widget

from Ui_mainwindow import Ui_MainWindow

from mainview import MainView
from Lib.loadSettings import LoadSettings
from chat_view import Chat

_fromUtf8 = QtCore.QString.fromUtf8

from django.dispatch import receiver
from django.db.models.signals import pre_init, post_init
from django.db.backends.signals import connection_created
from signalReceiver import Signal


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, main_app):

        QMainWindow.__init__(self)
        self.setupUi(self)
        
        Signal(self.signalReceiver)

        self.sb_Widget = StatusBar_Widget()
        self.statusBar.addPermanentWidget(self.sb_Widget, 100)

        self.version = '0.01'
        self.restart = False
        
#        self.frame_2.hide()

        
        self.main = MainView(self)
        self.main_app = main_app
        self.readSettings()
        
        self.countLoading = 0
        
        self.dockWidget.hide()
#        self.chat = Chat(self)
#        self.connect(self.chat.chatWidget, SIGNAL('closeReady'), self.chat_CloseReady)



#    @Signal
    def signalReceiver(self, sender, signature, data):

        if signature == 'startLoading':
            if self.countLoading == 0:
               self.startStatusWidget() 
            self.countLoading += 1
            
        if signature == 'finishedLoading':
            self.countLoading -= 1
            if self.countLoading == 0:
                self.statusWidget.close()
        
        if signature == 'killLoading':
            self.countLoading = 0
            self.statusWidget.close()
            
            
    

     
    def startStatusWidget(self):
        self.statusWidget = ShowStatus(self.pos(), self.size())
        
        self.statusWidget.show()
        

    #------------------------------------------------------------------
    #ToolBox
    #------------------------------------------------------------------
    @pyqtSignature("int")
    def on_toolBox_currentChanged(self, index):
        self.main.checkToolBoxIndex(index)
    #-----------------------------Ende--------------------------------
    
    
    #------------------------------------------------------------------
    #Push Buttons
    #------------------------------------------------------------------
    @pyqtSignature("")
    def on_pushButton_as_new_clicked(self):
        self.main.runWizard('AS')
        
    @pyqtSignature("")
    def on_pushButton_kunde_new_clicked(self):
        self.main.runWizard('Kunde')


    @pyqtSignature("")
    def on_pushButton_material_new_clicked(self):
        self.main.runWizard('Material')

        
    @pyqtSignature("")
    def on_pushButton_project_new_clicked(self):
        self.main.runWizard('Project')

    #-----------------------------Ende--------------------------------
    
    
    #------------------------------------------------------------------
    #Tool Bar Actions
    #------------------------------------------------------------------
    @pyqtSignature("")
    def on_actionProjekte_triggered(self):
        self.main.runProjekte()
    
    @pyqtSignature("")
    def on_actionKunden_triggered(self):
        self.main.runKunden()

    @pyqtSignature("")
    def on_actionArbeitsstunden_triggered(self):
        self.main.runArbeitStd()

    @pyqtSignature("")
    def on_actionMaterial_triggered(self):
        self.main.runBelege()
        
    @pyqtSignature("")
    def on_actionBelege_triggered(self):
        self.main.runBelege()
        
    @pyqtSignature("")
    def on_action2011_triggered(self):
        self.setCurrentYear('2011')
        self.main.clearAll()
        self.main.startWidget()

    @pyqtSignature("")
    def on_action2012_triggered(self):
        self.setCurrentYear('2012')
        self.main.clearAll()
        self.main.startWidget()
    

    @pyqtSignature("")
    def on_actionOptionen_triggered(self):
        self.main.openSettings()
        
        
    #-----------------------------Ende--------------------------------
    
    def optionParser(self):
        pass
#        from optparse import OptionParser
#
#        parser = OptionParser(version="%prog 0.1");
#        parser.add_option("-r", "--restart", dest="restart",
#                      help="relativer Pfad des Programms", default=False, metavar="Pfad");
#        parser.add_option("-g", "--gui", dest="gui",
#                      help="Programm mit GUI", default='False', metavar="Bool")
#                      
#        (options, args) = parser.parse_args()
#        print options.restart



    def readSettings(self):
        
        settings = QSettings("GanjD-Soft", "GalaBau");
        
        settings.beginGroup("MainWindow")
        self.resize(settings.value("size", QtCore.QSize(400, 400)).toSize())
        self.move(settings.value("pos", QtCore.QPoint(200, 200)).toPoint())
        self.user = settings.value('user', 'David').toString()
        
        self.jahrList = settings.value('jahrList', [2011, 2012]).toList()
        self.setCurrentYear(settings.value('jahr', 2011).toString())
        settings.endGroup()
        
        
        
    def setCurrentYear(self, jahr):
        jahr = str(jahr)

        exec 'self.action'+jahr+'.setChecked(True)'
        
        for entry in self.jahrList:
            if entry != jahr:
                exec 'self.action'+str(entry.toString())+'.setChecked(False)'
        
        
        settings = QSettings("GanjD-Soft", "GalaBau")
        settings.beginGroup("MainWindow")
        settings.setValue('jahr', jahr)
        settings.endGroup()
        
        self.setWindowTitle('GalaBau - '+jahr+' - '+self.user)
        self.sb_Widget.setUser(self.user)
        self.sb_Widget.setJahr(jahr)
        self.sb_Widget.setInfo('')
        
        


    def chat_CloseReady(self):
        if self.closing == True:
            if self.closeReady == False:
                self.closeReady = True
                return
                
            if self.closeReady == True:
                if self.restart == True:
                    self.main_app.exit(1000)
                else:
                    self.main_app.exit()




    def writeSettings(self):
        settings = QSettings("GanjD-Soft", "GalaBau")
        settings.beginGroup("MainWindow")
        settings.setValue("size", self.size())
        settings.setValue("pos", self.pos())
        settings.endGroup()
                    
    
    def closeEvent(self, event):
        self.writeSettings()
        event.accept()
            
        
    

