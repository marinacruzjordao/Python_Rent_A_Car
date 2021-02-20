import pymysql.cursors
import sqlite3
from PyQt5 import uic, QtWidgets
from email_rent_a_car import Email


class Rents:
    def __init__(self,id_car, id_client, days):
        self.id_car = id_car
        self.id_client = id_client
        self.days = days

        self.start()
    
    def start(self):
        self.rents_data_base_connection()


    def rents_parameters_validation(self):
        # connect to client data base and verify if id is there
        self.clients_connection = sqlite3.connect('clients_database.db')
        self.clients_cursor = self.clients_connection.cursor()
        self.clients_cursor.execute('SELECT id FROM clients')
        
        aux_client = False
        for i in self.clients_cursor.fetchall():
            aux_id_client=i[0] 
            if aux_id_client == int(self.id_client):
                aux_client = True


        if aux_client == False:
            return f'This client id does not exist in the system.', False

        else:
            # connect to car data base and verify if id is there
            self.car_connection = sqlite3.connect('cars_database.db')
            self.car_cursor = self.car_connection.cursor()
            self.car_cursor.execute('SELECT * FROM cars')
            
            aux_car = False
            aux_car_status = False
            for i in self.car_cursor.fetchall():
                id_car_number, brand, model, year, plate, kilometers, self.level, status = i
                aux_id_car=id_car_number
                if aux_id_car == int(self.id_car):
                    aux_car = True
                    if status=='available':
                        aux_car_status = True
                        self.level_final =self.level
                    


            if aux_car == False :
                return f'This car id does not exist in the system.', False
            if aux_car_status == False:
                return f'This car is not available for rent.', False
        try:  
            self.days = int(self.days)

        except ValueError:
            return f'Number of Days must be an integer.' , False

        return f'' , True    

        #connect to database
    def rents_data_base_connection(self):
        self.conection_rent=pymysql.connect(
            host='127.0.0.1',
            port=8889,
            user='root',
            password='root',
            db='rents',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
    
        self.rents_cursor=self.conection_rent.cursor()

     #add a client to data base
    def rents_add_data_base(self):
        #introduce to data base
        sql='INSERT INTO rents (ID_Car, ID_Client, Days, Price, Status) VALUES'\
            '(%s, %s, %s, %s, %s)'
        

        #obtained the car level to calculate the price
        self.price=self.days*100*int(self.level_final)
        self.rents_cursor.execute(sql,(int(self.id_car),int(self.id_client),int(self.days),self.price,'Open'))
        self.conection_rent.commit()

        #update car data base and disable the status
        self.car_cursor.execute('UPDATE cars SET Status=:Status WHERE id=:id',{'Status' : 'disable', 'id': self.id_car})
        self.car_connection.commit()

        #update client data base and status 'active rents'
        self.clients_cursor.execute('UPDATE clients SET Status=:Status WHERE id=:id',{'Status' : 'rent active', 'id': self.id_client})
        self.clients_connection.commit()

        #send email to client
        # connect to client data base and verify if id is there
        self.clients_connection = sqlite3.connect('clients_database.db')
        self.clients_cursor = self.clients_connection.cursor()
        self.clients_cursor.execute('SELECT * FROM clients')
        
        #find the name of client
        for i in self.clients_cursor.fetchall():
            aux_id=str(i[0])
            id_number, first_name, last_name, email, phone, nif, status = i
            if int(id_number) == int(self.id_client):
                name=first_name+ ' '+ last_name
                email_client=email
        
       
        e=Email(email_client,name,self.id_client, self.price)
        e.email_open_rent()

        
        return f'Rent: {self.id_car}, {self.id_client} was introduced to the system. Rent Price: {self.price}'

    def rents_list(self):
        #display all clients
        self.rents_cursor.execute('SELECT * From rents')
        aux_rents=[]
        for i in self.rents_cursor.fetchall():
            aux_rent = {
                'ID_number:': i['id'],
                'ID_Car:' : i['ID_Car'],
                'ID_Client:' : i['ID_Client'],
                'Days:' : i['Days'],
                'Price:': i['Price'],
                'Status:': i['Status'],
            }
            aux_rents.append(aux_rent)
        
        return aux_rents
   
   #update the rent
    def rent_close(self,id_number,kilometers):
        #validate if this rent ID is in the system
        self.rents_cursor.execute('SELECT * FROM rents')


        for i in self.rents_cursor.fetchall():
            if i['id'] == int(id_number):
                    id_car = i['ID_Car']
                    id_client = i['ID_Client']
                    #close rent from data base
                    sql='UPDATE rents SET Status=%s WHERE id=%s'
                    self.rents_cursor.execute(sql,('Close',id_number))
                    result=self.rents_cursor.fetchall()
                    self.conection_rent.commit()

                    #update car data base, disable the status, update kilometers
                    self.car_connection = sqlite3.connect('cars_database.db')
                    self.car_cursor = self.car_connection.cursor()
                    self.car_cursor.execute('UPDATE cars SET Status=:Status WHERE id=:id',{'Status' : 'available', 'id': id_car})
                    self.car_cursor.execute('UPDATE cars SET Kilometers=:Kilometers WHERE id=:id',{'Kilometers' : kilometers, 'id': id_car})

                    self.car_connection.commit()

                    #update client data base and  the status
                    self.clients_connection = sqlite3.connect('clients_database.db')
                    self.clients_cursor = self.clients_connection.cursor()
                    self.clients_cursor.execute('UPDATE clients SET Status=:Status WHERE id=:id',{'Status' : 'No active rents', 'id': id_client})
                    self.clients_connection.commit()


                     #send email to client
                    # connect to client data base and verify if id is there
                    self.clients_connection = sqlite3.connect('clients_database.db')
                    self.clients_cursor = self.clients_connection.cursor()
                    self.clients_cursor.execute('SELECT * FROM clients')
                    
                    #find the name of client
                    for i in self.clients_cursor.fetchall():
                        aux_id=str(i[0])
                        id_number, first_name, last_name, email, phone, nif, status = i
                        if int(id_number) == int(id_client):
                            name=first_name+ ' '+ last_name
                            email_client=email
        

                    e=Email(email_client,name,self.id_client, self.price)
                    e.email_close_rent()

                    return f'Cliente ID: {id_number} was close.'

        return f'This client {id_number} does not exist.'
           
