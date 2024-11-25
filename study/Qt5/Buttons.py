from PyQt5 import QtCore,QtGui,QtWidgets
import sys
if __name__ =="__main__":
    app = QtWidgets.QApplication(sys.argv) 
    window=QtWidgets.QWidget()
    window.setGeometry(200,200,350,200)
    btn1=QtWidgets.QPushButton('Zeyad',window)
    btn1.setGeometry(100,50,150,50) #There is move and resize functions also available
    btn1.setStyleSheet('background-color:red;color:blue;font-size:20px;border:2px solid black;border-radius:20px')
    btn1.setToolTip("Do u know me ?") #appears when hover the btn1 "Appears with same style of btn"
    btn2=QtWidgets.QPushButton('Tharwat',window)
    btn2.setGeometry(100,102,150,50)
    btn2.setStyleSheet('background-color:blue;color:red;border:2px dashed black;border-radius:20px')
    btn2.setIcon(QtGui.QIcon(r'C:\Users\pc\Downloads\ahly.png'))
    btn2.setToolTip("Do u know me ?") 
    btn3=QtWidgets.QPushButton('Exit',window)
    btn3.setGeometry(100,154,150,50)
    btn3.setStyleSheet('border:2px solid red;border-radius:20px;background-color:black;color:white')
    btn3.setToolTip('Exit the application')
    btn3.clicked.connect(exit)
    window.show()
    app.exec_()