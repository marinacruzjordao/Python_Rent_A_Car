import sqlite3
from PyQt5 import uic, QtWidgets


class Cars:
    def __init__(self, brand, model, year, plate, kilometers, level):
        self.brand = brand
        self.model = model
        self.year = year
        self.plate = plate
        self.kilometers = kilometers
        self.level = level

        self.start()


    def start(self):
        self.cars_data_base_connection()

    def car_parameters_validation(self):
        try:  
            self.car_year = int(self.year)

        except ValueError:
            return f'Year must be an integer.' , False

        try:  
            self.car_kilometers = float(self.kilometers)
        except ValueError:
            return f'Kilometers must be a float number.' , False

        try:  
            self.car_level = int(self.level)
        except ValueError:
            return f'Level must be an integer.' , False

        return f'' , True

    #connect to database
    def cars_data_base_connection(self):
        #connect to database
        self.car_connection = sqlite3.connect('cars_database.db')
        
        #create cursor to execute database functions
        self.car_cursor = self.car_connection.cursor()
        
        #create a car table if not exists
        self.car_cursor.execute('CREATE TABLE IF NOT EXISTS cars('
            'id INTEGER PRIMARY KEY AUTOINCREMENT,'
            'Brand TEXT,'
            'Model TEXT,'
            'Year INTEGER,'
            'Plate TEXT,'
            'Kilometers REAL,'
            'Level INTEGER,'
            'Status TEXT'
            ')')
    
    #add a car to data base
    def cars_add_data_base(self):
        #validate if this plate is in the system
        self.car_cursor.execute('SELECT Plate FROM cars')
        
        for i in self.car_cursor.fetchall():
            aux_plate=str(i[0])
            if aux_plate == self.plate:
                return f'This car is already in system.'

        #introduce to data base
        car = (self.brand, self.model, self.year, self.plate, self.kilometers,self.level,'available')
        self.car_cursor.execute('INSERT INTO cars (brand, model, year, plate, kilometers, Level, Status) VALUES (?,?,?,?,?,?,?) ', car)
        self.car_connection.commit()
        return f'Car: {self.brand}, {self.model}, {self.plate} was introduced to the system.'

    def cars_list(self):
        #display all cars
        self.car_cursor.execute('SELECT * From cars')
        aux_cars=[]
        for i in self.car_cursor.fetchall():
            id_number, brand, model, year, plate, kilometers, level, status = i
            aux_car = {
                'ID_number:': id_number,
                'Brand:' : brand,
                'Model:' : model,
                'Year:' : year,
                'Plate:': plate,
                'Kilometers:' : kilometers,
                'Rent Level:': level,
                'Status:': status,
            }
            aux_cars.append(aux_car)
        
        return aux_cars

    def car_delete(self,id_number):
        #validate if this car ID is in the system
        self.car_cursor.execute('SELECT id FROM cars')
        
        for i in self.car_cursor.fetchall():
            aux_id=str(i[0])
            if int(aux_id) == int(id_number):
                    #delete car from data base
                    self.car_cursor.execute('DELETE FROM cars WHERE id=:id',{'id':id_number})
                    self.car_connection.commit()
                    return f'Car ID: {id_number} was deleted.'
            
        return f'This car {id_number} does not exist.'
        





        

