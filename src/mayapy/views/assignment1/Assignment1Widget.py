# Assignment1Widget.py
# (C)2013
# Scott Ernst

import nimble
from nimble import cmds
from nimble import cmds as cmd
from pyglass.widgets.PyGlassWidget import PyGlassWidget

#___________________________________________________________________________________________________ Assignment1Widget
class Assignment1Widget(PyGlassWidget):
    """A class for Assignment 1"""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, parent, **kwargs):
        """Creates a new instance of Assignment1Widget."""
        super(Assignment1Widget, self).__init__(parent, **kwargs)
        self.exampleBtn.clicked.connect(self._handleExampleButton)
        self.bubble.clicked.connect(self._handleBubbleButton)
        self.homeBtn.clicked.connect(self._handleReturnHome)

#===================================================================================================
#                                                                                 H A N D L E R S

#_______________________________________________________________________________________________ _handleExaampleButton
    def _handleExampleButton(self):
        """
        This callback creates a polygonal cylinder in the Maya scene.

        """
        r = 5
        a = 2.0*r
        y = (0, 1, 0)
        c = cmds.polyCylinder(
            r=r, h=5, sx=40, sy=1, sz=1, ax=y, rcp=0, cuv=2, ch=1, n='exampleCylinder')[0]
        cmds.select(c)
        response = nimble.createRemoteResponse(globals())
        response.put('name', c)
#___________________________________________________________________________________________________ _handleBubble
    def _handleBubbleButton(self):
        """
        This callback creates a polygonal sphere in the Maya scene.
        it then translates it.
        """
        r = 2
        a = 2.0*r
        y = (0, 1, 0) # y up
        c = cmds.polySphere(
            r=r, sx=10, sy=10, ax=y, cuv=2, ch=1, n='Bubble')[0]
        cmds.select(c)
        cmd.move(0, 5, 0, r = True)
        response = nimble.createRemoteResponse(globals())
        response.put('name', c)

#___________________________________________________________________________________________________ _handleReturnHome
    def _handleReturnHome(self):
        self.mainWindow.setActiveWidget('home')
