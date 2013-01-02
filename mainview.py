# -*- coding: utf-8 -*-


from Lib.tools import Tools

from Ui.Wizard.wizard import Wizard

from Lib.arbeitsstunden.main_aStd import AStd_Main
from Lib.projekte.main_projekt import Projekt
from Lib.kunden.main_kunden import Kunden
from Lib.belege.main_belege import Belege

from PyQt4.QtCore import QThread
from PyQt4.QtCore import QSettings
from PyQt4.QtCore import SIGNAL
from PyQt4.QtCore import QObject

from Ui.settings import Settings

from PyQt4.QtGui import QMainWindow


#_fromUtf8 = QtCore.QString.fromUtf8



class MainView(QObject):
    
    def __init__(self, MainWindow):
        
        QObject.__init__(self)
        
        self.MainWindow = MainWindow

        self.run()
        
#        self.MainWindow.toolBar.hide()


    def run(self):
   
        self.ak = AStd_Main()
        self.projekte = Projekt()
        self.kunden = Kunden()
        self.belege = Belege()
        
        self.startWidget()
        


    def startWidget(self):
        self.runProjekte()



    def runKunden(self):
        print 'Kunden'
        self.clearAll()
        self.kunden.refresh()
        self.MainWindow.verticalLayout_6.addWidget(self.kunden)
#        self.MainWindow.label_main_title.setText('Kunden')

       
    def runProjekte(self):
        print 'Projekte'
        self.clearAll()
        self.projekte.refresh()
        self.MainWindow.verticalLayout_6.addWidget(self.projekte.tabWidget)
#        self.MainWindow.label_main_title.setText('Projekte')
        
        
    def runArbeitStd(self):
        print 'Arbeitsstunden'
        self.clearAll()
        self.ak.refresh()
        self.MainWindow.verticalLayout_6.addWidget(self.ak)
#        self.MainWindow.label_main_title.setText('Arbeitsstunden')


    def runBelege(self):
        self.clearAll()
        self.belege.refresh()
        self.MainWindow.verticalLayout_6.addWidget(self.belege)
        
        

    def openSettings(self):
        self.settings = Settings()
        self.settings.show()
        
        
        
    def clearAll(self):
        self.projekte.close()
        self.kunden.close()
        self.ak.close()
        self.belege.close()
