#!/usr/bin/env python3
import sqlite3
import random

con = sqlite3.connect("jabbas-data.db")
cur = con.cursor()


# DO NOT USE anymore, table already created
def create_weapons_table():
    weapons_table = """CREATE TABLE weapons(
                id INT NOT NULL,
                name TEXT NOT NULL,
                price FLOAT NOT NULL,
                category TEXT NOT NULL,
                manufacturer TEXT,
                range TEXT
    )"""
    cur.execute(weapons_table)

def sort_weapons_by_id_asc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM weapons ORDER BY id ASC")
    else:
        result = cur.execute(f"SELECT * FROM weapons WHERE category='{category}' ORDER BY id ASC")

    res = result.fetchall()
    return res

def sort_weapons_by_id_desc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM weapons ORDER BY id DESC")
    else:
        result = cur.execute(f"SELECT * FROM weapons WHERE category='{category}' ORDER BY id DESC")

    res = result.fetchall()
    return res

def sort_weapons_by_name_asc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM weapons ORDER BY name ASC")
    else:
        result = cur.execute(f"SELECT * FROM weapons WHERE category='{category}' ORDER BY ASC")

    res = result.fetchall()
    return res

def sort_weapons_by_name_desc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM weapons ORDER BY name DESC")
    else:
        result = cur.execute(f"SELECT * FROM weapons WHERE category='{category}' ORDER BY name DESC")

    res = result.fetchall()
    return res

def sort_weapons_by_price_asc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM weapons ORDER BY price ASC")
    else:
        result = cur.execute(f"SELECT * FROM weapons WHERE category='{category}' ORDER BY price ASC")

    res = result.fetchall()
    return res



con.commit()
con.close()
