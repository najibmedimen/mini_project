
import app_functions as fn
import query_functions as fq
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
                fq.display_products(list = print)
                                
            elif product_input == 2:
                while True:
                    print('\nOur Products are Given Below:\n')
                    fq.display_products(list = print)
                    
                    new_product_name = input(f'\nSuggest a Name for The New Product.\n')
                    product_price = float(input(f'\n Please Enter the Price for New Product.\n'))
                    
                    query = "INSERT INTO products (name, price$) VALUES (%s, %s)"
                    values = (new_product_name, product_price)
                    fq.execute_query(query, values)

                    print('\nOur Products are Given Below:\n')
                    fq.display_products(list = print)  

                    fn.print_product_sub_menu()
                    further_options = int(input())
                    if further_options == 0:
                        break
            
            elif product_input == 3:
                
                while True:
                    print('\nOur Products are Given Below:\n')
                    fq.display_products(list = print)
                    
                    user_input = input('\nChoose an Index to Update a Porduct:\n')
                    product_name = input(f'\nSuggest a New Name for The Product.\n')
                    product_price = input(f'\n Please Enter New Price for The Product.\n')
                    if user_input:
                        if product_name:
                            if product_price:
                                query = f'UPDATE products SET name = "{product_name}", price$ = "{product_price}" \
                                        WHERE product_id = "{user_input}"'
                                fq.execute_query(query)
                            
                            else:
                                query = f'UPDATE products SET name = "{product_name}" WHERE product_id = "{user_input}"' 
                                fq.execute_query(query)
                        
                        elif product_price:
                            query = f'UPDATE products SET price$ = "{product_price}" WHERE product_id = "{user_input}"'
                            fq.execute_query(query)
                        
                        else:
                            pass
                    
                    print('\nOur Products are Given Below:\n')
                    fq.display_products(list = print)

                    fn.print_product_Up_sub_menu()
                    further_options = int(input())
                    if further_options == 0:
                        break
                                                                
            elif product_input == 4:
                while True:
                    print('\nOur Products are Given Below:\n')
                    fq.display_products(list = print)
                    
                    delete_input = int(input('\nPlease Choose an Index to delete a Product:\n'))
                    query = f'DELETE FROM products WHERE product_id = "{delete_input}"'
                    fq.execute_query(query)

                    print('\nOur Products are Given Below:\n')
                    fq.display_products(list = print)  

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
                fq.display_couriers(list = print)

            elif courier_input == 2:
                while True:
                    print('\nOur Couriers are Given Below:\n')
                    fq.display_couriers(list = print)

                    new_courier_name = input(f'\nSuggest a Name for The New Courier.\n')
                    courier_phone_number = input(f'\n Enter Courier Phone Number.\n')
                    query = "INSERT INTO couriers (name, phone) VALUES (%s, %s)"
                    values = (new_courier_name, courier_phone_number)
                    fq.execute_query(query, values)

                    print('\nOur Couriers are Given Below:\n')
                    fq.display_couriers(list = print)
                    
                    fn.print_courier_sub_menu()
                    further_options = int(input())
                    if further_options == 0:
                        break
                    
            elif courier_input == 3:
                while True:
                    print('\nOur Couriers are Given Below:\n')
                    fq.display_couriers(list = print)

                    user_input = input('\nChoose an Index to Update a Courier:\n')
                    courier_name = input(f'\nSuggest a New Name for The Courier.\n')
                    courier_phone = input(f'\n Please Enter New Phone Number.\n')
                    if user_input:
                        if courier_name:
                            if courier_phone:
                                query = f'UPDATE couriers SET name = "{courier_name}", phone = "{courier_phone}" \
                                        WHERE courier_id = "{user_input}"'
                                fq.execute_query(query)
                            
                            else:
                                query = f'UPDATE couriers SET name = "{courier_name}" WHERE courier_id = "{user_input}"' 
                                fq.execute_query(query)
                        
                        elif courier_phone:
                            query = f'UPDATE couriers SET phone = "{courier_phone}" WHERE courier_id = "{user_input}"'
                            fq.execute_query(query)
                        
                        else:
                            pass
                    
                    print('\nOur Couriers are Given Below:\n')
                    fq.display_couriers(list = print)

                    fn.print_courier_Up_sub_menu()
                    further_options = int(input())
                    if further_options == 0:
                        break

            elif courier_input == 4:
                while True:
                    print('\nOur Couriers are Given Below:\n')
                    fq.display_couriers(list = print)
                    
                    delete_input = int(input('\nPlease Choose an Index to delete a Courier:\n'))
                    query = f'DELETE FROM couriers WHERE courier_id = "{delete_input}"'
                    fq.execute_query(query)

                    print('\nOur Couriers are Given Below:\n')
                    fq.display_couriers(list = print) 

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
                fq.display_orders()
            
            elif order_input == 2:
                while True:

                    customer_name = input(f'\nPlease Enter Customer Name:\n')
                    customer_address = input(f'\nPlease Enter Customer Address:\n')
                    customer_phone = input(f'\nPlease Enter Customer Phone Number:\n')
                    
                    query1 = "INSERT INTO customers (name, address, phone) VALUES (%s, %s, %s)"
                    values1 = (customer_name, customer_address,customer_phone)
                    fq.execute_query(query1, values1)
    
                    customer_id = fq.return_customer_id(customer_phone)
    
                    fq.display_products(list = print)
    
                    list_of_products = fq.product_user_list()
    
                    fq.display_couriers(list = print)
    
                    courier_id = int(input("Please Enter The Courier ID:"))
    
                    status_id = 1
    
                    query2 = "INSERT INTO orders (customer_id, courier_id, status_id) VALUES (%s, %s, %s)"
                    values2 = (customer_id, courier_id, status_id)
                    order_id = fq.execute_query(query2, values2)
    
                    query3 = "INSERT INTO products_on_orders (order_id, product_id) VALUES (%s, %s)"
                    #order_id = fq.return_order_id(customer_id)
                    values3 = []
                    for i in list_of_products:
                        values3.append((order_id, i))
                    fq.execute_multiple_values(query3, values3)

                    fn.print_new_order_menu()
                    further_options = int(input())
                    if further_options == 0:
                        break


            elif order_input == 3:
                while True:
                
                    fq.display_orders()
                    order_input = int(input("\nPlease enter an order_id to update status:\n"))
                    
                    fq.display_status(list = print)
                    status_input = int(input("\nPlease enter status_id to update status:\n"))
                                    
                    query = f'UPDATE orders SET status_id = "{status_input}" WHERE order_id = "{order_input}"'
                    fq.execute_query(query)

                    fn.print_order_status_sub_menu()
                    further_options = int(input())
                    if further_options == 0:
                        break
                

            elif order_input == 4:
                while True:

                    fq.display_orders()
                    order_id_input = int(input("\nPlease enter an order_id to update an order:\n"))
                    customer_id = fq.return_customer_id_from_orders(order_id_input)
    
                    name = input(f'\nPlease Enter Customer Name:\n')
                    address = input(f'\nPlease Enter Customer Address:\n')
                    phone = input(f'\nPlease Enter Customer Phone Number:\n')
    
                    query1 = f'UPDATE customers SET name = "{name}", address = "{address}", \
                        phone = "{phone}" WHERE customer_id = "{customer_id}"'
                    fq.execute_query(query1)
    
                    fq.display_products(list = print)
                    list_of_products = fq.product_user_list()
    
                    fq.display_couriers(list = print)
                    courier_id = int(input("\nPlease Enter The Courier ID:\n"))
    
                    query2 = f'UPDATE orders SET customer_id = "{customer_id}", courier_id = "{courier_id}"\
                        WHERE order_id = "{order_id_input}"'
                    fq.execute_query(query2)
                    
                    query3 = f'DELETE FROM products_on_orders WHERE order_id = "{order_id_input}"'
                    fq.execute_query(query3)
    
                    query4 = "INSERT INTO products_on_orders (order_id, product_id) VALUES (%s, %s)"
                    values = []
                    for i in list_of_products:
                        values.append(( order_id_input, i))
                    fq.execute_multiple_values(query4, values) 

                    fn.print_order_Up_sub_menu()
                    further_options = int(input())
                    if further_options == 0:
                        break    

            
            elif order_input == 5:
                while True:

                    fq.display_orders()
                    order_id_input = int(input("\nPlease enter an order_id to update an order:\n"))
    
                    query = f'DELETE FROM orders WHERE order_id = "{order_id_input}"'
                    fq.execute_query(query)
    
                    fq.display_orders()

                    fn.print_order_delete_sub_menu()
                    further_options = int(input())
                    if further_options == 0:
                        break
                
              






#customer_name,customer_address,customer_phone,courier,product_order_list,status
#najib khan,15 Ashton place,0789887334,2,[1,2,3],preparing
#najaf,15 piccadilly,089767334,1,[1],preparing
#rana,12 china town,745277744,3,"[2, 5, 6]",preparing
#liaqat,03 roseville garden,8766545432,4,"[3, 4, 5]",preparing               
                






