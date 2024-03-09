#!/usr/bin/env python3
import sqlite3
import random

con = sqlite3.connect("jabbas-data.db")
cur = con.cursor()

# DO NOT USE anymore, table already created
def create_droid_table():
    droids_table = """CREATE TABLE droids(
                id INT NOT NULL,
                name TEXT NOT NULL,
                price FLOAT NOT NULL,
                category TEXT,
                manufacturer TEXT,
                height FLOAT,
                role TEXT
    )"""
    cur.execute(droids_table)

def add_droids():
    droid_id = int(input("Droid id: "))
    name = input("Droid name: ")
    price = float(input("Droid price: "))
    category =  input("Droid category: ")
    manufacturer = input("Droid manufacturer: ")
    height = float(input("Droid height: "))
    role = input("Droid role: ")
    cur.execute(f"INSERT INTO droids VALUES({droid_id}, '{name}', {price}, '{manufacturer}', {height}, '{role}')")

# Outputs a random droid
def get_random_droid(category):
    if category == "all":
        result = cur.execute("SELECT * FROM droids")
    else:
        result = cur.execute(f"SELECT * FROM droids WHERE category='{category}'")

    res = result.fetchall()
    rand_res = random.choice(res)
    return rand_res

# Outputs a random droid from a certain manufacturer
def get_random_droid_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM droid")
    else:
        result = cur.execute(f"SELECT * FROM droids WHERE manufacturer='{manufacturer}'")

    res = result.fetchall()
    rand_res = random.choice(res)
    return rand_res

# Searches droids by id
def get_droid_by_id(droid_id):
    if droid_id == "all":
        result = cur.execute("SELECT * FROM droids")
    else:
        result = cur.execute(f"SELECT * FROM droids WHERE id={droid_id}")

    res = result.fetchall()
    return res

# Search droids by name
def get_droids_by_name(name):
    if name == "all":
        result = cur.execute("SELECT * FROM droids")
    else:
        result = cur.execute(f"SELECT * FROM droids WHERE name='{name}'")

    res = result.fetchall()
    return res

# Lists droids over a specific price
def get_droids_over_price(price):
    if name == "all":
        result = cur.execute("SELECT * FROM droids")
    else:
        result = cur.execute(f"SELECT * FROM droids WHERE name='{name}'")

    res = result.fetchall()
    return res

# Lists droids over a certain price
def get_droids_over_price(price):
    result = cur.execute(f"SELECT * FROM droids WHERE price>{price}")
    res = result.fetchall()
    return res

# Lists droids under a certain price
def get_droids_under_price(price):
    result = cur.execute(f"SELECT * FROM droids WHERE price<{price}")
    res = result.fetchall()
    return res

# Lists all droids in a certain category
def get_droids_in_category(category):
    if category == "all":
        result = cur.execute("SELECT * FROM droids")
    else:
        result = cur.execute(f"SELECT * FROM droids WHERE category='{category}'")

    res = result.fetchall()
    return res

# Lists all droids from a specific manufacturer
def get_droids_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM droids")
    else:
        result = cur.execute(f"SELECT * FROM droids WHERE manufacturer='{manufacturer}'")

    res = result.fetchall()
    return res

# Lists all droids with a certain role
def get_droids_with_role(role):
    if role == "all":
        result = cur.execute("SELECT * FROM droids")
    else:
        result = cur.execute(f"SELECT * FROM droids WHERE role='{role}'")

    res = result.fetchall()
    return res

# Lists all droids over a certain height
def get_droids_over_height(height):
    result = cur.execute(f"SELECT * FROM droids WHERE height>{height}")
    res = result.fetchall()
    return res

# Lists all droids under a certain height
def get_droids_under_height(height):
    result = cur.execute(f"SELECT * FROM droids WHERE height<{height}")
    res = result.fetchall()
    return res

# Outputs the most expensive droid in a category
def most_expensive_droid(category):
    if category == "all":
        result = cur.execute("SELECT * FROM droids WHERE price=MAX(price)")
    else:
        result = cur.execute(f"SELECT * FROM droids WHERE price=MAX(price) AND category='{category}'")

    res = result.fetchall()
    return res

# Outputs the average droid price in a category
def average_droid_price(category):
    if category == "all":
        result = cur.execute("SELECT AVG(price) FROM droids")
    else:
        result = cur.execute(f"SELECT AVG(price) FROM droids WHERE category='{category}'")

    res = result.fetchall()
    return res

# Outputs the cheapest droid in a category
def cheapest_droid(category):
    if category == "all":
        result = cur.execute("SELECT * FROM droids WHERE price=MIN(price)")
    else:
        result = cur.execute(f"SELECT * FROM droids WHERE price=MIN(price) AND category='{category}'")

    res = result.fetchall()
    return res

# Outputs the most expensive droid from a manufacturer
def most_expensive_droid_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM droids WHERE price=MAX(price)")
    else:
        result = cur.execute(f"SELECT * FROM droids WHERE price=MAX(price) AND manufacturer='{manufacturer}'")

    res = result.fetchall()
    return res

# Outputs the average droid price from a manufacturer
def average_droid_price_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT AVG(price) FROM droids")
    else:
        result = cur.execute(f"SELECT AVG(price) FROM droids WHERE manufacturer='{manufacturer}'")

    res = result.fetchall()
    return res

# Outputs the cheapest droid from a manufacturer
def cheapest_droid_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM droids WHERE price=MIN(price)")
    else:
        result = cur.execute(f"SELECT * FROM droids WHERE price=MIN(price) AND manufacturer='{manufacturer}'")

    res = result.fetchall()
    return res

# Outputs the highest droid in a category
def highest_droid(category):
    if category == "all":
        result = cur.execute("SELECT * FROM droids WHERE height=MAX(height)")
    else:
        result = cur.execute(f"SELECT * FROM droids WHERE height=MAX(height) AND category='{category}'")

    res = result.fetchall()
    return res

# Outputs the average droid height
def average_droid_height(category):
    if category == "all":
        result = cur.execute("SELECT AVG(height) FROM droids")
    else:
        result = cur.execute(f"SELECT AVG(height) FROM droids WHERE category='{category}'")

    res = result.fetchall()
    return res

# Outputs the lowest droid in a category
def lowest_droid(category):
    if category == "all":
        result = cur.execute("SELECT * FROM droids WHERE height=MIN(height)")
    else:
        result = cur.execute(f"SELECT * FROM droids WHERE height=MIN(height) AND category='{category}'")

    res = result.fetchall()
    return res

# Outputs the highest droid from a manufacturer
def highest_droid_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM droids WHERE height=MAX(height)")
    else:
        result = cur.execute(f"SELECT * FROM droids WHERE height=MAX(height) AND manufacturer='{manufacturer}'")

    res = result.fetchall()
    return res

# Outputs the average droid height from a manufacturer
def average_droid_height_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT AVG(height) FROM droids")
    else:
        result = cur.execute(f"SELECT AVG(height) FROM droids WHERE manufacturer='{manufacturer}'")

    res = result.fetchall()
    return res

# Outputs the lowest droid from a manufacturer
def lowest_droid_from_manufacturer(manufacturer):
    if category == "all":
        result = cur.execute("SELECT * FROM droids WHERE height=MIN(height)")
    else:
        result = cur.execute(f"SELECT * FROM droids WHERE height=MIN(height) AND manufacturer='{manufacturer}'")

    res = result.fetchall()
    return res


# Sorting functions

# Sorts droids by id in ascending order
def sort_droids_by_id_asc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM droids ORDER BY id ASC")
    else:
        result = cur.execute(f"SELECT * FROM droids WHERE category='{category}' ORDER BY id ASC")

    res = result.fetchall()
    return res

# Sorts droids by id in descending order
def sort_droids_by_id_desc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM droids ORDER BY id DESC")
    else:
        result = cur.execute(f"SELECT * FROM droids WHERE category='{category}' ORDER BY id DESC")

    res = result.fetchall()
    return res

# Sorts droids by name in ascending order
def sort_droids_by_name_asc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM droids ORDER BY name ASC")
    else:
        result = cur.execute(f"SELECT * FROM droids WHERE category='{category}' ORDER BY name ASC")

    res = result.fetchall()
    return res

# Sorts droids by name in descending order
def sort_droids_by_name_desc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM droids ORDER BY name DESC")
    else:
        result = cur.execute(f"SELECT * FROM droids WHERE category='{category}' ORDER BY name DESC")

    res = result.fetchall()
    return res

# Sorts droids by price in ascending order
def sort_droids_by_price_asc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM droids ORDER BY price ASC")
    else:
        result = cur.execute(f"SELECT * FROM droids WHERE category='{category}' ORDER BY price ASC")

    res = result.fetchall()
    return res

# Sorts droids by price in descending order
def sort_droids_by_price_desc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM droids ORDER BY price DESC")
    else:
        result = cur.execute(f"SELECT * FROM droids WHERE category='{category}' ORDER BY price DESC")

    res = result.fetchall()
    return res

# Sorts droids by height in ascending order
def sort_droids_by_height_asc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM droids ORDER BY height ASC")
    else:
        result = cur.execute(f"SELECT * FROM droids WHERE category='{category}' ORDER BY height ASC")

    res = result.fetchall()
    return res

# Sorts droids by height in descending order
def sort_droids_by_height_desc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM droids ORDER BY height DESC")
    else:
        result = cur.execute(f"SELECT * FROM droids WHERE category='{category}' ORDER BY height DESC")

    res = result.fetchall()
    return res


con.commit()
con.close()
