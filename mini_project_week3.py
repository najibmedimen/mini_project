
from mini_project_functions import file_opener, display_list_by_index, file_writer, file_writer2, print_products_menu, print_main_menu
from mini_project_functions import print_product_sub_menu, print_couriers_menu, print_orders_menu
from mini_project_functions import print_product_update_menu, delete_item_from_list, update_listitem_by_name
from mini_project_functions import print_product_Up_sub_menu, print_product_delete_sub_menu, return_list
import mini_project_functions as fn
import csv

products = fn.csv_opener('products.csv')
couriers = fn.csv_opener('couriers.csv')
orders = fn.csv_opener('orders.csv')

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
                fn.csv_r_display("products.csv", "Product")
                                
            elif product_input == 2:
                while True:
                    fn.csv_r_display("products.csv", "Product")
                    new_product_name = input(f'\nSuggest a Name for The New Product.\n')
                    product_price = float(input(f'\n Please Enter the Price of New Product.\n'))
                    data_row_list = [new_product_name,product_price]
                    fn.csv_appender('products.csv', data_row_list)
                    fn.csv_r_display("products.csv", "Product")
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
                fn.csv_r_display("couriers.csv", "Courier")

            elif courier_input == 2:
                while True:
                    fn.csv_r_display("couriers.csv", "Courier")
                    new_courier_name = input(f'\nSuggest a Name for The New Courier.\n')
                    courier_phone_number = int(input(f'\n Enter Courier Phone Number.\n'))
                    data_row_list = [new_courier_name,courier_phone_number]
                    fn.csv_appender('couriers.csv', data_row_list)
                    fn.csv_r_display("couriers.csv", "Courier")
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
                fn.csv_r_display("orders.csv", 'Order')
            
            elif order_input == 2:
                new_order = {}
                customer_name = input(f'\nPlease Enter Customer Name:\n')
                customer_address = input(f'\nPlease Enter Customer Address:\n')
                customer_phone = int(input(f'\nPlease Enter Customer Phone Number:\n'))
                fn.csv_r_display("products.csv", "Product Index")
                list = str(input ("Please Enter Product Indices Seaparated By Commas:\n"))
                List = list.split(',')
                product_order_list =[]
                for item in List:
                    product_order_list.append(int(item))
                print(product_order_list)
                fn.csv_r_display("couriers.csv", "Courier Index")
                courier_index = int(input(f'\n Please Select A Courier Index:\n'))
                order_status = "preparing"
                #new_order['customer_name'] = customer_name
                #new_order['customer_address'] = customer_address
                #new_order['customer_phone'] = customer_phone
                #new_order['courier'] = courier_index
                #new_order['status'] = order_status

                data_row_list = [customer_name,customer_address,customer_phone,courier_index,product_order_list,order_status]
                fn.csv_appender('orders.csv', data_row_list)
                fn.csv_r_display("orders.csv", "Order Index")

            elif order_input == 3:
                orders_list = fn.csv_reader('orders.csv')
                fn.csv_r_display("orders.csv", 'Order')
                user_input1 = int(input('\nPlease Enter The Order Index to be Changed:\n'))
                fn.print_order_status_menu()
                
                index = int(input('\nPlease Enter The New Index to Update Status:\n'))
                if index == 1:
                        orders_list[user_input1-1]['status'] = 'Preparing'
                elif index == 2:
                        orders_list[user_input1-1]['status'] = 'Ready'
                elif index == 3:
                        orders_list[user_input1-1]['status'] = 'Out for Delivery'
                elif index == 4:
                        orders_list[user_input1-1]['status'] = 'Delivered'
                else:
                        print('Please Enter a Valid Index')
                                                                                           
                header_names = ['customer_name','customer_address','customer_phone','courier','product_order_list','status']
                fn.order_update_writer(orders_list,header_names)

#customer_name,customer_address,customer_phone,courier,product_order_list,status
#najib khan,15 Ashton place,0789887334,2,[1,2,3],preparing
#najaf,15 piccadilly,089767334,1,[1],preparing
#rana,12 china town,745277744,3,"[2, 5, 6]",preparing
#liaqat,03 roseville garden,8766545432,4,"[3, 4, 5]",preparing               
                






