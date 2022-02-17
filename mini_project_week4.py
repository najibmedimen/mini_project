
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
                print('\nOur Products are Given Below:\n')
                fn.csv_r_display('products.csv')
                                
            elif product_input == 2:
                while True:
                    print('\nOur Products are Given Below:\n')
                    fn.csv_r_display('products.csv')
                    new_product_name = input(f'\nSuggest a Name for The New Product.\n')
                    product_price = float(input(f'\n Please Enter the Price of New Product.\n'))
                    data_row_list = [new_product_name,product_price]
                    fn.csv_appender('products.csv', data_row_list)
                    print('\nOur Products are Given Below:\n')
                    fn.csv_r_display('products.csv')
                    print_product_sub_menu()
                    further_options = int(input())
                    if further_options == 0:
                        break
            
            elif product_input == 3:
                
                while True:
                    print('\nOur Products are Given Below:\n')
                    fn.csv_r_display('products.csv')
                    user_input = int(input('\nChoose an Index to Update a Porduct:\n'))
                    products_list = fn.csv_reader('products.csv')
                    for key, value in products_list[user_input-1].items():
                        key_input = input(f'\nPlease Insert New Value for {value}:\n')
                        if key_input:
                            products_list[user_input-1][key] = key_input
                    header_names = ['name','price($)']
                    fn.dict_writer('products.csv',products_list,header_names)
                    fn.print_product_Up_sub_menu()
                    further_options = int(input())
                    if further_options == 0:
                        break
                                                                
            elif product_input == 4:
                while True:
                    print('\nOur Products are Given Below:\n')
                    fn.csv_r_display('products.csv')
                    products_list = fn.csv_reader('products.csv')
                    delete_input = int(input('\nPlease Choose an Index to delete a Product:\n'))
                    del products_list[delete_input-1]
                    header_names = ['name','price($)']
                    fn.dict_writer('products.csv',products_list,header_names)
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
                print('\nOur Couriers are Given Below:\n')
                fn.csv_r_display('couriers.csv')

            elif courier_input == 2:
                while True:
                    print('\nOur Couriers are Given Below:\n')
                    fn.csv_r_display('couriers.csv')
                    new_courier_name = input(f'\nSuggest a Name for The New Courier.\n')
                    courier_phone_number = int(input(f'\n Enter Courier Phone Number.\n'))
                    data_row_list = [new_courier_name,courier_phone_number]
                    fn.csv_appender('couriers.csv', data_row_list)
                    print('\nOur Couriers are Given Below:\n')
                    fn.csv_r_display('couriers.csv')
                    fn.print_courier_sub_menu()
                    further_options = int(input())
                    if further_options == 0:
                        break
        
            
            elif courier_input == 3:
                while True:
                    print('\nOur Couriers are Given Below:\n')
                    fn.csv_r_display('couriers.csv')
                    user_input = int(input('\nChoose an Index to Update a Courier:\n'))
                    couriers_list = fn.csv_reader('couriers.csv')
                    for key, value in couriers_list[user_input-1].items():
                        key_input = input(f'\nPlease Insert New Value for {key}:\n')
                        if key_input:
                            couriers_list[user_input-1][key] = key_input
                    header_names = ['name','phone']
                    fn.dict_writer('couriers.csv',couriers_list,header_names)
                    fn.print_courier_Up_sub_menu()
                    further_options = int(input())
                    if further_options == 0:
                        break

            elif courier_input == 4:
                while True:
                    print('\nOur Couriers are Given Below:\n')
                    fn.csv_r_display('couriers.csv')
                    couriers_list = fn.csv_reader('couriers.csv')
                    delete_input = int(input('\nPlease Choose and Index to delete a Courier\n'))
                    del couriers_list[delete_input-1]
                    header_names = ['name','phone']
                    fn.dict_writer('couriers.csv',couriers_list,header_names)
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
                print('\nOur Current Orders are Given Below:\n')
                fn.csv_r_display('orders.csv')
            
            elif order_input == 2:
                new_order = {}
                customer_name = input(f'\nPlease Enter Customer Name:\n')
                customer_address = input(f'\nPlease Enter Customer Address:\n')
                customer_phone = int(input(f'\nPlease Enter Customer Phone Number:\n'))
                print('\nOur Products are Given Below:\n')
                fn.csv_r_display('products.csv')
                list = str(input ("Please Enter Product Indices Seaparated By Commas:\n"))
                List = list.split(',')
                product_order_list =[]
                for item in List:
                    product_order_list.append(int(item))
                print(product_order_list)
                print('\nOur Couriers are Given Below:\n')
                fn.csv_r_display('couriers.csv')
                courier_index = int(input(f'\n Please Select A Courier Index:\n'))
                order_status = "preparing"
                data_row_list = [customer_name,customer_address,customer_phone,courier_index,product_order_list,order_status]
                fn.csv_appender('orders.csv', data_row_list)
                print('\nOur Current Orders are Given Below:\n')
                fn.csv_r_display('orders.csv')

            elif order_input == 3:
                status = ['preparing','ready for collection','out for delivery','delivered']
                orders_list = fn.csv_reader('orders.csv')
                print('\nOur Current Orders are Given Below:\n')
                fn.csv_r_display('orders.csv')
                user_input = int(input('\nPlease Enter The Order Index to be Changed:\n'))
                print('\n=========Orders-Status=============\n')
                fn.display_list_by_index(status)
                index = int(input('\nPlease Enter An Index to Update Status:\n'))
                orders_list[user_input-1]['status'] = status[index-1]
                header_names = ['customer_name','customer_address','customer_phone','courier','product_order_list','status']
                fn.dict_writer('orders.csv',orders_list,header_names)

            elif order_input == 4:
                print('\nOur Current Orders are Given Below:\n')
                fn.csv_r_display('orders.csv')
                user_input = int(input('\nChoose an Index to Update an Order:\n'))
                orders_list = fn.csv_reader('orders.csv')
                for key, value in orders_list[user_input-1].items():
                        key_input = input(f'\nPlease Insert New Value for {key}:\n')
                        if key_input:
                            orders_list[user_input-1][key] = key_input
                header_names = ['customer_name','customer_address','customer_phone','courier','product_order_list','status']
                fn.dict_writer('orders.csv',orders_list,header_names)
                fn.print_order_Up_sub_menu()
                further_options = int(input())
                if further_options == 0:
                    break
            
            elif order_input == 5:
                while True:
                    print('\nOur Current Orders are Given Below:\n')
                    fn.csv_r_display('orders.csv')
                    orders_list = fn.csv_reader('orders.csv')
                    delete_input = int(input('\nChoose an Index to delete an Order\n'))
                    del orders_list[delete_input-1]
                    header_names = ['customer_name','customer_address','customer_phone','courier','product_order_list','status']
                    fn.dict_writer('orders.csv',orders_list,header_names)
                    fn.print_order_Up_sub_menu()
                    further_options = int(input())
                    if further_options == 0:
                        break  






#customer_name,customer_address,customer_phone,courier,product_order_list,status
#najib khan,15 Ashton place,0789887334,2,[1,2,3],preparing
#najaf,15 piccadilly,089767334,1,[1],preparing
#rana,12 china town,745277744,3,"[2, 5, 6]",preparing
#liaqat,03 roseville garden,8766545432,4,"[3, 4, 5]",preparing               
                






