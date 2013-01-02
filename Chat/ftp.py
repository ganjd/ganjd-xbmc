
import os
from PyQt4 import QtGui, QtCore

from PyQt4.QtNetwork import QFtp
from PyQt4.QtCore import QThread
from PyQt4.QtCore import SIGNAL



class Ftp(QFtp):
    
    def __init__(self):
        
        QFtp.__init__(self)
        
        self.action = False
        self.run()
        
        
    def uploadIp(self, ip):
        self.connectToHost('ftp.ganjd.de')
        self.action = 'Upload_Ip'
        self.ip = ip
        
        
    def logout(self):
        self.connectToHost('ftp.ganjd.de')
        self.action = 'Logout'
        
    def getIp(self):
        self.connectToHost('ftp.ganjd.de')
        self.action = 'Get_Ip'
        
    def uploadMsg(self, user, senden_an, msg):
        self.connectToHost('ftp.ganjd.de')
        self.action = 'Upload_Msg'
        self.cd_senden_an = False
        self.user = str(user)
        self.senden_an = str(senden_an)
        self.msg = str(msg)
        
    def getMsg(self, user):
        self.connectToHost('ftp.ganjd.de')
        self.action = 'Get_Msg'
        self.cd_senden_an = False
        self.no_offline_Msg = True
        self.offline_user_count = 0
        self.user = str(user)
        
        
        
    def startAction(self):
        if self.action == 'Upload_Ip':
            self.put(self.ip, 'ip')
            
        elif self.action == 'Logout':
            self.put('offline', 'ip')
            
        elif self.action == 'Get_Ip':
            self.get('ip')
            
        elif self.action == 'Upload_Msg':
            self.cd(self.senden_an+'/')

        elif self.action == 'Get_Msg':
            self.cd(self.user+'/')
            
        else:
            self.close()
        


    def run(self):   
        
        self.connect(self, SIGNAL('listInfo(const QUrlInfo&)'), self.info)
        self.connect(self, SIGNAL('stateChanged(int)'), self.stateChanged)
        self.connect(self, SIGNAL('dataTransferProgress(qint64,qint64)'),self.updateProgress)
        self.connect(self, SIGNAL('readyRead()'), self.readyRead)
        self.connect(self, SIGNAL('commandStarted(int)'), self.commandStarted)
        self.connect(self, SIGNAL('commandFinished(int,bool)'), self.commandFinished)
        self.connect(self, SIGNAL('done(bool)'), self.done)
        
        
    def info(self, urlInfo):
        print urlInfo.name()
        if self.action == 'Get_Msg':
            if urlInfo.name() != '.' and urlInfo.name() != '..':

                if self.currentId()> self.offline_user_count:
                    self.offline_user_count = self.currentId()+1
                    
                self.get(urlInfo.name())
                self.no_offline_Msg = False
                exec 'self.offline_user_%s = urlInfo.name()' %(self.offline_user_count, )
                self.offline_user_count += 1
        
        
    
    def stateChanged(self, state):
        print 'State', state
        if state == 3:
            self.login('u54306167', '11322794')
            
        if state == 4:
            self.cd('Datenbank/GalaBau/Chat/')
            self.startAction()
            
    
    def updateProgress(self, pos, total):
        print pos, total

    def readyRead(self):
        print 'readyRead'
        read = self.readAll()
        if self.action == 'Get_Ip':
            self.emit(SIGNAL('Status'), 'Ip', read)
            
        if self.action == 'Get_Msg':
            exec 'user = self.offline_user_%s' %(self.currentId(), )
            self.emit(SIGNAL('Status'), 'Msg_Get', [user, read])

            
        
    def commandStarted(self, int):
        print 'Start Command: ', int
            
        
    def commandFinished(self, int, bool):
        print 'Finished Command: ', int, bool

        if  self.currentCommand() == QFtp.Put:
            if self.action == 'Upload_Ip':
                self.emit(SIGNAL('Status'), 'Server', 'Started')
                self.close()
                
            if self.action == 'Logout':
                self.emit(SIGNAL('Status'), 'Logout', bool)
                self.close()
            
            if self.action == 'Upload_Msg':
                self.emit(SIGNAL('Status'), 'Msg_Send', bool)
                self.close()
                
        if self.currentCommand() == QFtp.Get:
            if self.action == 'Get_Ip':
                self.close()
            
            if self.action == 'Get_Msg':
                if self.hasPendingCommands() == False:
                    self.close()
                
        if self.currentCommand() == QFtp.Cd:
            if self.action == 'Upload_Msg':
                if self.cd_senden_an == True:
                    if bool == True:
                        self.mkdir(self.senden_an)
                        print bool, self.errorString()
                        
                    else:
                        self.put(self.msg, self.user)
                else:
                    self.cd_senden_an = True
                    
            if self.action == 'Get_Msg':
                if self.cd_senden_an == True:
                    if bool == True:
                        self.mkdir(self.user)
                        
                    else:
                        self.list()
                else:
                    self.cd_senden_an = True
                    
                    
        if self.currentCommand() == QFtp.Mkdir:
            if self.action == 'Upload_Msg':
                self.cd(self.senden_an+'/')
                
        if self.currentCommand() == QFtp.List:
            if self.action == 'Get_Msg':
                if self.no_offline_Msg == True:
                    self.close()

        
    def done(self, bool):
        print 'All Done: ', self.action, bool

        if bool == True:
            print self.currentCommand()
            print  self.error()
            print self.errorString()

