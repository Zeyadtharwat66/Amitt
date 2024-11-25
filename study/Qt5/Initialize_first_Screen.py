from PyQt5 import QtCore,QtGui,QtWidgets
import sys
if __name__ =="__main__":
    app = QtWidgets.QApplication(sys.argv) #initialize the application
    window=QtWidgets.QWidget() #Initialize the window
    # window.resize(350,200) #width,height size of window
    # window.move(100,150)#left,top distance of window
    window.setGeometry(100,150,350,200)#Do the same thing move and resize do both at same time -> left,top,width,height
    window.setWindowTitle('Zeyad First Screen') #Title in the bar of the window
    window.setStyleSheet('background-color:red')#css codes
    window.setWindowIcon(QtGui.QIcon(r'C:\Users\pc\Downloads\ahly.png'))#Set Icon to the window
    window.show() #shows window but it closes itself "Needs app excution"
    app.exec_() #For Excuting the application
