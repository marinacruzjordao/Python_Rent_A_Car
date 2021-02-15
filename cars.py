
import sqlite3
import images
from PySimpleGUI import PySimpleGUI as sg


class RentACar:
    def __init__(self):
        #layout
        sg.theme('Reddit')
    
    def wind_initial(self):
        
        self.layout=[
            [sg.Button(image_data=images.imge)], 
            [sg.Button('Cars Catalogue',size=(20,2)),sg.Button('Car Registration ',size=(20,2))],
            #[sg.Output(size=(140,10))],
        ] 

        return sg.Window('Rent a Car',layout=self.layout)

    def start(self):

        #Create initial window
        #self.window1, self.window2 =r.wind_initial(), None
        #self.w1 = sg.Window('Rent a Car',layout=self.layout)
        #self.w2 = sg.Window('Car Registration').layout(self.layout2)
        #connect cars data_base
        #r.cars_data_base_connection()

        wind1=r.wind_initial()

        while True:

            event, values = wind1.read()


            #self.event, value=self.w1.read()
            #self.letter=value.get('letter')

            #When window is closed
            if  event == sg.WINDOW_CLOSED:
            #if self.windows == self.w1 and self.event == sg.WIN_CLOSED:
                #r.close_program()
                break

            #if self.window == self.w1 and self.event == 'Cars Catalogue':
            #    r.display_cars()
            
            #if self. window == self.w1 and self.event == 'Car Registration':
            #    r.add_car()
        

r=RentACar()
r.start()