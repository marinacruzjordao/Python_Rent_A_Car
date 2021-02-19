import sqlite3
from PyQt5 import uic, QtWidgets

class Clients:
    def __init__(self,f_name, l_name, email, phone, nif):
        self.first_name = f_name
        self.last_name = l_name
        self.email = email
        self.phone = phone
        self.nif = nif

        self.start()

    def start(self):
        self.clients_data_base_connection()

    def clients_parameters_validation(self):
        try:  
            self.nif = int(self.nif)

        except ValueError:
            return f'NIF must be an integer.' , False

        return f'' , True    

        #connect to database
    def clients_data_base_connection(self):
        #connect to database
        self.clients_connection = sqlite3.connect('clients_database.db')
        
        #create cursor to execute database functions
        self.clients_cursor = self.clients_connection.cursor()
        
        #create a client table if not exists
        self.clients_cursor.execute('CREATE TABLE IF NOT EXISTS clients('
            'id INTEGER PRIMARY KEY AUTOINCREMENT,'
            'First_Name TEXT,'
            'Last_Name TEXT,'
            'Email TEXT,'
            'Phone TEXT,'
            'Nif INTEGER,'
            'Status TEXT'
            ')')

     #add a client to data base
    def clients_add_data_base(self):
        #validate if this NIF is in the system
        self.clients_cursor.execute('SELECT Nif FROM clients')
        
        for i in self.clients_cursor.fetchall():
            aux_nif=str(i[0])
            if int(aux_nif) == self.nif:
                return f'This client is already in system.'
        
        self.clients_cursor.execute('SELECT Email FROM clients')      

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
        

                
        

