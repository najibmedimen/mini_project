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

#This creates table with two columns names name, address and are NULL

#cursor.execute("CREATE TABLE products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) Not Null, price$ DECIMAL(2,2) Not Null)")



connection.commit()
cursor.close()
connection.close()