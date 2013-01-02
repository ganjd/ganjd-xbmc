# -*- coding: utf-8 -*-

import os
import sys
from PyQt4 import QtGui

from Lib.loadSettings import LoadSettings
import restartScript



def main():
    
    app = QtGui.QApplication(sys.argv)
    
#    try:
        
    #--------------------------------------------------
    #Style Options
    #--------------------------------------------------
    app.setStyle(LoadSettings().style())
    #-----------------Ende---------------------------



    from Ui.mainwindow import MainWindow
#        from SplashScreen import SplashScreen
#        splash = SplashScreen()

#        splash.showMessage('Lade Datenbank')

    
    myapp = MainWindow(app)       
        
    myapp.show() 
#        splash.finish(myapp)
    ret = app.exec_()
    
    if ret == 1000:
        myapp.close()
        restartScript.main()

    sys.exit()



if __name__ == "__main__":
    main()
    


