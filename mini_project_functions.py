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

def display_list(items):
    for i, product in enumerate(items):
        print(f' {i+1}: {product.strip()}')

# with r+, this replaces the first line with the user_input text
def file_writer(file, user_input):
    with open(file, 'r+') as file_object:
        file_object.write(user_input)
    file_object.close

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


