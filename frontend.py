from PyQt5 import QtCore, QtWidgets
from assets import retry

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 390)
        Form.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.Biglabel = QtWidgets.QLabel(Form)
        self.Biglabel.setGeometry(QtCore.QRect(30, 60, 571, 31))
        self.Biglabel.setObjectName("Biglabel")
        self.smalllabel = QtWidgets.QLabel(Form)
        self.smalllabel.setGeometry(QtCore.QRect(70, 120, 481, 21))
        self.smalllabel.setObjectName("smalllabel")
        self.mainlabel = QtWidgets.QLabel(Form)
        self.mainlabel.setGeometry(QtCore.QRect(60, 180, 511, 171))
        self.mainlabel.setStyleSheet("background-color: rgb(85, 87, 83);\n"
"border-radius:20px;")
        self.mainlabel.setText("")
        self.mainlabel.setObjectName("mainlabel")
        self.Output = QtWidgets.QLabel(Form)
        self.Output.setGeometry(QtCore.QRect(70, 190, 401, 31))
        self.Output.setStyleSheet("background-color: rgb(85, 87, 83);")
        self.Output.setObjectName("Output")
        self.slider = QtWidgets.QSlider(Form)
        self.slider.setGeometry(QtCore.QRect(190, 255, 291, 16))
        self.slider.setMouseTracking(True)
        self.slider.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.slider.setMaximum(20)
        self.slider.setPageStep(1)
        self.slider.setSliderPosition(10)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setInvertedControls(False)
        self.slider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.slider.setTickInterval(1)
        self.slider.setObjectName("slider")
        self.passlength = QtWidgets.QLabel(Form)
        self.passlength.setGeometry(QtCore.QRect(70, 250, 111, 21))
        self.passlength.setStyleSheet("background-color: rgb(85, 87, 83);")
        self.passlength.setObjectName("passlength")
        self.line2 = QtWidgets.QFrame(Form)
        self.line2.setGeometry(QtCore.QRect(80, 290, 471, 2))
        self.line2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line2.setObjectName("line2")
        self.uppercase = QtWidgets.QCheckBox(Form)
        self.uppercase.setGeometry(QtCore.QRect(70, 310, 92, 23))
        self.uppercase.setStyleSheet("background-color: rgb(85, 87, 83);\n"
"color:white")
        self.uppercase.setChecked(True)
        self.uppercase.setObjectName("uppercase")
        self.lowercase = QtWidgets.QCheckBox(Form)
        self.lowercase.setGeometry(QtCore.QRect(180, 310, 92, 23))
        self.lowercase.setStyleSheet("background-color: rgb(85, 87, 83);\n"
"color:white")
        self.lowercase.setChecked(True)
        self.lowercase.setObjectName("lowercase")
        self.digit = QtWidgets.QCheckBox(Form)
        self.digit.setGeometry(QtCore.QRect(310, 310, 81, 23))
        self.digit.setStyleSheet("background-color: rgb(85, 87, 83);\n"
"color:white")
        self.digit.setChecked(True)
        self.digit.setObjectName("digit")
        self.specSymbol = QtWidgets.QCheckBox(Form)
        self.specSymbol.setGeometry(QtCore.QRect(410, 310, 131, 23))
        self.specSymbol.setStyleSheet("background-color: rgb(85, 87, 83);\n"
"color:white")
        self.specSymbol.setChecked(True)
        self.specSymbol.setObjectName("specSymbol")
        self.line1 = QtWidgets.QFrame(Form)
        self.line1.setGeometry(QtCore.QRect(80, 230, 471, 2))
        self.line1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line1.setObjectName("line1")
        self.number = QtWidgets.QLabel(Form)
        self.number.setGeometry(QtCore.QRect(490, 247, 67, 31))
        self.number.setStyleSheet("background-color: rgb(85, 87, 83);\n"
"color:white;")
        self.number.setObjectName("number")
        self.retry = QtWidgets.QPushButton(Form)
        self.retry.setGeometry(QtCore.QRect(490, 190, 31, 31))
        self.retry.setStyleSheet("QPushButton{\n"
"    border-image: url(:/newPrefix/retry.png);\n"
"}\n"
"QpushButton:hover{\n"
"background-color: rgb(186, 189, 182);\n"
"}")
        self.retry.setText("")
        self.retry.setObjectName("retry")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Biglabel.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600; color:#ffffff;\">Strong Password Generate</span></p></body></html>"))
        self.smalllabel.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#ffffff;\">Create a Strong unique Password</span></p></body></html>"))
        self.Output.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">output</span></p></body></html>"))
        self.passlength.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">Password length</span></p></body></html>"))
        self.uppercase.setText(_translate("Form", "uppercase"))
        self.lowercase.setText(_translate("Form", "Lowercase"))
        self.digit.setText(_translate("Form", "Digit"))
        self.specSymbol.setText(_translate("Form", "Special Symbol"))
        self.number.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#ffffff;\">10</span></p></body></html>"))





    
