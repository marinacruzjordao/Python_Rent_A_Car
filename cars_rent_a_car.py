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
        print('saiu base dados')


    def testar(self,a):
        return f'testar {a}'



    def car_parameters_validation(self):
        try:  
            print(self.year)
            self.car_year = int(self.year)
            print(self.year, '2')

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

        print(f'A brand e {self.brand} {self.year}')
        print(type(self.year))

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
            'Rent Level INTEGER'
            'Status TEXT'
            ')')

        print(' car connect base dados')
    

    




        

