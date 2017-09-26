#Created by : Alireza Teimoori
#Created on : 26 Sept. 2017
#Created for : ICS3UR
# Daily Assignment - Unit1-05
# This program calculates the cost of a pizza with the diameter inputed by user

import ui

def calculate_pizza_price_touch_up_inside(sender):
    #Calculates the price of the pizza
    
    #constants
    LABOUR_COST = 0.75
    RENT_COST = 1.00
    MATERIALS_COST= 0.50
    HST = 1.13
    
    #input
    diameter = float(view['diameter_textfield'].text)
    
    #process
    total_cost = (LABOUR_COST+RENT_COST+MATERIALS_COST*diameter)*HST
    
    #output
    view['price_lable'].text = "The cost is : "+"${:,.2f}".format(total_cost)
    
view = ui.load_view()
view.present('full_screen')
