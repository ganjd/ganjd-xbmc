 # -*- coding: utf-8 -*-

from PyQt4.QtCore import QThread
from PyQt4.QtCore import QString
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QWizardPage
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtCore import SIGNAL

from Ui_wizardFinalPage import Ui_WizardPage

from Orm.db.models import *
from Lib.tools import Tools
from signalReceiver import Signal
from Ui.messageBox import MessageBox
import datetime



_fromUtf8 = QString.fromUtf8


class WizardFinalPage(QWizardPage, Ui_WizardPage):

    def __init__(self, parent = None):

        QWizardPage.__init__(self, parent)
        self.setupUi(self)
        
        self.tools = Tools()
        self.messageBox = MessageBox(self)
    
        self.initialize_Threads()
        self.validate = False
        self.dict = {}
        
    
    def initialize_Threads(self):
        self.saveA_Tag = Save_A_Tag()
        self.connect(self.saveA_Tag, SIGNAL('savingFinished'), self.savingFinished)
        self.connect(self.saveA_Tag, SIGNAL('connect_error'), self.connect_error)
        self.connect(self.saveA_Tag, SIGNAL('error'), self.error)
    

    def initializePage(self):
        
        self.clearWidget()
        self.akDetails()
        
        datum = self.field('Datum').toDate().toPyDate()
        kunde = self.field('Kunde').toString()
        projekt = self.field('Projekt').toString()
        status = self.field('Status').toString()
        
        kundeData = self.wizard().kunde
        projektData = self.wizard().projekt


        
        self.label_Datum.setText('Datum:   '+datum.strftime('%d.%m.%Y'))
        self.label_Kunde.setText('Kunde:   '+kunde)
        self.label_Projekt.setText('Projekt:   '+projekt)
        self.label_Status.setText('Status:   '+status)
        
        self.dict['Datum'] = datum
        self.dict['Kunde'] = kundeData
        self.dict['Projekt'] = projektData
        self.dict['Status'] = self.tools.shortStatusName(status)
        
        print self.dict




    def akDetails(self):
        
        for i in range(1,  self.field('AKs').toInt()[0] + 1):
        
            count = str(i)
            
            ak = self.field('AK_'+count).toString().toUtf8()
            beginn = datetime.time(self.field('Start_H_'+count).toInt()[0], self.field('Start_M_'+count).toInt()[0])
            ende = datetime.time(self.field('Ende_H_'+count).toInt()[0], self.field('Ende_M_'+count).toInt()[0])
            
            pause = self.field('Pause_'+count).toString()
            if pause == '':
                pause = 0
            else:
                pause = self.field('Pause_'+count).toInt()[0]
                
            ak_status = self.field('AK_Status_'+count).toString()
            
            
            self.setWidget(ak, beginn, ende, pause, ak_status)
            
            self.dict['AK_'+count] = [ak, beginn, ende, pause, self.tools.shortStatusName_AK(ak_status)] 
            self.dict['count'] = count
        
        
        
    def setWidget(self, ak, beginn, ende, pause, ak_status):
        
        font_groupbox = QtGui.QFont()
        font_groupbox.setPointSize(10)
        
        font_label = QtGui.QFont()
        font_label.setPointSize(10)
        
        self.groupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setFlat(True)
        self.groupBox.setFont(font_groupbox)
        self.groupBox.setTitle(_fromUtf8(ak))
        
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(80, -1, -1, -1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        
        self.label_Start = QtGui.QLabel(self.groupBox)
        self.label_Start.setFont(font_label)
        self.label_Start.setText('Arbeitsbeginn:   '+beginn.strftime('%H : %M'))
        self.horizontalLayout.addWidget(self.label_Start)
        
        self.label_Ende = QtGui.QLabel(self.groupBox)
        self.label_Ende.setFont(font_label)
        self.label_Ende.setText('Arbeitsende:   '+ende.strftime('%H : %M'))
        self.horizontalLayout.addWidget(self.label_Ende)
        
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        self.label_Pause = QtGui.QLabel(self.groupBox)
        self.label_Pause.setFont(font_label)
        self.label_Pause.setText('Pause:   '+str(pause))
        
        self.verticalLayout.addWidget(self.label_Pause)
        
        self.label_Status_AK = QtGui.QLabel(self.groupBox)
        self.label_Status_AK.setFont(font_label)
        self.label_Status_AK.setText('Status:   '+ak_status)
        
        self.verticalLayout.addWidget(self.label_Status_AK)
        self.verticalLayout_4.addWidget(self.groupBox)

    
    def clearWidget(self):

        self.scrollAreaWidgetContents.close()
        
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 483, 233))

        self.verticalLayout_4 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        

    def setOption(self, option):
        self.option = option
    
    
    def savingFinished(self):
        self.validate = True
        self.wizard().next()
    
    def validatePage(self):
        if not self.validate:
            self.saveA_Tag.setValues(self.dict, self.option)
            self.saveA_Tag.start()
        print self.validate
        return self.validate

        

    def connect_error(self, sender):
        reply = self.messageBox.connect_error()
        if reply:
            sender.start()

    def error(self, sender, err):
        reply = self.messageBox.error({'err': err, 'sender': sender})



class Save_A_Tag(QThread):
    
    def __init__(self):
        QThread.__init__(self)
        
        self.signal = Signal()
        self.signal.registerLoading(self)
        
        
    def setValues(self, input, option):
        self.input = input 
        self.option = option
        
    def run(self):
        try:
            self.signal.startLoading(self)
            
            input = self.input
            
            update = False
            
            if self.option != False:
                
                for identifier in self.option.keys():
                    
                    if identifier == 'Edit':
                        _a_tag = self.option[identifier]
                        _a_tag.projekt = input['Projekt']
                        _a_tag.datum = input['Datum']
                        _a_tag.status = input['Status']
                        _a_tag.anzahl_ak = input['count']
                        
                        update = True
    
            if not update:
                _a_tag = A_Tag(
                    projekt = input['Projekt'], 
                    datum = input['Datum'], 
                    status = input['Status'], 
                    anzahl_ak = input['count'], 
                    )
                    
            _a_tag.save()
            
            if update:
                for entry in AK.objects.filter(a_tag=_a_tag):
                    entry.delete()
                    
    
            for i in range(1, int(input['count'])+1):
                _ak = AK(
                    a_tag=_a_tag, 
                    ak = input['AK_'+str(i)][0],
                    beginn = input['AK_'+str(i)][1], 
                    ende = input['AK_'+str(i)][2], 
                    pause = input['AK_'+str(i)][3], 
                    status = input['AK_'+str(i)][4], 
                    )
    
                _ak.save()
                
            self.signal.finishedLoading(self)
            self.emit(SIGNAL('savingFinished'))
            
        except Exception, err:
            self.signal.killLoading(self)
            if err.__class__.__name__ == 'OperationalError':
                self.emit(SIGNAL('connect_error'), self)
            else:
                self.emit(SIGNAL('error'), self, err)

        


