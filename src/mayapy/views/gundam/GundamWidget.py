# Assignment2Widget.py
# (C)2013
# Scott Ernst

from pyglass.widgets.PyGlassWidget import PyGlassWidget
from gundam_skeleton_v1 import Skeleton
from gundam_v2 import Gundam as Gundam
from gundam_v3 import Gundam as Gundam3
from gundam_strike_v1 import Gundam as GundamStrike
from gundam_v3 import Gundam as GundamArtemie
from mayapy.views.assignment2.Assignment2Widget import Assignment2Widget,listOfMaterialShader,listOfMaterials
from enum import Enum
from mayapy.views.physics.PhysicPlieIk import PlieIk
from nimble import cmds as mc
gundams_need = []
#___________________________________________________________________________________________________ Assignment2Widget
class GundamWidget(PyGlassWidget):
    """A class for..."""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, parent, **kwargs):
        global listOfMaterialShader
        global listOfMaterials
        """Creates a new instance of Assignment2Widget."""
        super(GundamWidget, self).__init__(parent, **kwargs)
        self.gundams = list()
        self.SkeletonBtn.clicked.connect(self._handleSkeletonButton)
        self.V2Btn.clicked.connect(self._handleV2Button)
        self.strikeBtn.clicked.connect(self._handleStrikeButton)
        self.homeBtn.clicked.connect(self._handleReturnHome)
        self.attachAllBtn.clicked.connect(self._handleAttachAllButton)
        self.detachAllBtn.clicked.connect(self._handleDetachAllButton)
        self.attachArmsBtn.clicked.connect(self._handleAttachArmButton)
        self.detachArmsBtn.clicked.connect(self._handleDetachArmButton)
        self.attachFeetBtn.clicked.connect(self._handleAttachLegButton)
        self.detachFeetBtn.clicked.connect(self._handleDetachLegButton)
        self.initBtn.clicked.connect(self._handleInit)

        #listOfMaterials.__repr__()

        #self.gundamTypeListCB.addItem("Gundam v1")
        self.gundamTypeListCB.addItem("Gundam v2")
        self.gundamTypeListCB.addItem("Gundam v3")
        self.gundamTypeListCB.addItem("Strike")
        self.gundamTypeListCB.addItem("Artemie")
        for i in range(len(listOfMaterialShader)):
            x = listOfMaterialShader[i]
            if x == None:
                listOfMaterials[i] # this works
            #print listOfMaterialShader[i]
            self.materialList1.addItem(x)
            self.materialList2.addItem(x)
            self.materialList3.addItem(x)

        self.materialList1.setCurrentIndex(1)
        self.materialList2.setCurrentIndex(2)
        self.materialList3.setCurrentIndex(3)

#___________________________________________________________________________________________________ _activateWidgetDisplayImpl
    def _activateWidgetDisplayImpl(self, **kwargs):
        cbCount = self.materialList1.count()
        mlCount = len(listOfMaterialShader)
        '''
        print cbCount
        print mlCount
        for i in range(len(listOfMaterialShader)):
            print listOfMaterialShader[i]
        '''
        if cbCount != mlCount:
            print "update matelial list"
            for idx in range(cbCount,mlCount):
                x = listOfMaterialShader[idx]
                self.materialList1.addItem(x)
                self.materialList2.addItem(x)
                self.materialList3.addItem(x)
        pass

#===================================================================================================
#                                                                                 H A N D L E R S
#___________________________________________________________________________________________________ _handleReturnHome
    def _handleInit(self):
        floor = mc.polyPlane(w=600,h=600)
        mc.move(0,-5,0)

        mc.ambientLight()
        mc.pointLight()
        mc.move(600,600,600)
#___________________________________________________________________________________________________ _handleReturnHome
    def _handleReturnHome(self):
        self.mainWindow.setActiveWidget('home')

#___________________________________________________________________________________________________ _handleLeftFootBtn
    def _handleSkeletonButton(self):
        seleton_1 = Skeleton("Bob")
        self.gundamList.addItem("Bob")
#___________________________________________________________________________________________________ _handleLeftFootBtn
    def _handleV2Button(self):
        gundam = Gundam("Jeremy")
        self.gundamList.addItem("Jeremy")

#___________________________________________________________________________________________________ _handleLeftFootBtn
    def _handleStrikeButton(self):
        global gundams_need
        print(self.maleName.text())
        idx = self.gundamTypeListCB.currentIndex()
        if idx == 0:
            gundam = Gundam(self.maleName.text())
        elif idx == 1:
            gundam = Gundam3(self.maleName.text())
        elif idx == 2:
            c1 = None
            c2 = None
            c3 = None
            idx = self.materialList1.currentIndex()
            if idx != 0:
                c1 = listOfMaterialShader[idx]
            idx = self.materialList2.currentIndex()
            if idx != 0:
                c2 = listOfMaterialShader[idx]
            idx = self.materialList3.currentIndex()
            if idx != 0:
                c3 = listOfMaterialShader[idx]
            gundam = GundamStrike(self.maleName.text(),c1,c2,c3)
        elif idx == 3:
            gundam = GundamArtemie(self.maleName.text())

        #gundam = Gundam(self.maleName.text())
        self.gundams.append(gundam)
        self.gundamList.addItem(gundam.name)
        gundam.attachIKToRoot()
        size = int(self.maleSize.text())
        ratio = size / 2.0
        print(ratio)
        gundam.scale(ratio)
        print self.gundams
        gundams_need.append((gundam,"second"))
        #plie = PlieIk("first",0,160,gundam)
        #plie2 = PlieIk("second",160,320,gundam)

#___________________________________________________________________________________________________ _handleLeftFootBtn
    def _handleAttachAllButton(self):
        idx = self.gundamList.currentIndex()

        temp = self.gundams[idx]

        temp.attachIKToRoot()
#___________________________________________________________________________________________________ _handleLeftFootBtn
    def _handleDetachAllButton(self):
        idx = self.gundamList.currentIndex()
        temp = self.gundams[idx]
        temp.detachIKFromRoot()

#___________________________________________________________________________________________________ _handleLeftFootBtn
    def _handleAttachArmButton(self):
        idx = self.gundamList.currentIndex()
        temp = self.gundams[idx]
        temp.attachArmsIKToRoot()
#___________________________________________________________________________________________________ _handleLeftFootBtn
    def _handleDetachArmButton(self):
        idx = self.gundamList.currentIndex()
        temp = self.gundams[idx]
        temp.detachArmsIKFromRoot()

#___________________________________________________________________________________________________ _handleLeftFootBtn
    def _handleAttachLegButton(self):
        idx = self.gundamList.currentIndex()
        temp = self.gundams[idx]
        temp.attachLegsIKToRoot()
#___________________________________________________________________________________________________ _handleLeftFootBtn
    def _handleDetachLegButton(self):
        idx = self.gundamList.currentIndex()
        temp = self.gundams[idx]
        temp.detachLegsIKFromRoot()


