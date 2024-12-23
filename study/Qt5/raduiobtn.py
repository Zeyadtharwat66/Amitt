from PyQt5 import QtCore, QtGui, QtWidgets
import sys
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.setGeometry(200, 200, 350, 200)
    radio_option1 = QtWidgets.QRadioButton("Option 1", window)
    radio_option1.setGeometry(100, 100, 150, 30)
    radio_option2 = QtWidgets.QRadioButton("Option 2", window)
    radio_option2.setGeometry(100, 130, 150, 30)
    radio_option1.setChecked(True)
    def radio_button_changed():
        if radio_option1.isChecked():
            print("Option 1 selected")
        elif radio_option2.isChecked():
            print("Option 2 selected")
    radio_option1.toggled.connect(radio_button_changed)
    window.show()
    app.exec_()
