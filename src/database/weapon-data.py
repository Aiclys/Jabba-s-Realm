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


def get_weapon_by_id(weapon_id):
    if weapon_id == "all":
        result = cur.execute("SELECT * FROM weapons")
    else:
        result = cur.execute(f"SELECT * FROM weapons WHERE id={weapon_id}")

    res = result.fetchall
    return res

def get_weapon_by_name(name):
    if name == "all":
        result = cur.execute("SELECT * FROM weapons")
    else:
        result = cur.execute(f"SELECT * FROM weapons WHERE name='{name}'")

    res = result.fetchall()
    return res

def get_weapons_over_price(price):
    result = cur.execute(f"SELECT * FROM weapons WHERE price>{price}")
    res = result.fetchall()
    return res

def get_weapons_under_price(price):
    result = cur.execute(f"SELECT * FROM weapons WHERE price<{price}")
    res = result.fetchall()
    return res

def get_weapons_over_range(weapon_range):
    result = cur.execute(f"SELECT * FROM weapons WHERE range>{weapon_range}")
    res = result.fetchall()
    return res

def get_weapons_under_range(weapon_range):
    result = cur.execute(f"SELECT * FROM weapons WHERE range<{weapon_range}")
    res = result.fetchall()
    return res


# Lists all weapons in a specific category
def get_weapons_in_category(category):
    if category == "all":
        result = cur.execute("SELECT * FROM weapons")
    else:
        result = cur.execute(f"SELECT * FROM weapons WHERE category='{category}'")

    res = result.fetchall()
    return res

# Lists all weapons from a specific manufacturer
def get_weapons_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM weapons")
    else:
        result = cur.execute(f"SELECT * FROM weapons WHERE manufacturer='{manufacturer}'")

    res = result.fetchall()
    return res

def average_price_in_category(category):
    if category == "all":
        result = cur.execute("SELECT AVG(price) FROM weapons")
    else:
        result = cur.execute(f"SELECT AVG(price) FROM weapons WHERE category='{category}'")

    res = result.fetchall()
    return res

def most_expensive_weapon_in_category(category):
    if category == "all":
        result = cur.execute("SELECT * FROM weapons WHERE price=MAX(price)")
    else:
        result = cur.execute(f"SELECT * FROM weapons WHERE price=MAX(price) AND category='{category}'")

    res = result.fetchall()
    return res

def cheapest_in_category(category):
    if category == "all":
        result = cur.execute("SELECT * FROM weapons WHERE price=MIN(price)")
    else:
        result = cur.execute(f"SELECT * FROM weapons WHERE price=MIN(price) AND category='{category}'")

    res = result.fetchall()
    return res

def average_price_from_manufacturer(manufacturer):
    if category == "all":
        result = cur.execute("SELECT AVG(price) FROM weapons")
    else:
        result = cur.execute(f"SELECT AVG(price) FROM weapons WHERE manufacturer='{manufacturer}'")

    res = result.fetchall()
    return res

def most_expensive_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM weapons WHERE price=MAX(price)")
    else:
        result = cur.execute(f"SELECT * FROM weapons WHERE price=MAX(price) AND manufacturer='{manufacturer}'")

    res = result.fetchall()
    return res

def cheapest_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM weapons WHERE price=MIN(price)")
    else:
        result = cur.execute(f"SELECT * FROM weapons WHERE price=MIN(price) AND manufacturer='{manufacturer}'")

    res = result.fetchall()
    return res





# Sorting functions

# Sorts weapons by id (ascending)
def sort_weapons_by_id_asc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM weapons ORDER BY id ASC")
    else:
        result = cur.execute(f"SELECT * FROM weapons WHERE category='{category}' ORDER BY id ASC")

    res = result.fetchall()
    return res

# Sorts weapons by id (descending)
def sort_weapons_by_id_desc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM weapons ORDER BY id DESC")
    else:
        result = cur.execute(f"SELECT * FROM weapons WHERE category='{category}' ORDER BY id DESC")

    res = result.fetchall()
    return res

# Sorts weapons by name (ascending)
def sort_weapons_by_name_asc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM weapons ORDER BY name ASC")
    else:
        result = cur.execute(f"SELECT * FROM weapons WHERE category='{category}' ORDER BY name ASC")

    res = result.fetchall()
    return res

# Sorts weapons by name (descending)
def sort_weapons_by_name_desc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM weapons ORDER BY name DESC")
    else:
        result = cur.execute(f"SELECT * FROM weapons WHERE category='{category}' ORDER BY name DESC")

    res = result.fetchall()
    return res

# Sorts weapons by price (ascending)
def sort_weapons_by_price_asc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM weapons ORDER BY price ASC")
    else:
        result = cur.execute(f"SELECT * FROM weapons WHERE category='{category}' ORDER BY price ASC")

    res = result.fetchall()
    return res

# Sorts weapons by price (descending)
def sort_weapons_by_price_desc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM weapons ORDER BY price DESC")
    else:
        result = cur.execute(f"SELECT * FROM weapons WHERE category='{category}' ORDER BY price ASC")

    res = result.fetchall()
    return res

# Sorts weapons by range (ascending)
def sort_weapons_by_range_asc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM weapons ORDER BY range ASC")
    else:
        result = cur.execute(f"SELECT * FROM weapons WHERE category='{category}' ORDER BY range ASC")

    res = result.fetchall()
    return res

# Sorts weapons by range (descending)
def sort_weapons_by_range_desc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM weapons ORDER BY range DESC")
    else:
        result = cur.execute(f"SELECT * FROM weapons WHERE category='{category}' ORDER BY range DESC")

    res = result.fetchall()
    return res





con.commit()
con.close()
