from PyQt4.QtCore import SIGNAL
from PyQt4.QtNetwork import QTcpServer
from PyQt4.QtNetwork import QHostAddress
from PyQt4.QtNetwork import QTcpSocket
from PyQt4 import QtGui, QtCore
import sys



class Server(QTcpServer):
    
    def __init__(self):
        QTcpServer.__init__(self)
        
        self.userlist = [['David','1234'], ['Esra','1234'], ['Test','1234']]
        
        self.dict = {}
        for user in self.userlist:
            self.dict[user[0]] = 'offline'
        
        
        self.connect(self, SIGNAL('newConnection()'), self.newConnection)
        

    def runServer(self):
        self.listen(QHostAddress.Any, 5006)
        print self.serverAddress().toString()
        print self.serverPort()

        
    def newConnection(self):
        print 'newConnection'
        self.tcp = self.nextPendingConnection()
        self.connect(self.tcp, SIGNAL('readyRead()'), self.incoming)
#        self.dict[self.tcp.socketDescriptor()] = self.tcp
        

        
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
                
        for user in self.dict.keys():
            tcpObject = self.dict[user]
            
            if tcpObject != self.sender():
                print 'Senden an ' +user

                if tcpObject != 'offline':
                    text = "{'%s': '''['%s','%s']'''}" %('text', sender_user, msg_Value)
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
    address = QHostAddress('82.165.219.204')#'92.74.14.48'
    server.listen(QHostAddress.Any, 5006)#
    print server.serverAddress().toString()
    print server.serverPort()
    sys.exit(app.exec_())
