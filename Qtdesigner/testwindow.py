from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip

class Teste:
    def __init__(self):
        self.window_init()

    def window_init(self):
        #import file
        app=QtWidgets.QApplication([])
        self.w1 = uic.loadUi('mainwindow.ui') 
        self.w2 = uic.loadUi('car_regs.ui') 

        #button
        self.w1.pushButton.clicked.connect(self.car_registration) #button 1
        self.w1.pushButton_2.clicked.connect(self.client_registration) #button2

    #
        self.w1.show()
        app.exec()

    def car_registration(self):
        print('car registration')

        #read from Line Edit
        read_car= self.w1.lineEdit.text()
        print(read_car)

        #clean the line edit data in the screen
        self.w1.lineEdit.setText('')

        #write in list widget
        self.w1.listWidget.addItem(read_car)


    def client_registration(self):
        print('client registration')

        #clean all data in the list widget
        self.w1.listWidget.clear()
        
        self.w2.show()

        #self.w2.pushButton.clicked.connect() #button 1
        #read_brand=self.w2.lineEdit.text() #read 
        #self.w2.close()
        #self.w1.listWidget.addItem(read_brand)
        self.w2.pushButton.clicked.connect(self.read_cars)

    def read_cars(self):
        print('registei o carro')

        #read from Line Edit
        read_car_brand= self.w2.lineEdit.text()
        print(read_car_brand)


t=Teste()
t.window_init()
