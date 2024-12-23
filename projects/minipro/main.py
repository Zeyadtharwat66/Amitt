from PyQt5 import QtCore,QtGui,QtWidgets
import sys
import numpy as np
from GUI import GUI
from pol_regression import pol_reg
from linear_reg import lin_reg
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import warnings 
warnings.filterwarnings("ignore")
#     C:\D\Amitt\session\Salary_Data.csv
def on_radio_button_select():
    if radio_option2.isChecked():  #Polynomial
        window3.show()
        window2.close()
    elif radio_option1.isChecked():  #Linear
        window4.show()
        window2.close()
pol=None
def on_submit_poly():
    global pol 
    degree = int(degree_txt_P.text())
    train_size = float(train_txt_P.text())
    random_state = int(rand_txt_P.text())
    pol = pol_reg(path_txt.text(), degree, train_size, random_state)
    window3.close()
    window5.show()
        
def make_prediction_pol():
    input_text = data_for_prediction_P.text()  # Extract text from QLineEdit
    prediction = pol.predict(np.array([[float(input_text)]]))
    print("Prediction:", prediction)
    
lin=None
def make_prediction_lin():
    input_text = data_for_prediction_L.text() 
    prediction = lin.predict(np.array([[float(input_text)]]))
    return prediction
def on_submit_linear():
    global lin
    alpha = float(alpha_txt_L.text())
    train_size = float(train_txt_L.text())
    random_state = int(rand_txt_L.text())
    lin = lin_reg(path_txt.text(), alpha, train_size, random_state)
    window4.close()
    lin.performance()
    lblzzz=QtWidgets.QLabel(f"MSE = {lin.mse_train}\nMAE = {lin.r2_test}",window6)
    lblzzz.setGeometry(200, 100, 300, 30)
    lblzzz.setStyleSheet("color:white")
    window6.show()
    print(lin.mse_train)
def the_per():
    lin.performance()
    return (lin.mse_train,lin.r2_train)

if __name__ =="__main__":
    app = QtWidgets.QApplication(sys.argv)
    window1=QtWidgets.QWidget() 
    window1.setGeometry(500,250,400,300)
    window1.setWindowTitle('Project') 
    window1.setStyleSheet('background-color:black')
    x=GUI()
    path_txt = x.txt_field(window1, 100, 50, 200, 30)
    btn1=x.btn(window1,'Next',150,100,100,30)
    lbl=QtWidgets.QLabel("Enter Your file Path",window1)
    lbl.setGeometry(100, 20, 150, 30)
    lbl.setStyleSheet("color:white")
    window2=QtWidgets.QWidget() 
    window2.setGeometry(500,250,400,300)
    window2.setWindowTitle('Select Regression Technique') 
    window2.setStyleSheet('background-color:black')
    btn1.clicked.connect(lambda:(window1.close(),window2.show()))
    lbl2=QtWidgets.QLabel("Choose the Technique you want to use: ",window2)
    lbl2.setGeometry(65, 10, 265, 30) 
    lbl2.setStyleSheet("color:white;font-size:15px;")
    radio_option1 = QtWidgets.QRadioButton("Linear Regression", window2)
    radio_option1.setGeometry(100, 100, 150, 30)
    radio_option1.setStyleSheet("color:white")
    radio_option2 = QtWidgets.QRadioButton("Polynomial Regression", window2)
    radio_option2.setGeometry(100, 150, 150, 30)
    radio_option2.setStyleSheet("color:white")
    btn2=x.btn(window2,'Select Model',150,250,100,30)
    window3=QtWidgets.QWidget() 
    window3.setGeometry(500,250,400,300)
    window3.setWindowTitle('Polynomial Regression') 
    window3.setStyleSheet('background-color:black')
    btn2.clicked.connect(on_radio_button_select)
    degree_txt_P = x.txt_field(window3, 100, 50, 200, 30)
    lb3=QtWidgets.QLabel("Enter Degree",window3)
    lb3.setGeometry(100, 20, 300, 30)
    lb3.setStyleSheet("color:white")
    train_txt_P = x.txt_field(window3, 100, 120, 200, 30)
    lb4=QtWidgets.QLabel("Enter size of data you want to train 'Optional'",window3)
    lb4.setGeometry(100, 90, 300, 30)
    lb4.setStyleSheet("color:white")
    rand_txt_P = x.txt_field(window3, 100, 190, 200, 30) 
    lbl5=QtWidgets.QLabel("Enter Random state you want 'Optional'",window3)
    lbl5.setGeometry(100, 160, 300, 30)
    lbl5.setStyleSheet("color:white")
    submit_btn_P = x.btn(window3,'Submit',150,240,100,30)
    submit_btn_P.clicked.connect(on_submit_poly)
    window5=QtWidgets.QWidget() 
    window5.setGeometry(500,250,400,300)
    window5.setWindowTitle('Predictions') 
    window5.setStyleSheet('background-color:black')
    data_for_prediction_P = x.txt_field(window5, 100, 190, 200, 30)
    submit_btns_P = x.btn(window5,'Submit',150,240,100,30)   
    submit_btns_P.clicked.connect(make_prediction_pol)
    window4=QtWidgets.QWidget() 
    window4.setGeometry(500,250,400,300)
    window4.setWindowTitle('Linear Regression') 
    window4.setStyleSheet('background-color:black')
    alpha_txt_L = x.txt_field(window4, 100, 50, 200, 30)
    lb6=QtWidgets.QLabel("Enter Alpha",window4)
    lb6.setGeometry(100, 20, 300, 30)
    lb6.setStyleSheet("color:white")
    train_txt_L = x.txt_field(window4, 100, 120, 200, 30)
    lb7=QtWidgets.QLabel("Enter size of data you want to train 'Optional'",window4)
    lb7.setGeometry(100, 90, 300, 30)
    lb7.setStyleSheet("color:white")
    rand_txt_L = x.txt_field(window4, 100, 190, 200, 30) 
    lbl8=QtWidgets.QLabel("Enter Random state you want 'Optional'",window4)
    lbl8.setGeometry(100, 160, 300, 30)
    lbl8.setStyleSheet("color:white")
    submit_btn_L = x.btn(window4,'Submit',150,240,100,30)
    submit_btn_L.clicked.connect(on_submit_linear)
    window6=QtWidgets.QWidget()
    window6.setGeometry(500,250,550,300)
    window6.setWindowTitle('Predictions') 
    window6.setStyleSheet('background-color:black')
    lblpred=QtWidgets.QLabel(f"House Price Prediction : ",window6)
    lblpred.setGeometry(3, 30 , 1000, 500)
    lblpred.setStyleSheet("color:white;font-weight:bold;font-size:20px;")
    data_for_prediction_L = x.txt_field(window6, 140, 160, 235, 30)
    submit_btns_L = x.btn(window6,'Submit',140,200,235,30)
    def predict_and_update_label():
        prediction = make_prediction_lin()  # Call the prediction function
        if prediction is not None:
            lblpred.setText(f"House Price Prediction: {prediction} $")
            lblpred.show()  # Ensure the label is visible
        else:
            lblpred.setText("Error in prediction. Check input and model.")
            lblpred.setStyleSheet("color: red") 
    
    submit_btns_L.clicked.connect(predict_and_update_label)
    
    window1.show()
    app.exec_() 