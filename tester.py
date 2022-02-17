
from subprocess import STARTF_USESHOWWINDOW
from mini_project_functions import file_opener, display_list_by_index, file_writer, file_writer2, print_products_menu, print_main_menu
from mini_project_functions import print_product_sub_menu, print_couriers_menu, print_orders_menu
from mini_project_functions import return_list, delete_item_from_list, update_listitem_by_name
import mini_project_functions as fn
import csv
products  = file_opener("products.txt")
couriers = file_opener("couriers.txt")



#orders = fn.csv_opener('orders.csv')
#with open('people.csv', mode='w') as file:
#        fieldnames = ['first_name', 'last_name', 'age']
#        writer = csv.DictWriter(file, fieldnames=fieldnames)
#        writer.writeheader()
#        writer.writerow({ 'first_name': 'Jan','last_name': 'Smith','age': 60})

#lisst = [
#{'customer_name': 'najib khan', 'customer_address': '15 Ashton place', 'customer_phone': '0789887334', 'courier': '2', 'product_order_list': '[1,3]','status': 'preparing'},
#{'customer_name': 'najaf', 'customer_address': '15 piccadilly', 'customer_phone': '089767334', 'courier': '1', 'product_order_list': '[1]', 'status': 'preparing'},
#{'customer_name': 'rana', 'customer_address': '12 china town', 'customer_phone': '745277744', 'courier': '7', 'product_order_list': '[2, 5, 6]', 'status': 'preparing'},
#{'customer_name': 'liaqat', 'customer_address': '03 roseville garden', 'customer_phone': '8766545432', 'courier': '4', 'product_order_list': '[3, 4, 5]', 'status': 'preparing'}
#] 
#print(list)
#list = []
#with open('orders.csv', 'r') as file_object:
#        csv_file = csv.DictReader(file_object)
#        for row in csv_file:
#                list.append(row)
#        user_input1 = int(input('\nPlease Enter The Order Index to be Changed:\n'))
#        row = list[user_input1]
#        print(row)
#        user_input2 = input('\nPlease Choose A Key to Update:\n')
#        user_input3 = input('\nPlease Suggest a New Value for The Key:\n')
#        list[user_input1][user_input2] = user_input3
#print(list)
#with open ('orders.csv', 'w', newline='') as file:
#        column_names = ['customer_name','customer_address','customer_phone','courier','product_order_list','status']
#        myfile = csv.DictWriter(file, fieldnames = column_names)
#        myfile.writeheader()
#        for i in range (len(list)):
#                myfile.writerow(list[i])
#                print(f'finished writing row{i}')

                #with open('orders.csv', 'w',newline='') as file:
                #        fieldnames= ['customer_name','customer_address','customer_phone','courier','product_order_list','status']
                #        writer = csv.DictWriter(file,  delimiter=",", fieldnames = fieldnames) 
                #        writer.writeheader()
                #        for item in list:
                #                writer.writerow(item)                               writer.writerow(item)

                        #writer.writerow({'customer_name': 'naka','customer_address': '12 james ville','customer_phone':'08457','courier':'1','product_order_list':'[1,2]','status':'ready'})


#with open('orders.csv', 'r+', newline ='') as subscribers_csv:
#        #fields = ['customer_name','customer_address','customer_phone','courier','product_order_list','status']
#        reader = csv.DictReader(subscribers_csv)
#        writer = csv.DictWriter(subscribers_csv,  delimiter=",", fieldnames= ['customer_name','customer_address','customer_phone','courier','product_order_list','status'])
#        for subscriber in reader:
#                subscriber_row = {'customer_name': subscriber['customer_name'],
#                'customer_address': subscriber['customer_address'],
#                'customer_phone': subscriber['customer_phone'],
#                'courier': subscriber['courier'],
#                'product_order_list': subscriber['product_order_list'],
#                'status': subscriber['status']}
#                writer.writerow(subscriber)

#customer_name,customer_address,customer_phone,courier,product_order_list,status
#najib khan,15 Ashton place,0789887334,2,"[1,3]",preparing
#najaf,15 piccadilly,089767334,1,[1],preparing
#rana,12 china town,745277744,7,"[2, 5, 6]",preparing
#liaqat,03 roseville garden,8766545432,4,"[3, 4, 5]",preparing
############################################################################
###########################################################################
########this is fully working to change anything in a csv list##############
#def order_update_input(file):
#        orders_list = []
#        with open(file, 'r') as file_object:
#                csv_file = csv.DictReader(file_object)
#                for row in csv_file:
#                        orders_list.append(row)
#                fn.csv_r_display("orders.csv", 'Order')
#                user_input1 = int(input('\nPlease Enter The Order Index to be Changed:\n'))
#                row = orders_list[user_input1-1]
#                print(row)
#                user_input2 = input('\nPlease Choose A Key to Update:\n')
#                user_input3 = input('\nPlease Suggest a New Value for The Key:\n')
#        
#                orders_list[user_input1-1][user_input2] = user_input3
#                return orders_list
#        
#
#def order_update_writer(list,header_names):
#        with open ('orders.csv', 'w', newline='') as file:
#                #column_names = ['customer_name','customer_address','customer_phone','courier','product_order_list','status']
#                
#                newfile = csv.DictWriter(file, fieldnames = header_names)
#                newfile.writeheader()
#                for i in range (len(list)):
#                        newfile.writerow(list[i])
#                        print(f'finished writing row{i}')
#orders_list = order_update_input('orders.csv')
#header_names = ['customer_name','customer_address','customer_phone','courier','product_order_list','status']
#order_update_writer(orders_list,header_names)
################################################################################
#def order_status_update_input(file):
#        orders_list = []
#        with open(file, 'r') as file_object:
#                csv_file = csv.DictReader(file_object)
#                for row in csv_file:
#                        orders_list.append(row)
#        return orders_list


#Products
#name,price($)
#coke,1.10
#coffee,1.50
#tea,1.10
#latte,1.3
#mocha,1.3
#espresso,1.0
#cafeno,1.5
