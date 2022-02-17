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
#cursor.execute("CREATE TABLE products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) Not Null, price$ DECIMAL(3,2) Not Null)")
#cursor.execute("CREATE TABLE couriers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) Not Null, phone INT Not Null)")

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

########################Insert multiple records ######################
#################Insert multiple records ######################
#sql = "INSERT INTO couriers (name, phone) VALUES (%s, %s)"
#val = [
#('jane', '08766546536'),
#('raj', '08766565456'),
#('rashid', '07677676767'),
#('garry', '07655432345'),
#('william', '07677676767'),
#('james', '07899654567')
#]
#cursor.executemany(sql, val)

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