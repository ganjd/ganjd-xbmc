
from PyQt4.QtCore import SIGNAL
from PyQt4.QtNetwork import QHostAddress
from PyQt4.QtNetwork import QTcpSocket
from PyQt4.QtCore import QByteArray
from PyQt4 import QtCore




class Client(QTcpSocket):
    
    def __init__(self):
        QTcpSocket.__init__(self)
        
        
        self.connect(self, SIGNAL('stateChanged(QAbstractSocket::SocketState)'), self.stateChanged)
        self.connect(self, SIGNAL('readyRead()'), self.incoming)
        self.connect(self, SIGNAL('bytesWritten(qint64)'), self.bytesWritten)
        self.connect(self, SIGNAL('error(QAbstractSocket::SocketError)'), self.error)
        self.connect(self, SIGNAL('readChannelFinished()'), self.readChannelFinished)
        
    
        self.logout_state = False
    
    
    def readChannelFinished(self):
        print 'readChannelFinished'
        
        
    
    def readSize(self):
        size = ''
        while True:
            msg = str(self.read(1))
            
            try: 
                size_int= int(msg)
                size = size + str(size_int)
            except Exception, err:
                print err
                break
                
        return msg, int(size)-1
        


    def incoming(self): 
        
        while True:
            msg, size = self.readSize()
    
            msg = msg + str(self.read(size))
            
            msg = eval(msg)
            msg_Key = msg.keys()[0]
            msg_Value = msg[msg_Key]
            
            if msg_Key == 'text':
                msg_Value = eval(msg_Value)
                user = msg_Value[0]
                text = msg_Value[1]
                print user
                print text
                self.emit(SIGNAL('Incoming'), text, user)
                
            if msg_Key == 'userlist':
                userlist = eval(msg_Value)
                
                self.emit(SIGNAL('Userlist'), False, False)
                for entry in userlist:
                    entry = eval(entry)
                    user = entry[0]
                    status = entry[1]
                    self.emit(SIGNAL('Userlist'), user, status)
                    
            if msg_Key == 'fehler':
                print msg_Value
            
            print self.atEnd()
            if self.atEnd() == True:
                break
                
      
    def bytesWritten(self, qint64):
        self.emit(SIGNAL('Written'))
        if self.logout_state == True:
            self.logout_state = False
            self.emit(SIGNAL('closeReady'))
        
        
        
    def stateChanged(self, state):
        print state, 'Status'
        self.emit(SIGNAL('State'), state)
        if state == 3:
            login = "{'login':'%s&%s'}" %(self.username, self.password)
            self.writeData(login)
            
        
        
    def error(self, error):
        print error, self.errorString()
        

    def send(self, text, send_an='Alle'):
        if self.state() == 3:
#            text = "{'text': '"+text+"'}"
            text = "{'%s': '''%s'''}" %('text', [send_an, text])
            self.write(text)
            
        elif self.state() > 0:
            print 'Warten Verbindung wir hergestellt'
        else:
            print 'Nicht Verbunden'
            self.connectClient()
        

    def connectClient(self):
        self.connectToHost('ganjd.no-ip.info', 5006)

        
        
    def setUser(self, username, password):
        self.username = username
        self.password = password
        
        
        
    def logout(self):
        text = "{'logout': '"+str(self.username)+"'}"
        self.write(text)
        self.logout_state = True
        return True
        


