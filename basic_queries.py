import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# Establish a database connection
connection = pymysql.connect(
    host = host,
    user =user,
    password =password,
    database = database
)
cursor = connection.cursor()
#
#sql = """INSERT INTO person (first_name, last_name, age, email)
#VALUES (%s, %s, %s, %s)"""
#val = [("basha", "kanu", 37, "blinkeye@gmail.com"), ("crystal", "clear", 23, "fazool@gmail.com")]
#cursor.executemany(sql, val)

#############create database #################################################
#cursor.execute("CREATE DATABASE cafe_ap")

#########################create tables #######################################
#cursor.execute("CREATE TABLE products (product_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) Not Null, price$ DECIMAL(3,2) Not Null)")
#cursor.execute("CREATE TABLE couriers (courier_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) Not Null, phone VARCHAR(255) Not Null)")
#cursor.execute("CREATE TABLE order_status (status_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) Not Null)")
#cursor.execute("CREATE TABLE customers (customer_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) Not Null, address VARCHAR(255) Not Null, phone INT Not Null)")
#cursor.execute("CREATE TABLE orders (order_id INT AUTO_INCREMENT PRIMARY KEY, customer_id INT, courier_id INT, status_id int, FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE SET NULL, FOREIGN KEY (courier_id) REFERENCES couriers(courier_id) ON DELETE SET NULL, FOREIGN KEY (status_id) REFERENCES order_status(status_id) ON DELETE SET NULL)")
#cursor.execute("CREATE TABLE order_status (order_status_id INT AUTO_INCREMENT PRIMARY KEY, order_id INT, status_id INT, FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE SET NULL, FOREIGN KEY (status_id) REFERENCES status(status_id) ON DELETE SET NULL)")
#cursor.execute("CREATE TABLE products_on_orders (id INT AUTO_INCREMENT PRIMARY KEY, order_id INT, product_id INT, FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE SET NULL, FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE SET NULL)")
#################Drop Table ############################
#sql = "DROP TABLE products"
#cursor.execute(sql)

#################Insert multiple records ######################
#sql = "INSERT INTO products (name, price$) VALUES (%s, %s)"
#val = [
#  ('coke', 1.10),
#  ('coffee', 1.50),
#  ('tea', 1.80),
#  ('moch', 1.30),
#  ('espresso', 1.00),
#  ('cafeno', 3.00)
#]
#cursor.executemany(sql, val)

#######################Insert multiple records ######################
#sql = "INSERT INTO couriers (name, phone) VALUES (%s, %s)"
#val = [
#('deliveroo', '07766546536'),
#('ubereat', '07766565456'),
#('justeat', '07677676767'),
#('tishtosh', '07655432345')
#]
#cursor.executemany(sql, val)

########################Insert multiple records ######################
#sql = "INSERT INTO order_status (name) VALUES (%s)"
#val = [
#('preparing'),
#('out_for_delivery'),
#('delivered')
#]
#cursor.executemany(sql, val)

########################Insert multiple records ######################
#sql = "INSERT INTO customers (name, address, phone) VALUES (%s, %s, %s)"
#val = [
#('najib', '15 Ashton place', '0789887334'),
#('jerry', '12 china town', '0745277744'),
#('garry', '03 roseville garden', '07766545432'),
#('william', '88 primrose avenue', '07655432345'),
#('johnson', '10 ashton view', '07655676567')
#]
#cursor.executemany(sql, val)

########################Insert multiple records ######################
#sql = "INSERT INTO orders (customer_id, courier_id, status_id) VALUES (%s, %s, %s)"
#val = [
#(3, 4)
#]
#cursor.executemany(sql, val)

########################Insert multiple records ######################
#sql = "INSERT INTO products_on_orders (order_id, product_id) VALUES (%s, %s)"
#val = [
#(3, 5),
#(3, 5),
#(3, 5)
#]
#cursor.executemany(sql, val)
#
########################Insert multiple records ######################
#sql = "INSERT INTO order_status (order_id, status_id) VALUES (%s, %s)"
#val = [
#(2, 3)
#]
#cursor.executemany(sql, val)
##
#########################Insert Single record ###############
#sql = "INSERT INTO products (name, price$) VALUES (%s, %s)"
#val = ("espresso", 1.90)
#cursor.execute(sql, val)

###################### fetch all and print ###########
#cursor.execute("SELECT * FROM products")
#myresult = cursor.fetchall()
#for x in myresult:
#    print(f'{[x[0]]}: name: {x[1].ljust(8)}     price$: {x[2]} ')

#################### cfetch one row and print ###########
#cursor.execute("SELECT * FROM products")
#myresult = cursor.fetchone()
#print(myresult)

################ Filtering by WHERE statement #################
#sql = "SELECT * FROM products WHERE name ='coke'"
#cursor.execute(sql)
#myresult = cursor.fetchall()
#for x in myresult:
#    print(x)

################ Wild Card Filtering by WHERE statement ###########
#sql = "SELECT * FROM products WHERE name Like '%ke%'"
#cursor.execute(sql)
#myresult = cursor.fetchall()
#for x in myresult:
#    print(x)

#############Escape query values by using the placholder %s method to avoid injection########
#sql = "SELECT * FROM products WHERE name = %s"
#item = ("coke", )
#cursor.execute(sql, item)
#myresult = cursor.fetchall()
#for x in myresult:
#    print(x)

###############Order results #################
################can also include name DESC or name ASC 
#sql = "SELECT * FROM products ORDER BY name"
#cursor.execute(sql)
#myresult = cursor.fetchall()
#for x in myresult:
#    print(x)

############ It deletes recores and prints how many record(s) deleted ########
#sql = "DELETE FROM products WHERE name = 'espresso'"
#cursor.execute(sql)
#connection.commit()
#print(cursor.rowcount, "record(s) deleted")

############## Deleted records but also avoids injections by placeholer %s ####
#sql = "DELETE FROM customers WHERE address = %s"
#item = ("Yellow Garden 2", )
#cursor.execute(sql, item)
#connection.commit()
#print(cursor.rowcount, "record(s) deleted")

######################### Update a row record ###################
#sql = "UPDATE products SET name = 'milk tea' WHERE name = 'tea'"
#cursor.execute(sql)
#connection.commit()
#print(cursor.rowcount, "record(s) affected")

################### Update with preventing Injection ###############
#sql = "UPDATE products SET name = %s WHERE name = %s"
#val = ("milk tea", "tea")
#cursor.execute(sql, val)
#connection.commit()
#print(cursor.rowcount, "record(s) affected")


############Limit records in fetch #############################
#cursor.execute("SELECT * FROM products LIMIT 5")
#myresult = cursor.fetchall()
#for x in myresult:
#    print(x)

######## this will skip first 2 records and bring next 5 recrods #############
#cursor.execute("SELECT * FROM products LIMIT 5 OFFSET 2")
#myresult = cursor.fetchall()
#for x in myresult:
#    print(x)


connection.commit()
cursor.close()
connection.close()