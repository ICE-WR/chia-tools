# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\peng\Desktop\chia-tools\ui\PlotWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PlotWidget(object):
    def setupUi(self, PlotWidget):
        PlotWidget.setObjectName("PlotWidget")
        PlotWidget.resize(778, 533)
        self.verticalLayout = QtWidgets.QVBoxLayout(PlotWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.treePlot = QtWidgets.QTreeWidget(PlotWidget)
        self.treePlot.setExpandsOnDoubleClick(False)
        self.treePlot.setObjectName("treePlot")
        self.verticalLayout.addWidget(self.treePlot)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.checkBoxPhase1Limit = QtWidgets.QCheckBox(PlotWidget)
        self.checkBoxPhase1Limit.setObjectName("checkBoxPhase1Limit")
        self.horizontalLayout_4.addWidget(self.checkBoxPhase1Limit)
        self.spinBoxPhase1Count = QtWidgets.QSpinBox(PlotWidget)
        self.spinBoxPhase1Count.setMinimum(1)
        self.spinBoxPhase1Count.setObjectName("spinBoxPhase1Count")
        self.horizontalLayout_4.addWidget(self.spinBoxPhase1Count)
        self.checkBoxTotalLimit = QtWidgets.QCheckBox(PlotWidget)
        self.checkBoxTotalLimit.setObjectName("checkBoxTotalLimit")
        self.horizontalLayout_4.addWidget(self.checkBoxTotalLimit)
        self.spinBoxTotalCount = QtWidgets.QSpinBox(PlotWidget)
        self.spinBoxTotalCount.setMinimum(1)
        self.spinBoxTotalCount.setObjectName("spinBoxTotalCount")
        self.horizontalLayout_4.addWidget(self.spinBoxTotalCount)
        self.checkBoxNextWhenFullyComplete = QtWidgets.QCheckBox(PlotWidget)
        self.checkBoxNextWhenFullyComplete.setObjectName("checkBoxNextWhenFullyComplete")
        self.horizontalLayout_4.addWidget(self.checkBoxNextWhenFullyComplete)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.buttonCreateBatchPlots = QtWidgets.QPushButton(PlotWidget)
        self.buttonCreateBatchPlots.setObjectName("buttonCreateBatchPlots")
        self.horizontalLayout_4.addWidget(self.buttonCreateBatchPlots)
        self.buttonCreatePlot = QtWidgets.QPushButton(PlotWidget)
        self.buttonCreatePlot.setObjectName("buttonCreatePlot")
        self.horizontalLayout_4.addWidget(self.buttonCreatePlot)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(PlotWidget)
        QtCore.QMetaObject.connectSlotsByName(PlotWidget)

    def retranslateUi(self, PlotWidget):
        _translate = QtCore.QCoreApplication.translate
        PlotWidget.setWindowTitle(_translate("PlotWidget", "Form"))
        self.treePlot.headerItem().setText(0, _translate("PlotWidget", "临时目录（固态）"))
        self.treePlot.headerItem().setText(1, _translate("PlotWidget", "最终目录（机械）"))
        self.treePlot.headerItem().setText(2, _translate("PlotWidget", "状态"))
        self.treePlot.headerItem().setText(3, _translate("PlotWidget", "当前数量"))
        self.treePlot.headerItem().setText(4, _translate("PlotWidget", "开始时间"))
        self.treePlot.headerItem().setText(5, _translate("PlotWidget", "用时"))
        self.treePlot.headerItem().setText(6, _translate("PlotWidget", "使用内存"))
        self.treePlot.headerItem().setText(7, _translate("PlotWidget", "进度"))
        self.checkBoxPhase1Limit.setText(_translate("PlotWidget", "限制阶段1的并发数量"))
        self.spinBoxPhase1Count.setSuffix(_translate("PlotWidget", "个"))
        self.checkBoxTotalLimit.setText(_translate("PlotWidget", "限制总并发数量"))
        self.spinBoxTotalCount.setSuffix(_translate("PlotWidget", "个"))
        self.checkBoxNextWhenFullyComplete.setText(_translate("PlotWidget", "等待任务100%后再执行下一个"))
        self.buttonCreateBatchPlots.setText(_translate("PlotWidget", "批量创建任务"))
        self.buttonCreatePlot.setText(_translate("PlotWidget", "创建任务"))
