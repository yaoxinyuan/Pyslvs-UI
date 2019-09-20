# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyslvs_ui/core/synthesis/collections/structure_widget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from qtpy import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(438, 662)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/structure.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_by_files_button = QtWidgets.QPushButton(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/loadfile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_by_files_button.setIcon(icon1)
        self.add_by_files_button.setObjectName("add_by_files_button")
        self.horizontalLayout.addWidget(self.add_by_files_button)
        self.add_by_edges_button = QtWidgets.QPushButton(Form)
        self.add_by_edges_button.setIcon(icon)
        self.add_by_edges_button.setObjectName("add_by_edges_button")
        self.horizontalLayout.addWidget(self.add_by_edges_button)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.save_atlas = QtWidgets.QPushButton(Form)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/picture.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_atlas.setIcon(icon2)
        self.save_atlas.setObjectName("save_atlas")
        self.horizontalLayout.addWidget(self.save_atlas)
        self.save_edges = QtWidgets.QPushButton(Form)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/save_file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_edges.setIcon(icon3)
        self.save_edges.setObjectName("save_edges")
        self.horizontalLayout.addWidget(self.save_edges)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.delete_button = QtWidgets.QPushButton(Form)
        self.delete_button.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_button.setIcon(icon4)
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout.addWidget(self.delete_button)
        self.clear_button = QtWidgets.QPushButton(Form)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/clean.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_button.setIcon(icon5)
        self.clear_button.setObjectName("clear_button")
        self.horizontalLayout.addWidget(self.clear_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.collection_list = QtWidgets.QListWidget(self.splitter)
        self.collection_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.collection_list.setIconSize(QtCore.QSize(100, 100))
        self.collection_list.setMovement(QtWidgets.QListView.Static)
        self.collection_list.setResizeMode(QtWidgets.QListView.Adjust)
        self.collection_list.setViewMode(QtWidgets.QListView.IconMode)
        self.collection_list.setUniformItemSizes(True)
        self.collection_list.setObjectName("collection_list")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.graph_engine_text = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.graph_engine_text.setObjectName("graph_engine_text")
        self.horizontalLayout_7.addWidget(self.graph_engine_text)
        self.graph_engine = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.graph_engine.setObjectName("graph_engine")
        self.horizontalLayout_7.addWidget(self.graph_engine)
        self.reload_atlas = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.reload_atlas.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/data_update.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reload_atlas.setIcon(icon6)
        self.reload_atlas.setObjectName("reload_atlas")
        self.horizontalLayout_7.addWidget(self.reload_atlas)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.graph_link_as_node = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.graph_link_as_node.setObjectName("graph_link_as_node")
        self.horizontalLayout_7.addWidget(self.graph_link_as_node)
        self.graph_show_label = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.graph_show_label.setChecked(True)
        self.graph_show_label.setObjectName("graph_show_label")
        self.horizontalLayout_7.addWidget(self.graph_show_label)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.edges_text = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edges_text.setReadOnly(True)
        self.edges_text.setObjectName("edges_text")
        self.horizontalLayout_3.addWidget(self.edges_text)
        self.expr_copy = QtWidgets.QPushButton(self.verticalLayoutWidget)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.expr_copy.setIcon(icon7)
        self.expr_copy.setObjectName("expr_copy")
        self.horizontalLayout_3.addWidget(self.expr_copy)
        self.capture_graph = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.capture_graph.setIcon(icon2)
        self.capture_graph.setObjectName("capture_graph")
        self.horizontalLayout_3.addWidget(self.capture_graph)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.selection_window = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.selection_window.setMinimumSize(QtCore.QSize(210, 230))
        self.selection_window.setMaximumSize(QtCore.QSize(210, 230))
        self.selection_window.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.selection_window.setIconSize(QtCore.QSize(200, 200))
        self.selection_window.setMovement(QtWidgets.QListView.Static)
        self.selection_window.setViewMode(QtWidgets.QListView.IconMode)
        self.selection_window.setObjectName("selection_window")
        self.horizontalLayout_2.addWidget(self.selection_window)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.nl_text = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.nl_text.setObjectName("nl_text")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.nl_text)
        self.nl_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.nl_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.nl_label.setObjectName("nl_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.nl_label)
        self.nj_text = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.nj_text.setObjectName("nj_text")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.nj_text)
        self.nj_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.nj_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.nj_label.setObjectName("nj_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.nj_label)
        self.dof_text = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.dof_text.setObjectName("dof_text")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.dof_text)
        self.dof_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.dof_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dof_label.setObjectName("dof_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.dof_label)
        self.is_degenerate_text = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.is_degenerate_text.setObjectName("is_degenerate_text")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.is_degenerate_text)
        self.is_degenerate_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.is_degenerate_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.is_degenerate_label.setObjectName("is_degenerate_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.is_degenerate_label)
        self.verticalLayout_5.addLayout(self.formLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.link_assortment_text = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.link_assortment_text.setObjectName("link_assortment_text")
        self.verticalLayout_4.addWidget(self.link_assortment_text)
        self.link_assortment_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.link_assortment_label.setObjectName("link_assortment_label")
        self.verticalLayout_4.addWidget(self.link_assortment_label)
        self.contracted_link_assortment_text = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.contracted_link_assortment_text.setObjectName("contracted_link_assortment_text")
        self.verticalLayout_4.addWidget(self.contracted_link_assortment_text)
        self.contracted_link_assortment_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.contracted_link_assortment_label.setObjectName("contracted_link_assortment_label")
        self.verticalLayout_4.addWidget(self.contracted_link_assortment_label)
        self.duplicate_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.duplicate_button.setEnabled(False)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/reflect.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.duplicate_button.setIcon(icon8)
        self.duplicate_button.setObjectName("duplicate_button")
        self.verticalLayout_4.addWidget(self.duplicate_button)
        self.configure_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.configure_button.setEnabled(False)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/configure.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.configure_button.setIcon(icon9)
        self.configure_button.setObjectName("configure_button")
        self.verticalLayout_4.addWidget(self.configure_button)
        self.merge_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.merge_button.setEnabled(False)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/merge.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.merge_button.setIcon(icon10)
        self.merge_button.setObjectName("merge_button")
        self.verticalLayout_4.addWidget(self.merge_button)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.grounded_list = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.grounded_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.grounded_list.setIconSize(QtCore.QSize(150, 150))
        self.grounded_list.setMovement(QtWidgets.QListView.Static)
        self.grounded_list.setResizeMode(QtWidgets.QListView.Adjust)
        self.grounded_list.setViewMode(QtWidgets.QListView.IconMode)
        self.grounded_list.setUniformItemSizes(True)
        self.grounded_list.setObjectName("grounded_list")
        self.horizontalLayout_4.addWidget(self.grounded_list)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addWidget(self.splitter)

        self.retranslateUi(Form)
        self.graph_engine.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.add_by_files_button.setStatusTip(_translate("Form", "Add the chain by edge expression from text files."))
        self.add_by_edges_button.setStatusTip(_translate("Form", "Add the chain by edge expression."))
        self.save_atlas.setStatusTip(_translate("Form", "Save the atlas to image file."))
        self.save_atlas.setText(_translate("Form", "Save as image"))
        self.save_edges.setStatusTip(_translate("Form", "Save the edges of atlas to text file."))
        self.save_edges.setText(_translate("Form", "Save as list"))
        self.delete_button.setStatusTip(_translate("Form", "Delete this structure."))
        self.clear_button.setStatusTip(_translate("Form", "Delete all of structures."))
        self.graph_engine_text.setText(_translate("Form", "Engine: "))
        self.graph_engine.setStatusTip(_translate("Form", "Layout engine from NetworkX."))
        self.reload_atlas.setToolTip(_translate("Form", "Re-layout"))
        self.graph_link_as_node.setText(_translate("Form", "Link as node"))
        self.graph_show_label.setText(_translate("Form", "Show labels"))
        self.expr_copy.setStatusTip(_translate("Form", "Copy expression."))
        self.nl_text.setToolTip(_translate("Form", "Number of links"))
        self.nl_text.setText(_translate("Form", "NL: (?)"))
        self.nl_label.setText(_translate("Form", "0"))
        self.nj_text.setToolTip(_translate("Form", "Number of joints"))
        self.nj_text.setText(_translate("Form", "NJ: (?)"))
        self.nj_label.setText(_translate("Form", "0"))
        self.dof_text.setToolTip(_translate("Form", "Degrees of freedom"))
        self.dof_text.setText(_translate("Form", "DOF: (?)"))
        self.dof_label.setText(_translate("Form", "0"))
        self.is_degenerate_text.setText(_translate("Form", "Is degenerate:"))
        self.is_degenerate_label.setText(_translate("Form", "N/A"))
        self.link_assortment_text.setToolTip(_translate("Form", "Link assortment"))
        self.link_assortment_text.setText(_translate("Form", "LA: (?)"))
        self.link_assortment_label.setText(_translate("Form", "N/A"))
        self.contracted_link_assortment_text.setToolTip(_translate("Form", "Contracted link assortment"))
        self.contracted_link_assortment_text.setText(_translate("Form", "CLA: (?)"))
        self.contracted_link_assortment_label.setText(_translate("Form", "N/A"))
        self.duplicate_button.setText(_translate("Form", "Make Duplicate"))
        self.configure_button.setStatusTip(_translate("Form", "Use trangular formula to do dimentional synthesis."))
        self.configure_button.setText(_translate("Form", "Configure"))
        self.merge_button.setStatusTip(_translate("Form", "Merge the specified chain to canvas with current layout."))
        self.merge_button.setText(_translate("Form", "Merge"))
from pyslvs_ui import icons_rc
