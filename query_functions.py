import pymysql
import os
from dotenv import load_dotenv
from prettytable import PrettyTable

# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

##########Executes querries ####################
def execute_query(query, values = None):
    connection = pymysql.connect(
    host = host,
    user =user,
    password =password,
    database = database
    )
    cursor = connection.cursor()
    if values:
        cursor.execute(query, values)
    else:
        cursor.execute(query)
        
    connection.commit()
    last_row_id = cursor.lastrowid
    cursor.close()
    connection.close()
    return last_row_id

#query = "SELECT * FROM products"
#values = (new_product_name, product_price)
#values = None
#execute_query(query, values, print)

#################################################
############Execute multiple values in query ####
###############################################
##########Executes querries ####################
def execute_multiple_values(query, values = None):
    connection = pymysql.connect(
    host = host,
    user =user,
    password =password,
    database = database
    )
    cursor = connection.cursor()
    if values:
        cursor.executemany(query, values)
    else:
        cursor.executemany(query)
        
    connection.commit()
    cursor.close()
    connection.close()

#query = "SELECT * FROM products"
#values = (new_product_name, product_price)
#values = None
#execute_query(query, values, print)


#################################
#### Display full table of products #######
##############################
def display_products(dict ='', list = ''):
    connection = pymysql.connect(
    host = host,
    user =user,
    password =password,
    database = database
    )
    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products")
    
    myresult = cursor.fetchall()
    if dict:
        for x in myresult:
            product= {"id":x[0], "name":x[1], "price$":x[2]}
            print(product)
    if list:
        for x in myresult:
            print(f'{[x[0]]}: name: {x[1].ljust(8)}   price$: {x[2]} ')

    connection.commit()
    cursor.close()
    connection.close()

#################################
#### Display full table of couriers #######
##############################
def display_couriers(dict ='', list = ''):
    connection = pymysql.connect(
    host = host,
    user =user,
    password =password,
    database = database
    )
    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM couriers")
    
    myresult = cursor.fetchall()
        
    if dict:
        for x in myresult:
            product= {"id":x[0], "name":x[1], "phone":x[2]}
            print(product)
    if list:
        for x in myresult:
            print(f'{[x[0]]}: name: {x[1].ljust(8)}   phone: {x[2]}')

    connection.commit()
    cursor.close()
    connection.close()

#################################
#### Display full table of orders #######
##############################
def display_orders():
    connection = pymysql.connect(
    host = host,
    user =user,
    password =password,
    database = database
    )
    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM orders")
    
    myresult = cursor.fetchall()
    my_list =[]
    my_dict = {}
    for x in myresult:
        my_dict['order_id'] = x[0]
        my_dict['customer_id'] = x[1]  
        my_dict['courier_id'] = x[2]
        my_list.append(my_dict)
    
    for item in my_list:
        print(item)
    connection.commit()
    cursor.close()
    connection.close()

#display_orders()
def display_orders():
    connection = pymysql.connect(
    host = host,
    user =user,
    password =password,
    database = database
    )
    x = PrettyTable()
    
    cursor = connection.cursor()
   
    cursor.execute("\
    SELECT orders.order_id, customers.name, customers.address, customers.phone, couriers.courier_id, order_status.name, products_on_orders.product_id \
    FROM orders \
    JOIN customers\
    ON orders.customer_id = customers.customer_id\
    JOIN couriers\
    ON orders.courier_id = couriers.courier_id\
    JOIN products_on_orders\
    ON orders.order_id = products_on_orders.order_id\
    JOIN order_status\
    ON orders.status_id = order_status.status_id\
    order by orders.order_id ASC\
    ")

    myresult = cursor.fetchall()
   
    
    fields = ["order_id", "customer_name", "customer_address", "customer_phone", "courier_id", "order_status", "product_id"]
    x.field_names = fields
        
    for row in myresult:
        x.add_row(row)
    print(x)

    connection.commit()
    cursor.close()  
    connection.close()


############################ get customer id ###
def return_customer_id(phone):
    connection = pymysql.connect(
    host = host,
    user =user,
    password =password,
    database = database
    )
    cursor = connection.cursor()
    sql = f'SELECT customer_id FROM customers WHERE phone = "{phone}"'
    cursor.execute(sql)
    myresult = cursor.fetchall()
    for x in myresult:
        return list(x)[0]
    connection.commit()
    cursor.close()
    connection.close()


##################### comma separated input ##############
def product_user_list():
    list = str(input ("Please Enter Product Indices Separated By Commas:\n"))
    List = list.split(',')
    product_order_list =[]
    for item in List:
        product_order_list.append(int(item))
    return product_order_list

################# returns order_id using customer_id #################

def return_order_id(customer_id):
    connection = pymysql.connect(
    host = host,
    user =user,
    password =password,
    database = database
    )
    cursor = connection.cursor()
    sql = f'SELECT order_id FROM orders WHERE customer_id = "{customer_id}"'
    cursor.execute(sql)
    myresult = cursor.fetchall()
    for x in myresult:
        return list(x)[0]
    connection.commit()
    cursor.close()
    connection.close()

################# order status ###########################

def display_status(dict ='', list = ''):
    connection = pymysql.connect(
    host = host,
    user =user,
    password =password,
    database = database
    )
    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM order_status")
    
    myresult = cursor.fetchall()
    if dict:
        for x in myresult:
            product= {"status_id":x[0], "name":x[1]}
            print(product)
    if list:
        for x in myresult:
            print(f'{[x[0]]}: name: {x[1].ljust(8)}')

    connection.commit()
    cursor.close()
    connection.close()

############ get customer_id using order_id ###################

def return_customer_id_from_orders(order_id):
    connection = pymysql.connect(
    host = host,
    user =user,
    password =password,
    database = database
    )
    cursor = connection.cursor()
    sql = f'SELECT customer_id FROM orders WHERE order_id = "{order_id}"'
    cursor.execute(sql)
    myresult = cursor.fetchall()
    for x in myresult:
        return list(x)[0]
    connection.commit()
    cursor.close()
    connection.close()

###########Display items as a table from database ############

def display_products():
    connection = pymysql.connect(
    host = host,
    user =user,
    password =password,
    database = database
    )
    x = PrettyTable()
    
          
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products")
    
    myresult = cursor.fetchall()
    
    fields = ["product_id", "name", "price$"]
    x.field_names = fields
        
    for row in myresult:
        x.add_row(row)
    print(x)

    connection.commit()
    cursor.close()
    connection.close()

######### Display couriers from database ##########
def display_couriers():
    connection = pymysql.connect(
    host = host,
    user =user,
    password =password,
    database = database
    )
    x = PrettyTable()
    
          
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM couriers")
    
    myresult = cursor.fetchall()
    
    fields = ["courier_id", "name", "phone"]
    x.field_names = fields
        
    for row in myresult:
        x.add_row(row)
    print(x)

    connection.commit()
    cursor.close()
    connection.close()

