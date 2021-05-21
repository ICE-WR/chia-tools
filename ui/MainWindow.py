# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\peng\Desktop\chia-tools\ui\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(901, 598)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabFolders = QtWidgets.QWidget()
        self.tabFolders.setObjectName("tabFolders")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabFolders)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabFoldersWidget = FoldersWidget(self.tabFolders)
        self.tabFoldersWidget.setObjectName("tabFoldersWidget")
        self.verticalLayout_2.addWidget(self.tabFoldersWidget)
        self.tabWidget.addTab(self.tabFolders, "")
        self.tabPlot = QtWidgets.QWidget()
        self.tabPlot.setObjectName("tabPlot")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tabPlot)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabPlotWidget = PlotWidget(self.tabPlot)
        self.tabPlotWidget.setObjectName("tabPlotWidget")
        self.verticalLayout_5.addWidget(self.tabPlotWidget)
        self.tabWidget.addTab(self.tabPlot, "")
        self.tabMine = QtWidgets.QWidget()
        self.tabMine.setObjectName("tabMine")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tabMine)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tabMineWidget = MineWidget(self.tabMine)
        self.tabMineWidget.setObjectName("tabMineWidget")
        self.verticalLayout_6.addWidget(self.tabMineWidget)
        self.tabWidget.addTab(self.tabMine, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ChiaTools"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabFolders), _translate("MainWindow", "硬盘"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPlot), _translate("MainWindow", "P图任务"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMine), _translate("MainWindow", "HPool矿池挖矿"))
from widgets.FoldersWidget import FoldersWidget
from widgets.MineWidget import MineWidget
from widgets.PlotWidget import PlotWidget
