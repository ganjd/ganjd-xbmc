# -*- coding: utf-8 -*-

from PyQt4.QtGui import QWizard
from PyQt4.QtGui import QWizardPage
from PyQt4.QtCore import pyqtSignature

from Ui_wizardLastPage import Ui_WizardPage

class WizardLastPage(QWizardPage, Ui_WizardPage):

    def __init__(self, parent = None):

        QWizardPage.__init__(self, parent)
        self.setupUi(self)
        
        
    
    def initializePage(self):
        self.wizard().setOption(QWizard.NoCancelButton)
        self.wizard().setOption(QWizard.NoBackButtonOnLastPage)
