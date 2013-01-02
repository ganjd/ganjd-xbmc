# -*- coding: utf-8 -*-


from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_settings import Ui_Dialog
from Lib.saveSettings import SaveSettings

#Impotiere Einstellung Widgets
from Ui.Setting_Widgets.allgemein import Settings_Allgemein
from Ui.Setting_Widgets.arbeiter import Settings_Arbeiter
#from Ui.Setting_Widgets.datenbank import Settings_Datenbank


_fromUtf8 = QtCore.QString.fromUtf8


TREEWIDGET_ITEMS = {
'Allgemein':'Settings_Allgemein', 
'Arbeiter':'Settings_Arbeiter', 
}


TREEWIDGET_FONT = 'Verdana'
TREEWIDGET_FONTSIZE = int('10')




class Settings(QDialog, Ui_Dialog):

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        
        self.identifyerDict = {}
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        
        self.loadTreeWidget()
        self.initializePage()
        
        
    def loadTreeWidget(self):
        self.treeWidget.clear()
        

        for entry in TREEWIDGET_ITEMS.keys():
            
            item= QtGui.QTreeWidgetItem()
            item.setData(0, 32, QtCore.QVariant(TREEWIDGET_ITEMS[entry]))

            item.setText(0, _fromUtf8(entry))
            item.setFont(0, QtGui.QFont(TREEWIDGET_FONT, TREEWIDGET_FONTSIZE)) 
            self.treeWidget.addTopLevelItem(item)
                
        self.treeWidget.sortItems(0, QtCore.Qt.AscendingOrder)

        
        
    def initializePage(self):
        count = self.treeWidget.topLevelItemCount()
        for i in range(0, count):
            className =  self.treeWidget.topLevelItem(i).data(0, 32).toString()
            try:
                exec 'self.%s = %s()' % (className, className)
                if i == 0:
                    exec 'self.ui = self.%s' % className
                    self.verticalLayout.addWidget(self.ui)
                    self.ui.show()
            except Exception, err:
                print err


    
    @pyqtSignature("QTreeWidgetItem*, int")
    def on_treeWidget_itemClicked(self, item, column):
        className =  item.data(0, 32).toString()
        self.load_Settings_Widget(className)
        
        
    def load_Settings_Widget(self, className):
    
        self.ui.close()

        try:
            exec 'self.ui = self.%s' % className
            self.verticalLayout.addWidget(self.ui)
            self.ui.show()
        except Exception, err:
            print err

    
    @pyqtSignature("")
    def on_pushButton_ok_clicked(self):
  
        self.identifyerDict[self.ui.identifyer] = self.ui.getWerte()
        SaveSettings().save(self.identifyerDict)
        self.close()
        

    
    @pyqtSignature("QTreeWidgetItem*, QTreeWidgetItem*")
    def on_treeWidget_currentItemChanged(self, current, previous):
        if previous != None:
            className = previous.data(0, 32).toString()
            try:
                exec 'identifyer = self.%s.identifyer' % className
                exec 'werte = self.%s.getWerte()' % className
                self.identifyerDict[identifyer] = werte
            except Exception, err:
                print err
                
    
    @pyqtSignature("")
    def on_pushButton_abbrechen_clicked(self):
        self.close()

    
    @pyqtSignature("")
    def on_pushButton_anwenden_clicked(self):
        self.identifyerDict[self.ui.identifyer] = self.ui.getWerte()
        SaveSettings().save(self.identifyerDict)
    
    @pyqtSignature("")
    def on_pushButton_standard_clicked(self):
        reply = QtGui.QMessageBox.question(self, _fromUtf8('Zurücksetzen'), _fromUtf8('Sollen alle Einstellungen wirklich zurückgesetzt werden ?'), 'Ja', 'Nein')
        if reply == 0:
            SaveSettings().setStandard()
            self.ui.close()
            self.initializePage()
        

