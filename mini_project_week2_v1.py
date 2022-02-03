
#    # start of the mini project
#    
#products = ["coffee", "tea", "cakes", "wraps", "sandwiches", "cold_drinks"]
#couriers = {"courier_1":["John", "Travolta"], "courier_2":["Tom", "Cruise"], "courier_3":["Roger", "Twose"]}
#print(couriers)    
#    
#    #coffee = ["espresso", "cafe latte", "cafe mocha", "caramel machhiato", "cappuccino"]
#    #tea = ["black tea", "green tea", "white tea", "oolong tea"]
#    #cakes = ["cheesecake", "dump cake", "butter cake", "coffee cake"]
#    #wraps = ["breakfast wrap", "whole wheat egg wrap", "chicken salad wrap", "turkey club wrap"]
#    #sandwiches = ["egg and cress sandwich", "chicken salad sandwich", "tuna sandwich"]
#    #cold_drinks = ["rose water",  "coke", "pepsi", "strawberry lemonade", "mermaid slushie"]
#    
#
#print(f'A list of our products is given below: \n{products}\n')
#while True:   
#    users = input("""please select your favourite items by choosing from the options below: \n
#                  press 0 to EXIT app
#                  press 1 to have a look at our main menu
#                  press 2 Suggest new product
#                  press 3 Update an existing product
#                  press 4 Delete an existing product
#                  """)
#    items = [users]
#    
#    for item in items:
#        #------------------------------------------------
#        #------------------------------------------------
#        
#        if item == "0":
#            print("Thnaks for visiting! see you soon. \n")
#            break
#        
#        elif item =="1":
#            print(f'This is our main menu \n{products}')
#            
#        #-------------------------------------------------
#        #-------------------------------------------------
#            
#        elif item == "2":
#            new_product = input("please enter the name of new product \n")
#            print(f'The new product you suggested is:\n{new_product}')
#            products.append(new_product)
#            print(f' \nthe updated main menu list is: \n{products}')
#        #-------------------------------------------------
#        #-------------------------------------------------
#        elif item == "3":
#            for index, product in enumerate(products):
#                print(f'Index: {index}  Product: {product}')
#            product_list_length = len(products)
#            user_input = int(input(f'\nplease can you suggest an index for a product from 0 to {product_list_length}\n'))
#            #print(user_input)
#            new_product_suggestion = input(f'\nplease suggest a name for product\n')
#            print(f'\n{new_product_suggestion}')
#            products.insert(user_input, new_product_suggestion)
#            print(f' The product indexing has been update as suggested \n{products}\n')
#            print('The updated indexes and products are given below:\n')
#            for index, product in enumerate(products):
#                print(f' Index: {index}  Product: {product}')
#       #---------------------------------------------------
#       #---------------------------------------------------
#        elif item == "4":
#            print(f' The product List is: {products}\n')
#            product_list_length = len(products)
#            for index, product in enumerate(products):
#                print(f'Index: {index}  Product: {product}')
#            message = ''' please suggest a product to be removed from list
#      by selecting product index from 0 to '''
#            user_input = int(input(f'\n {message}{product_list_length}\n'''))
#            product_name = products[user_input] 
#            del products[user_input]        
#            print(f' The product "{product_name}" with index "{user_input}" is removed from the List: \n {products}\n')
#            
    
products = ["coffee", "tea", "cakes", "wraps", "sandwiches", "cold_drinks"]
couriers = {"courier_1":["John", "Travolta"], "courier_2":["Tom", "Cruise"], "courier_3":["Roger", "Twose"]}
print(couriers)  

filename = 'products.txt'
with open(filename, 'a') as file_object:
    

    
 
