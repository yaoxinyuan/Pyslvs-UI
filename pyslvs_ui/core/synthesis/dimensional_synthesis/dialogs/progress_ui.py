# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyslvs_ui/core/synthesis/dimensional_synthesis/dialogs/progress.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from qtpy import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(567, 163)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/dimensional_synthesis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.time_label = QtWidgets.QLabel(Dialog)
        self.time_label.setObjectName("time_label")
        self.horizontalLayout_2.addWidget(self.time_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.batch_label = QtWidgets.QLabel(Dialog)
        self.batch_label.setObjectName("batch_label")
        self.horizontalLayout_2.addWidget(self.batch_label)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.loopTime = QtWidgets.QSpinBox(Dialog)
        self.loopTime.setMinimum(1)
        self.loopTime.setMaximum(10)
        self.loopTime.setObjectName("loopTime")
        self.horizontalLayout_2.addWidget(self.loopTime)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.fast_kernel_label = QtWidgets.QLabel(Dialog)
        self.fast_kernel_label.setWordWrap(True)
        self.fast_kernel_label.setObjectName("fast_kernel_label")
        self.verticalLayout.addWidget(self.fast_kernel_label)
        self.full_kernel_label = QtWidgets.QLabel(Dialog)
        self.full_kernel_label.setWordWrap(True)
        self.full_kernel_label.setObjectName("full_kernel_label")
        self.verticalLayout.addWidget(self.full_kernel_label)
        self.interrupt_label = QtWidgets.QLabel(Dialog)
        self.interrupt_label.setWordWrap(True)
        self.interrupt_label.setObjectName("interrupt_label")
        self.verticalLayout.addWidget(self.interrupt_label)
        self.progress_bar = QtWidgets.QProgressBar(Dialog)
        self.progress_bar.setObjectName("progress_bar")
        self.verticalLayout.addWidget(self.progress_bar)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.fitness_label = QtWidgets.QLabel(Dialog)
        self.fitness_label.setObjectName("fitness_label")
        self.horizontalLayout.addWidget(self.fitness_label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.start_button = QtWidgets.QPushButton(Dialog)
        self.start_button.setObjectName("start_button")
        self.horizontalLayout.addWidget(self.start_button)
        self.interrupt_button = QtWidgets.QPushButton(Dialog)
        self.interrupt_button.setEnabled(False)
        self.interrupt_button.setObjectName("interrupt_button")
        self.horizontalLayout.addWidget(self.interrupt_button)
        self.button_box = QtWidgets.QDialogButtonBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_box.sizePolicy().hasHeightForWidth())
        self.button_box.setSizePolicy(sizePolicy)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.button_box.setObjectName("button_box")
        self.horizontalLayout.addWidget(self.button_box)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.button_box.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dimensional Synthesis"))
        self.label_6.setText(_translate("Dialog", "Time spent:"))
        self.time_label.setText(_translate("Dialog", "00:00:00"))
        self.label_4.setText(_translate("Dialog", "Batch execution:"))
        self.label_7.setText(_translate("Dialog", "with"))
        self.label_5.setText(_translate("Dialog", "time(s)."))
        self.fast_kernel_label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#00aa00;\">※ The mechanism of configuration has enabled logical acceleration process, the performance can be more faster.</span></p></body></html>"))
        self.full_kernel_label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">※ The mechanism of configuration has enabled full CAD kernel process, the performance might be more slower.</span></p></body></html>"))
        self.interrupt_label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">※ The interrupt button will stop the process, but you can keep the result.</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "Fitness: "))
        self.fitness_label.setText(_translate("Dialog", "N/A"))
        self.start_button.setText(_translate("Dialog", "Start"))
        self.interrupt_button.setText(_translate("Dialog", "Interrupt"))
from pyslvs_ui import icons_rc
