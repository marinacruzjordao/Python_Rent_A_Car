from PyQt5 import uic, QtWidgets
from cars_rent_a_car import Cars


class RentACar:
    def __init__(self):
        self.main_window()

    #open main window
    def main_window(self):
        app=QtWidgets.QApplication([])
        self.window_main = uic.loadUi('mainwindow.ui')
        self.window_car_registration = uic.loadUi('car_regs.ui')
        
        #button car registration selection
        self.window_main.pushButton.clicked.connect(self.cars_registration)

        self.window_main.show()
        app.exec()

    #car registration window
    def cars_registration(self):
        self.window_car_registration.show()

        #button registration
        self.window_car_registration.pushButton.clicked.connect(self.car_read_parameters)
       

    #read car parameters 
    def car_read_parameters(self):
        #read parameters
        self.car_brand = self.window_car_registration.lineEdit.text()
        self.car_model = self.window_car_registration.lineEdit_2.text()
        self.car_year = self.window_car_registration.lineEdit_3.text()
        self.car_plate = self.window_car_registration.lineEdit_4.text()
        self.car_kilometers = self.window_car_registration.lineEdit_5.text()
        self.car_level = self.window_car_registration.lineEdit_6.text()
        

        c=Cars(self.car_brand, self.car_model, self.car_year, self.car_plate, self.car_kilometers, self.car_level)
        print(c.testar(1900))
        
        #cars validation
        info, car_status = c.car_parameters_validation()
        print(car_status)

        # validation complete
        if car_status==True:
        
        #colocar na base dados
        else :
            #write information in board
            self.window_car_registration.listWidget.addItem(info)
            self.window_main.listWidget.addItem(info)


c=RentACar()