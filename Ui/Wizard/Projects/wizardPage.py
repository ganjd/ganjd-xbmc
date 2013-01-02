# -*- coding: utf-8 -*-

"""
Module implementing WizardPage.
"""

from PyQt4.QtGui import QWizardPage
from PyQt4.QtCore import pyqtSignature

from Ui_wizardPage import Ui_WizardPage

class WizardPage(QWizardPage, Ui_WizardPage):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QWizardPage.__init__(self, parent)
        self.setupUi(self)
