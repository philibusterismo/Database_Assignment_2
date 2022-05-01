import mysql.connector
from mysql.connector import errorcode

cnx = mysql.connector.connect(user='root',
                              password='root',
                              # database='cars',
                              # host='127.0.0.1:8889'
                              unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock',)
