from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt
from RPi import GPIO 


class Ui_Controller(QWidget):
    def __init__(self):
        super().__init__()
        self.n = 0
        self.LED = 23
        
     
        self.setObjectName("Controller")
        self.resize(683, 320)
        self.setStyleSheet("background-color: rgb(108, 80, 74);\n"
"color: rgb(252, 252, 252);\n"
"alternate-background-color: rgb(250, 250, 250);")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(150, 10, 381, 71))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(270, 230, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(12)

#Pushbutton
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border-color: rgb(11, 11, 11);\n"
"\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Power_on)
        
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(310, 130, 41, 51))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
#Intializing
        
        QtCore.QMetaObject.connectSlotsByName(self)
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Controller", "Controller"))
        self.label.setText(_translate("Controller", "RASPBERRY PI LED_CONTROLLER"))
        self.pushButton.setText(_translate("Controller", "POWER"))
        self.label_2.setText(_translate("Controller", "OFF"))

    def Power_on(self):
        self.n = self.n + 1
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.LED,GPIO.OUT)
        if self.n%2 == 1:
            self.label_2.setText("ON")
            #Hardware Code for lighting UP LED
            GPIO.output(self.LED,GPIO.HIGH)
            
        else:
            self.label_2.setText("OFF")
            #Hardware Code for lighting Down LED
            GPIO.output(self.LED,GPIO.LOW)
            
            
    def keyPressEvent(self,e):
        if e.key() == Qt.Key_L :
            self.Power_on()
    
    def closeEvent(self, event):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.LED,GPIO.OUT)        
        close = QtWidgets.QMessageBox.question(self,"QUIT","Are you sure want to stop process?",QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if close == QtWidgets.QMessageBox.Yes:
            event.accept()
            GPIO.cleanup()
        else:
            event.ignore()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = Ui_Controller()
    ui.show()
    sys.exit(app.exec_())
