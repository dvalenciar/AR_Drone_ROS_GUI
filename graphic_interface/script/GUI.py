# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created: Fri Jan 25 14:49:57 2019
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(916, 344)
        MainWindow.setMaximumSize(QtCore.QSize(1040, 640))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_7 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.Take_Off_Button = QtGui.QPushButton(self.centralwidget)
        self.Take_Off_Button.setStyleSheet(_fromUtf8("background-color: rgb(175, 0, 0);\n"
"color: rgb(255, 255, 255);"))
        self.Take_Off_Button.setObjectName(_fromUtf8("Take_Off_Button"))
        self.gridLayout_5.addWidget(self.Take_Off_Button, 0, 1, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.Right_Button = QtGui.QPushButton(self.centralwidget)
        self.Right_Button.setObjectName(_fromUtf8("Right_Button"))
        self.gridLayout_2.addWidget(self.Right_Button, 1, 2, 1, 1)
        self.Up_Button = QtGui.QPushButton(self.centralwidget)
        self.Up_Button.setObjectName(_fromUtf8("Up_Button"))
        self.gridLayout_2.addWidget(self.Up_Button, 0, 1, 1, 1)
        self.Left_Button = QtGui.QPushButton(self.centralwidget)
        self.Left_Button.setObjectName(_fromUtf8("Left_Button"))
        self.gridLayout_2.addWidget(self.Left_Button, 1, 0, 1, 1)
        self.Down_Button = QtGui.QPushButton(self.centralwidget)
        self.Down_Button.setObjectName(_fromUtf8("Down_Button"))
        self.gridLayout_2.addWidget(self.Down_Button, 2, 1, 1, 1)
        self.Stop_Button = QtGui.QPushButton(self.centralwidget)
        self.Stop_Button.setObjectName(_fromUtf8("Stop_Button"))
        self.gridLayout_2.addWidget(self.Stop_Button, 1, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 3, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem, 4, 1, 1, 1)
        self.Land_Button = QtGui.QPushButton(self.centralwidget)
        self.Land_Button.setStyleSheet(_fromUtf8("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);"))
        self.Land_Button.setObjectName(_fromUtf8("Land_Button"))
        self.gridLayout_5.addWidget(self.Land_Button, 5, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem1, 1, 1, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.Rotate_Right_Button = QtGui.QPushButton(self.centralwidget)
        self.Rotate_Right_Button.setObjectName(_fromUtf8("Rotate_Right_Button"))
        self.gridLayout.addWidget(self.Rotate_Right_Button, 1, 2, 1, 1)
        self.Front_Button = QtGui.QPushButton(self.centralwidget)
        self.Front_Button.setObjectName(_fromUtf8("Front_Button"))
        self.gridLayout.addWidget(self.Front_Button, 0, 1, 1, 1)
        self.Rotate_Left_Button = QtGui.QPushButton(self.centralwidget)
        self.Rotate_Left_Button.setObjectName(_fromUtf8("Rotate_Left_Button"))
        self.gridLayout.addWidget(self.Rotate_Left_Button, 1, 0, 1, 1)
        self.Back_Button = QtGui.QPushButton(self.centralwidget)
        self.Back_Button.setObjectName(_fromUtf8("Back_Button"))
        self.gridLayout.addWidget(self.Back_Button, 2, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout, 3, 0, 1, 1)
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.Velocity_Slider = QtGui.QSlider(self.centralwidget)
        self.Velocity_Slider.setMaximum(10)
        self.Velocity_Slider.setProperty("value", 1)
        self.Velocity_Slider.setOrientation(QtCore.Qt.Vertical)
        self.Velocity_Slider.setObjectName(_fromUtf8("Velocity_Slider"))
        self.gridLayout_6.addWidget(self.Velocity_Slider, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_6, 3, 1, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_5.addWidget(self.label, 2, 1, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout.addWidget(self.label_12)
        self.lcd_Altitude = QtGui.QLCDNumber(self.centralwidget)
        self.lcd_Altitude.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);"))
        self.lcd_Altitude.setObjectName(_fromUtf8("lcd_Altitude"))
        self.verticalLayout.addWidget(self.lcd_Altitude)
        self.gridLayout_5.addLayout(self.verticalLayout, 6, 2, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.lineEdit_Y = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_Y.setObjectName(_fromUtf8("lineEdit_Y"))
        self.gridLayout_3.addWidget(self.lineEdit_Y, 2, 1, 1, 1)
        self.lineEdit_X = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_X.setObjectName(_fromUtf8("lineEdit_X"))
        self.gridLayout_3.addWidget(self.lineEdit_X, 2, 0, 1, 1)
        self.lineEdit_Yaw = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_Yaw.setObjectName(_fromUtf8("lineEdit_Yaw"))
        self.gridLayout_3.addWidget(self.lineEdit_Yaw, 2, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setIndent(91)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setIndent(91)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_3.addWidget(self.label_13, 1, 1, 1, 1)
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setIndent(80)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_3.addWidget(self.label_14, 1, 2, 1, 1)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setMargin(0)
        self.label_7.setIndent(25)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 6, 0, 1, 2)
        self.gridLayout_7.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 916, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "GUI", None))
        self.Take_Off_Button.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>", None))
        self.Take_Off_Button.setText(_translate("MainWindow", "Take Off", None))
        self.Right_Button.setText(_translate("MainWindow", "Right", None))
        self.Up_Button.setText(_translate("MainWindow", "Up", None))
        self.Left_Button.setText(_translate("MainWindow", "Left", None))
        self.Down_Button.setText(_translate("MainWindow", "Down", None))
        self.Stop_Button.setText(_translate("MainWindow", "STOP", None))
        self.Land_Button.setText(_translate("MainWindow", "Land", None))
        self.Rotate_Right_Button.setText(_translate("MainWindow", "Rotate Right", None))
        self.Front_Button.setText(_translate("MainWindow", "Front", None))
        self.Rotate_Left_Button.setText(_translate("MainWindow", "Rotate Left", None))
        self.Back_Button.setText(_translate("MainWindow", "Back", None))
        self.label.setText(_translate("MainWindow", "Speed Control", None))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Altitude</p></body></html>", None))
        self.label_6.setText(_translate("MainWindow", "X", None))
        self.label_13.setText(_translate("MainWindow", "Y", None))
        self.label_14.setText(_translate("MainWindow", "Yaw", None))
        self.label_7.setText(_translate("MainWindow", "Position", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

