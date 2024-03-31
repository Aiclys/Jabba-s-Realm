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

create_droid_table()

def add_droids():
    droid_id = int(input("Droid id: "))
    name = input("Droid name: ")
    price = float(input("Droid price: "))
    category =  input("Droid category: ")
    manufacturer = input("Droid manufacturer: ")
    height = float(input("Droid height: "))
    role = input("Droid role: ")
    droid_info = [
        droid_id,
        name,
        price,
        category,
        manufacturer,
        height,
        role
    ]
    cur.execute("INSERT INTO droids VALUES(?, ?, ?, ?, ?, ?)", droid_info)

# Outputs a random droid
def get_random_droid(category):
    if category == "all":
        result = cur.execute("SELECT * FROM droids")
    else:
        droid_category = [category]
        result = cur.execute("SELECT * FROM droids WHERE category=?", droid_category)

    res = result.fetchall()
    rand_res = random.choice(res)
    return rand_res

# Outputs a random droid from a certain manufacturer
def get_random_droid_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM droid")
    else:
        droid_manufacturer = [manufacturer]
        result = cur.execute("SELECT * FROM droids WHERE manufacturer=?", droid_manufacturer)

    res = result.fetchall()
    rand_res = random.choice(res)
    return rand_res

# Searches droids by id
def get_droid_by_id(droid_id):
    if droid_id == "all":
        result = cur.execute("SELECT * FROM droids")
    else:
        droid_id = [droid_id]
        result = cur.execute("SELECT * FROM droids WHERE id=?", droid_id)

    res = result.fetchall()
    return res

# Search droids by name
def get_droids_by_name(name):
    if name == "all":
        result = cur.execute("SELECT * FROM droids")
    else:
        droid_name = [name]
        result = cur.execute("SELECT * FROM droids WHERE name=?", droid_name)

    res = result.fetchall()
    return res

# Lists droids over a certain price
def get_droids_over_price(price):
    droid_price = [price]
    result = cur.execute("SELECT * FROM droids WHERE price>?", droid_price)
    res = result.fetchall()
    return res

# Lists droids under a certain price
def get_droids_under_price(price):
    droid_price = [price]
    result = cur.execute("SELECT * FROM droids WHERE price<?", droid_price)
    res = result.fetchall()
    return res

# Lists all droids in a certain category
def get_droids_in_category(category):
    if category == "all":
        result = cur.execute("SELECT * FROM droids")
    else:
        droid_category = [category]
        result = cur.execute("SELECT * FROM droids WHERE category=?", droid_manufacturer)

    res = result.fetchall()
    return res

# Lists all droids from a specific manufacturer
def get_droids_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM droids")
    else:
        droid_manufacturer = [manufacturer]
        result = cur.execute("SELECT * FROM droids WHERE manufacturer=?", droid_manufacturer)

    res = result.fetchall()
    return res

# Lists all droids with a certain role
def get_droids_with_role(role):
    if role == "all":
        result = cur.execute("SELECT * FROM droids")
    else:
        droid_role = [role]
        result = cur.execute("SELECT * FROM droids WHERE role=?", droid_role)

    res = result.fetchall()
    return res

# Lists all droids over a certain height
def get_droids_over_height(height):
    droid_height = [height]
    result = cur.execute("SELECT * FROM droids WHERE height>?", droid_height)
    res = result.fetchall()
    return res

# Lists all droids under a certain height
def get_droids_under_height(height):
    droid_height = [height]
    result = cur.execute("SELECT * FROM droids WHERE height<?", droid_height)
    res = result.fetchall()
    return res

# Outputs the most expensive droid in a category
def most_expensive_droid(category):
    if category == "all":
        result = cur.execute("SELECT * FROM droids WHERE price=MAX(price)")
    else:
        droid_category = [category]
        result = cur.execute("SELECT * FROM droids WHERE price=MAX(price) AND category=?", droid_category)

    res = result.fetchall()
    return res

# Outputs the average droid price in a category
def average_droid_price(category):
    if category == "all":
        result = cur.execute("SELECT AVG(price) FROM droids")
    else:
        droid_category = [category]
        result = cur.execute("SELECT AVG(price) FROM droids WHERE category=?", droid_category)

    res = result.fetchall()
    return res

# Outputs the cheapest droid in a category
def cheapest_droid(category):
    if category == "all":
        result = cur.execute("SELECT * FROM droids WHERE price=MIN(price)")
    else:
        droid_category = [category]
        result = cur.execute("SELECT * FROM droids WHERE price=MIN(price) AND category=?", droid_category)

    res = result.fetchall()
    return res

# Outputs the most expensive droid from a manufacturer
def most_expensive_droid_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM droids WHERE price=MAX(price)")
    else:
        droid_manufacturer = [manufacturer]
        result = cur.execute("SELECT * FROM droids WHERE price=MAX(price) AND manufacturer=?", droid_manufacturer)

    res = result.fetchall()
    return res

# Outputs the average droid price from a manufacturer
def average_droid_price_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT AVG(price) FROM droids")
    else:
        droid_manufacturer = [manufacturer]
        result = cur.execute("SELECT AVG(price) FROM droids WHERE manufacturer=?", droid_manufacturer)

    res = result.fetchall()
    return res

# Outputs the cheapest droid from a manufacturer
def cheapest_droid_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM droids WHERE price=MIN(price)")
    else:
        droid_manufacturer = [manufacturer]
        result = cur.execute("SELECT * FROM droids WHERE price=MIN(price) AND manufacturer=?", droid_manufacturer)

    res = result.fetchall()
    return res

# Outputs the highest droid in a category
def highest_droid(category):
    if category == "all":
        result = cur.execute("SELECT * FROM droids WHERE height=MAX(height)")
    else:
        droid_category = [category]
        result = cur.execute("SELECT * FROM droids WHERE height=MAX(height) AND category=?", droid_category)

    res = result.fetchall()
    return res

# Outputs the average droid height
def average_droid_height(category):
    if category == "all":
        result = cur.execute("SELECT AVG(height) FROM droids")
    else:
        droid_category = [category]
        result = cur.execute("SELECT AVG(height) FROM droids WHERE category=?", droid_category)

    res = result.fetchall()
    return res

# Outputs the lowest droid in a category
def lowest_droid(category):
    if category == "all":
        result = cur.execute("SELECT * FROM droids WHERE height=MIN(height)")
    else:
        droid_category = [category]
        result = cur.execute("SELECT * FROM droids WHERE height=MIN(height) AND category=?", droid_category)

    res = result.fetchall()
    return res

# Outputs the highest droid from a manufacturer
def highest_droid_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM droids WHERE height=MAX(height)")
    else:
        droid_manufacturer = [manufacturer]
        result = cur.execute("SELECT * FROM droids WHERE height=MAX(height) AND manufacturer=?", droid_manufacturer)

    res = result.fetchall()
    return res

# Outputs the average droid height from a manufacturer
def average_droid_height_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT AVG(height) FROM droids")
    else:
        droid_manufacturer = [manufacturer]
        result = cur.execute("SELECT AVG(height) FROM droids WHERE manufacturer=?", droid_manufacturer)

    res = result.fetchall()
    return res

# Outputs the lowest droid from a manufacturer
def lowest_droid_from_manufacturer(manufacturer):
    if category == "all":
        result = cur.execute("SELECT * FROM droids WHERE height=MIN(height)")
    else:
        droid_manufacturer = [manufacturer]
        result = cur.execute("SELECT * FROM droids WHERE height=MIN(height) AND manufacturer=?", droid_manufacturer)

    res = result.fetchall()
    return res


# Sorting functions

# Sorts droids by id in ascending order
def sort_droids_by_id_asc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM droids ORDER BY id ASC")
    else:
        droid_category = [category]
        result = cur.execute("SELECT * FROM droids WHERE category=? ORDER BY id ASC", droid_category)

    res = result.fetchall()
    return res

# Sorts droids by id in descending order
def sort_droids_by_id_desc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM droids ORDER BY id DESC")
    else:
        droid_category = [category]
        result = cur.execute("SELECT * FROM droids WHERE category=? ORDER BY id DESC", droid_category)

    res = result.fetchall()
    return res

# Sorts droids by name in ascending order
def sort_droids_by_name_asc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM droids ORDER BY name ASC")
    else:
        droid_category = [category]
        result = cur.execute("SELECT * FROM droids WHERE category=? ORDER BY name ASC", droid_category)

    res = result.fetchall()
    return res

# Sorts droids by name in descending order
def sort_droids_by_name_desc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM droids ORDER BY name DESC")
    else:
        droid_category = [category]
        result = cur.execute("SELECT * FROM droids WHERE category=? ORDER BY name DESC", droid_category)

    res = result.fetchall()
    return res

# Sorts droids by price in ascending order
def sort_droids_by_price_asc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM droids ORDER BY price ASC")
    else:
        droid_category = [category]
        result = cur.execute("SELECT * FROM droids WHERE category=? ORDER BY price ASC", droid_category)

    res = result.fetchall()
    return res

# Sorts droids by price in descending order
def sort_droids_by_price_desc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM droids ORDER BY price DESC")
    else:
        droid_category = [category]
        result = cur.execute("SELECT * FROM droids WHERE category=? ORDER BY price DESC", droid_category)

    res = result.fetchall()
    return res

# Sorts droids by height in ascending order
def sort_droids_by_height_asc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM droids ORDER BY height ASC")
    else:
        droid_category = [category]
        result = cur.execute("SELECT * FROM droids WHERE category=? ORDER BY height ASC", droid_category)

    res = result.fetchall()
    return res

# Sorts droids by height in descending order
def sort_droids_by_height_desc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM droids ORDER BY height DESC")
    else:
        droid_category = [category]
        result = cur.execute("SELECT * FROM droids WHERE category=? ORDER BY height DESC", droid_category)

    res = result.fetchall()
    return res


con.commit()
con.close()
