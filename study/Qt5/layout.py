from PyQt5 import QtCore,QtGui,QtWidgets
import sys
if __name__ =="__main__":
    app = QtWidgets.QApplication(sys.argv) 
    window=QtWidgets.QWidget()
    window.setGeometry(200,200,350,200)
    layout = QtWidgets.QVBoxLayout(window)
    layout.setContentsMargins(0,0,0,0)
    window.show()
    app.exec_()