
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import SIGNAL
from PyQt4.QtNetwork import QTcpServer
from PyQt4.QtNetwork import QHostAddress

from ftp import Ftp

import sys
from getPublicIp import PublicIp



class Server(QTcpServer):
    
    def __init__(self):
        QTcpServer.__init__(self)
        
        self.ftp = Ftp()
        self.connect(self.ftp, SIGNAL('Status'), self.ftpStatus)
        
#        self.getPublicIp = PublicIp()
#        self.connect(self.getPublicIp, SIGNAL('Public_Ip'), self.setPublicIp)
#        self.getPublicIp.start()
        
        
        self.userlist = [['David','1234'], ['Exse', '1234']]#, ['Esra','1234'], ['Test','1234']
        
        self.dict = {}
        for user in self.userlist:
            self.dict[user[0]] = 'offline'
        
        self.connect(self, SIGNAL('newConnection()'), self.newConnection)


    def setPublicIp(self, ip):
        self.ftp.uploadIp(ip)
        print ip
        

    def runServer(self):
        self.listen(QHostAddress.Any, 5006)
        print self.serverAddress().toString()
        print self.serverPort()
        
    def stopServer(self):
        self.ftp.logout()
        
        
    def ftpStatus(self, id, status):
        self.emit(SIGNAL('Status'), id, status)

        
    def newConnection(self):
        print 'newConnection'
        self.tcp = self.nextPendingConnection()
        self.connect(self.tcp, SIGNAL('readyRead()'), self.incoming)

        
    def incoming(self):
        print self.dict
        print self.sender()

        msg = str(self.sender().readAll())
        
        msg = eval(msg)
        msg_Key = msg.keys()[0]
        msg_Value = msg[msg_Key]
        

        if msg_Key == 'login':
            self.__login(msg_Value)
            
        if msg_Key == 'logout':
            self.dict[msg_Value].close()
            self.dict[msg_Value] = 'offline'
            self.sendUserlist()
            print self.dict
            
                
        if  msg_Key == 'text':
            self.__text(msg_Value)
            
            
            
            
    def __login(self, msg_Value):
        
        user = self.checkUser(msg_Value)
        
        if  user[0] == True:
            print 'Login Richtig'
            
            self.dict[user[1]] = self.sender()
            self.sendUserlist()
            return
            
        else:
            print 'Login Falsch'
            self.sender().close()
            return

                    
        
    def __text(self, msg_Value):
        
        for user in self.dict.keys():
            tcpObject = self.dict[user]
            
            if tcpObject == self.sender():
                sender_user = user
                print 'Nachricht von ' +user
                
                
        
        msg_Value = eval(msg_Value)
        send_an = msg_Value[0]
        send_text = msg_Value[1]
        
        if send_an != 'Alle':
       
            tcpObject = self.dict[send_an]
            if tcpObject != 'offline':
                print tcpObject.state()
                if tcpObject.state() == 3:
                    text = "{'%s': '''['%s','%s']'''}" %('text', sender_user, send_text)
                    tcpObject.write(text)
                    print 'Senden an '+send_an+'>> '+send_text
                else:
                    print send_an+' ist mittlerweile Offline'
                    text = "{'%s': '%s'}" %('fehler', 'user=offline')
                    self.sender().write(text)
                
            else:
                print send_an+' ist Offline'
                
        else:
        
            for user in self.dict.keys():
                tcpObject = self.dict[user]
                
                if tcpObject != self.sender():
                    print 'Senden an ' +user
    
                    if tcpObject != 'offline':
                        text = "{'%s': '''['%s','%s']'''}" %('text', sender_user, send_text)
                        tcpObject.write(text)
                    else:
                        print user, 'Offline'
                        
                        

    def sendUserlist(self):
        userlist = []
        for all_user in self.dict.keys():
            

            if self.dict[all_user] == 'offline':
                text = "['%s','%s']" %( all_user, 'offline')
            else:
                text = "['%s','%s']" %(all_user, 'online')
            userlist.append(text)

        text = "{'%s': '''%s'''}" %('userlist', userlist)
        
        for user in self.dict.keys():
            tcpObject = self.dict[user]
            if tcpObject != 'offline':
                tcpObject.write(text)
    
    def checkUser(self, login):
        
        user = login.split('&')[0]
        pwd = login.split('&')[1]
        print user, pwd
        
        for entry in self.userlist:
            
            if entry[0] == user:
                if entry[1] == pwd:
                    return True, user
        
        return False, False
        
        

                
            
if __name__ == '__main__':
    
    app = QtGui.QApplication(sys.argv)
    
    server = Server()
    server.listen(QHostAddress.Any, 5006)
    print server.serverAddress().toString()
    print server.serverPort()
    sys.exit(app.exec_())
