# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NefiTemplateView.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1336, 988)
        self.CentralView = QtWidgets.QWidget(MainWindow)
        self.CentralView.setObjectName("CentralView")
        self.gridLayout = QtWidgets.QGridLayout(self.CentralView)
        self.gridLayout.setObjectName("gridLayout")
        self.Images_Pipeline_Placeholder = QtWidgets.QWidget(self.CentralView)
        self.Images_Pipeline_Placeholder.setMinimumSize(QtCore.QSize(250, 0))
        self.Images_Pipeline_Placeholder.setMaximumSize(QtCore.QSize(250, 16777215))
        self.Images_Pipeline_Placeholder.setObjectName("Images_Pipeline_Placeholder")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.Images_Pipeline_Placeholder)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 241, 941))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.Images_Pipeline_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.Images_Pipeline_layout.setObjectName("Images_Pipeline_layout")
        self.gridLayout.addWidget(self.Images_Pipeline_Placeholder, 0, 2, 1, 1)
        self.DetailedView = QtWidgets.QWidget(self.CentralView)
        self.DetailedView.setMinimumSize(QtCore.QSize(800, 0))
        self.DetailedView.setObjectName("DetailedView")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.DetailedView)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 801, 941))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.Images_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.Images_layout.setObjectName("Images_layout")
        self.gridLayout.addWidget(self.DetailedView, 0, 3, 1, 1)
        self.RightView = QtWidgets.QWidget(self.CentralView)
        self.RightView.setMaximumSize(QtCore.QSize(250, 16777215))
        self.RightView.setObjectName("RightView")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.RightView)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Settings_Placeholder = QtWidgets.QWidget(self.RightView)
        self.Settings_Placeholder.setMinimumSize(QtCore.QSize(250, 300))
        self.Settings_Placeholder.setAutoFillBackground(False)
        self.Settings_Placeholder.setObjectName("Settings_Placeholder")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.Settings_Placeholder)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 241, 611))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.Settings_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.Settings_layout.setObjectName("Settings_layout")
        self.verticalLayout.addWidget(self.Settings_Placeholder)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.Pipeline_Order_Placeholder = QtWidgets.QWidget(self.RightView)
        self.Pipeline_Order_Placeholder.setMinimumSize(QtCore.QSize(250, 300))
        self.Pipeline_Order_Placeholder.setMaximumSize(QtCore.QSize(250, 300))
        self.Pipeline_Order_Placeholder.setObjectName("Pipeline_Order_Placeholder")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.Pipeline_Order_Placeholder)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 241, 291))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.Pipeline_Order_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.Pipeline_Order_layout.setObjectName("Pipeline_Order_layout")
        self.verticalLayout.addWidget(self.Pipeline_Order_Placeholder)
        self.gridLayout.addWidget(self.RightView, 0, 4, 1, 1)
        MainWindow.setCentralWidget(self.CentralView)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1336, 30))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuImages = QtWidgets.QMenu(self.menuBar)
        self.menuImages.setObjectName("menuImages")
        MainWindow.setMenuBar(self.menuBar)
        self.PipelineMenu = QtWidgets.QAction(MainWindow)
        self.PipelineMenu.setObjectName("PipelineMenu")
        self.actionImages = QtWidgets.QAction(MainWindow)
        self.actionImages.setObjectName("actionImages")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionLoad_2 = QtWidgets.QAction(MainWindow)
        self.actionLoad_2.setObjectName("actionLoad_2")
        self.actionSave_2 = QtWidgets.QAction(MainWindow)
        self.actionSave_2.setObjectName("actionSave_2")
        self.actionLoad_3 = QtWidgets.QAction(MainWindow)
        self.actionLoad_3.setObjectName("actionLoad_3")
        self.actionLoad_Image_Folder = QtWidgets.QAction(MainWindow)
        self.actionLoad_Image_Folder.setObjectName("actionLoad_Image_Folder")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionLoad_2)
        self.menuImages.addAction(self.actionSave_2)
        self.menuImages.addSeparator()
        self.menuImages.addAction(self.actionLoad_3)
        self.menuImages.addAction(self.actionLoad_Image_Folder)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuImages.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NEFI 2.0"))
        self.menuFile.setTitle(_translate("MainWindow", "Pipe&line"))
        self.menuImages.setTitle(_translate("MainWindow", "Ima&ge"))
        self.PipelineMenu.setText(_translate("MainWindow", "Pipeline"))
        self.PipelineMenu.setToolTip(_translate("MainWindow", "Menuentrys for saving and loading pipelines"))
        self.actionImages.setText(_translate("MainWindow", "Images"))
        self.actionImages.setToolTip(_translate("MainWindow", "Menu for saving and loading images"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionLoad.setToolTip(_translate("MainWindow", "Load a presaved pipeline in json format"))
        self.actionSave.setText(_translate("MainWindow", "&Save"))
        self.actionSave.setToolTip(_translate("MainWindow", "Save the pipeline settings in a json format. You can load your specified Pipeline in later program calls to process the same settings on other images."))
        self.actionLoad_2.setText(_translate("MainWindow", "&Load"))
        self.actionLoad_2.setToolTip(_translate("MainWindow", "Load a presaved Pipeline in json format."))
        self.actionSave_2.setText(_translate("MainWindow", "&Specify Output location"))
        self.actionSave_2.setToolTip(_translate("MainWindow", "Specify the default output location in yout file system. Your processed images and graphs will be stored there after processing."))
        self.actionLoad_3.setText(_translate("MainWindow", "&Load Image"))
        self.actionLoad_3.setToolTip(_translate("MainWindow", "Load a single image file from the file system."))
        self.actionLoad_Image_Folder.setText(_translate("MainWindow", "Load &Image Folder"))
        self.actionLoad_Image_Folder.setToolTip(_translate("MainWindow", "Load a complete folder of images. To display immediate results, the program will use the first image of the folder as default."))

