# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_stiffener.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class ui_stiffener(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(620, 276)
        self.txt_stiffnrHeight = QtWidgets.QLineEdit(Dialog)
        self.txt_stiffnrHeight.setGeometry(QtCore.QRect(179, 27, 118, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.txt_stiffnrHeight.setFont(font)
        self.txt_stiffnrHeight.setReadOnly(True)
        self.txt_stiffnrHeight.setObjectName("txt_stiffnrHeight")
        self.plateHeight = QtWidgets.QLabel(Dialog)
        self.plateHeight.setGeometry(QtCore.QRect(9, 27, 83, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.plateHeight.setFont(font)
        self.plateHeight.setObjectName("plateHeight")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(9, 60, 85, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txt_stiffnrWidth = QtWidgets.QLineEdit(Dialog)
        self.txt_stiffnrWidth.setGeometry(QtCore.QRect(179, 60, 118, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.txt_stiffnrWidth.setFont(font)
        self.txt_stiffnrWidth.setReadOnly(True)
        self.txt_stiffnrWidth.setObjectName("txt_stiffnrWidth")
        self.label_163 = QtWidgets.QLabel(Dialog)
        self.label_163.setGeometry(QtCore.QRect(9, 90, 104, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_163.setFont(font)
        self.label_163.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_163.setObjectName("label_163")
        self.txt_stiffnrThickness = QtWidgets.QLineEdit(Dialog)
        self.txt_stiffnrThickness.setGeometry(QtCore.QRect(179, 90, 118, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.txt_stiffnrThickness.setFont(font)
        self.txt_stiffnrThickness.setReadOnly(True)
        self.txt_stiffnrThickness.setObjectName("txt_stiffnrThickness")
        self.txt_stiffnrMomentDemand = QtWidgets.QLineEdit(Dialog)
        self.txt_stiffnrMomentDemand.setGeometry(QtCore.QRect(180, 120, 118, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.txt_stiffnrMomentDemand.setFont(font)
        self.txt_stiffnrMomentDemand.setReadOnly(True)
        self.txt_stiffnrMomentDemand.setObjectName("txt_stiffnrMomentDemand")
        self.label_164 = QtWidgets.QLabel(Dialog)
        self.label_164.setGeometry(QtCore.QRect(10, 120, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_164.setFont(font)
        self.label_164.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_164.setObjectName("label_164")
        self.txt_stiffnrMomenCapacity = QtWidgets.QLineEdit(Dialog)
        self.txt_stiffnrMomenCapacity.setGeometry(QtCore.QRect(180, 150, 118, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.txt_stiffnrMomenCapacity.setFont(font)
        self.txt_stiffnrMomenCapacity.setReadOnly(True)
        self.txt_stiffnrMomenCapacity.setObjectName("txt_stiffnrMomenCapacity")
        self.label_165 = QtWidgets.QLabel(Dialog)
        self.label_165.setGeometry(QtCore.QRect(10, 150, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_165.setFont(font)
        self.label_165.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_165.setObjectName("label_165")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(320, 20, 281, 241))
        self.widget.setObjectName("widget")
        self.label_166 = QtWidgets.QLabel(Dialog)
        self.label_166.setGeometry(QtCore.QRect(10, 180, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_166.setFont(font)
        self.label_166.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_166.setObjectName("label_166")
        self.txt_stiffnrShearDemand = QtWidgets.QLineEdit(Dialog)
        self.txt_stiffnrShearDemand.setGeometry(QtCore.QRect(180, 180, 118, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.txt_stiffnrShearDemand.setFont(font)
        self.txt_stiffnrShearDemand.setReadOnly(True)
        self.txt_stiffnrShearDemand.setObjectName("txt_stiffnrShearDemand")
        self.label_167 = QtWidgets.QLabel(Dialog)
        self.label_167.setGeometry(QtCore.QRect(10, 210, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_167.setFont(font)
        self.label_167.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_167.setObjectName("label_167")
        self.txt_stiffnrShearCapacity = QtWidgets.QLineEdit(Dialog)
        self.txt_stiffnrShearCapacity.setGeometry(QtCore.QRect(180, 210, 118, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.txt_stiffnrShearCapacity.setFont(font)
        self.txt_stiffnrShearCapacity.setReadOnly(True)
        self.txt_stiffnrShearCapacity.setObjectName("txt_stiffnrShearCapacity")
        self.txt_stiffnrNotchSize = QtWidgets.QLineEdit(Dialog)
        self.txt_stiffnrNotchSize.setGeometry(QtCore.QRect(180, 240, 118, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.txt_stiffnrNotchSize.setFont(font)
        self.txt_stiffnrNotchSize.setReadOnly(True)
        self.txt_stiffnrNotchSize.setObjectName("txt_stiffnrNotchSize")
        self.label_168 = QtWidgets.QLabel(Dialog)
        self.label_168.setGeometry(QtCore.QRect(10, 240, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_168.setFont(font)
        self.label_168.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_168.setObjectName("label_168")
        self.txt_stiffnrHeight.raise_()
        self.plateHeight.raise_()
        self.label_2.raise_()
        self.txt_stiffnrWidth.raise_()
        self.label_163.raise_()
        self.txt_stiffnrThickness.raise_()
        self.txt_stiffnrMomentDemand.raise_()
        self.txt_stiffnrMomenCapacity.raise_()
        self.label_165.raise_()
        self.label_164.raise_()
        self.widget.raise_()
        self.label_166.raise_()
        self.txt_stiffnrShearDemand.raise_()
        self.label_167.raise_()
        self.txt_stiffnrShearCapacity.raise_()
        self.txt_stiffnrNotchSize.raise_()
        self.label_168.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Stiffener"))
        self.plateHeight.setText(_translate("Dialog", "Height (mm)"))
        self.label_2.setText(_translate("Dialog", "Width (mm)"))
        self.label_163.setText(_translate("Dialog", "<html><head/><body><p>Thickness (mm)</p></body></html>"))
        self.label_164.setText(_translate("Dialog", "<html><head/><body><p>Moment demand (kNm)</p></body></html>"))
        self.label_165.setText(_translate("Dialog", "<html><head/><body><p>Moment capacity (kNm)</p></body></html>"))
        self.label_166.setText(_translate("Dialog", "<html><head/><body><p>Shear Demand (kN)</p></body></html>"))
        self.label_167.setText(_translate("Dialog", "<html><head/><body><p>Shear Capacity (kN)</p></body></html>"))
        self.label_168.setText(_translate("Dialog", "<html><head/><body><p>Notch Size (mm)</p></body></html>"))
