
import sys
from PyQt4 import QtCore, QtGui
from Ui.mainwidget import MainWidget



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    
    #--------------------------------------------------
    #Style Options
    #--------------------------------------------------
#    app.setStyle("Plastique")
    app.setStyle("Cleanlooks")
#
#    a = QtGui.QStyleFactory.keys()[5]
#    b = QtGui.QStyleFactory.create(a)
#    app.setStyle(b)
    #-----------------Ende---------------------------

    myapp = MainWidget('David', server=True)
#    myapp = MainWidget('Test')
    myapp = MainWidget('Esra')
    myapp.show()
#    myapp.startStatusWidget()
    sys.exit(app.exec_())

