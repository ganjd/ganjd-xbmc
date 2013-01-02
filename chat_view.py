# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from Chat.Ui.mainwidget import MainWidget


_fromUtf8 = QtCore.QString.fromUtf8

class Chat(QtCore.QObject):
    def __init__(self, MainWindow):
        
        QtCore.QObject.__init__(self)
        
        self.main = MainWindow
        
        self.user = self.main.user
        self.dockWidget = self.main.dockWidgetContents
        
        if self.user == 'Server':
            self.chatWidget = MainWidget(self.user, server=True)
            self.server = True

        else:
            self.chatWidget = MainWidget(self.user)
            self.server = False
            print 'NoServer'
            
        self.connect(self.chatWidget.client, QtCore.SIGNAL('Userlist'), self.userlist)
        self.connect(self.chatWidget.client, QtCore.SIGNAL('State'), self.state)
            
            
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidget)
        self.verticalLayout.addWidget(self.chatWidget)
        
        
    def state(self, state):
#        if state == 0:
#            self.dockWidget.hide()
        if state == 3:
            self.dockWidget.show()
        
    def userlist(self, user, status):
        text = '%s ist jetzt %s' % (user, status)
        print text
        
        if user != self.user:
            
            if status == 'online':
                self.main.dockWidget.show()
                
        
#                self.msgBox = QtGui.QMessageBox(self.main)
#                self.msgBox.setWindowTitle('Online')
#                self.msgBox.addButton('OK', QtGui.QMessageBox.AcceptRole)
#    #            self.msgBox.addButton('Abbrechen', QtGui.QMessageBox.RejectRole)
#        
#                self.msgBox.setText(_fromUtf8(text))
#        #        self.msgBox.setInformativeText(_fromUtf8('Internetverbindung prüfen und Vorgang wiederholen.\n'))
#                
#                reply = self.msgBox.exec_()
                
    
    def close(self):
        
        self.chatWidget.close()
