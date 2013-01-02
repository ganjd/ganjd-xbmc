# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QWidget
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QMenu

from Ui_details import Ui_Form
from Lib.contextMenu import ContextMenu


_fromUtf8 = QtCore.QString.fromUtf8


class Projekt_Details_Ui(QWidget, Ui_Form):

    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)


        self.toolButton_beleg.hide()#TODO: Belege versteckt
        self.toolButtonProperty()
        self.show_AS()
        self.frame_filter.hide()
        self.setStyle()
        
        
    def toolButtonProperty(self):
        toolButtonMenu_new = QMenu()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/res/1318969250_gnome-planner.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        toolButtonMenu_new.addAction(icon, _fromUtf8('Arbeitsstunden'))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/res/1318969228_applications-development.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        toolButtonMenu_new.addAction(icon, _fromUtf8('Beleg'))
        
        toolButtonMenu_ansicht = QMenu()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/res/1318969250_gnome-planner.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        toolButtonMenu_ansicht.addAction(icon, _fromUtf8('Arbeitsstunden'))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/res/1318969228_applications-development.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        toolButtonMenu_ansicht.addAction(icon, _fromUtf8('Material'))
        toolButtonMenu_ansicht.addSeparator()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/res/1318972409_view_detailed.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        toolButtonMenu_ansicht.addAction(icon, _fromUtf8('Beides'))
        
        self.toolButton.setMenu(toolButtonMenu_new)
        self.toolButton_ansicht.setMenu(toolButtonMenu_ansicht)
        

    
    @pyqtSignature("QPoint")
    def on_treeWidget_customContextMenuRequested(self, pos):
        self.menu = ContextMenu(self.treeWidget)
        self.connect(self.menu.contextMenu, QtCore.SIGNAL("triggered(QAction *)"), self.contextMenuActions_AS)
        
        if len(self.treeWidget.selectedItems()) > 0:
            
#            if self.parent.checkPosExsist() == False:
            self.menu.projekt_as()
#            else:
#                self.menu.projekt_as_PosEdit()
                
        else:
            self.menu.noSelection()
        self.menu.show(pos)

    
    @pyqtSignature("QPoint")
    def on_treeWidget_2_customContextMenuRequested(self, pos):
        self.menu = ContextMenu(self.treeWidget_2)
        self.connect(self.menu.contextMenu, QtCore.SIGNAL("triggered(QAction *)"), self.contextMenuActions_Material)
        
        if len(self.treeWidget_2.selectedItems()) > 0:
            self.menu.projekt_material()
        else:
            self.menu.noSelection()
        self.menu.show(pos)
        
        
    @pyqtSignature("")
    def on_toolButton_clicked(self):
        self.toolButton.showMenu()

    
    @pyqtSignature("QAction*")
    def on_toolButton_triggered(self, action):
        self.toolButtonActions(action)
    
    
    @pyqtSignature("")
    def on_toolButton_pos_clicked(self):
        self.showRechnungen()
        pass
#        self.runPos_All()
    
    
    @pyqtSignature("")
    def on_toolButton_switch_clicked(self):

        if self.frame_as.isHidden() == True:
            self.show_AS()
            
        else:
            self.show_Material()
            
            
    @pyqtSignature("")
    def on_toolButton_ansicht_clicked(self):
        self.toolButton_ansicht.showMenu()

    
    @pyqtSignature("QAction*")
    def on_toolButton_ansicht_triggered(self, action):
        action = action.text()
        if action == 'Arbeitsstunden':
            self.show_AS()
        if action == 'Material':
            self.show_Material()
        if action == 'Beides':
            self.show_Beides()

        
        
    def show_Material(self):
        self.frame_material.show()
        self.toolButton_switch.setText('Arbeitsstunden')
        
        self.frame_as.hide()
        self.line_3.hide()
        
        
    def show_AS(self):
        self.frame_as.show()
        self.toolButton_switch.setText('Material')
        
        self.frame_material.hide()
        self.line_3.hide()
        
    
    def show_Beides(self):
        self.frame_as.show()
        self.frame_material.show()
        self.line_3.show()
        
    
    @pyqtSignature("")
    def on_toolButton_ak_clicked(self):
        self.runArbeiter()
    
    @pyqtSignature("")
    def on_toolButton_beleg_clicked(self):
        self.runBeleg()
        
        
    @pyqtSignature("")
    def on_toolButton_filter_clicked(self):
        if self.toolButton_filter.isChecked() == False:
            self.frame_filter.hide()
        else:
            self.frame_filter.show()
            self.label_10.setText(_fromUtf8(self.comboBox_filter_art.currentText() + ' wählen:'))
    

    @pyqtSignature("QString")
    def on_comboBox_filter_art_activated(self, filter_art):
        self.loadFilter_Material(filter_art)
        self.label_10.setText(_fromUtf8(filter_art + ' wählen:'))

    
    @pyqtSignature("QString")
    def on_comboBox_filter_string_activated(self, filter_string):
        filter_art = self.comboBox_filter_art.currentText()
        self.loadFilter_Material(filter_art, filter_string)
        

    def setStyle(self):
        from PyQt4 import QtGui
        a = QtGui.QStyleFactory.keys()[5]
        b = QtGui.QStyleFactory.create(a)
        self.comboBox_filter_art.setStyle(b)
        self.comboBox_filter_string.setStyle(b)


