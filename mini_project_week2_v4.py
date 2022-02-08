
#    Start of the mini_project
#    
products = ["coffee", "tea", "cakes", "wraps", "sandwiches", "cold_drinks"]
#couriers = {"courier_1":["John", "Travolta"], "courier_2":["Tom", "Cruise"], "courier_3":["Roger", "Twose"]}

product_menu = """\n
Please Select From Options for The Product Menu: \n
============ Product Menu ========== \n
press 0:  Return to Main Menu
press 1:  Look at Product List
press 2:  Suggest a New Product
press 3:  Update an Existing Product
press 4:  Delete an Existing Product
=====================================
"""
main_menu = """\n
Welcome to ChaCha Cafe! \n
Please Select from the Main Menu. \n
============ Main Menu =========== \n
Press 0:  Exit App
Press 1:  View Product Menu
==================================
"""
new_product_sub_menu = '''\n1
Press 0: To Return to Product Menu
Press 1: To Suggest Another Product.\n
'''

from mini_project_functions import file_opener, display_list, file_writer, file_writer2
products  = file_opener("products.txt")
couriers = file_opener("couriers.txt")

while True:   
    users = int(input(main_menu))
            
    if users == 0:
            print("\nThanks for Visiting! See You Soon! \n")
            
            break
    elif users ==1:
            while True:
                print(product_menu + "\n ")
                product_input = int(input(" "))
                
                if product_input == 0:
                    break

                elif product_input == 1:
                    print("Our Product List is Given Below: ")
                    display_list(products)
                                    
                elif product_input == 2:
                    active = True
                    while active:
                        display_list(products)
                        product_list_length = len(products)
                        product_input = int(input(f'\n Choose an Index Position to Add New Product.\n'))
                        new_product_suggestion = input(f'\nSuggest a Name for The New Product.\n')
                        print("\n")
                        products.insert(product_input-1, new_product_suggestion)
                        display_list(products)

                        further_options = int(input(new_product_sub_menu))
                        if further_options == 0:
                            break
                        elif further_options == 1:
                            active 

                elif product_input == 3:
                    print("\nOur product list is given below: \n")
                    for i, product in enumerate(products):
                        print(f' {i+1}: {product}')
                    update_product = input("\nPlease Choose The Product Name from The List: \n")
                    if update_product not in products:
                        print("This Product is not in The Existing Products List.")
                    else:
                        index_update_input = int(input(f'\n Press 1: To Update {update_product} Index \n Press 2: To Update {update_product} Name.\n'))
                        if index_update_input == 1:
                            new_index = int(input(f'\nChoose New Index for {update_product}: \n'))
                            earlier_index_of_product = products.index(update_product)
                            del products[earlier_index_of_product]
                            products.insert(new_index-1, update_product)
                            print('\nThe updated indexes and products are given below:\n')
                            for index, product in enumerate(products):
                                print(f' Index: {index+1}  Product: {product}')
                        elif index_update_input ==2:
                            new_name = input(f'\nChoose New Name for {update_product}: \n')
                            earlier_index_of_product = products.index(update_product)
                            products[earlier_index_of_product] = new_name
                            print('\nThe updated indexes and products are given below:\n')
                            for index, product in enumerate(products):
                                print(f' Index: {index+1}  Product: {product}')
                                              
                elif product_input == 4:
                    #print(f' The product List is: {products}\n')
                    product_list_length = len(products)
                    for index, product in enumerate(products):
                        print(f'Index: {index+1}  Product: {product}')
                    message = 'Please Choose an Index to Remove a Product.'
                    user_input = int(input(f'\n {message}\n'''))
                    product_name = products[user_input-1] 
                    del products[user_input-1]        
                    print(f' The product "{product_name}" with index "{user_input}" is removed from the List: \n')
                    for index, product in enumerate(products):
                        print(f'Index: {index+1}  Product: {product}')
    
# 
#couriers = {"courier_1":["John", "Travolta"], "courier_2":["Tom", "Cruise"], "courier_3":["Roger", "Twose"]}
#print(couriers)  





