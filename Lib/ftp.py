
import os
from PyQt4 import QtGui, QtCore

from PyQt4.QtNetwork import QFtp
from PyQt4.QtCore import QThread
from PyQt4.QtCore import SIGNAL


#ids
#----------------------------------------------

#newSync
#Progress
#State
#Fertig
#User
#Logout
#Login
#Done
#Ping
#Update
#------------------------------------------------



class Ftp(QFtp):
    
    def __init__(self, path, lastSync=False):
        
        QFtp.__init__(self)
        
        self.path = str(path)
        
        self.userLoggedIn = False
        self.verbindung = None
        self.user = False
        self.action = False
        self.udateLastSync = False
        self.lastSync = lastSync
        
        self.ping = Ping()
        self.ping.start()
        self.run()
        

    def run(self):   
        
        self.connect(self, SIGNAL('listInfo(const QUrlInfo&)'), self.info)
        self.connect(self, SIGNAL('stateChanged(int)'), self.stateChanged)
        self.connect(self, SIGNAL('dataTransferProgress(qint64,qint64)'),self.updateProgress)
        self.connect(self, SIGNAL('readyRead()'), self.readyRead)
        self.connect(self, SIGNAL('commandStarted(int)'), self.commandStarted)
        self.connect(self, SIGNAL('commandFinished(int,bool)'), self.commandFinished)
        self.connect(self, SIGNAL('done(bool)'), self.done)
        self.connect(self.ping, SIGNAL('Ping_Status'), self.pingStatus)

        
    def pingStatus(self, bool):
        
        if self.verbindung != bool:
            if bool == True:
                
                self.verbindung = bool
                self.emit(SIGNAL('Status'), 'Ping', True)

                if self.action == 'Login':
                    self.verbinden()
                    
            if bool == False:

                self.verbindung = bool
                self.emit(SIGNAL('Status'), 'Ping', False)
                
        else:
            self.verbindung = bool

        
    def checkUpdate(self):
        self.setAction('Update')
        self.cd('Update')
        self.get('version')
        
    def getUpdate(self):
        
        self.setAction('GetUpdate')
        self.cd('Update')
        
        filename = 'update.zip'
        
        self.outfile = QtCore.QFile(os.getcwd()+'\\'+filename)
        self.outfile.open(QtCore.QIODevice.WriteOnly)

        self.get(filename, self.outfile)
        
        
        
    def reLogIn(self):
        if self.verbindung == True:
            self.verbinden()
        else:
            self.emit(SIGNAL('Status'), 'Fehler', True)
        
        
    def logIn(self, user):
        self.setUser(user)
        self.setAction('Login')

        
    def registerUser(self):
        self.register = True
        self.put(self.user, 'user') 
        

    def setUser(self, user):
        from Lib.tools import Tools
        user = Tools().getEncodedString(user)
        self.user = str(user)


    def setAction(self, action):
        self.action = action
        
        if action == 'Download':
            self.list()
            
        if action == 'Upload':
            if self.verbindung == True:
                self.upload()
            else:
                self.emit(SIGNAL('Status'), 'Fehler', True)
                
            
        if action == 'Logout':
            
            if self.verbindung == True:
                self.upload()
                self.cd('User')
                self.remove('user')
            else:
                self.emit(SIGNAL('Status'), 'Fehler', True)
            

        
    def startAction(self):

        if self.action == 'Download':
            if  self.lastModified != self.lastSync:
                self.download()
            else:
                self.emit(SIGNAL('Status'), 'Fertig', 'Download')

                
            
    def verbinden(self):
        self.connectToHost('ftp.ganjd.de')

        
        

    #------------------------------------------------------------------
    #SIGNAL Actions
    #------------------------------------------------------------------
    
    def commandStarted(self, int):
        pass
            
    def done(self, bool):
        self.emit(SIGNAL('Status'),'Done', bool)
        

            
    def commandFinished(self, int, bool):

        if self.currentCommand() == QFtp.List:
            if self.action == 'Login':
                if self.userLoggedIn == False:
                    self.registerUser()


        if self.currentCommand() == QFtp.Get:

            if self.action == 'Download':
                self.outfile.close()
                self.extractAll('archive.zip')
                os.remove(self.path+'archive.zip')
                self.udateLastSync = True
                self.list()

                self.emit(SIGNAL('Status'), 'Fertig', 'Download')
                return
                
                
            if self.userLoggedIn == True and self.action == 'Login':
                self.clearPendingCommands()
                self.cd('..')
                self.emit(SIGNAL('Status'), 'Login', False)
                return
                
            
            if self.action == 'Update':
                self.cd('..')
                self.emit(SIGNAL('Status'), 'Update', self.version)
                return

                
            if self.action == 'GetUpdate':
                self.outfile.close()
                self.extractAll('update.zip')
                os.remove(os.getcwd()+'\\update.zip')
                self.cd('..')
                
                

        if self.currentCommand() == QFtp.Put:
            
            if self.register == False:
                os.remove(self.path+'archive.zip')
                self.emit(SIGNAL('Status'), 'Fertig', 'Upload')
                
            if self.register == True:
                self.cd('..')
                self.emit(SIGNAL('Status'), 'Login', True)
            

        if self.currentCommand() == QFtp.Remove:
            self.emit(SIGNAL('Status'), 'Logout', bool)
            self.close()


    
    def updateProgress(self, pos, total):
        percent = str(float(pos)/float(total)*100) + '%'
        self.emit(SIGNAL('Status'), 'Progress', percent)
        
        

    def readyRead(self):
        
        if self.userLoggedIn == True and self.action == 'Login':
            read = self.readAll()
            self.loggedInUser = read
            self.emit(SIGNAL('Status'), 'User', read)
            
        if self.action == 'Update':
            self.version = self.readAll()
            
        
        
        
    def info(self, urlInfo):
        print urlInfo.name()

        if str(urlInfo.name()) == 'user':
            if  urlInfo.lastModified().secsTo(QtCore.QDateTime().currentDateTime()) <=3600 :
                self.userLoggedIn = True
                self.get(urlInfo.name())
            else:
                print 'Login veraltet neuer Login'
                
            return
            

        if str(urlInfo.name()) == 'archive.zip':
            
            if self.udateLastSync == False:
                
                self.lastModified = urlInfo.lastModified()
                self.startAction()

            else:
                self.emit(SIGNAL('Status'), 'newSync', urlInfo.lastModified())
                
        return



    def stateChanged(self, state):
        self.emit(SIGNAL('Status'), 'State', state)
        
        if state == 0:
            print 'Verbindung verloren'
        
        if state == 1:
            pass
            
            
        if state == 3:
            self.login('u54306167', '11322794')
        
        if state == 4:
            self.cd('Datenbank/GalaBau/')
            

            if self.action == 'Login':
                self.cd('User')
                self.list()
                

    #-----------------------------Ende--------------------------------

        
        
    def upload(self):
        self.register = False
        
        self.makeArchive()

        filename = 'archive.zip'
        
        upfile= QtCore.QFile(self.path+filename)
        upfile.open(QtCore.QIODevice.ReadOnly)
        read = upfile.readAll()
        upfile.close()
        
        self.put(read, filename)  ## Uploads, but no dataTransferProgress signal.
        
        
            
            
    def download(self):
        self.userLoggedIn = False
        
        filename = 'archive.zip'
        
        self.outfile = QtCore.QFile(self.path+filename)
        self.outfile.open(QtCore.QIODevice.WriteOnly)

        self.get(filename, self.outfile)
        
        
    def makeArchive(self):
    
        import zipfile, os
        
        path = self.path
        archive = path + 'archive.zip'
        
        fileList = []
        for entry in os.walk(path):
            print entry
            for folder in entry[1]:
                fileList.append(os.path.join(entry[0], folder))
                
            for file in entry[2]:
                fileList.append(os.path.join(entry[0], file))
        
        
        """
        'fileList' is a list of file names - full path each name
        'archive' is the file name for the archive with a full path
        """
        try:
            # ZipFile will accept a file name or file object
            a = zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED)
            for f in fileList:
                print "archiving file %s" % (f)
                a.write(f, os.path.relpath(f, path))#(f) os.path.basename(f)
            a.close()
            return True
        except: return False
    
    
    
    def extractAll(self, filename):
        import zipfile, os
        
        if self.action == 'Download':
            path = self.path
        if self.action == 'GetUpdate':
            path = os.getcwd()+'\\'
            
        archive = path + filename
        
        a = zipfile.ZipFile(archive, 'r', zipfile.ZIP_DEFLATED)
        a.extractall(path)
        a.close
        
        
class Ping(QThread):
    
    def __init__(self):
        
        QThread.__init__(self)

        
    def run(self):
        
        while True:
            self.sleep(2)
            from PyQt4.QtNetwork import QTcpSocket
            self.sock = QTcpSocket()
            self.sock.connectToHost('ftp.ganjd.de', 21)
            self.sock.waitForConnected(2000)

            if self.sock.error() != -1:
                print self.sock.errorString()
                self.emit(SIGNAL('Ping_Status'), False)
            else:
                self.emit(SIGNAL('Ping_Status'), True)
                print 'Connection is True'
            self.sock.close()
            self.sleep(2)
        

