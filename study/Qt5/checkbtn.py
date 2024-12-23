from PyQt5 import QtCore, QtGui, QtWidgets
import sys
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.setGeometry(200, 200, 350, 200)
    chk_option = QtWidgets.QCheckBox("Accept Terms and Conditions", window)
    chk_option.setGeometry(100, 100, 200, 30)
    def checkbox_changed():
        if chk_option.isChecked():
            print("Checkbox is checked")
        else:
            print("Checkbox is unchecked")
    chk_option.toggled.connect(checkbox_changed)
    window.show()
    app.exec_()
