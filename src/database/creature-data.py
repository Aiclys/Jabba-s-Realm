#!/usr/bin/env python3
import sqlite3

con = sqlite3.connect("jabbas-data.db")
cur = con.cursor()

def create_creatures_table():
    creatures_table = """CREATE TABLE creatures(
                id INT NOT NULL,
                name TEXT NOT NULL,
                price FLOAT NOT NULL,
                origin TEXT NOT NULL,
                food TEXT,
                danger_level TEXT
    )"""
    cur.execute(creatures_table)

create_creatures_table()

con.close()
