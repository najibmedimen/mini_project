import csv
from prettytable import PrettyTable
def print_main_menu():
    print( """\n
Welcome to ChaCha Cafe! \n
Please Select from the Main Menu. \n
============ Main Menu =========== \n
Press 0:  Exit App
Press 1:  Product Menu
Press 2:  Courier Menu
Press 3:  Orders Menu  
==================================
""")

def print_products_menu():
    print("""\n
Please Select From Options for The Product Menu: \n
============ Product Menu ========== \n
Press 0:  Return to Main Menu
Press 1:  Look at Product List
Press 2:  Suggest a New Product
Press 3:  Update an Existing Product
Press 4:  Delete an Existing Product
=====================================
""")

def print_product_sub_menu():
    print("""\n
Select From Options for The Product Sub-Menu: \n
========== Product Sub-Menu ========= \n
Press 0:  Return to Product Menu
Press 1:  Suggest Another Product
=====================================\n
""")

def print_courier_sub_menu():
    print("""\n
Select From Options for The Courier Sub-Menu: \n
========== Courier Sub-Menu ========= \n
Press 0:  Return to Courier Menu
Press 1:  Add Another Courier
=====================================\n
""")

def print_product_update_menu():
    print(f'''\n
Select an Option From Product Update-Menu: \n
======== Product Update-Menu ======= \n
Press 1:  Update Product Index
Press 2:  Update Product Name
=====================================\n
''')

def print_product_Up_sub_menu():
    print("""\n
More Options for Product Update sub-Menu: \n
======= Product Update Sub-Menu ====== \n
Press 0:  Return to Product Menu
Press 1:  Update Another Product
=====================================\n
""")

def print_product_delete_sub_menu():
    print("""\n
Options for Product Delete sub-Menu: \n
======= Product Delete Sub-Menu ====== \n
Press 0:  Return to Product Menu
Press 1:  Delete Another Product
=====================================\n
""") 

def print_couriers_menu():
    print("""\n
Please Select From Options for The Couriers Menu: \n
=========== Couriers Menu ========= \n
Press 0:  Return to Main Menu
Press 1:  Look at Couriers List
Press 2:  Create a New Courier
Press 3:  Update an Existing Courier
Press 4:  Delete an Existing Courier
=====================================
""")

def print_courier_Up_sub_menu():
    print("""\n
More Options for Courier Update sub-Menu: \n
======= Courier Update Sub-Menu ====== \n
Press 0:  Return to Courier Menu
Press 1:  Update Another Courier
=====================================\n
""")

def print_product_update_menu():
    print(f'''\n
Select an Option From Product Update-Menu: \n
======== Product Update-Menu ======= \n
Press 1: Update Product & Price
Press 2: Update Product
Press 3: Update Price
=====================================\n
''')

def print_courier_update_menu():
    print(f'''\n
Select an Option From Courier Update-Menu: \n
======== Courier Update-Menu ======= \n
Press 1: Update Courier & Phone
Press 2: Update Courier
Press 3: Update Phone
=====================================\n
''')

def print_courier_delete_sub_menu():
    print("""\n
Options for Courier Delete sub-Menu: \n
======= Courier Delete Sub-Menu ====== \n
Press 0:  Return to Courier Menu
Press 1:  Delete Another Courier
=====================================\n
""")

def print_orders_menu():
    print("""\n
Please Select From Options for The Orders Menu: \n
============ Orders Menu ========== \n
Press 0:  Return to Main Menu
Press 1:  Look at Our Orders 
Press 2:  Create a New Order
Press 3:  Update Order Status
Press 4:  Update an Order
Press 5:  Delete an Order
=====================================
""")

def print_order_status_menu():
    print("""\n
============ Orders Status ========== \n
1:  Preparing
2:  Ready
3:  Out for Delivery
4:  Delivered
=====================================
""")

def print_order_Up_sub_menu():
    print("""\n
More Options for Order Update sub-Menu: \n
======= Order Update Sub-Menu ====== \n
Press 0:  Return to Orders Menu
Press 1:  Update Another Order
=====================================\n
""")

def print_order_delete_sub_menu():
    print("""\n
Options for Order Delete sub-Menu: \n
======= Order Delete Sub-Menu ====== \n
Press 0:  Return to Orders Menu
Press 1:  Delete Another Order
=====================================\n
""")

def print_order_status_sub_menu():
    print("""\n
More Options for Order Status Sub-Menu: \n
======= Order Status Sub-Menu ====== \n
Press 0:  Return to Orders Menu
Press 1:  Update Another Order Status
=====================================\n
""")

def print_new_order_menu():
    print("""\n
More Options for New Orders: \n
======= New Order Sub-Menu ====== \n
Press 0:  Return to Orders Menu
Press 1:  Enter Another Order
=====================================\n
""")







#def open_products():
#    with open ("products.txt") as file_object:
#        products = file_object.readlines() 
#        for i, product in enumerate(products):
#                        print(f' {i+1}: {product.strip()}')
#def open_products():
#    with open ("products.txt") as file_object:
#        products = file_object.readlines()
#        for i, product in enumerate(products):
#            print(f' {i+1}: {product.strip()}')

def file_opener(file):
    with open (file) as file_object:
        items = file_object.readlines()
        return items

def return_list(products):
    List = []
    for i in products:
        List.append(i.strip())
    return List

def display_list_by_index(items):
    for i, product in enumerate(items):
        print(f' {i+1}: {product.strip()}')

def delete_item_from_list(products, item_name):
        earlier_index_of_product = return_list(products).index(item_name)
        del products[earlier_index_of_product]
        return products
        
def update_listitem_by_name(products, product_name,new_name):
        earlier_index_of_product = return_list(products).index(product_name)
        products[earlier_index_of_product] = new_name
        return products
# with r+, this replaces the first line with the user_input text
def file_writer(file_w, items_list):
    with open(file_w, 'w') as file:
        for item in items_list:
            file.write(item.strip()+ '\n')



#def csv_r_display(file):
#    list = []
#    with open(file, 'r') as file_object:
#        csv_file = csv.DictReader(file_object)
#        for row in csv_file:
#            list.append(row)
#    for index, order in enumerate(list):
#        print(f' {index+1}: {order}')



#def file_writer(file, user_input):
#    with open(file, 'w') as file_object:
#        file_object.write(user_input)
#    #file_object.close

# this appends to the end of the list
def file_writer2(file, user_input):
    with open(file, 'a') as file_object:
        file_object.write(user_input)
    file_object.close    

#file_opener("products.txt")
        
#display_list()

    

def save_products():
    with open ("products.txt") as file_object:
        products = file_object.readlines() 
        for i, product in enumerate(products):
                        print(f' {i+1}: {product.strip()}')
     
def list_items(products):
    for i, product in enumerate(products):
        print(f' {i+1}: {product.strip()}')

def open_couriers():
    with open ("couriers.txt") as file_object:
        couriers = file_object.readlines()
        for i, courier in enumerate(couriers):
                        print(f' {i+1}: {courier.strip()}')

def list_couriers(couriers):
    for i, courier in enumerate(couriers):
        print(f' {i+1}: {courier.strip()}')

##############################################
######### Below are CSV Functions ############
##############################################

#This code is perfect for opening and reading the CSV files
#######################################################
def csv_opener(file):
        with open(file, 'r') as file_object:
                csv_file = csv.DictReader(file_object)
                return csv_file

#products = csv_opener('products.csv')
######################################################
#It displays the file_object from a read mode csv_opener
######################################################

def csv_file_displayer(file):
    list = []
    for row in file:
            list.append(row)
    for index, order in enumerate(list):
            print(f' {index+1}: {order}')
#csv_file_displayer(products)
#csv_r_display("products.csv")

#####################################################
# this is csv read only and siaplay function
#####################################################
def csv_r_display(file):
    list = []
    with open(file, 'r') as file_object:
        csv_file = csv.DictReader(file_object)
        for row in csv_file:
            list.append(row)
    for index, order in enumerate(list):
        print(f' {index+1}: {order}')
#csv_r_display("products.csv")
######################################################
# The following code is successfully appending the orders in csv
# while appending it does not delete anything
########################################################
def csv_appender(file,b):
    with open(file, mode= 'a', newline='') as file_object:
        writer = csv.writer(file_object, delimiter=',')
        writer.writerow(b)
        object = writer
        return object

#data_row_list = ['cake', 1.5]
#csv_appender('products.csv', data_row_list)
########################################################

# open the people.csv and write row from dict
# it first deletes and thgen writes data
################################################################
def dict_writer(file, fieldnames, data_row):
    file = file
    fieldnames = fieldnames
    data_row = data_row
    with open(file, mode='w') as file:
        
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter = ',')
        writer.writeheader()
        writer.writerow(data_row)
#fieldnames = ['name','price($)']
#data_row = {'latte':1.2, 'coke':1.3}
#dict_writer("products.csv", fieldnames, data_row)
#####################################################################

# This is perfect dict writer, deletes and overwrites file
###################################################################
def func(row_dictslist, fieldnames):
    with open('people.csv', mode='w', newline = '') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for item in row_dictslist:
            writer.writerow(item)
        
#row_dictslist = [{
#    'first_name': 'Jan',
#    'last_name': 'Smith',
#    'age': 60
#    }]
#fieldnames_list = ['first_name', 'last_name', 'age']
#func(row_dictslist, fieldnames_list)

#########################################################
#This is perfect csv writer, it deletes existing file and
#then writes whatever is provided in nested list
def csv_row_writer(c):
    with open('people.csv', mode='w', newline = '') as file:
        writer = csv.writer(file, delimiter=',')
        for item in c:
            writer.writerow(item)
#c= [
#    ['Joe', 'Bloggs', 40],
#    ['Jane', 'Smith', 50]
#    ]       
#csv_row_writer(c)
###########################################################
### This is my proper dict writer##########################
###########################################################
def dict_writer(file,list,header_names):
    with open (file, 'w', newline='') as file_object:
        newfile = csv.DictWriter(file_object, fieldnames = header_names)
        newfile.writeheader()
        for i in range (len(list)):
                newfile.writerow(list[i])
#order_update_writer(give csv file, give a list of dicts, give a list of header names)
###########################################################
############ This perfect csv reader that returns a list
def csv_reader(file):
    orders_list = []
    with open(file, 'r') as file_object:
        csv_file = csv.DictReader(file_object)
        for row in csv_file:
                orders_list.append(row)
    return orders_list
#csv_reader('orders.csv')
##########order update status #########################
###########################################################
def order_status_update(a):
    if a =='1':
        status = 'Preparing'
    elif a =='2':
        status = 'Ready'
    elif a =='3':
        status = 'Out for Delivery'
    elif a =='4':
        status = 'Delivered'
    else:
        print('Please Enter a Valid Index')
    return status
#order_status_update(user_index_input)
#########################################################

