# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_App_Calc(object):
    def setupUi(self, App_Calc):
        App_Calc.setObjectName("App_Calc")
        App_Calc.resize(340, 330)
        App_Calc.setMinimumSize(QtCore.QSize(340, 330))
        App_Calc.setMaximumSize(QtCore.QSize(340, 330))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        App_Calc.setFont(font)
        App_Calc.setStyleSheet("background-color: rgb(255, 255, 200);")
        self.Calculator = QtWidgets.QWidget(App_Calc)
        self.Calculator.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Calculator.sizePolicy().hasHeightForWidth())
        self.Calculator.setSizePolicy(sizePolicy)
        self.Calculator.setObjectName("Calculator")
        self.layoutWidget = QtWidgets.QWidget(self.Calculator)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 70, 320, 256))
        self.layoutWidget.setAutoFillBackground(False)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(4)
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.b_2 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(25)
        self.b_2.setFont(font)
        self.b_2.setStyleSheet("background-color: rgb(200, 100, 0);\n"
"color: rgb(255, 255, 130);\n")
        self.b_2.setObjectName("b_2")
        self.gridLayout.addWidget(self.b_2, 3, 1, 1, 1)
        self.b_8 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(25)
        self.b_8.setFont(font)
        self.b_8.setStyleSheet("background-color: rgb(200, 100, 0);\n"
"color: rgb(255, 255, 130);\n")
        self.b_8.setObjectName("b_8")
        self.gridLayout.addWidget(self.b_8, 1, 1, 1, 1)
        self.b_subtr = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b_subtr.setFont(font)
        self.b_subtr.setStyleSheet("background-color: rgb(200, 100, 0);\n"
"color: rgb(30, 30, 30);\n")
        self.b_subtr.setObjectName("b_subtr")
        self.gridLayout.addWidget(self.b_subtr, 2, 3, 1, 1)
        self.b_mr = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(25)
        self.b_mr.setFont(font)
        self.b_mr.setStyleSheet("background-color: rgb(200, 100, 0);\n"
"color: rgb(30, 30, 30);\n")
        self.b_mr.setObjectName("b_mr")
        self.gridLayout.addWidget(self.b_mr, 0, 1, 1, 1)
        self.b_m = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(25)
        self.b_m.setFont(font)
        self.b_m.setStyleSheet("background-color: rgb(200, 100, 0);\n"
"color: rgb(30, 30, 30);")
        self.b_m.setDefault(False)
        self.b_m.setFlat(False)
        self.b_m.setObjectName("b_m")
        self.gridLayout.addWidget(self.b_m, 0, 0, 1, 1)
        self.b_5 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(25)
        self.b_5.setFont(font)
        self.b_5.setStyleSheet("background-color: rgb(200, 100, 0);\n"
"color: rgb(255, 255, 130);\n")
        self.b_5.setObjectName("b_5")
        self.gridLayout.addWidget(self.b_5, 2, 1, 1, 1)
        self.b_0 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        self.b_0.setFont(font)
        self.b_0.setStyleSheet("background-color: rgb(200, 100, 0);\n"
"color: rgb(255, 255, 130);\n")
        self.b_0.setObjectName("b_0")
        self.gridLayout.addWidget(self.b_0, 4, 1, 1, 1)
        self.b_equals = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b_equals.setFont(font)
        self.b_equals.setToolTipDuration(-1)
        self.b_equals.setAutoFillBackground(False)
        self.b_equals.setStyleSheet("background-color: rgb(200, 100, 0);\n"
"color: rgb(30, 30, 30);")
        self.b_equals.setObjectName("b_equals")
        self.gridLayout.addWidget(self.b_equals, 4, 3, 1, 1)
        self.b_6 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(25)
        self.b_6.setFont(font)
        self.b_6.setStyleSheet("background-color: rgb(200, 100, 0);\n"
"color: rgb(255, 255, 130);\n")
        self.b_6.setObjectName("b_6")
        self.gridLayout.addWidget(self.b_6, 2, 2, 1, 1)
        self.b_7 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(25)
        self.b_7.setFont(font)
        self.b_7.setStyleSheet("background-color: rgb(200, 100, 0);\n"
"color: rgb(255, 255, 130);\n")
        self.b_7.setObjectName("b_7")
        self.gridLayout.addWidget(self.b_7, 1, 0, 1, 1)
        self.b_01 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        self.b_01.setFont(font)
        self.b_01.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.b_01.setAutoFillBackground(False)
        self.b_01.setStyleSheet("background-color: rgb(200, 100, 0);\n"
"color: rgb(255, 255, 130);\n")
        self.b_01.setObjectName("b_01")
        self.gridLayout.addWidget(self.b_01, 4, 2, 1, 1)
        self.b_3 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(25)
        self.b_3.setFont(font)
        self.b_3.setStyleSheet("background-color: rgb(200, 100, 0);\n"
"color: rgb(255, 255, 130);\n")
        self.b_3.setObjectName("b_3")
        self.gridLayout.addWidget(self.b_3, 3, 2, 1, 1)
        self.b_9 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(25)
        self.b_9.setFont(font)
        self.b_9.setStyleSheet("background-color: rgb(200, 100, 0);\n"
"color: rgb(255, 255, 130);\n")
        self.b_9.setObjectName("b_9")
        self.gridLayout.addWidget(self.b_9, 1, 2, 1, 1)
        self.b_plus = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(25)
        self.b_plus.setFont(font)
        self.b_plus.setStyleSheet("background-color: rgb(200, 100, 0);\n"
"color: rgb(30, 30, 30);\n")
        self.b_plus.setObjectName("b_plus")
        self.gridLayout.addWidget(self.b_plus, 3, 3, 1, 1)
        self.b_4 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(25)
        self.b_4.setFont(font)
        self.b_4.setStyleSheet("background-color: rgb(200, 100, 0);\n"
"color: rgb(255, 255, 130);\n")
        self.b_4.setObjectName("b_4")
        self.gridLayout.addWidget(self.b_4, 2, 0, 1, 1)
        self.b_multiply = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(25)
        self.b_multiply.setFont(font)
        self.b_multiply.setStyleSheet("background-color: rgb(200, 100, 0);\n"
"color: rgb(30, 30, 30);")
        self.b_multiply.setObjectName("b_multiply")
        self.gridLayout.addWidget(self.b_multiply, 0, 3, 1, 1)
        self.b_1 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(25)
        self.b_1.setFont(font)
        self.b_1.setStyleSheet("background-color: rgb(200, 100, 0);\n"
"color: rgb(255, 255, 130);\n")
        self.b_1.setObjectName("b_1")
        self.gridLayout.addWidget(self.b_1, 3, 0, 1, 1)
        self.b_percent = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(25)
        self.b_percent.setFont(font)
        self.b_percent.setStyleSheet("background-color: rgb(200, 100, 0);\n"
"color: rgb(30, 30, 30);")
        self.b_percent.setObjectName("b_percent")
        self.gridLayout.addWidget(self.b_percent, 0, 2, 1, 1)
        self.b_c = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b_c.setFont(font)
        self.b_c.setStyleSheet("background-color: rgb(200, 100, 0);\n"
"color: rgb(30, 30, 30);\n")
        self.b_c.setObjectName("b_c")
        self.gridLayout.addWidget(self.b_c, 4, 0, 1, 1)
        self.b_divide = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b_divide.setFont(font)
        self.b_divide.setStyleSheet("background-color: rgb(200, 100, 0);\n"
"color: rgb(30, 30, 30);")
        self.b_divide.setObjectName("b_divide")
        self.gridLayout.addWidget(self.b_divide, 1, 3, 1, 1)
        self.numbers = QtWidgets.QLCDNumber(self.Calculator)
        self.numbers.setEnabled(False)
        self.numbers.setGeometry(QtCore.QRect(10, 10, 320, 55))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        self.numbers.setFont(font)
        self.numbers.setToolTipDuration(0)
        self.numbers.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.numbers.setAutoFillBackground(False)
        self.numbers.setStyleSheet("color: rgb(255, 255, 127);\n"
"background-color: rgb(200, 100, 0);")
        self.numbers.setLineWidth(1)
        self.numbers.setMidLineWidth(1)
        self.numbers.setDigitCount(13)
        self.numbers.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.numbers.setProperty("value", 0.0)
        self.numbers.setObjectName("numbers")
        App_Calc.setCentralWidget(self.Calculator)

        self.retranslateUi(App_Calc)
        QtCore.QMetaObject.connectSlotsByName(App_Calc)

    def retranslateUi(self, App_Calc):
        _translate = QtCore.QCoreApplication.translate
        App_Calc.setWindowTitle(_translate("App_Calc", "????????????????"))
        self.b_2.setText(_translate("App_Calc", "2"))
        self.b_8.setText(_translate("App_Calc", "8"))
        self.b_subtr.setText(_translate("App_Calc", "-"))
        self.b_mr.setText(_translate("App_Calc", "MR"))
        self.b_m.setText(_translate("App_Calc", "M"))
        self.b_5.setText(_translate("App_Calc", "5"))
        self.b_0.setText(_translate("App_Calc", "0"))
        self.b_equals.setText(_translate("App_Calc", "="))
        self.b_6.setText(_translate("App_Calc", "6"))
        self.b_7.setText(_translate("App_Calc", "7"))
        self.b_01.setText(_translate("App_Calc", "0.1"))
        self.b_3.setText(_translate("App_Calc", "3"))
        self.b_9.setText(_translate("App_Calc", "9"))
        self.b_plus.setText(_translate("App_Calc", "+"))
        self.b_4.setText(_translate("App_Calc", "4"))
        self.b_multiply.setText(_translate("App_Calc", "x"))
        self.b_1.setText(_translate("App_Calc", "1"))
        self.b_percent.setText(_translate("App_Calc", "%"))
        self.b_c.setText(_translate("App_Calc", "C"))
        self.b_divide.setText(_translate("App_Calc", "??"))
        self.numbers.setToolTip(_translate("App_Calc", "<html><head/><body><p align=\"right\">0</p></body></html>"))
        self.numbers.setWhatsThis(_translate("App_Calc", "<html><head/><body><p align=\"right\">0</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    App_Calc = QtWidgets.QMainWindow()
    ui = Ui_App_Calc()
    ui.setupUi(App_Calc)
    App_Calc.show()
    sys.exit(app.exec_())
