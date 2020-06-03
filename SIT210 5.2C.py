from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(14, GPIO.OUT)

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()
        
    def button_clicked(self):
        self.label.setText("you pressed button red")
        self.update()
        GPIO.output(10, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(10, GPIO.LOW)

    def button_clicked2(self):
        self.label.setText("you pressed button green")
        self.update()
        GPIO.output(12, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(12, GPIO.LOW)

    def button_clicked3(self):
        self.label.setText("you pressed button blue")
        self.update()
        GPIO.output(14, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(14, GPIO.LOW)

    def initUI(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Tech With Anlan")

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Buttons")
        self.label.move(10,10)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("button 1")
        self.b1.clicked.connect(self.button_clicked)
        self.b1.move(60,60)

        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("button 2")
        self.b2.clicked.connect(self.button_clicked2)
        self.b2.move(80,80)

        self.b3 = QtWidgets.QPushButton(self)
        self.b3.setText("button 3")
        self.b3.clicked.connect(self.button_clicked3)
        self.b3.move(100,100)

    def update(self):
        self.label.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()
