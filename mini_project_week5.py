
import app_functions as fn
import query_function as fq
import csv


orders = fn.csv_opener('orders.csv')
status = ['preparing','ready for collection','out for delivery','delivered']

while True: 
    fn.print_main_menu()  
    users = int(input())
            
    if users == 0:
        print("\nThanks for Visiting! See You Soon! \n")
        break

    elif users ==1:
        while True:
            fn.print_products_menu()
            product_input = int(input())
            
            if product_input == 0:
                break

            elif product_input == 1:
                print('\nOur Products are Given Below:\n')
                fq.display_products()
                                
            elif product_input == 2:
                while True:
                    print('\nOur Products are Given Below:\n')
                    fq.display_products()
                    
                    new_product_name = input(f'\nSuggest a Name for The New Product.\n')
                    product_price = float(input(f'\n Please Enter the Price for New Product.\n'))
                    
                    query = "INSERT INTO products (name, price$) VALUES (%s, %s)"
                    values = (new_product_name, product_price)
                    fq.execute_query(query, values)

                    print('\nOur Products are Given Below:\n')
                    fq.display_products()  

                    fn.print_product_sub_menu()
                    further_options = int(input())
                    if further_options == 0:
                        break
            
            elif product_input == 3:
                
                while True:
                    print('\nOur Products are Given Below:\n')
                    fq.display_products()
                    
                    user_input = input('\nChoose an Index to Update a Porduct:\n')
                    product_name = input(f'\nSuggest a New Name for The Product.\n')
                    product_price = input(f'\n Please Enter New Price for The Product.\n')
                    if user_input:
                        if product_name:
                            if product_price:
                                query = f'UPDATE products SET name = "{product_name}", price$ = "{product_price}" \
                                        WHERE id = "{user_input}"'
                                fq.execute_query(query)
                            
                            else:
                                query = f'UPDATE products SET name = "{product_name}" WHERE id = "{user_input}"' 
                                fq.execute_query(query)
                        
                        elif product_price:
                            query = f'UPDATE products SET price$ = "{product_price}" WHERE id = "{user_input}"'
                            fq.execute_query(query)
                        
                        else:
                            pass
                    
                    print('\nOur Products are Given Below:\n')
                    fq.display_products()

                    fn.print_product_Up_sub_menu()
                    further_options = int(input())
                    if further_options == 0:
                        break
                                                                
            elif product_input == 4:
                while True:
                    print('\nOur Products are Given Below:\n')
                    fq.display_products()
                    
                    delete_input = int(input('\nPlease Choose an Index to delete a Product:\n'))
                    query = f'DELETE FROM products WHERE id = "{delete_input}"'
                    fq.execute_query(query)

                    print('\nOur Products are Given Below:\n')
                    fq.display_products()  

                    fn.print_product_delete_sub_menu()
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
                fq.display_couriers()

            elif courier_input == 2:
                while True:
                    print('\nOur Couriers are Given Below:\n')
                    fq.display_couriers()

                    new_courier_name = input(f'\nSuggest a Name for The New Courier.\n')
                    courier_phone_number = input(f'\n Enter Courier Phone Number.\n')
                    query = "INSERT INTO couriers (name, phone) VALUES (%s, %s)"
                    values = (new_courier_name, courier_phone_number)
                    fq.execute_query(query, values)

                    print('\nOur Couriers are Given Below:\n')
                    fq.display_couriers()
                    
                    fn.print_courier_sub_menu()
                    further_options = int(input())
                    if further_options == 0:
                        break
                    
            elif courier_input == 3:
                while True:
                    print('\nOur Couriers are Given Below:\n')
                    fq.display_couriers()

                    user_input = input('\nChoose an Index to Update a Courier:\n')
                    courier_name = input(f'\nSuggest a New Name for The Courier.\n')
                    courier_phone = input(f'\n Please Enter New Phone Number.\n')
                    if user_input:
                        if courier_name:
                            if courier_phone:
                                query = f'UPDATE couriers SET name = "{courier_name}", phone = "{courier_phone}" \
                                        WHERE id = "{user_input}"'
                                fq.execute_query(query)
                            
                            else:
                                query = f'UPDATE couriers SET name = "{courier_name}" WHERE id = "{user_input}"' 
                                fq.execute_query(query)
                        
                        elif courier_phone:
                            query = f'UPDATE couriers SET phone = "{courier_phone}" WHERE id = "{user_input}"'
                            fq.execute_query(query)
                        
                        else:
                            pass
                    
                    print('\nOur Couriers are Given Below:\n')
                    fq.display_couriers()

                    fn.print_courier_Up_sub_menu()
                    further_options = int(input())
                    if further_options == 0:
                        break

            elif courier_input == 4:
                while True:
                    print('\nOur Couriers are Given Below:\n')
                    fq.display_couriers()
                    
                    delete_input = int(input('\nPlease Choose an Index to delete a Courier:\n'))
                    query = f'DELETE FROM couriers WHERE id = "{delete_input}"'
                    fq.execute_query(query)

                    print('\nOur Couriers are Given Below:\n')
                    fq.display_couriers() 

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
                






