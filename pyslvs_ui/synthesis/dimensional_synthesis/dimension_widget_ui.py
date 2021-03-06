# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyslvs_ui/synthesis/dimensional_synthesis/dimension_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from qtpy import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(430, 714)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/dimensional_synthesis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.main_splitter = QtWidgets.QSplitter(Form)
        self.main_splitter.setOrientation(QtCore.Qt.Vertical)
        self.main_splitter.setObjectName("main_splitter")
        self.verticalGroupBox = QtWidgets.QGroupBox(self.main_splitter)
        self.verticalGroupBox.setObjectName("verticalGroupBox")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.verticalGroupBox)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.result_list = QtWidgets.QListWidget(self.verticalGroupBox)
        self.result_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.result_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.result_list.setObjectName("result_list")
        self.verticalLayout_13.addWidget(self.result_list)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.result_load_settings = QtWidgets.QPushButton(self.verticalGroupBox)
        self.result_load_settings.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/data_update.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.result_load_settings.setIcon(icon1)
        self.result_load_settings.setObjectName("result_load_settings")
        self.horizontalLayout_10.addWidget(self.result_load_settings)
        self.result_clipboard = QtWidgets.QPushButton(self.verticalGroupBox)
        self.result_clipboard.setEnabled(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.result_clipboard.setIcon(icon2)
        self.result_clipboard.setObjectName("result_clipboard")
        self.horizontalLayout_10.addWidget(self.result_clipboard)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.delete_button = QtWidgets.QPushButton(self.verticalGroupBox)
        self.delete_button.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_button.setIcon(icon3)
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout_10.addWidget(self.delete_button)
        self.merge_button = QtWidgets.QPushButton(self.verticalGroupBox)
        self.merge_button.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/merge.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.merge_button.setIcon(icon4)
        self.merge_button.setObjectName("merge_button")
        self.horizontalLayout_10.addWidget(self.merge_button)
        self.verticalLayout_13.addLayout(self.horizontalLayout_10)
        self.target_label = QtWidgets.QLabel(self.verticalGroupBox)
        self.target_label.setWordWrap(True)
        self.target_label.setObjectName("target_label")
        self.verticalLayout_13.addWidget(self.target_label)
        self.horizontalLayout_6.addLayout(self.verticalLayout_13)
        self.options_tab = QtWidgets.QTabWidget(self.main_splitter)
        self.options_tab.setObjectName("options_tab")
        self.structure = QtWidgets.QWidget()
        self.structure.setObjectName("structure")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.structure)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.load_profile = QtWidgets.QPushButton(self.structure)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/collections.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.load_profile.setIcon(icon5)
        self.load_profile.setObjectName("load_profile")
        self.horizontalLayout_7.addWidget(self.load_profile)
        self.save_profile = QtWidgets.QPushButton(self.structure)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/save_file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_profile.setIcon(icon6)
        self.save_profile.setObjectName("save_profile")
        self.horizontalLayout_7.addWidget(self.save_profile)
        self.profile_name = QtWidgets.QLineEdit(self.structure)
        self.profile_name.setReadOnly(True)
        self.profile_name.setObjectName("profile_name")
        self.horizontalLayout_7.addWidget(self.profile_name)
        self.clear_button = QtWidgets.QPushButton(self.structure)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/clean.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_button.setIcon(icon7)
        self.clear_button.setObjectName("clear_button")
        self.horizontalLayout_7.addWidget(self.clear_button)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.expression_string = QtWidgets.QLineEdit(self.structure)
        self.expression_string.setReadOnly(True)
        self.expression_string.setObjectName("expression_string")
        self.horizontalLayout_17.addWidget(self.expression_string)
        self.expr_copy = QtWidgets.QPushButton(self.structure)
        self.expr_copy.setIcon(icon2)
        self.expr_copy.setObjectName("expr_copy")
        self.horizontalLayout_17.addWidget(self.expr_copy)
        self.verticalLayout_6.addLayout(self.horizontalLayout_17)
        self.up_splitter = QtWidgets.QSplitter(self.structure)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.up_splitter.sizePolicy().hasHeightForWidth())
        self.up_splitter.setSizePolicy(sizePolicy)
        self.up_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.up_splitter.setObjectName("up_splitter")
        self.parameter_list = QtWidgets.QTableWidget(self.up_splitter)
        self.parameter_list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.parameter_list.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.parameter_list.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.parameter_list.setObjectName("parameter_list")
        self.parameter_list.setColumnCount(5)
        self.parameter_list.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.parameter_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.parameter_list.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.parameter_list.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.parameter_list.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.parameter_list.setHorizontalHeaderItem(4, item)
        self.preview_box = QtWidgets.QGroupBox(self.up_splitter)
        self.preview_box.setObjectName("preview_box")
        self.preview_layout = QtWidgets.QVBoxLayout(self.preview_box)
        self.preview_layout.setObjectName("preview_layout")
        self.show_solutions = QtWidgets.QCheckBox(self.preview_box)
        self.show_solutions.setChecked(True)
        self.show_solutions.setObjectName("show_solutions")
        self.preview_layout.addWidget(self.show_solutions)
        self.verticalLayout_6.addWidget(self.up_splitter)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/structure.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.options_tab.addTab(self.structure, icon8, "")
        self.target_path = QtWidgets.QWidget()
        self.target_path.setObjectName("target_path")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.target_path)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.down_splitter = QtWidgets.QSplitter(self.target_path)
        self.down_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.down_splitter.setObjectName("down_splitter")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.down_splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.target_points = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.target_points.setObjectName("target_points")
        self.verticalLayout.addWidget(self.target_points)
        self.shape_only_option = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.shape_only_option.setObjectName("shape_only_option")
        self.verticalLayout.addWidget(self.shape_only_option)
        self.wavelet_mode_option = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.wavelet_mode_option.setObjectName("wavelet_mode_option")
        self.verticalLayout.addWidget(self.wavelet_mode_option)
        self.layoutWidget = QtWidgets.QWidget(self.down_splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.point_num = QtWidgets.QLabel(self.layoutWidget)
        self.point_num.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.point_num.setObjectName("point_num")
        self.horizontalLayout_2.addWidget(self.point_num)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.path_paste = QtWidgets.QPushButton(self.layoutWidget)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.path_paste.setIcon(icon9)
        self.path_paste.setObjectName("path_paste")
        self.horizontalLayout_2.addWidget(self.path_paste)
        self.path_copy = QtWidgets.QPushButton(self.layoutWidget)
        self.path_copy.setIcon(icon2)
        self.path_copy.setObjectName("path_copy")
        self.horizontalLayout_2.addWidget(self.path_copy)
        self.path_clear = QtWidgets.QPushButton(self.layoutWidget)
        self.path_clear.setIcon(icon7)
        self.path_clear.setAutoDefault(False)
        self.path_clear.setObjectName("path_clear")
        self.horizontalLayout_2.addWidget(self.path_clear)
        self.verticalLayout_8.addLayout(self.horizontalLayout_2)
        self.path_list = QtWidgets.QListWidget(self.layoutWidget)
        self.path_list.setObjectName("path_list")
        self.verticalLayout_8.addWidget(self.path_list)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.point_up = QtWidgets.QPushButton(self.layoutWidget)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/arrow_up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.point_up.setIcon(icon10)
        self.point_up.setObjectName("point_up")
        self.horizontalLayout_8.addWidget(self.point_up)
        self.point_down = QtWidgets.QPushButton(self.layoutWidget)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/arrow_down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.point_down.setIcon(icon11)
        self.point_down.setObjectName("point_down")
        self.horizontalLayout_8.addWidget(self.point_down)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.point_delete = QtWidgets.QPushButton(self.layoutWidget)
        self.point_delete.setIcon(icon3)
        self.point_delete.setObjectName("point_delete")
        self.horizontalLayout_8.addWidget(self.point_delete)
        self.edit_target_point_button = QtWidgets.QPushButton(self.layoutWidget)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/translate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_target_point_button.setIcon(icon12)
        self.edit_target_point_button.setCheckable(True)
        self.edit_target_point_button.setChecked(True)
        self.edit_target_point_button.setObjectName("edit_target_point_button")
        self.horizontalLayout_8.addWidget(self.edit_target_point_button)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_5.addLayout(self.verticalLayout_8)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.save_path_button = QtWidgets.QPushButton(self.layoutWidget)
        self.save_path_button.setIcon(icon6)
        self.save_path_button.setIconSize(QtCore.QSize(40, 40))
        self.save_path_button.setObjectName("save_path_button")
        self.verticalLayout_3.addWidget(self.save_path_button)
        self.import_csv_button = QtWidgets.QPushButton(self.layoutWidget)
        self.import_csv_button.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/loadfile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.import_csv_button.setIcon(icon13)
        self.import_csv_button.setIconSize(QtCore.QSize(40, 40))
        self.import_csv_button.setObjectName("import_csv_button")
        self.verticalLayout_3.addWidget(self.import_csv_button)
        self.import_xlsx_button = QtWidgets.QPushButton(self.layoutWidget)
        self.import_xlsx_button.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/excel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.import_xlsx_button.setIcon(icon14)
        self.import_xlsx_button.setIconSize(QtCore.QSize(40, 40))
        self.import_xlsx_button.setObjectName("import_xlsx_button")
        self.verticalLayout_3.addWidget(self.import_xlsx_button)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.edit_path_button = QtWidgets.QPushButton(self.layoutWidget)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/icons/formula.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_path_button.setIcon(icon15)
        self.edit_path_button.setIconSize(QtCore.QSize(40, 40))
        self.edit_path_button.setObjectName("edit_path_button")
        self.verticalLayout_3.addWidget(self.edit_path_button)
        self.efd_button = QtWidgets.QPushButton(self.layoutWidget)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/icons/efd.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.efd_button.setIcon(icon16)
        self.efd_button.setIconSize(QtCore.QSize(40, 40))
        self.efd_button.setObjectName("efd_button")
        self.verticalLayout_3.addWidget(self.efd_button)
        self.norm_path_button = QtWidgets.QPushButton(self.layoutWidget)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/icons/normalization.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.norm_path_button.setIcon(icon17)
        self.norm_path_button.setIconSize(QtCore.QSize(40, 40))
        self.norm_path_button.setObjectName("norm_path_button")
        self.verticalLayout_3.addWidget(self.norm_path_button)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addWidget(self.down_splitter)
        self.options_tab.addTab(self.target_path, icon, "")
        self.algorithm = QtWidgets.QWidget()
        self.algorithm.setObjectName("algorithm")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.algorithm)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.algorithm_layout = QtWidgets.QVBoxLayout()
        self.algorithm_layout.setObjectName("algorithm_layout")
        self.verticalLayout_7.addLayout(self.algorithm_layout)
        self.advance_button = QtWidgets.QPushButton(self.algorithm)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/icons/properties.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.advance_button.setIcon(icon18)
        self.advance_button.setObjectName("advance_button")
        self.verticalLayout_7.addWidget(self.advance_button)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(self.algorithm)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.timeShow = QtWidgets.QLabel(self.algorithm)
        self.timeShow.setObjectName("timeShow")
        self.horizontalLayout.addWidget(self.timeShow)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/icons/synthesis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.options_tab.addTab(self.algorithm, icon19, "")
        self.verticalLayout_4.addWidget(self.main_splitter)
        self.synthesis_button = QtWidgets.QPushButton(Form)
        self.synthesis_button.setEnabled(False)
        self.synthesis_button.setMinimumSize(QtCore.QSize(120, 0))
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/icons/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.synthesis_button.setIcon(icon20)
        self.synthesis_button.setAutoDefault(True)
        self.synthesis_button.setObjectName("synthesis_button")
        self.verticalLayout_4.addWidget(self.synthesis_button)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.verticalGroupBox.setTitle(_translate("Form", "Results"))
        self.result_load_settings.setStatusTip(_translate("Form", "Load the setting of this result."))
        self.delete_button.setStatusTip(_translate("Form", "Delete this result."))
        self.merge_button.setStatusTip(_translate("Form", "Merge this result to canvas."))
        self.target_label.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ff0000;\">※ Use &quot;Alt + LF&quot; to add the path points.</span></p></body></html>"))
        self.load_profile.setStatusTip(_translate("Form", "Load profile from triangular iteration database."))
        self.save_profile.setStatusTip(_translate("Form", "Save the structure profile back to the database."))
        self.clear_button.setStatusTip(_translate("Form", "Clear the current profile and settings."))
        self.parameter_list.setStatusTip(_translate("Form", "All the joints of grounded link will show here."))
        item = self.parameter_list.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Name"))
        item = self.parameter_list.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Role"))
        item = self.parameter_list.horizontalHeaderItem(2)
        item.setText(_translate("Form", "p0"))
        item = self.parameter_list.horizontalHeaderItem(3)
        item.setText(_translate("Form", "p1"))
        item = self.parameter_list.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Range"))
        self.preview_box.setTitle(_translate("Form", "Preview"))
        self.show_solutions.setText(_translate("Form", "Show solutions"))
        self.options_tab.setTabText(self.options_tab.indexOf(self.structure), _translate("Form", "Structure"))
        self.shape_only_option.setText(_translate("Form", "Compare shape only"))
        self.wavelet_mode_option.setText(_translate("Form", "Wavelet transform (alpha)"))
        self.point_num.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#00aa00;\">0</span></p></body></html>"))
        self.path_paste.setStatusTip(_translate("Form", "Past path data from string format."))
        self.path_copy.setStatusTip(_translate("Form", "Copy the path data as a string."))
        self.path_clear.setStatusTip(_translate("Form", "Clear all points."))
        self.point_up.setStatusTip(_translate("Form", "Move the point up."))
        self.point_down.setStatusTip(_translate("Form", "Move the point down."))
        self.point_delete.setStatusTip(_translate("Form", "Remove the point."))
        self.edit_target_point_button.setStatusTip(_translate("Form", "User can edit target point immediately."))
        self.save_path_button.setStatusTip(_translate("Form", "Save current path as csv file."))
        self.import_csv_button.setStatusTip(_translate("Form", "Import path from CSV format."))
        self.import_xlsx_button.setStatusTip(_translate("Form", "Import path from Microsoft Excel format."))
        self.edit_path_button.setStatusTip(_translate("Form", "Edit the target path."))
        self.efd_button.setStatusTip(_translate("Form", "Using Elliptical Fourier Descriptor to regenerate the path."))
        self.norm_path_button.setStatusTip(_translate("Form", "Apply normalization on current path."))
        self.options_tab.setTabText(self.options_tab.indexOf(self.target_path), _translate("Form", "Target path"))
        self.advance_button.setStatusTip(_translate("Form", "More algorithm settings."))
        self.advance_button.setText(_translate("Form", "Advance Options"))
        self.label_7.setText(_translate("Form", "Time spent:"))
        self.timeShow.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt;\">[N/A]</span></p></body></html>"))
        self.options_tab.setTabText(self.options_tab.indexOf(self.algorithm), _translate("Form", "Algorithm"))
        self.synthesis_button.setStatusTip(_translate("Form", "Start dimesional synthesis."))
        self.synthesis_button.setText(_translate("Form", "Synthesis"))
