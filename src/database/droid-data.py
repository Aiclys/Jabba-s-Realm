#!/usr/bin/env python3
import sqlite3

con = sqlite3.connect("jabbas-data.db")
cur = con.cursor()

# DO NOT USE anymore, table already created
def create_droid_table():
    droids_table = """CREATE TABLE droids(
                id INT NOT NULL,
                name TEXT NOT NULL,
                manufacturer TEXT,
                height FLOAT,
                role TEXT
    )"""
    cur.execute(droids_table)

create_droids_table()

con.close()
