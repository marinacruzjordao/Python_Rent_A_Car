import sqlite3
from PyQt5 import uic, QtWidgets

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
            print('aquiiii',self.id_client)
            print(aux_id_client,self.id_client)
            if aux_id_client == int(self.id_client):
                aux_client = True
                print('entrei')

        print(aux_client)

        if aux_client == False:
            return f'This client id does not exist in the system.', False

        else:
            # connect to car data base and verify if id is there
            self.car_connection = sqlite3.connect('cars_database.db')
            self.car_cursor = self.car_connection.cursor()
            self.car_cursor.execute('SELECT id FROM cars')
            
            aux_car = False
            for i in self.car_cursor.fetchall():
                aux_id_car=i[0]
                if aux_id_car == int(self.id_car):
                    aux_car = True

            if aux_car == False:
                return f'This car id does not exist in the system.', False
        
        try:  
            self.days = int(self.days)

        except ValueError:
            return f'Year must be an integer.' , False

        return f'' , True    

        #connect to database
    def rents_data_base_connection(self):
        #connect to database
        self.rents_connection = sqlite3.connect('rents_database.db')
        
        #create cursor to execute database functions
        self.rents_cursor = self.rents_connection.cursor()
        
        #create a client table if not exists
        self.rents_cursor.execute('CREATE TABLE IF NOT EXISTS rents('
            'id INTEGER PRIMARY KEY AUTOINCREMENT,'
            'ID_Car TEXT,'
            'ID_Client TEXT,'
            'Days INTEGER,'
            'PRICE REAL,'
            'Status TEXT'
            ')')
'''
     #add a client to data base
    def clients_add_data_base(self):
        #validate if this NIF is in the system
        self.clients_cursor.execute('SELECT Nif FROM clients')
        
        for i in self.clients_cursor.fetchall():
            aux_nif=str(i[0])
            if int(aux_nif) == self.nif:
                return f'This client is already in system.'

        #introduce to data base
        client = (self.first_name, self.last_name, self.email, self.phone, self.nif,'No active rents')
        self.clients_cursor.execute('INSERT INTO clients (First_Name, Last_Name, Email, Phone, Nif, Status) VALUES (?,?,?,?,?,?) ', client)
        self.clients_connection.commit()
        return f'Client: {self.first_name}, {self.last_name}, {self.nif} was introduced to the system.'

    def clients_list(self):
        #display all clients
        self.clients_cursor.execute('SELECT * From clients')
        aux_clients=[]
        for i in self.clients_cursor.fetchall():
            id_number, first_name, last_name, email, phone, nif, status = i
            aux_client = {
                'ID_number:': id_number,
                'First Name:' : first_name,
                'Last Name:' : last_name,
                'Email:' : email,
                'Phone:': phone,
                'NIF:' : nif,
                'Status:': status,
            }
            aux_clients.append(aux_client)
        
        return aux_clients
    
    def client_delete(self,id_number):
        #validate if this client ID is in the system
        self.clients_cursor.execute('SELECT id FROM clients')
        
        for i in self.clients_cursor.fetchall():
            aux_id=str(i[0])
            if int(aux_id) == int(id_number):
                    #delete client from data base
                    self.clients_cursor.execute('DELETE FROM clients WHERE id=:id',{'id':id_number})
                    self.clients_connection.commit()
                    return f'Cliente ID: {id_number} was deleted.'
            
        return f'This client {id_number} does not exist.'
        

'''                
        
