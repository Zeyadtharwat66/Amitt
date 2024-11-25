from PyQt5 import QtCore,QtGui,QtWidgets
import sys
if __name__ =="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=QtWidgets.QWidget()
    window.setGeometry(100,150,350,200)
    lbl1=QtWidgets.QLabel("<u>Zeyad Tharwat Soliman</u>",window)
    lbl1.move(100,25)
    lbl1.setStyleSheet('color:red;font-size:16px;font-familt:tajawal;')
    lbl2=QtWidgets.QLabel("<b>Zeyad Tharwat Soliman</b>",window)
    lbl2.move(100,45)
    lbl3=QtWidgets.QLabel("<i>Zeyad tharwat</i>",window)
    lbl3.move(100,65)
    z=''''
    Our Names are:
    1- Zeyad
            2- Omar
    3- Adel
            4- Mostafa
    '''
    lbl4=QtWidgets.QLabel(z,window)
    lbl4.move(190,90)
    window.show()
    app.exec_()
    