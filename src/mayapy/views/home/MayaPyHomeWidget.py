# MayaPyHomeWidget.py
# (C)2013
# Scott Ernst

from PySide import QtGui

from pyglass.widgets.PyGlassWidget import PyGlassWidget

from mayapy.mayapy_enum.UserConfigEnum import UserConfigEnum
from mayapy.views.home.NimbleStatusElement import NimbleStatusElement

#___________________________________________________________________________________________________ MayaPyHomeWidget
class MayaPyHomeWidget(PyGlassWidget):
    """A class for..."""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, parent, **kwargs):
        """Creates a new instance of MayaPyHomeWidget."""
        super(MayaPyHomeWidget, self).__init__(parent, **kwargs)
        self._firstView = True

        self.assignment1Btn.clicked.connect(self._handleAssignment1)
        self.assignment2Btn.clicked.connect(self._handleAssignment2)
        self.gundamBtn.clicked.connect(self._handleGundam)
        self.movesBtn.clicked.connect(self._handleMoves)

        self._statusBox, statusLayout = self._createElementWidget(self, QtGui.QVBoxLayout, True)
        statusLayout.addStretch()

        self._nimbleStatus = NimbleStatusElement(
            self._statusBox,
            disabled=self.mainWindow.appConfig.get(UserConfigEnum.NIMBLE_TEST_STATUS, True) )
        statusLayout.addWidget(self._nimbleStatus)
#===================================================================================================
#                                                                               P R O T E C T E D

#___________________________________________________________________________________________________ _activateWidgetDisplayImpl
    def _activateWidgetDisplayImpl(self, **kwargs):
        if self._firstView:
            self._nimbleStatus.refresh()
            self._firstView = False

#===================================================================================================
#                                                                                 H A N D L E R S

#___________________________________________________________________________________________________ _handleAssignment1
    def _handleAssignment1(self):
        self.mainWindow.setActiveWidget('assignment1')

#___________________________________________________________________________________________________ _handleAssignment2
    def _handleAssignment2(self):
        self.mainWindow.setActiveWidget('assignment2')

#___________________________________________________________________________________________________ _handleGundam
    def _handleGundam(self):
        self.mainWindow.setActiveWidget('gundam')

#___________________________________________________________________________________________________ _handleMoves
    def _handleMoves(self):
        self.mainWindow.setActiveWidget('Moves')
