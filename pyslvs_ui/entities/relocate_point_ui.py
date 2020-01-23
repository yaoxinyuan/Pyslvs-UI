# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyslvs_ui/entities/relocate_point.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from qtpy import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(301, 468)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/calculator.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tab_widget = QtWidgets.QTabWidget(Dialog)
        self.tab_widget.setObjectName("tab_widget")
        self.plap_tab = QtWidgets.QWidget()
        self.plap_tab.setObjectName("plap_tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.plap_tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.panel_layout = QtWidgets.QHBoxLayout()
        self.panel_layout.setObjectName("panel_layout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.plap_p1_label = QtWidgets.QLabel(self.plap_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plap_p1_label.sizePolicy().hasHeightForWidth())
        self.plap_p1_label.setSizePolicy(sizePolicy)
        self.plap_p1_label.setObjectName("plap_p1_label")
        self.horizontalLayout_2.addWidget(self.plap_p1_label)
        self.plap_p1_box = QtWidgets.QComboBox(self.plap_tab)
        self.plap_p1_box.setObjectName("plap_p1_box")
        self.horizontalLayout_2.addWidget(self.plap_p1_box)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.plap_p1x_label = QtWidgets.QLabel(self.plap_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plap_p1x_label.sizePolicy().hasHeightForWidth())
        self.plap_p1x_label.setSizePolicy(sizePolicy)
        self.plap_p1x_label.setObjectName("plap_p1x_label")
        self.horizontalLayout.addWidget(self.plap_p1x_label)
        self.plap_p1x_box = QtWidgets.QDoubleSpinBox(self.plap_tab)
        self.plap_p1x_box.setMinimum(-9999.99)
        self.plap_p1x_box.setMaximum(9999.99)
        self.plap_p1x_box.setObjectName("plap_p1x_box")
        self.horizontalLayout.addWidget(self.plap_p1x_box)
        self.plap_p1y_label = QtWidgets.QLabel(self.plap_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plap_p1y_label.sizePolicy().hasHeightForWidth())
        self.plap_p1y_label.setSizePolicy(sizePolicy)
        self.plap_p1y_label.setObjectName("plap_p1y_label")
        self.horizontalLayout.addWidget(self.plap_p1y_label)
        self.plap_p1y_box = QtWidgets.QDoubleSpinBox(self.plap_tab)
        self.plap_p1y_box.setMinimum(-9999.99)
        self.plap_p1y_box.setMaximum(9999.99)
        self.plap_p1y_box.setObjectName("plap_p1y_box")
        self.horizontalLayout.addWidget(self.plap_p1y_box)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.plap_angle_label = QtWidgets.QLabel(self.plap_tab)
        self.plap_angle_label.setObjectName("plap_angle_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.plap_angle_label)
        self.plap_angle_box = QtWidgets.QDoubleSpinBox(self.plap_tab)
        self.plap_angle_box.setMaximum(360.0)
        self.plap_angle_box.setObjectName("plap_angle_box")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.plap_angle_box)
        self.plap_distance_label = QtWidgets.QLabel(self.plap_tab)
        self.plap_distance_label.setObjectName("plap_distance_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.plap_distance_label)
        self.plap_distance_box = QtWidgets.QDoubleSpinBox(self.plap_tab)
        self.plap_distance_box.setMaximum(9999.99)
        self.plap_distance_box.setObjectName("plap_distance_box")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.plap_distance_box)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.panel_layout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.panel_layout)
        spacerItem = QtWidgets.QSpacerItem(20, 126, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.tab_widget.addTab(self.plap_tab, "")
        self.pllp_tab = QtWidgets.QWidget()
        self.pllp_tab.setObjectName("pllp_tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.pllp_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pllp_p1_label = QtWidgets.QLabel(self.pllp_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pllp_p1_label.sizePolicy().hasHeightForWidth())
        self.pllp_p1_label.setSizePolicy(sizePolicy)
        self.pllp_p1_label.setObjectName("pllp_p1_label")
        self.horizontalLayout_4.addWidget(self.pllp_p1_label)
        self.pllp_p1_box = QtWidgets.QComboBox(self.pllp_tab)
        self.pllp_p1_box.setObjectName("pllp_p1_box")
        self.horizontalLayout_4.addWidget(self.pllp_p1_box)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pllp_p1x_label = QtWidgets.QLabel(self.pllp_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pllp_p1x_label.sizePolicy().hasHeightForWidth())
        self.pllp_p1x_label.setSizePolicy(sizePolicy)
        self.pllp_p1x_label.setObjectName("pllp_p1x_label")
        self.horizontalLayout_3.addWidget(self.pllp_p1x_label)
        self.pllp_p1x_box = QtWidgets.QDoubleSpinBox(self.pllp_tab)
        self.pllp_p1x_box.setMinimum(-9999.99)
        self.pllp_p1x_box.setMaximum(9999.99)
        self.pllp_p1x_box.setObjectName("pllp_p1x_box")
        self.horizontalLayout_3.addWidget(self.pllp_p1x_box)
        self.pllp_p1y_label = QtWidgets.QLabel(self.pllp_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pllp_p1y_label.sizePolicy().hasHeightForWidth())
        self.pllp_p1y_label.setSizePolicy(sizePolicy)
        self.pllp_p1y_label.setObjectName("pllp_p1y_label")
        self.horizontalLayout_3.addWidget(self.pllp_p1y_label)
        self.pllp_p1y_box = QtWidgets.QDoubleSpinBox(self.pllp_tab)
        self.pllp_p1y_box.setMinimum(-9999.99)
        self.pllp_p1y_box.setMaximum(9999.99)
        self.pllp_p1y_box.setObjectName("pllp_p1y_box")
        self.horizontalLayout_3.addWidget(self.pllp_p1y_box)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pllp_p2_label = QtWidgets.QLabel(self.pllp_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pllp_p2_label.sizePolicy().hasHeightForWidth())
        self.pllp_p2_label.setSizePolicy(sizePolicy)
        self.pllp_p2_label.setObjectName("pllp_p2_label")
        self.horizontalLayout_5.addWidget(self.pllp_p2_label)
        self.pllp_p2_box = QtWidgets.QComboBox(self.pllp_tab)
        self.pllp_p2_box.setObjectName("pllp_p2_box")
        self.horizontalLayout_5.addWidget(self.pllp_p2_box)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pllp_p2x_label = QtWidgets.QLabel(self.pllp_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pllp_p2x_label.sizePolicy().hasHeightForWidth())
        self.pllp_p2x_label.setSizePolicy(sizePolicy)
        self.pllp_p2x_label.setObjectName("pllp_p2x_label")
        self.horizontalLayout_6.addWidget(self.pllp_p2x_label)
        self.pllp_p2x_box = QtWidgets.QDoubleSpinBox(self.pllp_tab)
        self.pllp_p2x_box.setMinimum(-9999.99)
        self.pllp_p2x_box.setMaximum(9999.99)
        self.pllp_p2x_box.setObjectName("pllp_p2x_box")
        self.horizontalLayout_6.addWidget(self.pllp_p2x_box)
        self.pllp_p2y_label = QtWidgets.QLabel(self.pllp_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pllp_p2y_label.sizePolicy().hasHeightForWidth())
        self.pllp_p2y_label.setSizePolicy(sizePolicy)
        self.pllp_p2y_label.setObjectName("pllp_p2y_label")
        self.horizontalLayout_6.addWidget(self.pllp_p2y_label)
        self.pllp_p2y_box = QtWidgets.QDoubleSpinBox(self.pllp_tab)
        self.pllp_p2y_box.setMinimum(-9999.99)
        self.pllp_p2y_box.setObjectName("pllp_p2y_box")
        self.horizontalLayout_6.addWidget(self.pllp_p2y_box)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.pllp_distance1_box = QtWidgets.QDoubleSpinBox(self.pllp_tab)
        self.pllp_distance1_box.setMaximum(9999.99)
        self.pllp_distance1_box.setObjectName("pllp_distance1_box")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pllp_distance1_box)
        self.pllp_distance1_label = QtWidgets.QLabel(self.pllp_tab)
        self.pllp_distance1_label.setObjectName("pllp_distance1_label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.pllp_distance1_label)
        self.pllp_distance2_box = QtWidgets.QDoubleSpinBox(self.pllp_tab)
        self.pllp_distance2_box.setMaximum(9999.99)
        self.pllp_distance2_box.setObjectName("pllp_distance2_box")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pllp_distance2_box)
        self.pllp_distance2_label = QtWidgets.QLabel(self.pllp_tab)
        self.pllp_distance2_label.setObjectName("pllp_distance2_label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pllp_distance2_label)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.pllp_inversed_box = QtWidgets.QCheckBox(self.pllp_tab)
        self.pllp_inversed_box.setObjectName("pllp_inversed_box")
        self.verticalLayout_2.addWidget(self.pllp_inversed_box)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.tab_widget.addTab(self.pllp_tab, "")
        self.verticalLayout.addWidget(self.tab_widget)
        self.preview_label = QtWidgets.QLabel(Dialog)
        self.preview_label.setObjectName("preview_label")
        self.verticalLayout.addWidget(self.preview_label)
        self.button_box = QtWidgets.QDialogButtonBox(Dialog)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.verticalLayout.addWidget(self.button_box)

        self.retranslateUi(Dialog)
        self.button_box.rejected.connect(Dialog.reject)
        self.button_box.accepted.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Relocate"))
        self.plap_p1_label.setText(_translate("Dialog", "Point"))
        self.plap_p1x_label.setText(_translate("Dialog", "X"))
        self.plap_p1y_label.setText(_translate("Dialog", "Y"))
        self.plap_angle_label.setText(_translate("Dialog", "Angle"))
        self.plap_distance_label.setText(_translate("Dialog", "Distance"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.plap_tab), _translate("Dialog", "Polar"))
        self.pllp_p1_label.setText(_translate("Dialog", "Point 1"))
        self.pllp_p1x_label.setText(_translate("Dialog", "X"))
        self.pllp_p1y_label.setText(_translate("Dialog", "Y"))
        self.pllp_p2_label.setText(_translate("Dialog", "Point 2"))
        self.pllp_p2x_label.setText(_translate("Dialog", "X"))
        self.pllp_p2y_label.setText(_translate("Dialog", "Y"))
        self.pllp_distance1_label.setText(_translate("Dialog", "Distance 1"))
        self.pllp_distance2_label.setText(_translate("Dialog", "Distance 2"))
        self.pllp_inversed_box.setText(_translate("Dialog", "Inverse two points"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.pllp_tab), _translate("Dialog", "Two Points"))
from pyslvs_ui import icons_rc
