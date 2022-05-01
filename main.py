import os
import mysql.connector
from mysql.connector import errorcode
import initialisingDB as DB

# Important!!!
# Please set up the paths below to get to species.csv and planets.csv.
# Thank you

abilityfile = "csv files\\ability.csv"
pokedexfile = "csv files\\pokedex.csv"
typesfile = "csv files\\types.csv"

cnx = mysql.connector.connect(user='root',
                              password='root',
                              host='127.0.0.1',
                              )

DB_NAME = 'pokemon'

cursor = cnx.cursor()


try:
    # if exists
    cursor.execute("USE {}".format(DB_NAME))
    print("The database exists. Please enter what you would like to do.")


except mysql.connector.Error as err:
    # if doesnt exist
    print("Database {} does not exist".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        DB.create_database(cursor, DB_NAME)
        print("Database {} created succesfully.".format(DB_NAME))
        cnx.database = DB_NAME
        DB.create_table_types(cursor)
        DB.insert_file_to_types(cursor, typesfile)
        DB.create_table_abilities(cursor)
        DB.insert_file_to_abilities(cursor, abilityfile)
        DB.create_table_pokedex(cursor)
        DB.insert_file_to_pokedex(cursor, pokedexfile)

    else:
        print(err)
