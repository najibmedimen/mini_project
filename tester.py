
from mini_project_functions import file_opener, display_list_by_index, file_writer, file_writer2, print_products_menu, print_main_menu
from mini_project_functions import print_product_sub_menu, print_couriers_menu, print_orders_menu
from mini_project_functions import return_list, delete_item_from_list, update_listitem_by_name
import mini_project_functions as fn
products  = file_opener("products.txt")
couriers = file_opener("couriers.txt")
#order_status = file_opener("order_status.txt")
#
#orders=[
#{"customer_name": "najib khan", 
#"customer_address": " 15 Ashton place",
#"customer_phone": "0789887334",
#"courier": 2,
#"status": "preparing"
#}, 
#{"customer_name": "najaf", 
#"customer_address": " 15 piccadilly",
#"customer_phone": "0789767334",
#"courier": 1,
#"status": "preparing"}
#]
##def order_opener(orders):
##        with open file 
#import csv
#
import csv
#with open('people.csv', mode='w') as file:
#writer = csv.writer(file, delimiter=',')
#writer.writerow(['Joe', 'Bloggs', 40])

#This code is perfect for reading the CSV files

#def csv_r_display(file):
#        with open(file, 'r') as file_object:
#                csv_file = csv.DictReader(file_object)
#                list = []
#                for row in csv_file:
#                        list.append(row)
#                for index, order in enumerate(list):
#                        print(f'order {index+1}: {order}')
#
#csv_r_display("products.csv")


# The following code is successfully appending the orders in csv
# while appending it does not delete anything
#def csv_appender(file):
#
#    with open(file, mode='a') as file_object:
#        writer = csv.writer(file_object, delimiter=',')
#        writer.writerow(['cake', 1.5])
#        return writer
#csv_appender("products.csv")

# open the people.csv and write row from dict


#def dict_writer(file, fieldnames, data_row):
#    file = file
#    fieldnames = fieldnames
#    data_row = data_row
#    with open(file, mode='w') as file:
#        
#        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter = ',')
#        writer.writeheader()
#        writer.writerow(data_row)
#fieldnames = ['name','price($)']
#data_row = {'latte':1.2, 'coke':1.3}
#dict_writer("products.csv", fieldnames, data_row)


# This is perfect dict writer, deletes and overwrites file
#def func(row_dictdata, fieldnames):
#    with open('people.csv', mode='w', newline = '') as file:
#        writer = csv.DictWriter(file, fieldnames=fieldnames)
#        writer.writeheader()
#        writer.writerow(row_dictdata)
#        writer.writerow(row_dictdata)
#row_dictdata = {
#    'first_name': 'Jan',
#    'last_name': 'Smith',
#    'age': 60
#    }
#fieldnames_listdata = ['first_name', 'last_name', 'age']
#func(row_dictdata, fieldnames_listdata)


#This is perfect csv writer, it deletes existing file and
#then writes whatever is provided in nested list
#def csv_row_writer(c):
#    with open('people.csv', mode='w', newline = '') as file:
#        writer = csv.writer(file, delimiter=',')
#        for item in c:
#            writer.writerow(item)
#c= [
#    ['Joe', 'Bloggs', 40],
#    ['Jane', 'Smith', 50]
#    ]       
#csv_row_writer(c)



#def print_order_list(file):
#        print("\n")
#        for index, order in enumerate(file):
#                print(f' order {index+1}: {order}')
#        print("\n")
#

#def create_new_order(display_list_by_index, couriers, order_status):
#        new_order_dict =dict()
#        while True:
#                customer_name = input("\nPlease Enter Customer Name:\n")
#                customer_address = input("\nPlease Enter Customer Address:\n")
#                customer_phone = input("\nPlease Enter Customer Phone Number:\n")
#                print("\n")
#                display_list_by_index(couriers)
#           
#                courier_index = int(input("\nPlease Choose a Courier Index for Your Order:\n"))
#                print("\n")
#                display_list_by_index(order_status)
#                set_order_status = int(input("\nPlease Set The Order Status By Choosing An Index:\n"))
#                status = order_status[set_order_status-1]
#
#                new_order_dict["customer_name"] = customer_name
#                new_order_dict["customer_address"] = customer_address
#                new_order_dict["customer_phone"] = customer_phone
#                new_order_dict["courier"] = courier_index
#                new_order_dict["status"] = status.strip()
#                orders.append(new_order_dict)
#                options = int(input("press 0 to exit or 1 to place another order\n"))
#                if options == 0:
#                        break
#create_new_order(display_list_by_index, couriers, order_status)               
#
#print_order_list(orders)


