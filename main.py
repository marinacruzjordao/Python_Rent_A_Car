#rent a car

import sqlite3
import images
from PySimpleGUI import PySimpleGUI as sg

class RentACar:
    def __init__(self):
        #



    def cars_data_base_connection(self):
        #connect to database
        self.connection = sqlite3.connect('car_database.db')

        #create cursor to execute commands in data base
        self.cursor = self.connection.cursor()

        #create a car table if not exists
        self.cursor.execute('CREATE TABLE IF NOT EXISTS cars('
                    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                    'brand TEXT,'
                    'model TEXT,'
                    'year INTEGER,'
                    'plate TEXT,'
                    'kilometers REAL'
                    'Status TEXT'
                    ')')

    def display_cars(self):
        #read values in table
        self.cursor.execute('SELECT * FROM cars')
        for i in self.cursor.fetchall():
            identification, brand, model, year, plate, kilometers= i
            print(f'ID: {identification}, Brand: {brand}, Model: {model}, Year: {year}, Plate: {plate}, Kilometers: {kilometers}')
            
    def add_car(self):
        #Create item
        
            
        a=('For', 'Focus',2014, " 12-XL-89", 105504 )
        self.cursor.execute('INSERT INTO cars (brand, model, year, plate, kilometers) VALUES (?,?,?,?,? )',a)
        self.connection.commit()

    def start(self):


        #connect cars data_base
        r.cars_data_base_connection()



            #self.event, value=self.w1.read()
            #self.letter=value.get('letter')

            #When window is closed
            #if self.event == sg.WINDOW_CLOSED:
        if self.window == self.w1 and self.event == sg.WIN_CLOSED:
            r.close_program()
            break

        if self.window == self.w1 and self.event == 'Cars Catalogue':
            r.display_cars()
            
        if self. window == self.w1 and self.event == 'Car Registration':
            r.add_car()

    def close_program(self):
        #close cursor
        self.cursor.close()

        #close connection with database
        self.connection.close()






r=RentACar()
r.start()

#Update car
#cursor.execute('UPDATE cars SET brand=:brand WHERE id=:id',{'brand' : 'BMW', 'id': 5})
#connection.commit()

#Delete item
#cursor.execute('DELETE FROM cars WHERE id=:id',{'id':4})
#connection.commit()


        

#read specific value
#self.cursor.execute('SELECT brand, year FROM cars WHERE year> :year', {'year': 2013})
#for i in self.cursor.fetchall():
#    print(i)



