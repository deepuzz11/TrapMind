import pymysql

# Function to connect to MySQL database
def connect_db():
    connection = pymysql.connect(host='localhost',
                                  user='root',
                                  password='password',
                                  database='trapmind_db')
    return connection
