
import re
import urllib2
import urllib

from hashlib import md5

from PyQt4 import QtCore
from PyQt4.QtCore import SIGNAL
from PyQt4.QtCore import QThread


_fromUtf8 = QtCore.QString.fromUtf8

PWD = '322794'


class PublicIp(QThread):
    
    def __init__(self):
        QThread.__init__(self)
        
        
    def run(self):
        self.getIp()
        
    
    def getIp(self):
        
        f = urllib2.urlopen('http://fritz.box/login.lua?')
        read = f.read()
        
        sPattern = '<br>security:status/challenge = (.*?)\n'
        parse = re.compile(sPattern, re.DOTALL).findall(read) 
        
        challenge = parse[0]
        
        md5_passwd = md5(_fromUtf8(challenge+'-'+PWD)).hexdigest()
        response = challenge+'-'+md5_passwd
        
        post_data = urllib.urlencode({'response':response,'get_page':'/home/home.lua'})
        print post_data
        
        f = urllib2.urlopen('http://fritz.box/login.lua', post_data)
        read = f.read()
    #    print read
        
        sPattern = "<div id='ipv4_info'>.*?IP-Adresse: (.*?)</div>"
        parse = re.compile(sPattern, re.DOTALL).findall(read) 
        
        publicIp = parse[0]
        
        self.emit(SIGNAL('Public_Ip'), publicIp)
        return 
    


