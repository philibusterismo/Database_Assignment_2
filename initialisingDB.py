import csv
import mysql.connector
from mysql.connector import errorcode

cnx = mysql.connector.connect(user='root',
                              password='root',
                              # database='cars',
                              # host='127.0.0.1:8889'
                              unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock',)


def create_database(cursor, DB_NAME):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Faild to create database {}".format(err))
        exit(1)


def create_table_pokedex(cursor):
    create_pokedex = "CREATE TABLE `pokedex` (" \
        "  `dex_number` int NOT NULL," \
        "  `name` varchar(14) NOT NULL," \
        "  `type_1` varchar(14)," \
        "  `type_2` varchar(14)," \
        "  `hp` int," \
        "  `attack` int," \
        "  `defense` int," \
        "  `special_attack` int," \
        "  `special_defense` int," \
        "  `speed` int," \
        "  `ability_1` varchar(20)," \
        "  `ability_2` varchar(20)," \
        "  `ability_3` varchar(20)," \
        "  `evolves_into` int," \
        "  `height` int," \
        "  `weight` int," \
        "  `species` varchar(30)," \
        "  PRIMARY KEY (`dex_number`)," \
        "  FOREIGN KEY (`type_1`) REFERENCES `types`(`type`),"\
        "  FOREIGN KEY (`type_2`) REFERENCES `types`(`type`)"\
        ") ENGINE=InnoDB"

    try:
        print("Creating table pokedex: ")
        cursor.execute(create_pokedex)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")


def insert_file_to_pokedex(cursor, path):
    file = open(path)
    csvreader = csv.reader(file)
    matrix = []
    for row in csvreader:
        matrix.append(row)
    file.close()

    for i in range(len(matrix) - 1):
        values = "VALUES ("
        for x in range(len(matrix[1])):
            if (matrix[i + 1][x] == "NULL"):
                values += (matrix[i + 1][x]) + ", "
            else:
                values += "\"" + str(matrix[i + 1][x]) + "\", "
        values = values[:-2]
        values += ");"
        insertee = (
            "INSERT INTO pokedex (dex_number, name, type_1, type_2, hp, attack, defense, special_attack, special_defense, speed, ability_1, ability_2, ability_3, evolves_into, height, weight, species)" + values)
        try:
            cursor.execute(insertee)
        except mysql.connector.Error as err:
            print(err.msg)
        else:
            cnx.commit()


def create_table_types(cursor):
    create_types = "CREATE TABLE `types` (" \
        "  `type` varchar(20)," \
        "  `vs_normal` int," \
        "  `vs_fire` int," \
        "  `vs_water` int," \
        "  `vs_electric` int," \
        "  `vs_grass` int," \
        "  `vs_ice` int," \
        "  `vs_fighting` int," \
        "  `vs_poison` int," \
        "  `vs_ground` int," \
        "  `vs_flying` int," \
        "  `vs_psychic` int," \
        "  `vs_bug` int," \
        "  `vs_rock` int," \
        "  `vs_ghost` int," \
        "  `vs_dragon` int," \
        "  `vs_dark` int," \
        "  `vs_steel` int," \
        "  `vs_fairy` int," \
        "  PRIMARY KEY (`type`)" \
        ") ENGINE=InnoDB"

    try:
        print("Creating table types: ")
        cursor.execute(create_types)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")


def insert_file_to_types(cursor, path):
    file = open(path)
    csvreader = csv.reader(file)
    matrix = []
    for row in csvreader:
        matrix.append(row)
    file.close()

    for i in range(len(matrix) - 1):
        values = "VALUES ("
        for x in range(len(matrix[1])):
            if (matrix[i + 1][x] == "NULL"):
                values += (matrix[i + 1][x]) + ", "
            else:
                values += "\"" + str(matrix[i + 1][x]) + "\", "
        values = values[:-2]
        values += ");"
        insertee = (
            "INSERT INTO types (type, vs_normal, vs_fire, vs_water, vs_electric, vs_grass, vs_ice, vs_fighting, vs_poison, vs_ground, vs_flying, vs_psychic, vs_bug, vs_rock, vs_ghost, vs_dragon, vs_dark, vs_steel, vs_fairy)" + values)
        try:
            cursor.execute(insertee)
        except mysql.connector.Error as err:
            print(err.msg)
        else:
            cnx.commit()


def create_table_abilities(cursor):
    create_abilities = "CREATE TABLE `abilities` (" \
        "  `name` varchar(20) NOT NULL," \
        "  `description` varchar(100)," \
        "  PRIMARY KEY (`name`)" \
        ") ENGINE=InnoDB"

    try:
        print("Creating table abilities: ")
        cursor.execute(create_abilities)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")


def insert_file_to_abilities(cursor, path):
    file = open(path)
    csvreader = csv.reader(file)
    matrix = []
    for row in csvreader:
        matrix.append(row)
    file.close()

    for i in range(len(matrix) - 1):
        values = "VALUES ("
        for x in range(len(matrix[1])):
            if (matrix[i + 1][x] == "NULL"):
                values += (matrix[i + 1][x]) + ", "
            else:
                values += "\"" + str(matrix[i + 1][x]) + "\", "
        values = values[:-2]
        values += ");"
        insertee = (
            "INSERT INTO abilities (name, description)" + values)
        try:
            cursor.execute(insertee)
        except mysql.connector.Error as err:
            print(err.msg)
        else:
            cnx.commit()
