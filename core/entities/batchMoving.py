# -*- coding: utf-8 -*-
##Pyslvs - Open Source Planar Linkage Mechanism Simulation and Dimensional Synthesis System.
##Copyright (C) 2016-2017 Yuan Chang
##E-mail: pyslvs@gmail.com
##
##This program is free software; you can redistribute it and/or modify
##it under the terms of the GNU Affero General Public License as published by
##the Free Software Foundation; either version 3 of the License, or
##(at your option) any later version.
##
##This program is distributed in the hope that it will be useful,
##but WITHOUT ANY WARRANTY; without even the implied warranty of
##MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##GNU Affero General Public License for more details.
##
##You should have received a copy of the GNU Affero General Public License
##along with this program; if not, write to the Free Software
##Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

from ..QtModules import *
from .Ui_batchMoving import Ui_Dialog as batchMoving_Dialog

class batchMoving_show(QDialog, batchMoving_Dialog):
    def __init__(self, Points, selectedPoints, parent=None):
        super(batchMoving_show, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        icon = self.windowIcon()
        self.Points = Points
        for i in selectedPoints:
            self.selected.addItem(QListWidgetItem(icon, 'Point{}'.format(i)))
        for i in set(range(len(self.Points)))-set(selectedPoints):
            self.noSelected.addItem(QListWidgetItem(icon, 'Point{}'.format(i)))
