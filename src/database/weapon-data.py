#!/usr/bin/env python3
import sqlite3

con = sqlite3.connect("jabbas-data.db")
cur = con.cursor()


# DO NOT USE anymore, table already created
def create_weapons_table():
    weapons_table = """CREATE TABLE weapons(
                id INT NOT NULL,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                manufacturer TEXT,
                range TEXT
    )"""
    cur.execute(weapons_table)

create_weapons_table()

con.close()
