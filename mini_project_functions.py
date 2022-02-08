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
Press 1:  Look at Orders Dictionary
Press 2:  Create a New Order
Press 3:  Update an Existing Order
Press 4:  Further Updates on an Existing Order
Press 5:  Delete an Existing Order
=====================================
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

#def save_products():


