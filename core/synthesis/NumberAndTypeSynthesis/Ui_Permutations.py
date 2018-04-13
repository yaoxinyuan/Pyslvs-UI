# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ahshoe/桌面/Pyslvs-PyQt5/core/synthesis/NumberAndTypeSynthesis/Permutations.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(471, 671)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/NumberAndTypeSynthesis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Expression_joint_text = QtWidgets.QLabel(Form)
        self.Expression_joint_text.setObjectName("Expression_joint_text")
        self.verticalLayout_4.addWidget(self.Expression_joint_text)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Expression_edges = QtWidgets.QLineEdit(Form)
        self.Expression_edges.setReadOnly(True)
        self.Expression_edges.setObjectName("Expression_edges")
        self.horizontalLayout_4.addWidget(self.Expression_edges)
        self.Expression_copy = QtWidgets.QPushButton(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Expression_copy.setIcon(icon1)
        self.Expression_copy.setObjectName("Expression_copy")
        self.horizontalLayout_4.addWidget(self.Expression_copy)
        self.Expression_add_collection = QtWidgets.QPushButton(Form)
        self.Expression_add_collection.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/collections.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Expression_add_collection.setIcon(icon2)
        self.Expression_add_collection.setObjectName("Expression_add_collection")
        self.horizontalLayout_4.addWidget(self.Expression_add_collection)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.ReloadMechanism = QtWidgets.QPushButton(Form)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/mechanism.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ReloadMechanism.setIcon(icon3)
        self.ReloadMechanism.setIconSize(QtCore.QSize(50, 50))
        self.ReloadMechanism.setAutoDefault(True)
        self.ReloadMechanism.setDefault(True)
        self.ReloadMechanism.setObjectName("ReloadMechanism")
        self.horizontalLayout_3.addWidget(self.ReloadMechanism)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_7.addWidget(self.line)
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.NJ_text = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.NJ_text.setObjectName("NJ_text")
        self.gridLayout.addWidget(self.NJ_text, 0, 1, 1, 1)
        self.NL_text = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.NL_text.setObjectName("NL_text")
        self.gridLayout.addWidget(self.NL_text, 0, 0, 1, 1)
        self.NL_input = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.NL_input.setMinimum(4)
        self.NL_input.setObjectName("NL_input")
        self.gridLayout.addWidget(self.NL_input, 2, 0, 1, 1)
        self.NJ_input = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.NJ_input.setMinimum(4)
        self.NJ_input.setObjectName("NJ_input")
        self.gridLayout.addWidget(self.NJ_input, 2, 1, 1, 1)
        self.DOF_text = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.DOF_text.setObjectName("DOF_text")
        self.gridLayout.addWidget(self.DOF_text, 0, 2, 1, 1)
        self.DOF = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.DOF.setEnabled(False)
        self.DOF.setMinimum(-99)
        self.DOF.setProperty("value", 1)
        self.DOF.setObjectName("DOF")
        self.gridLayout.addWidget(self.DOF, 2, 2, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.keep_dof = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.keep_dof.setChecked(True)
        self.keep_dof.setObjectName("keep_dof")
        self.verticalLayout_5.addWidget(self.keep_dof)
        self.Combine_number = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Combine_number.setAutoDefault(True)
        self.Combine_number.setObjectName("Combine_number")
        self.verticalLayout_5.addWidget(self.Combine_number)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.Expression_number = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.Expression_number.setObjectName("Expression_number")
        self.verticalLayout_2.addWidget(self.Expression_number)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.graph_engine_text = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.graph_engine_text.setObjectName("graph_engine_text")
        self.horizontalLayout.addWidget(self.graph_engine_text)
        self.graph_engine = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.graph_engine.setObjectName("graph_engine")
        self.horizontalLayout.addWidget(self.graph_engine)
        self.reload_atlas = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.reload_atlas.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/dataupdate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reload_atlas.setIcon(icon4)
        self.reload_atlas.setObjectName("reload_atlas")
        self.horizontalLayout.addWidget(self.reload_atlas)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Combine_type_all = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Combine_type_all.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Combine_type_all.setAutoDefault(True)
        self.Combine_type_all.setObjectName("Combine_type_all")
        self.horizontalLayout_5.addWidget(self.Combine_type_all)
        self.Combine_type = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Combine_type.setAutoDefault(True)
        self.Combine_type.setObjectName("Combine_type")
        self.horizontalLayout_5.addWidget(self.Combine_type)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7.addLayout(self.verticalLayout_6)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.graph_link_as_node = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.graph_link_as_node.setObjectName("graph_link_as_node")
        self.verticalLayout.addWidget(self.graph_link_as_node)
        self.graph_degenerate = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.graph_degenerate.setObjectName("graph_degenerate")
        self.verticalLayout.addWidget(self.graph_degenerate)
        self.horizontalLayout_7.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.Topologic_result = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.Topologic_result.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.Topologic_result.setIconSize(QtCore.QSize(200, 200))
        self.Topologic_result.setMovement(QtWidgets.QListView.Static)
        self.Topologic_result.setResizeMode(QtWidgets.QListView.Adjust)
        self.Topologic_result.setViewMode(QtWidgets.QListView.IconMode)
        self.Topologic_result.setUniformItemSizes(True)
        self.Topologic_result.setObjectName("Topologic_result")
        self.verticalLayout_3.addWidget(self.Topologic_result)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.time_title_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.time_title_label.setObjectName("time_title_label")
        self.horizontalLayout_6.addWidget(self.time_title_label)
        self.time_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.time_label.setObjectName("time_label")
        self.horizontalLayout_6.addWidget(self.time_label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.save_atlas = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/picture.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_atlas.setIcon(icon5)
        self.save_atlas.setObjectName("save_atlas")
        self.horizontalLayout_6.addWidget(self.save_atlas)
        self.save_edges = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/savefile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_edges.setIcon(icon6)
        self.save_edges.setObjectName("save_edges")
        self.horizontalLayout_6.addWidget(self.save_edges)
        self.Edges_to_altas = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/edges_to_atlas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Edges_to_altas.setIcon(icon7)
        self.Edges_to_altas.setIconSize(QtCore.QSize(40, 16))
        self.Edges_to_altas.setObjectName("Edges_to_altas")
        self.horizontalLayout_6.addWidget(self.Edges_to_altas)
        self.save_edges_auto = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.save_edges_auto.setObjectName("save_edges_auto")
        self.horizontalLayout_6.addWidget(self.save_edges_auto)
        self.save_edges_auto_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.save_edges_auto_label.setObjectName("save_edges_auto_label")
        self.horizontalLayout_6.addWidget(self.save_edges_auto_label)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout_7.addWidget(self.splitter)

        self.retranslateUi(Form)
        self.graph_engine.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Expression_joint_text.setText(_translate("Form", "Generalized expression:"))
        self.Expression_copy.setStatusTip(_translate("Form", "Copy expression."))
        self.Expression_add_collection.setStatusTip(_translate("Form", "Add to collection."))
        self.ReloadMechanism.setStatusTip(_translate("Form", "Analyze current mechanism from canvas."))
        self.NJ_text.setToolTip(_translate("Form", "Number of joints"))
        self.NJ_text.setText(_translate("Form", "NJ (?)"))
        self.NL_text.setToolTip(_translate("Form", "Number of links"))
        self.NL_text.setText(_translate("Form", "NL (?)"))
        self.DOF_text.setToolTip(_translate("Form", "Degree of freedom"))
        self.DOF_text.setText(_translate("Form", "DOF (?)"))
        self.keep_dof.setStatusTip(_translate("Form", "Keep the degrees of freedom when adjusting numbers."))
        self.keep_dof.setText(_translate("Form", "Keep the DOF"))
        self.Combine_number.setStatusTip(_translate("Form", "Find the possible number of different joints."))
        self.Combine_number.setText(_translate("Form", "Number Synthesis"))
        self.graph_engine_text.setText(_translate("Form", "Engine: "))
        self.graph_engine.setStatusTip(_translate("Form", "Layout engine from NetworkX and Pydot (Graphviz)."))
        self.reload_atlas.setToolTip(_translate("Form", "Re-layout"))
        self.Combine_type_all.setStatusTip(_translate("Form", "Find the structure of mechanism from all numbers."))
        self.Combine_type_all.setText(_translate("Form", "Find all"))
        self.Combine_type.setStatusTip(_translate("Form", "Find the structure of mechanism from specified numbers."))
        self.Combine_type.setText(_translate("Form", "Type Synthesis"))
        self.graph_link_as_node.setStatusTip(_translate("Form", "Show the edges as nodes."))
        self.graph_link_as_node.setText(_translate("Form", "Linkage as node"))
        self.graph_degenerate.setStatusTip(_translate("Form", "Keep degenerate chains in the result."))
        self.graph_degenerate.setText(_translate("Form", "Three edges loop"))
        self.time_title_label.setText(_translate("Form", "Find in:"))
        self.save_atlas.setStatusTip(_translate("Form", "Save the atlas to image file."))
        self.save_edges.setStatusTip(_translate("Form", "Save the edges of atlas to text file."))
        self.Edges_to_altas.setStatusTip(_translate("Form", "Load the edges data from text file, then save them to image files."))
        self.save_edges_auto.setStatusTip(_translate("Form", "Re-synthesis when using save actions."))
        self.save_edges_auto_label.setText(_translate("Form", "<img src=\":icons/dataupdate.png\" width=\"20\">"))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

