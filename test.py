import pymysql
import os
from dotenv import load_dotenv
import query_function as fq
import app_functions as fn

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