# -*- coding: utf-8 -*-

from PyQt4 import QtCore
from PyQt4.QtCore import QString
from PyQt4.QtGui import QWizardPage
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtCore import SIGNAL

from Orm.db.models import *

from Ui_wizardPage import Ui_WizardPage

from signalReceiver import Signal
from Ui.messageBox import MessageBox

_fromUtf8 = QString.fromUtf8


class WizardPage(QWizardPage, Ui_WizardPage):

    def __init__(self, parent = None):

        QWizardPage.__init__(self, parent)
        self.setupUi(self)
        
        self.messageBox = MessageBox(self)
        self.setStyle()
 
        
    def initializePage(self):
        if self.option == False:
            pass
            
        else:
            self.identifyOption()
            
            
    def initialize_Threads(self):
        self.loadEditWerte = Load_EditWerte(self)
        self.connect(self.loadEditWerte, SIGNAL('addEditWerte'), self.addEditWerte)
        self.connect(self.loadEditWerte, SIGNAL('connect_error'), self.connect_error)
        self.connect(self.loadEditWerte, SIGNAL('error'), self.error)
            

    def setOption(self, option):
        self.option = option
 
 
    def identifyOption(self):
        self.initialize_Threads()
        for identifier in self.option.keys():
        
            if identifier == 'Projekt_Object':
                pass
            
            if identifier == 'Edit':
                self.loadEditWerte.setValues(self.option[identifier])
                self.loadEditWerte.start()

        
    def nextId(self):
        
        if self.field('AKs').toInt()[0] == self.wizard().currentId():
            return 11
        else:
            return self.wizard().currentId() + 1
            
        
        
    def register(self, count):
        self.registerField('AK_' + count, self.input_AK, 'currentText', SIGNAL('activated()'))
        self.registerField('Start_H_' + count, self.input_StartH, 'currentText', SIGNAL('activated()'))
        self.registerField('Start_M_' + count, self.input_StartM, 'currentText', SIGNAL('activated()'))
        self.registerField('Ende_H_' + count, self.input_EndeH, 'currentText', SIGNAL('activated()'))
        self.registerField('Ende_M_' + count, self.input_EndeM, 'currentText', SIGNAL('activated()'))
        self.registerField('Pause_' + count, self.input_Pause)
        self.registerField('AK_Status_' + count, self.input_Status, 'currentText', SIGNAL('activated()'))
 
        self.count = count
            
    def addEditWerte(self, dict):
        self.input_AK.setEditText(dict['ak'])
        self.input_StartH.setCurrentIndex(dict['start_H'])
        self.input_StartM.setCurrentIndex(self.getMinuten(dict['start_M']))
        self.input_EndeH.setCurrentIndex(dict['ende_H'])
        self.input_EndeM.setCurrentIndex(self.getMinuten(dict['ende_M']))
        self.input_Pause.setText(str(dict['pause']))
        self.input_Status.setCurrentIndex(self.getStatus(dict['status']))
        
        
    def editWerte(self, a_ta_object):

        q = AK.objects.filter(a_tag=a_ta_object)

        
        for i, entry in enumerate(q):

            if i+1 == self.wizard().currentId():
                
                self.input_AK.setEditText(entry.ak)
                self.input_StartH.setCurrentIndex(entry.beginn.hour)
                self.input_StartM.setCurrentIndex(self.getMinuten(entry.beginn.minute))
                self.input_EndeH.setCurrentIndex(entry.ende.hour)
                self.input_EndeM.setCurrentIndex(self.getMinuten(entry.ende.minute))
                self.input_Pause.setText(str(entry.pause))
                self.input_Status.setCurrentIndex(self.getStatus(entry.get_status_display()))
                


    
    def getStatus(self, status):
        if status == 'Offen':
            return 0
        if status == 'Ausgezahlt':
            return 1
            
            
    def getMinuten(self, minute):
        if minute == 0:
            return 0
        if minute == 15:
            return 1
        if minute == 30:
            return 2
        if minute == 45:
            return 3
        


    def setStyle(self):
        from PyQt4 import QtGui
        a = QtGui.QStyleFactory.keys()[5]
        b = QtGui.QStyleFactory.create(a)
        self.input_AK.setStyle(b)
        self.input_StartH.setStyle(b)
        self.input_StartM.setStyle(b)
        self.input_EndeH.setStyle(b)
        self.input_EndeM.setStyle(b)
        self.input_Status.setStyle(b)
        
        
    def connect_error(self, sender):
        reply = self.messageBox.connect_error()
        if reply:
            sender.start()


    def error(self, sender, err):
        reply = self.messageBox.error({'err': err, 'sender': sender})
        


class Load_EditWerte(QtCore.QThread):
    
    def __init__(self, parent):
        QtCore.QThread.__init__(self)
        
        self.signal = Signal()
        self.signal.registerLoading(self)
        self.currentId = parent.wizard().currentId()
        

    def setValues(self, a_tag_object):
        self.a_tag_object = a_tag_object
        
    
    def run(self):
        
        try:
            self.signal.startLoading(self)
            q = AK.objects.filter(a_tag=self.a_tag_object)

            for i, entry in enumerate(q):
    
                if i+1 == self.currentId:
            
                    self.emit(
                        SIGNAL('addEditWerte'), 
                        {
                            'ak': entry.ak, 
                            'start_H': entry.beginn.hour,
                            'start_M': entry.beginn.minute , 
                            'ende_H': entry.ende.hour, 
                            'ende_M': entry.ende.minute, 
                            'pause': entry.pause, 
                            'status': entry.get_status_display(), 
                        }
                        )
    
            self.signal.finishedLoading(self)
        
        except Exception, err:
            self.signal.killLoading(self)
            if err.__class__.__name__ == 'OperationalError':
                self.emit(SIGNAL('connect_error'), self)
            else:
                self.emit(SIGNAL('error'), self, err)
