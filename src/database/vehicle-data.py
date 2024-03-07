#!/usr/bin/env python3
import sqlite3

con = sqlite3.connect("jabbas-data.db")
cur = con.cursor()

# DO NOT USE ANYMORE, table already created
def create_vehicles_table():
    vehicles_table = """CREATE TABLE vehicles(
                id INT NOT NULL,
                name TEXT NOT NULL,
                price FLOAT,
                category TEXT NOT NULL,
                manufacturer TEXT,
                role TEXT,
                length FLOAT,
                width FLOAT,
                height FLOAT,
                max_speed FLOAT
    )"""
    cur.execute(vehicles_table)

create_vehicles_table()

con.close()
