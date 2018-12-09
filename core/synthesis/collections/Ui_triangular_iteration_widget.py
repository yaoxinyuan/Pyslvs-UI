# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ahshoe/桌面/Pyslvs-PyQt5/core/_synthesis/collections/TriangularIteration.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(434, 688)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/ti.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.add_collection_button = QtWidgets.QPushButton(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/structure.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_collection_button.setIcon(icon1)
        self.add_collection_button.setObjectName("add_collection_button")
        self.horizontalLayout_4.addWidget(self.add_collection_button)
        self.line_5 = QtWidgets.QFrame(Form)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_4.addWidget(self.line_5)
        self.load_button = QtWidgets.QPushButton(Form)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/collections.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.load_button.setIcon(icon2)
        self.load_button.setObjectName("load_button")
        self.horizontalLayout_4.addWidget(self.load_button)
        self.clear_button = QtWidgets.QPushButton(Form)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/clean.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_button.setIcon(icon3)
        self.clear_button.setObjectName("clear_button")
        self.horizontalLayout_4.addWidget(self.clear_button)
        self.save_button = QtWidgets.QPushButton(Form)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/save_file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_button.setIcon(icon4)
        self.save_button.setObjectName("save_button")
        self.horizontalLayout_4.addWidget(self.save_button)
        self.clipboard_button = QtWidgets.QPushButton(Form)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clipboard_button.setIcon(icon5)
        self.clipboard_button.setObjectName("clipboard_button")
        self.horizontalLayout_4.addWidget(self.clipboard_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_12.addLayout(self.horizontalLayout_4)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_12.addWidget(self.line)
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.main_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.main_layout.setObjectName("main_layout")
        self.joint_panel = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.joint_panel.setMaximumSize(QtCore.QSize(150, 16777215))
        self.joint_panel.setObjectName("joint_panel")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.joint_panel)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.joint_name_label = QtWidgets.QLabel(self.joint_panel)
        self.joint_name_label.setObjectName("joint_name_label")
        self.verticalLayout_6.addWidget(self.joint_name_label)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.joint_name = QtWidgets.QComboBox(self.joint_panel)
        self.joint_name.setObjectName("joint_name")
        self.horizontalLayout_5.addWidget(self.joint_name)
        self.add_customization = QtWidgets.QPushButton(self.joint_panel)
        self.add_customization.setMaximumSize(QtCore.QSize(30, 16777215))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/properties.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_customization.setIcon(icon6)
        self.add_customization.setObjectName("add_customization")
        self.horizontalLayout_5.addWidget(self.add_customization)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.status_show_label = QtWidgets.QLabel(self.joint_panel)
        self.status_show_label.setObjectName("status_show_label")
        self.verticalLayout_6.addWidget(self.status_show_label)
        self.status_show = QtWidgets.QLabel(self.joint_panel)
        self.status_show.setObjectName("status_show")
        self.verticalLayout_6.addWidget(self.status_show)
        self.solution_label = QtWidgets.QLabel(self.joint_panel)
        self.solution_label.setObjectName("solution_label")
        self.verticalLayout_6.addWidget(self.solution_label)
        self.PLAP_solution = QtWidgets.QPushButton(self.joint_panel)
        self.PLAP_solution.setEnabled(False)
        self.PLAP_solution.setObjectName("PLAP_solution")
        self.verticalLayout_6.addWidget(self.PLAP_solution)
        self.PLLP_solution = QtWidgets.QPushButton(self.joint_panel)
        self.PLLP_solution.setEnabled(False)
        self.PLLP_solution.setObjectName("PLLP_solution")
        self.verticalLayout_6.addWidget(self.PLLP_solution)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.main_layout.addWidget(self.joint_panel)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.line_3 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_7.addWidget(self.line_3)
        self.splitter_4 = QtWidgets.QSplitter(self.verticalLayoutWidget_2)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_4)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_3)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.driver_label = QtWidgets.QLabel(self.layoutWidget)
        self.driver_label.setObjectName("driver_label")
        self.verticalLayout_2.addWidget(self.driver_label)
        self.driver_list = QtWidgets.QListWidget(self.layoutWidget)
        self.driver_list.setObjectName("driver_list")
        self.verticalLayout_2.addWidget(self.driver_list)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.driver_base = QtWidgets.QComboBox(self.layoutWidget)
        self.driver_base.setObjectName("driver_base")
        self.verticalLayout_11.addWidget(self.driver_base)
        self.driver_rotator = QtWidgets.QComboBox(self.layoutWidget)
        self.driver_rotator.setObjectName("driver_rotator")
        self.verticalLayout_11.addWidget(self.driver_rotator)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem2)
        self.driver_add = QtWidgets.QPushButton(self.layoutWidget)
        self.driver_add.setObjectName("driver_add")
        self.verticalLayout_11.addWidget(self.driver_add)
        self.follower_add = QtWidgets.QPushButton(self.layoutWidget)
        self.follower_add.setObjectName("follower_add")
        self.verticalLayout_11.addWidget(self.follower_add)
        self.horizontalLayout.addLayout(self.verticalLayout_11)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.follower_label = QtWidgets.QLabel(self.layoutWidget)
        self.follower_label.setObjectName("follower_label")
        self.verticalLayout_4.addWidget(self.follower_label)
        self.follower_list = QtWidgets.QListWidget(self.layoutWidget)
        self.follower_list.setObjectName("follower_list")
        self.verticalLayout_4.addWidget(self.follower_list)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter_3)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.grounded_label = QtWidgets.QLabel(self.layoutWidget1)
        self.grounded_label.setObjectName("grounded_label")
        self.verticalLayout_15.addWidget(self.grounded_label)
        self.grounded_list = QtWidgets.QListWidget(self.layoutWidget1)
        self.grounded_list.setObjectName("grounded_list")
        self.verticalLayout_15.addWidget(self.grounded_list)
        self.horizontalLayout_2.addLayout(self.verticalLayout_15)
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_4)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget2 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.target_label = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.target_label.sizePolicy().hasHeightForWidth())
        self.target_label.setSizePolicy(sizePolicy)
        self.target_label.setObjectName("target_label")
        self.horizontalLayout_7.addWidget(self.target_label)
        self.target_button = QtWidgets.QPushButton(self.layoutWidget2)
        self.target_button.setObjectName("target_button")
        self.horizontalLayout_7.addWidget(self.target_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.target_list = QtWidgets.QListWidget(self.layoutWidget2)
        self.target_list.setObjectName("target_list")
        self.verticalLayout_3.addWidget(self.target_list)
        self.layoutWidget3 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.constraints_button = QtWidgets.QPushButton(self.layoutWidget3)
        self.constraints_button.setObjectName("constraints_button")
        self.verticalLayout_5.addWidget(self.constraints_button)
        self.constraint_list = QtWidgets.QListWidget(self.layoutWidget3)
        self.constraint_list.setObjectName("constraint_list")
        self.verticalLayout_5.addWidget(self.constraint_list)
        self.layoutWidget4 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.show_solutions = QtWidgets.QCheckBox(self.layoutWidget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.show_solutions.sizePolicy().hasHeightForWidth())
        self.show_solutions.setSizePolicy(sizePolicy)
        self.show_solutions.setChecked(True)
        self.show_solutions.setObjectName("show_solutions")
        self.horizontalLayout_6.addWidget(self.show_solutions)
        self.expression_list_label = QtWidgets.QLabel(self.layoutWidget4)
        self.expression_list_label.setObjectName("expression_list_label")
        self.horizontalLayout_6.addWidget(self.expression_list_label)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.expression_auto = QtWidgets.QPushButton(self.layoutWidget4)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/guide.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.expression_auto.setIcon(icon7)
        self.expression_auto.setObjectName("expression_auto")
        self.horizontalLayout_6.addWidget(self.expression_auto)
        self.verticalLayout_10.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.expression_list = QtWidgets.QListWidget(self.layoutWidget4)
        self.expression_list.setObjectName("expression_list")
        self.horizontalLayout_8.addWidget(self.expression_list)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.expression_clear = QtWidgets.QPushButton(self.layoutWidget4)
        self.expression_clear.setIcon(icon3)
        self.expression_clear.setObjectName("expression_clear")
        self.verticalLayout_9.addWidget(self.expression_clear)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem4)
        self.expression_pop = QtWidgets.QPushButton(self.layoutWidget4)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/arrow_up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.expression_pop.setIcon(icon8)
        self.expression_pop.setObjectName("expression_pop")
        self.verticalLayout_9.addWidget(self.expression_pop)
        self.horizontalLayout_8.addLayout(self.verticalLayout_9)
        self.verticalLayout_10.addLayout(self.horizontalLayout_8)
        self.verticalLayout_7.addWidget(self.splitter_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.link_expression_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.link_expression_label.setObjectName("link_expression_label")
        self.verticalLayout.addWidget(self.link_expression_label)
        self.link_expr_show = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.link_expr_show.setReadOnly(True)
        self.link_expr_show.setObjectName("link_expr_show")
        self.verticalLayout.addWidget(self.link_expr_show)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.expression_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.expression_label.setObjectName("expression_label")
        self.verticalLayout_8.addWidget(self.expression_label)
        self.expr_show = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.expr_show.setReadOnly(True)
        self.expr_show.setObjectName("expr_show")
        self.verticalLayout_8.addWidget(self.expr_show)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.verticalLayout_12.addWidget(self.splitter)
        self.splitter.raise_()
        self.line.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.add_collection_button.setStatusTip(_translate("Form", "Turn this structure diagram back to structure collections."))
        self.load_button.setStatusTip(_translate("Form", "Triangular iteration data and common structure data collections."))
        self.clear_button.setStatusTip(_translate("Form", "Create a new iteration profile."))
        self.save_button.setStatusTip(_translate("Form", "Save this iteration profile to data collections."))
        self.clipboard_button.setStatusTip(_translate("Form", "Save this iteration profile to clipboard as a string."))
        self.joint_name_label.setText(_translate("Form", "Joint:"))
        self.joint_name.setStatusTip(_translate("Form", "Choose a joint tag to see it\'s status."))
        self.add_customization.setStatusTip(_translate("Form", "Customize joints and multiple joints option interface."))
        self.status_show_label.setText(_translate("Form", "Status:"))
        self.status_show.setStatusTip(_translate("Form", "Each joint should have a solution to find out it\'s position."))
        self.status_show.setText(_translate("Form", "N/A"))
        self.solution_label.setText(_translate("Form", "Solutions:"))
        self.PLAP_solution.setText(_translate("Form", "PLAP"))
        self.PLLP_solution.setText(_translate("Form", "PLLP"))
        self.driver_label.setText(_translate("Form", "Drivers:"))
        self.driver_list.setStatusTip(_translate("Form", "These joints will setup an revolute input. The number of them as same as DOF."))
        self.driver_add.setText(_translate("Form", "<<"))
        self.follower_add.setText(_translate("Form", ">>"))
        self.follower_label.setText(_translate("Form", "Followers:"))
        self.follower_list.setStatusTip(_translate("Form", "These joints are on the grounded link, the position of them will generate. So they are don\'t need to have a solution."))
        self.label.setText(_translate("Form", "<<"))
        self.grounded_label.setText(_translate("Form", "Gounded:"))
        self.grounded_list.setStatusTip(_translate("Form", "Set a link as the ground. Existing solutions will be reset."))
        self.target_button.setText(_translate("Form", "Targets"))
        self.target_list.setStatusTip(_translate("Form", "Target points will match as the target path of dimensional _synthesis."))
        self.constraints_button.setText(_translate("Form", "Constraints"))
        self.constraint_list.setStatusTip(_translate("Form", "Four bar loop to apply Gruebler\'s Equation."))
        self.show_solutions.setStatusTip(_translate("Form", "Show triangle sketch on preview window."))
        self.expression_list_label.setText(_translate("Form", "Solutions:"))
        self.expression_auto.setStatusTip(_translate("Form", "Auto configure solutions."))
        self.expression_list.setStatusTip(_translate("Form", "Solutions to find all the positions of joints."))
        self.expression_clear.setStatusTip(_translate("Form", "Clear all the solutions."))
        self.expression_pop.setStatusTip(_translate("Form", "Remove the last solution."))
        self.link_expression_label.setText(_translate("Form", "Link expression:"))
        self.link_expr_show.setStatusTip(_translate("Form", "Link relative expression."))
        self.expression_label.setText(_translate("Form", "Expression:"))
        self.expr_show.setStatusTip(_translate("Form", "Triangular iteration expression."))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

