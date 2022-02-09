
from mini_project_functions import file_opener, display_list_by_index, file_writer, file_writer2, print_products_menu, print_main_menu
from mini_project_functions import print_product_sub_menu, print_couriers_menu, print_orders_menu
from mini_project_functions import print_product_update_menu, delete_item_from_list, update_listitem_by_name
from mini_project_functions import print_product_Up_sub_menu, print_product_delete_sub_menu, return_list
import mini_project_functions as fn
import csv
products  = file_opener("products.txt")
couriers = file_opener("couriers.txt")

while True: 
    print_main_menu()  
    users = int(input())
            
    if users == 0:
        print("\nThanks for Visiting! See You Soon! \n")
        break

    elif users ==1:
        while True:
            print_products_menu()
            product_input = int(input())
            
            if product_input == 0:
                break
            elif product_input == 1:
                print("Our Product List is Given Below:\n")
                display_list_by_index(products)
                                
            elif product_input == 2:
                while True:
                    display_list_by_index(products)
                    product_list_length = len(products)
                    new_product_index = int(input(f'\n Choose an Index Position to Add New Product.\n'))
                    new_product_name = input(f'\nSuggest a Name for The New Product.\n')
                    print("\n")
                    products.insert(new_product_index-1, new_product_name)
                    file_writer("products.txt", products)
                    display_list_by_index(products)
                    print_product_sub_menu()
                    further_options = int(input())
                    if further_options == 0:
                        break
            
            elif product_input == 3:
                
                while True:
                    display_list_by_index(products)
                    product_name = input("\nPlease Write The Name of An Existing Product to Update: \n") 
                    print_product_update_menu()
                    product_update_input = int(input())
                    
                    if product_update_input == 1:
                        new_index = int(input(f'\nChoose New Index for {product_name}: \n'))
                        delete_item_from_list(products, product_name)
                        products.insert(new_index-1, product_name)
                        file_writer("products.txt", products)
                        print('\nThe Updated List is Given Below:\n')
                        display_list_by_index(products)
                        print_product_Up_sub_menu()
                        further_options = int(input())
                        if further_options == 0:
                            break
                    
                    if product_update_input ==2:
                        new_name = input(f'\nChoose New Name for {product_name}: \n')
                        print('\nThe updated indexes and products are given below:\n')
                        update_listitem_by_name(products, product_name,new_name)
                        file_writer("products.txt", products)
                        display_list_by_index(products)
                        print_product_Up_sub_menu()
                        further_options = int(input())
                        if further_options == 0:
                            break
                                          
            elif product_input == 4:
                while True:
                    display_list_by_index(products)
                    message = 'Please Choose an Index to Remove a Product.'
                    user_input = int(input(f'\n {message}\n'''))
                    del products[user_input-1]
                    file_writer("products.txt", products)
                    print("\nThe Updated Product List is Given Below.\n")
                    display_list_by_index(products)
                    print_product_delete_sub_menu()
                    further_options = int(input())
                    if further_options == 0:
                        break

    elif users ==2:
        while True:
            fn.print_couriers_menu()
            courier_input = int(input())
            
            if courier_input == 0:
                break

            elif courier_input == 1:
                print("Our Couriers List is Given Below:\n")
                display_list_by_index(couriers)

            elif courier_input == 2:
                while True:
                    display_list_by_index(couriers)
                    courier_list_length = len(couriers)
                    new_courier_index = int(input(f'\n Choose an Index Position for New Courier.\n'))
                    new_courier_name = input(f'\nSuggest a Name for The New Courier.\n')
                    print("\n")
                    couriers.insert(new_courier_index-1, new_courier_name)
                    file_writer("couriers.txt", couriers)
                    display_list_by_index(couriers)
                    fn.print_courier_sub_menu()
                    further_options = int(input())
                    if further_options == 0:
                        break
            
            elif courier_input == 3:
                while True:
                    display_list_by_index(couriers)
                    courier_name = input("\nPlease Write The Name of An Existing Courier to Update: \n") 
                    print_product_update_menu()
                    courier_update_input = int(input())
                    
                    if courier_update_input == 1:
                        new_index = int(input(f'\nChoose New Index for {courier_name}: \n'))
                        delete_item_from_list(couriers, courier_name)
                        couriers.insert(new_index-1, courier_name)
                        file_writer("couriers.txt", couriers)
                        print('\nThe Updated List is Given Below:\n')
                        display_list_by_index(couriers)
                        fn.print_courier_Up_sub_menu
                        further_options = int(input())
                        if further_options == 0:
                            break
                    
                    if courier_update_input ==2:
                        new_name = input(f'\nChoose New Name for {courier_name}: \n')
                        print('\nThe Updated Indexes and Couriers are Given Below:\n')
                        update_listitem_by_name(couriers, courier_name,new_name)
                        file_writer("couriers.txt", couriers)
                        display_list_by_index(couriers)
                        fn.print_courier_Up_sub_menu
                        further_options = int(input())
                        if further_options == 0:
                            break

            elif courier_input == 4:
                while True:
                    display_list_by_index(couriers)
                    message = 'Please Choose an Index to Remove a Courier.'
                    user_input = int(input(f'\n {message}\n'''))
                    del couriers[user_input-1]
                    file_writer("couriers.txt", couriers)
                    print("\nThe Updated Courier List is Given Below.\n")
                    display_list_by_index(couriers)
                    fn.print_courier_delete_sub_menu()
                    further_options = int(input())
                    if further_options == 0:
                        break

    elif users ==3:
        while True:
            fn.print_orders_menu()
            order_input = int(input())
            
            if order_input == 0:
                break
            
            elif order_input == 1:
                print("\nOur Orders List is Given Below:\n")
                #display_list_by_index(couriers)
                fn.csv_r_display("orders.csv")
            
            elif order_input == 2:
                






