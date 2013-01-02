
from PyQt4.QtCore import QObject
from PyQt4.QtCore import SIGNAL


class Signal(QObject):
    __all__ = []
    def __init__(self, receiver=None):

        QObject.__init__(self)
        if receiver != None:
            self.__class__.__all__.append([receiver, self])


    
    def receiver(self, sender, signature, data={}):  
        for entry in self.__all__:
            entry[0](sender, signature, data)
            

    def send(self, sender, signature, data={}):
        sender.emit(SIGNAL(signature), sender, signature, data)

    
    def register(self, sender, signature):
        self.connect(sender, SIGNAL(signature), self.receiver)
        
    
    def registerLoading(self, sender):
        self.connect(sender, SIGNAL('startLoading'), self.receiver)
        self.connect(sender, SIGNAL('finishedLoading'), self.receiver)
        self.connect(sender, SIGNAL('killLoading'), self.receiver)
        
        
    def startLoading(self, sender):
        sender.emit(SIGNAL('startLoading'), sender, 'startLoading', {})
        
    def finishedLoading(self, sender):
        sender.emit(SIGNAL('finishedLoading'), sender, 'finishedLoading', {})
    
    def killLoading(self, sender):
        sender.emit(SIGNAL('killLoading'), sender, 'killLoading', {})
        
