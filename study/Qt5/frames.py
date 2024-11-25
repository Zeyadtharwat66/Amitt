from PyQt5 import QtCore,QtGui,QtWidgets
import sys
if __name__ =="__main__":
    app = QtWidgets.QApplication(sys.argv) 
    window=QtWidgets.QWidget()
    window.setGeometry(200,200,350,200)
    frame = QtWidgets.QFrame(window)
    frame.setFrameShape(frame.StyledPanel)
    frame.setGeometry(30, 30, 100, 100)
    frame.setStyleSheet("background-color: #f0f0f0;border: 1px solid green;border-radius:20px")
    window.show()
    app.exec_()