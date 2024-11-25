from PyQt5 import QtCore,QtGui,QtWidgets
import sys
if __name__ =="__main__":
    app = QtWidgets.QApplication(sys.argv) 
    window=QtWidgets.QWidget()
    window.setGeometry(200,200,350,200)
    txt_username = QtWidgets.QLineEdit(window)
    txt_username.setGeometry(200, 150, 200, 30)
    txt_username.setStyleSheet("background-color: white; border: 1px solid blue; border-radius: 10px;")
    print(txt_username.text())
    window.show()
    app.exec_()