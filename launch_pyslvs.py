# -*- coding: utf-8 -*-
##Pyslvs - Open Source Planar Linkage Mechanism Simulation and Mechanical Synthesis System. 
##Copyright (C) 2016-2018 Yuan Chang [pyslvs@gmail.com]
from sys import exit
from core import (
    MainWindow,
    ARGUMENTS,
    INFO,
    PyslvsSplash,
)

if __name__=='__main__':
    if ARGUMENTS.test:
        exit(0)
    else:
        print('\n'.join(INFO+('-'*7,)))
        from PyQt5.QtWidgets import QApplication
        QApp = QApplication([])
        if ARGUMENTS.fusion:
            QApp.setStyle('fusion')
        splash = PyslvsSplash()
        splash.show()
        run = MainWindow(ARGUMENTS)
        run.show()
        splash.finish(run)
        exit(QApp.exec())
