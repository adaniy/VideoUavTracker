# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(857, 656)
        Dialog.setFocusPolicy(QtCore.Qt.NoFocus)
        Dialog.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/plugins/tableManager/icons/tableManagerIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(True)
        self.gridlayout = QtWidgets.QGridLayout(Dialog)
        self.gridlayout.setObjectName("gridlayout")
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem1)
        self.butSaveAs = QtWidgets.QPushButton(Dialog)
        self.butSaveAs.setEnabled(False)
        self.butSaveAs.setMinimumSize(QtCore.QSize(0, 32))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/plugins/tableManager/dialog/icons/mActionFileSaveAs.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butSaveAs.setIcon(icon1)
        self.butSaveAs.setObjectName("butSaveAs")
        self.hboxlayout.addWidget(self.butSaveAs)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem3)
        self.gridlayout.addLayout(self.hboxlayout, 2, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridlayout1 = QtWidgets.QGridLayout(self.tab_2)
        self.gridlayout1.setObjectName("gridlayout1")
        self.fieldsTable = QtWidgets.QTableWidget(self.tab_2)
        self.fieldsTable.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldsTable.sizePolicy().hasHeightForWidth())
        self.fieldsTable.setSizePolicy(sizePolicy)
        self.fieldsTable.setMinimumSize(QtCore.QSize(0, 280))
        self.fieldsTable.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.fieldsTable.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.fieldsTable.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.fieldsTable.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.fieldsTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.fieldsTable.setGridStyle(QtCore.Qt.DotLine)
        self.fieldsTable.setWordWrap(False)
        self.fieldsTable.setCornerButtonEnabled(False)
        self.fieldsTable.setRowCount(0)
        self.fieldsTable.setColumnCount(2)
        self.fieldsTable.setObjectName("fieldsTable")
        item = QtWidgets.QTableWidgetItem()
        self.fieldsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.fieldsTable.setHorizontalHeaderItem(1, item)
        self.gridlayout1.addWidget(self.fieldsTable, 0, 0, 1, 1)
        self.vboxlayout = QtWidgets.QVBoxLayout()
        self.vboxlayout.setObjectName("vboxlayout")
        self.butUp = QtWidgets.QToolButton(self.tab_2)
        self.butUp.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butUp.sizePolicy().hasHeightForWidth())
        self.butUp.setSizePolicy(sizePolicy)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/plugins/tableManager/dialog/icons/crystalsvg_1uparrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butUp.setIcon(icon2)
        self.butUp.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.butUp.setObjectName("butUp")
        self.vboxlayout.addWidget(self.butUp)
        self.butDown = QtWidgets.QToolButton(self.tab_2)
        self.butDown.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butDown.sizePolicy().hasHeightForWidth())
        self.butDown.setSizePolicy(sizePolicy)
        self.butDown.setMinimumSize(QtCore.QSize(120, 0))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/plugins/tableManager/dialog/icons/crystalsvg_1downarrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butDown.setIcon(icon3)
        self.butDown.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.butDown.setObjectName("butDown")
        self.vboxlayout.addWidget(self.butDown)
        self.butRename = QtWidgets.QToolButton(self.tab_2)
        self.butRename.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butRename.sizePolicy().hasHeightForWidth())
        self.butRename.setSizePolicy(sizePolicy)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/plugins/tableManager/dialog/icons/tableManagerIcon3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butRename.setIcon(icon4)
        self.butRename.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.butRename.setObjectName("butRename")
        self.vboxlayout.addWidget(self.butRename)
        self.butDel = QtWidgets.QToolButton(self.tab_2)
        self.butDel.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butDel.sizePolicy().hasHeightForWidth())
        self.butDel.setSizePolicy(sizePolicy)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/plugins/tableManager/dialog/icons/mActionDeleteAttribute.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butDel.setIcon(icon5)
        self.butDel.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.butDel.setObjectName("butDel")
        self.vboxlayout.addWidget(self.butDel)
        self.butIns = QtWidgets.QToolButton(self.tab_2)
        self.butIns.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butIns.sizePolicy().hasHeightForWidth())
        self.butIns.setSizePolicy(sizePolicy)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/plugins/tableManager/dialog/icons/mActionNewAttribute.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butIns.setIcon(icon6)
        self.butIns.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.butIns.setObjectName("butIns")
        self.vboxlayout.addWidget(self.butIns)
        self.butClone = QtWidgets.QToolButton(self.tab_2)
        self.butClone.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butClone.sizePolicy().hasHeightForWidth())
        self.butClone.setSizePolicy(sizePolicy)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/plugins/tableManager/dialog/icons/mActionCopySelected.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butClone.setIcon(icon7)
        self.butClone.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.butClone.setObjectName("butClone")
        self.vboxlayout.addWidget(self.butClone)
        self.gridlayout1.addLayout(self.vboxlayout, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridlayout2 = QtWidgets.QGridLayout(self.tab_4)
        self.gridlayout2.setObjectName("gridlayout2")
        self.dataTable = QtWidgets.QTableWidget(self.tab_4)
        self.dataTable.setEnabled(True)
        self.dataTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.dataTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectColumns)
        self.dataTable.setGridStyle(QtCore.Qt.DotLine)
        self.dataTable.setWordWrap(False)
        self.dataTable.setCornerButtonEnabled(False)
        self.dataTable.setObjectName("dataTable")
        self.dataTable.setColumnCount(0)
        self.dataTable.setRowCount(0)
        self.gridlayout2.addWidget(self.dataTable, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.gridlayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.tabWidget, self.fieldsTable)
        Dialog.setTabOrder(self.fieldsTable, self.butUp)
        Dialog.setTabOrder(self.butUp, self.butDown)
        Dialog.setTabOrder(self.butDown, self.butRename)
        Dialog.setTabOrder(self.butRename, self.butDel)
        Dialog.setTabOrder(self.butDel, self.butIns)
        Dialog.setTabOrder(self.butIns, self.butClone)
        Dialog.setTabOrder(self.butClone, self.butSaveAs)
        Dialog.setTabOrder(self.butSaveAs, self.dataTable)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Table Manager"))
        self.butSaveAs.setToolTip(_translate("Dialog", "Save changes to a new layer"))
        self.butSaveAs.setText(_translate("Dialog", "Use this Fields"))
        item = self.fieldsTable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Name"))
        item = self.fieldsTable.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Type"))
        self.butUp.setToolTip(_translate("Dialog", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Move selected field up</p></body></html>"))
        self.butUp.setText(_translate("Dialog", "Move Up"))
        self.butDown.setToolTip(_translate("Dialog", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Move selected field down</p></body></html>"))
        self.butDown.setText(_translate("Dialog", "Move Down"))
        self.butRename.setToolTip(_translate("Dialog", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Rename selected field</p></body></html>"))
        self.butRename.setText(_translate("Dialog", "Rename"))
        self.butDel.setToolTip(_translate("Dialog", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Remove selected field</p></body></html>"))
        self.butDel.setText(_translate("Dialog", "Delete"))
        self.butIns.setToolTip(_translate("Dialog", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Insert new field</p></body></html>"))
        self.butIns.setText(_translate("Dialog", "Insert"))
        self.butClone.setToolTip(_translate("Dialog", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Clone selected field</p></body></html>"))
        self.butClone.setText(_translate("Dialog", "Clone"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Fields"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "Table preview"))
        self.label.setText(_translate("Dialog", "Progressive id, some coordinates stuff, and a link to a snapshot fields are already loaded."))

