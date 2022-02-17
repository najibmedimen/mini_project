import pymysql
import os
from dotenv import load_dotenv

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
    cursor.close()
    connection.close()

#query = "SELECT * FROM products"
#values = (new_product_name, product_price)
#values = None
#execute_query(query, values, print)


#################################
#### Display full table of products #######
##############################
def display_products():
    connection = pymysql.connect(
    host = host,
    user =user,
    password =password,
    database = database
    )
    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products")
    
    myresult = cursor.fetchall()
    for x in myresult:
        print(f'{[x[0]]}: name: {x[1].ljust(8)}   price$: {x[2]} ')

    connection.commit()
    cursor.close()
    connection.close()

#################################
#### Display full table of couriers #######
##############################
def display_couriers():
    connection = pymysql.connect(
    host = host,
    user =user,
    password =password,
    database = database
    )
    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM couriers")
    
    myresult = cursor.fetchall()
    for x in myresult:
        print(f'{[x[0]]}: name: {x[1].ljust(8)}   phone: {x[2]} ')

    connection.commit()
    cursor.close()
    connection.close()

