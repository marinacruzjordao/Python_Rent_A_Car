from PyQt5 import uic, QtWidgets
from cars_rent_a_car import Cars
from clients_rent_a_car import Clients
from rent_rent_a_car import Rents


class RentACar:
    def __init__(self):
        self.main_window()

    #open main window
    def main_window(self):
        app=QtWidgets.QApplication([])
        self.window_main = uic.loadUi('mainwindow.ui')
        self.window_car_registration = uic.loadUi('car_regs.ui')
        self.window_car_delete = uic.loadUi('car_delete.ui')
        self.window_client_registration = uic.loadUi('client_regs.ui')
        self.window_client_delete = uic.loadUi('client_delete.ui')
        self.window_rent_registration = uic.loadUi('rent_regs.ui')


        #button car registration 
        self.window_main.pushButton.clicked.connect(self.cars_registration)

        #button client registration
        self.window_main.pushButton_2.clicked.connect(self.client_registration)

        #button client list
        self.window_main.pushButton_4.clicked.connect(self.clients_list)

        #button car list
        self.window_main.pushButton_5.clicked.connect(self.car_list)
        
        #button delete client 
        self.window_main.pushButton_7.clicked.connect(self.client_delete) 

        #button delete car 
        self.window_main.pushButton_8.clicked.connect(self.car_delete) 

        #button rent registration
        self.window_main.pushButton_3.clicked.connect(self.rent_registration) 

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
        
        #cars validation
        info_car_val, car_status = c.car_parameters_validation()

        # validation complete
        if car_status==True:
            #insert data in data base
            info_db_car = c.cars_add_data_base()
            #write information to the board
            self.window_car_registration.listWidget.addItem(info_db_car)
            self.window_main.listWidget.addItem(info_db_car)
        else : #if not validate, inform user
            #write information to the board
            self.window_car_registration.listWidget.addItem(info_car_val)
            self.window_main.listWidget.addItem(info_car_val)
    
    def car_list(self):
        c=Cars(None,None,None,None,None,None)
        aux_cars=c.cars_list()
        self.window_main.listWidget.addItem('')
        self.window_main.listWidget.addItem('CARS LIST')

        for i in aux_cars:
            self.window_main.listWidget.addItem('_________________')
            for k in i:
                #print(k,':',i[k])
                a=str(k)+'  '+str(i[k])
                self.window_main.listWidget.addItem(a)

    #car delete window process
    def car_delete(self):
        #show window car delete
        self.window_car_delete.show()
        #button delete
        self.window_car_delete.pushButton.clicked.connect(self.car_delete_read_id)

    #cliente delete process
    def car_delete_read_id(self):
        #read id to delete
        id_to_delete = self.window_car_delete.lineEdit.text()
        #delete from data base
        c=Cars(None,None,None,None,None,None)
        car_delete=c.car_delete(id_to_delete)
        #show delete information in windows
        self.window_main.listWidget.addItem(car_delete)
        self.window_car_delete.listWidget.addItem(car_delete)


    #client registration window
    def client_registration(self):
        self.window_client_registration.show()
        #button registration
        self.window_client_registration.pushButton.clicked.connect(self.client_read_parameters)

    

    #read client parameters 
    def client_read_parameters(self):
        #read parameters
        self.client_first_name = self.window_client_registration.lineEdit.text()
        self.client_last_name = self.window_client_registration.lineEdit_2.text()
        self.client_email = self.window_client_registration.lineEdit_3.text()
        self.client_phone = self.window_client_registration.lineEdit_4.text()
        self.client_nif = self.window_client_registration.lineEdit_5.text()

        c=Clients(self.client_first_name, self.client_last_name, self.client_email, self.client_phone, self.client_nif)
        
        #client validation
        info_client_val, client_status = c.clients_parameters_validation()

        # validation complete
        if client_status==True:
            #insert data in data base
            info_db_client = c.clients_add_data_base()
            #write information to the board
            self.window_client_registration.listWidget.addItem(info_db_client)
            self.window_main.listWidget.addItem(info_db_client)
        else : #if not validate, inform user
            #write information to the board
            self.window_client_registration.listWidget.addItem(info_client_val)
            self.window_main.listWidget.addItem(info_client_val) 

    def clients_list(self):
        c=Clients(None,None,None,None,None)
        aux_clients=c.clients_list()
        
        self.window_main.listWidget.addItem('')
        self.window_main.listWidget.addItem('CLIENTS LIST')
 
        for i in aux_clients:
            self.window_main.listWidget.addItem('_________________')
            for k in i:
                #print(k,':',i[k])
                b=str(k)+'  '+str(i[k])
                self.window_main.listWidget.addItem(b)

    #client delete window process
    def client_delete(self):
        #show window client delete
        self.window_client_delete.show()
        #button delete
        self.window_client_delete.pushButton.clicked.connect(self.client_delete_read_id)

    #cliente delete process
    def client_delete_read_id(self):
        #read id to delete
        id_to_delete = self.window_client_delete.lineEdit.text()
        #delete from data base
        c=Clients(None,None,None,None,None)
        client_delete=c.client_delete(id_to_delete)
        #show delete information in windows
        self.window_main.listWidget.addItem(client_delete)
        self.window_client_delete.listWidget.addItem(client_delete)


    #rent registration window
    def rent_registration(self):
        self.window_rent_registration.show()

        #button registration
        self.window_rent_registration.pushButton.clicked.connect(self.rent_read_parameters)
       
    #read rent parameters 
    def rent_read_parameters(self):
        #read parameters
        self.rent_car_id = self.window_rent_registration.lineEdit.text()
        self.rent_client_id = self.window_rent_registration.lineEdit_2.text()
        self.rent_days = self.window_rent_registration.lineEdit_3.text()
        
        r=Rents(self.rent_car_id, self.rent_client_id, self.rent_days)
        #rent validation
        info_rent_val, rent_status = r.rents_parameters_validation()

        # validation complete
        if rent_status==True:
            #insert data in data base
            info_db_rent = r.rents_add_data_base()
            #write information to the board
            self.window_rent_registration.listWidget.addItem(info_db_rent)
            self.window_main.listWidget.addItem(info_db_rent)
        else : #if not validate, inform user
            #write information to the board
            self.window_rent_registration.listWidget.addItem(info_rent_val)
            self.window_main.listWidget.addItem(info_rent_val) 


c=RentACar()