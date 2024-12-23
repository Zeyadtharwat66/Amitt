from PyQt5 import QtCore,QtGui,QtWidgets
import sys
class GUI:
    def txt_field(self,parent, x, y, width, height):
        txt = QtWidgets.QLineEdit(parent)
        txt.setGeometry(x, y, width, height)
        txt.setStyleSheet("background-color: white; border: 1px solid blue; border-radius: 10px;")
        return txt
    def btn(self,parent, label,x, y, width, height):
        btn1=QtWidgets.QPushButton(label,parent)
        btn1.setGeometry(x,y,width,height)
        btn1.setStyleSheet('color:white;background-color:black;border:2px solid white;border-radius:30px')
        return btn1
    def check_box(self,label,parent,x,y,width,height):
        chk_option = QtWidgets.QCheckBox(label, parent)
        chk_option.setGeometry(x, y, width, height)
        chk_option.setStyleSheet('background-color:white;border:2px solid red;border-radius:30px')
        return chk_option

    
