# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_webspliceplate.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Webspliceplate(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(279, 174)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.txt_plateHeight = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.txt_plateHeight.setFont(font)
        self.txt_plateHeight.setReadOnly(True)
        self.txt_plateHeight.setObjectName("txt_plateHeight")
        self.gridLayout.addWidget(self.txt_plateHeight, 0, 1, 1, 1)
        self.label_163 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_163.setFont(font)
        self.label_163.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_163.setObjectName("label_163")
        self.gridLayout.addWidget(self.label_163, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.plateHeight_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.plateHeight_2.setFont(font)
        self.plateHeight_2.setObjectName("plateHeight_2")
        self.gridLayout.addWidget(self.plateHeight_2, 0, 0, 1, 1)
        self.txt_plateDemand = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.txt_plateDemand.setFont(font)
        self.txt_plateDemand.setReadOnly(True)
        self.txt_plateDemand.setObjectName("txt_plateDemand")
        self.gridLayout.addWidget(self.txt_plateDemand, 3, 1, 1, 1)
        self.txt_plateWidth = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.txt_plateWidth.setFont(font)
        self.txt_plateWidth.setReadOnly(True)
        self.txt_plateWidth.setObjectName("txt_plateWidth")
        self.gridLayout.addWidget(self.txt_plateWidth, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.txt_plateCapacity = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_plateCapacity.setFont(font)
        self.txt_plateCapacity.setObjectName("txt_plateCapacity")
        self.gridLayout.addWidget(self.txt_plateCapacity, 4, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Web splice plate"))
        self.label_163.setText(_translate("Dialog", "<html><head/><body><p>Demand (kN)</p></body></html>"))
        self.label_3.setText(_translate("Dialog", "Width (mm)"))
        self.plateHeight_2.setText(_translate("Dialog", "Height (mm)"))
        self.label.setText(_translate("Dialog", "Strength"))
        self.label_2.setText(_translate("Dialog", "Capacity (kN)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Webspliceplate()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

