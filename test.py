import pymysql
import os
from dotenv import load_dotenv
import query_functions as fq
import app_functions as fn
import json
from prettytable import PrettyTable

# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# Establish a database connection
#def connection():
#    connection = pymysql.connect(
#        host = host,
#        user =user,
#        password =password,
#        database = database
#    )
#    return connection.cursor()
#def execute_query(query, values = None):
#    connection = pymysql.connect(
#    host = host,
#    user =user,
#    password =password,
#    database = database
#    )
#    cursor = connection.cursor()
#    if values:
#        cursor.execute(query, values)
#    else:
#        cursor.execute(query)
#        
#    connection.commit()
#    cursor.close()
#    connection.close()
#
################ Display products ######################

#def display_products():
#    connection = pymysql.connect(
#    host = host,
#    user =user,
#    password =password,
#    database = database
#    )
#    
#    cursor = connection.cursor()
#    cursor.execute("SELECT * FROM products")
#    
#    myresult = cursor.fetchall()
#    for x in myresult:
#        print(f'{[x[0]]}: name: {x[1].ljust(8)}   price$: {x[2]} ')
#
#    connection.commit()
#    cursor.close()
#    connection.close()
#display_products()
#new_product_name = input(f'\nSuggest a Name for The New Product.\n')
#product_price = float(input(f'\n Please Enter the Price of New Product.\n'))


#print('\nOur Products are Given Below:\n')
#sql = "INSERT INTO products (name, price$) VALUES (%s, %s)"
#val = (new_product_name, product_price)
#execute_query(sql, val)
#query = "SELECT * FROM products"
#val = (new_product_name, product_price)
#values = None
#execute_query(query, values, print)

#def list_items(query):
#    cursor.execute(query)
#    cursor.execute()
#    myresult = cursor.fetchall()
#    for x in myresult:
#        print(f'{[x[0]]}: name: {x[1].ljust(8)}   price$: {x[2]} ')


#sql = "UPDATE products SET name = 'milk tea' WHERE name = 'tea'"
#cursor.execute(sql)

#pq.display_products()
#user_input = int(input('\nChoose an Index to Update a Porduct:\n'))
#product_name = input(f'\nSuggest a New Name for The Product.\n')
#product_price = float(input(f'\n Please Enter New Price for The Product.\n'))

#query = f'UPDATE products SET name = "chae", price$= "1.45" WHERE id = "2"'
#pq.execute_query(query)
#query = "UPDATE products SET price$ =1.35 WHERE id = 2"
#pq.execute_query(query)



#print('\nOur Products are Given Below:\n')
#fq.display_products()
#
#user_input = input('\nChoose an Index to Update a Porduct:\n')
#product_name = input(f'\nSuggest a New Name for The Product.\n')
#product_price = input(f'\n Please Enter New Price for The Product.\n')
#if user_input:
#    if product_name:
#        if product_price:
#            query = f'UPDATE products SET name = "{product_name}", price$ = "{product_price}" \
#                    WHERE id = "{user_input}"'
#            fq.execute_query(query)
#        
#        else:
#            query = f'UPDATE products SET name = "{product_name}" WHERE id = "{user_input}"' 
#            fq.execute_query(query)
#    
#    elif product_price:
#        query = f'UPDATE products SET price$ = "{product_price}" WHERE id = "{user_input}"'
#        fq.execute_query(query)
#    
#    else:
#        pass




#def execute_query(query, values = None):
#    connection = pymysql.connect(
#    host = host,
#    user =user,
#    password =password,
#    database = database
#    )
#    cursor = connection.cursor()
#    if values:
#        cursor.execute(query, values)
#    else:
#        cursor.execute(query)
#        
#    connection.commit()
#    cursor.close()
#    connection.close()
#
#####################################################################
#
#def execute_query(query, values = None):
#    connection = pymysql.connect(
#    host = host,
#    user =user,
#    password =password,
#    database = database
#    )
#    cursor = connection.cursor()
#    if values:
#        cursor.execute(query, values)
#    else:
#        cursor.execute(query)
#        
#    connection.commit()
#    cursor.close()
#    connection.close()

#ef display_products():
#   connection = pymysql.connect(
#   host = host,
#   user =user,
#   password =password,
#   database = database
#   )
#   
#   cursor = connection.cursor()
#   cursor.execute("SHOW 'columns' FROM 'products'")
#   columns = cursor.description 
#   result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
#
#   print(result)
    #myresult = cursor.fetchall()
    #for x in myresult:
    #    print(x)
        #print(f'{[x[0]]}: name: {x[1].ljust(8)}   price$: {x[2]} ')


    
    #list =[]
    #
    #mydict = {}
    #for x in myresult:
    #    print(x)
    #    mydict["order_id"] = x[0]
    #    mydict["customer_name"] = x[1]
    #    mydict["customer_address"] = x[2]
    #    mydict["customer_phone"] = x[3]
    #    mydict["courier_id"] = x[4]
    #    mydict["order_status"] = x[5]
    #    mydict["items"] = x[6]
    #    list.append(mydict)
    #    for item in list:
    #        print(item)
    #    

#


#x = PrettyTable()
#x.field_names = ["product_id", "name", "price$"]
#x.add_row([1,"coke",1.30])
#
#print(x)
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

display_orders()


#def display_items(fields, query):
#    connection = pymysql.connect(
#    host = host,
#    user =user,
#    password =password,
#    database = database
#    )
#    x = PrettyTable()
#    cursor = connection.cursor()
#    cursor.execute(query)
#    
#    myresult = cursor.fetchall()
#
#    x.field_names = fields
#        
#    for row in myresult:
#        x.add_row(row)
#    print(x)
#
#    connection.commit()
#    cursor.close()
#    connection.close()
#
#fields = ["product_id", "name", "price$"]
#query =  "SELECT * FROM products"  
#display_items(fields, query)








#sql = "INSERT INTO products (name, price$) VALUES (%s, %s)"
#val = ("espresso", 1.90)
#cursor.execute(sql, val)

#print('\nOur Products are Given Below:\n')
#fn.csv_r_display('products.csv')
#list = str(input ("Please Enter Product Indices Seaparated By Commas:\n"))
#List = list.split(',')
#product_order_list =[]
#for item in List:
#    product_order_list.append(int(item))
#print(product_order_list)
#print('\nOur Couriers are Given Below:\n')
#fn.csv_r_display('couriers.csv')
#courier_index = int(input(f'\n Please Select A Courier Index:\n'))
#order_status = "preparing"
#data_row_list = [customer_name,customer_address,customer_phone,courier_index,product_order_list,order_status]
#fn.csv_appender('orders.csv', data_row_list)
#print('\nOur Current Orders are Given Below:\n')
#fn.csv_r_display('orders.csv')





