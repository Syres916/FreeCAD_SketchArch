# ***************************************************************************
# *                                                                         *
# *   Copyright (c) 2018, 2019                                              *
# *   Paul Lee <paullee0@gmail.com>                                         *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Lesser General Public License (LGPL)    *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENCE text file.                                 *
# *                                                                         *
# *   This program is distributed in the hope that it will be useful,       *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU Library General Public License for more details.                  *
# *                                                                         *
# *   You should have received a copy of the GNU Library General Public     *
# *   License along with this program; if not, write to the Free Software   *
# *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
# *   USA                                                                   *
# *                                                                         *
# ***************************************************************************

import FreeCAD, FreeCADGui, Part, Draft, Sketcher
from PySide import QtGui, QtCore


App = FreeCAD
Gui = FreeCADGui

# ----------------------------------------------------------------------------#
#                             Class Definition                               #
# ----------------------------------------------------------------------------#


class selectObjectObserver:
    """General Purpose Selection Observer"""

    def __init__(self, callerNextDef, filterDoc=None, filterObj=None, filterSub=None):
        self.filterDoc = str(filterDoc)
        self.filterObj = str(filterObj)
        self.filterSub = str(filterSub)
        mw = FreeCADGui.getMainWindow()
        self.taskspanel = mw.findChild(QtGui.QDockWidget, "Tasks")
        self.manualUpdateBtn = self.taskspanel.findChild(
            QtGui.QToolButton, "manualUpdate"
        )
        self.manualUpdateBtn.destroyed.connect(self.tasksSketchClose)

    def tasksSketchClose(self):
        FreeCADGui.Selection.removeObserver(self)

    def addSelection(self, doc, obj, sub, pnt):
        if self.filterSub:
            if self.filterSub in sub:
                self.proceed(doc, obj, sub, pnt)

    def removeSelection(self, doc, obj, sub):
        App.Console.PrintMessage("removeSelection" + "\n")

    def setSelection(self, doc):
        App.Console.PrintMessage("setSelection" + "\n")

    def clearSelection(self, doc):
        App.Console.PrintMessage("clearSelection" + "\n")


class selectObject:
    """General Purpose Selection Observer"""

    def __init__(
        self,
        callerInstance,
        callerNextDef,
        filterDoc=None,
        filterObj=None,
        filterSub=None,
    ):
        self.callerInstance = callerInstance
        self.callerNextDef = str(callerNextDef)
        self.filterDoc = str(filterDoc)
        self.filterObj = str(filterObj)
        self.filterSub = str(filterSub)
        mw = FreeCADGui.getMainWindow()
        self.taskspanel = mw.findChild(QtGui.QDockWidget, "Tasks")
        self.manualUpdateBtn = self.taskspanel.findChild(
            QtGui.QToolButton, "manualUpdate"
        )
        self.manualUpdateBtn.destroyed.connect(self.tasksSketchClose)

    def tasksSketchClose(self):
        FreeCADGui.Selection.removeObserver(self)

    def addSelection(self, doc, obj, sub, pnt):
        if self.filterSub:
            if self.filterSub in sub:
                self.callerInstance.proceed(doc, obj, sub, pnt)

    def removeSelection(self, doc, obj, sub):
        App.Console.PrintMessage("removeSelection" + "\n")

    def setSelection(self, doc):
        App.Console.PrintMessage("setSelection" + "\n")

    def clearSelection(self, doc):
        App.Console.PrintMessage("clearSelection" + "\n")
