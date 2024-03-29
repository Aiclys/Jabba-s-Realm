#!/usr/bin/env python3
import sqlite3
import random

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
                crew INT,
                length FLOAT,
                width FLOAT,
                height FLOAT,
                max_speed FLOAT
    )"""
    cur.execute(vehicles_table)

create_vehicles_table()

# Add vehicles to database
def add_vehicles():
    vehicle_id = int(input("Vehicle id: "))
    name = input("Vehicle name: ")
    price = float(input("Vehicle price: "))
    category = input("Vehicle category: ")
    manufacturer = input("Vehicle manufacturer: ")
    role = input("Vehicle role: ")
    length = float(input("Vehicle length: "))
    width = float(input("Vehicle widht: "))
    height = float(input("Vehicle height: "))
    max_speed = float(input("Vehicle max speed: "))
    vehicle_info = [
        vehicle_id,
        name,
        price,
        cateogry,
        manufacturer,
        role,
        length,
        width,
        height,
        max_speed
    ]
    cur.execute("INSERT INT vehicles VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", vehicle_info)
    con.commit()

# Outputs a random vehicle
def get_random_vehicle(category):
    if category == "all":
        result = cur.execute("SELECT * FROM vehicles")
    else:
        vehicle_category = [category]
        result = cur.execute("SELECT * FROM vehicles WHERE category=?", vehicle_category)

    res = result.fetchall()
    rand_res = random.choice(res)
    return rand_res

# Outputs a random vehicle from a certain manufacturer
def get_random_vehicle_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM vehicles")
    else:
        vehicle_manufacturer = [manufacturer]
        result = cur.execute("SELECT * FROM vehicles WHERE manufacturer=?", vehicle_manufacturer)

    res = result.fetchall()
    rand_res = random.choice(res)
    return rand_res

# Searches vehicles by id
def get_vehicles_by_id(vehicle_id):
    if vehicle_id == "all":
        result = cur.execute("SELECT * FROM vehicles")
    else:
        ve_id = [vehicle_id]
        result = cur.execute("SELECT * FROM vehicles WHERE id=?", ve_id)

    res = result.fetchall()
    return res

# Search vehicles by name
def get_vehicles_by_name(name):
    if name == "all":
        result = cur.execute("SELECT * FROM vehicle")
    else:
        vehicle_name = [name]
        result = cur.execute("SELECT * FROM vehicle WHERE name=?", vehicle_name)

    res = result.fetchall()
    return res

# Lists vehicles over a specific price
def get_vehicles_over_price(price):
    if price == "all":
        result = cur.execute("SELECT * FROM vehicles")
    else:
        vehicle_price = [price]
        result = cur.execute("SELECT * FROM vehicles WHERE name=?", vehicle_price)

    res = result.fetchall()
    return res

# Lists vehicles over a certain price
def get_vehicles_over_price(price):
    vehicle_price = [price]
    result = cur.execute("SELECT * FROM vehicles WHERE price>?", vehicle_price)
    res = result.fetchall()
    return res

# Lists vehicles under a certain price
def get_vehicles_under_price(price):
    vehicle_price = [price]
    result = cur.execute("SELECT * FROM vehicles WHERE price<?", vehicle_price)
    res = result.fetchall()
    return res

# Lists vehicles with more than ... crew members
def get_vehicles_over_crewmembers(crew):
    crew_members = [crew]
    result = cur.execute("SELECT * FROM vehicles WHERE crew>?", crew_members)
    res = result.fetchall()
    return res

# Lists vehicles with less than ... crew members
def get_vehicles_under_crewmembers(crew):
    crew_members = [crew]
    result = cur.execute("SELECT * FROM vehicles WHERE crew<?", crew_members)
    res = result.fetchall()
    return res

# Lists all vehicles in a certain category
def get_vehicles_in_category(category):
    if category == "all":
        result = cur.execute("SELECT * FROM vehicles")
    else:
        vehicle_category = [category]
        result = cur.execute("SELECT * FROM vehicles WHERE category=?", vehicle_category)

    res = result.fetchall()
    return res

# Lists all vehicles from a specific manufacturer
def get_vehicles_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM vehicles")
    else:
        vehicle_manufacturer = [manufacturer]
        result = cur.execute("SELECT * FROM vehicles WHERE manufacturer=?", vehicle_manufacturer)

    res = result.fetchall()
    return res

# Lists all vehicles with a certain role
def get_vehicles_with_role(role):
    if role == "all":
        result = cur.execute("SELECT * FROM vehicles")
    else:
        vehicle_role = [role]
        result = cur.execute("SELECT * FROM vehicles WHERE role=?", vehicle_role)

    res = result.fetchall()
    return res

# Lists all vehicles over a certain length
def get_vehicles_over_length(length):
    vehicle_length = [length]
    result = cur.execute("SELECT * FROM vehicles WHERE length>", vehicle_length)
    res = result.fetchall()
    return res

# Lists all vehicles under a certain length
def get_vehicles_under_length(length):
    vehicle_length = [length]
    result = cur.execute("SELECT * FROM vehicles WHERE length<", vehicle_length)
    res = result.fetchall()
    return res

# Lists all vehicles over a certain width
def get_vehicles_over_width(width):
    vehicle_width = [width]
    result = cur.execute("SELECT * FROM vehicles WHERE width>?", vehicle_width)
    res = result.fetchall()
    return res

# Lists all vehicles under a certain width
def get_vehicles_under_width(width):
    vehicle_width = [width]
    result = cur.execute("SELECT * FROM vehicles WHERE width<?", vehicle_width)
    res = result.fetchall()
    return res

# Lists all vehicles over a certain height
def get_vehicles_over_height(height):
    vehicle_height = [height]
    result = cur.execute("SELECT * FROM vehicles WHERE height>?", vehicle_height)
    res = result.fetchall()
    return res

# Lists all vehicles under a certain height
def get_vehicles_under_height(height):
    vehicle_height = [height]
    result = cur.execute("SELECT * FROM vehicles WHERE height<?", vehicle_height)
    res = result.fetchall()
    return res

# Lists all vehicles over a certain speed
def get_vehicles_over_speed(speed):
    vehicle_speed = [speed]
    result = cur.execute("SELECT * FROM vehicles WHERE max_speed>?", vehicle_speed)
    res = result.fetchall()
    return res

# Lists all vehicles under a certain speed
def get_vehicles_under_speed(speed):
    vehicle_speed = [speed]
    result = cur.execute("SELECT * FROM vehicles WHERE max_speed<?", vehicle_speed)
    res = result.fetchall()
    return res

# Outputs the most expensive vehicles in a category
def most_expensive_vehicles(category):
    if category == "all":
        result = cur.execute("SELECT * FROM vehicles WHERE price=MAX(price)")
    else:
        vehicle_category = [category]
        result = cur.execute("SELECT * FROM vehicles WHERE price=MAX(price) AND category=?", vehicle_category)

    res = result.fetchall()
    return res

# Outputs the average vehicle price in a category
def average_vehicle_price(category):
    if category == "all":
        result = cur.execute("SELECT AVG(price) FROM vehicles")
    else:
        vehicle_category = [category]
        result = cur.execute("SELECT AVG(price) FROM vehicles WHERE category=?", vehicle_category)

    res = result.fetchall()
    return res

# Outputs the cheapest vehicles in a category
def cheapest_vehicle(category):
    if category == "all":
        result = cur.execute("SELECT * FROM vehicles WHERE price=MIN(price)")
    else:
        vehicle_category = [category]
        result = cur.execute("SELECT * FROM vehicles WHERE price=MIN(price) AND category=?", vehicle_category)

    res = result.fetchall()
    return res

# Outputs the most expensive vehicles from a manufacturer
def most_expensive_vehicle_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM vehicles WHERE price=MAX(price)")
    else:
        vehicle_manufacturer = [manufacturer]
        result = cur.execute("SELECT * FROM vehicles WHERE price=MAX(price) AND manufacturer=?", vehicle_manufacturer)

    res = result.fetchall()
    return res

# Outputs the average vehicle price from a manufacturer
def average_vehicle_price_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT AVG(price) FROM vehicles")
    else:
        vehicle_manufacturer = [manufacturer]
        result = cur.execute("SELECT AVG(price) FROM vehicles WHERE manufacturer=?", vehicle_manufacturer)

    res = result.fetchall()
    return res

# Outputs the cheapest vehicle from a manufacturer
def cheapest_vehicle_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM vehicles WHERE price=MIN(price)")
    else:
        vehicle_manufacturer = [manufacturer]
        result = cur.execute("SELECT * FROM vehicles WHERE price=MIN(price) AND manufacturer=?", vehicle_manufacturer)

    res = result.fetchall()
    return res

# Outputs the longest vehicle in a category
def longest_vehicle(category):
    if category == "all":
        result = cur.execute("SELECT * FROM vehicles WHERE length=MAX(length)")
    else:
        vehicle_category = [category]
        result = cur.execute("SELECT * FROM vehicles WHERE length=MAX(length) AND category=?", vehicle_category)

    res = result.fetchall()
    return res

# Outputs the average vehicle length in a category
def average_vehicle_length(category):
    if category == "all":
        result = cur.execute("SELECT AVG(length) FROM vehicles")
    else:
        vehicle_category = [category]
        result = cur.execute("SELECT AVG(length) FROM vehicles WHERE category=?", vehicle_category)

    res = result.fetchall()
    return res

# Outputs the shortest vehicle in a category
def shortest_vehicle(category):
    if category == "all":
        result = cur.execute("SELECT * FROM vehicles WHERE length=MIN(length)")
    else:
        vehicle_category = [category]
        result = cur.execute("SELECT * FROM vehicles WHERE length=MIN(length) AND category=?", vehicle_category)

    res = result.fetchall()
    return res

# Outputs the longest vehicle from a manufacturer
def longest_vehicle_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM vehicles WHERE length=MAX(length)")
    else:
        vehicle_manufacturer = [manufacturer]
        result = cur.execute("SELECT * FROM vehicles WHERE length=MAX(length) AND manufacturer=?", vehicle_manufacturer)

    res = result.fetchall()
    return res

# Outputs the average vehicle length from a manufacturer
def average_vehicle_length_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT AVG(length) FROM vehicles")
    else:
        vehicle_manufacturer = [manufacturer]
        result = cur.execute("SELECT AVG(length) FROM vehicles WHERE manufacturer=?", vehicle_manufacturer)

    res = result.fetchall()
    return res

# Outputs the shortest vehicle from a manufacturer
def shortest_vehicle_from_manufacturer(manufacturer):
    if category == "all":
        result = cur.execute("SELECT * FROM vehicles WHERE length=MIN(length)")
    else:
        vehicle_manufacturer = [manufacturer]
        result = cur.execute("SELECT * FROM vehicles WHERE length=MIN(length) AND manufacturer=?", vehicle_manufacturer)

    res = result.fetchall()
    return res

# Outputs the widest vehicle in a category
def widest_vehicle(category):
    if category == "all":
        result = cur.execute("SELECT * FROM vehicles WHERE width=MAX(width)")
    else:
        vehicle_category = [category]
        result = cur.execute("SELECT * FROM vehicles WHERE width=MAX(width) AND category=?", vehicle_category)

    res = result.fetchall()
    return res

# Outputs the average vehicle width in a category
def average_vehicle_width(category):
    if category == "all":
        result = cur.execute("SELECT AVG(width) FROM vehicles")
    else:
        vehicle_category = [category]
        result = cur.execute("SELECT AVG(width) FROM vehicles WHERE category=?", vehicle_category)

    res = result.fetchall()
    return res

# Outputs the least wide vehicle in a category
def least_wide_vehicle(category):
    if category == "all":
        result = cur.execute("SELECT * FROM vehicles WHERE width=MIN(width)")
    else:
        vehicle_category = [category]
        result = cur.execute("SELECT * FROM vehicles WHERE width=MIN(width) AND category=?", vehicle_category)

    res = result.fetchall()
    return res

# Outputs the widest vehicle from a manufacturer
def widest_vehicle_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM vehicles WHERE width=MAX(width)")
    else:
        vehicle_manufacturer = [manufacturer]
        result = cur.execute("SELECT * FROM vehicles WHERE width=MAX(width) AND manufacturer=?", vehicle_manufacturer)

    res = result.fetchall()
    return res

# Outputs the average vehicle width from a manufacturer
def average_vehicle_width_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT AVG(width) FROM vehicles")
    else:
        vehicle_manufacturer = [manufacturer]
        result = cur.execute("SELECT AVG(width) FROM vehicles WHERE manufacturer=?", vehicle_manufacturer)

    res = result.fetchall()
    return res

# Outputs the least wide vehicle from a manufacturer
def least_wide_vehicle_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM vehicles WHERE width=MIN(width)")
    else:
        vehicle_manufacturer = [manufacturer]
        result = cur.execute("SELECT * FROM vehicles WHERE width=MIN(width) AND manufacturer=?", vehicle_manufacturer)

    res = result.fetchall()
    return res

# Outputs the highest vehicle in a category
def highest_vehicle(category):
    if category == "all":
        result = cur.execute("SELECT * FROM vehicles WHERE height=MAX(height)")
    else:
        vehicle_category = [category]
        result = cur.execute("SELECT * FROM vehicles WHERE height=MAX(height) AND category=?", vehicle_category)

    res = result.fetchall()
    return res

# Outputs the average vehicle height
def average_spaceship_height(category):
    if category == "all":
        result = cur.execute("SELECT AVG(height) FROM vehicles")
    else:
        vehicle_category = [category]
        result = cur.execute("SELECT AVG(height) FROM vehicles WHERE category=?", vehicle_category)

    res = result.fetchall()
    return res

# Outputs the lowest vehicle in a category
def lowest_vehicle(category):
    if category == "all":
        result = cur.execute("SELECT * FROM vehicles WHERE height=MIN(height)")
    else:
        vehicle_category = [category]
        result = cur.execute("SELECT * FROM vehicles WHERE height=MIN(height) AND category=?", vehicle_category)

    res = result.fetchall()
    return res

# Outputs the highest vehicles from a manufacturer
def highest_vehicle_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM vehicles WHERE height=MAX(height)")
    else:
        vehicle_manufacturer = [manufacturer]
        result = cur.execute("SELECT * FROM vehicles WHERE height=MAX(height) AND manufacturer=?", vehicle_manufacturer)

    res = result.fetchall()
    return res

# Outputs the average vehicle height from a manufacturer
def average_vehicle_height_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT AVG(height) FROM vehicles")
    else:
        vehicle_manufacturer = [manufacturer]
        result = cur.execute("SELECT AVG(height) FROM vehicles WHERE manufacturer=?". vehicle_manufacturer)

    res = result.fetchall()
    return res

# Outputs the lowest vehicle from a manufacturer
def lowest_vehicle_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM vehicles WHERE height=MIN(height)")
    else:
        vehicle_manufacturer = [manufacturer]
        result = cur.execute("SELECT * FROM vehicles WHERE height=MIN(height) AND manufacturer=?", vehicle_manufacturer)

    res = result.fetchall()
    return res

# Outputs the vehicle with the most crew members in a category
def most_crewmembers_in_vehicle(category):
    if category == "all":
        result = cur.execute("SELECT * FROM vehicles WHERE crew=MAX(crew)")
    else:
        vehicle_category = [category]
        result = cur.execute("SELECT * FROM vehicles WHERE crew=MAX(crew) AND category=?", vehicle_category)

    res = result.fetchall()
    return res

# Outputs the average amount of crew members in a vehicle in a category
def average_crewmembers_in_vehicle(category):
    if category == "all":
        result = cur.execute("SELECT AVG(crew) FROM vehicles")
    else:
        vehicle_category = [category]
        result = cur.execute("SELECT AVG(crew) FROM vehicles WHERE category=?", vehicle_category)

    res = result.fetchall()
    return res

# Outputs the vehicles with the least crew members in a category
def least_crewmembers_in_vehicle(category):
    if category == "all":
        result = cur.execute("SELECT * FROM vehicles WHERE crew=MIN(crew)")
    else:
        vehicle_category = [category]
        result = cur.execute("SELECT * FROM vehicles WHERE crew=MIN(crew) AND category=?", vehicle_category)

    res = result.fetchall()
    return res

# Outputs the vehicle with the most crew members from a manufacturer
def most_crewmembers_in_vehicle_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM vehicles WHERE crew=MAX(crew)")
    else:
        vehicle_manufacturer = [manufacturer]
        result = cur.execute("SELECT * FROM vehicles WHERE crew=MAX(crew) AND manufacturer=?", vehicle_manufacturer)

    res = result.fetchall()
    return res

# Outputs the average amount of crew members in a vehicle from a manufcaturer
def average_crewmembers_in_vehicle_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT AVG(crew) FROM vehicles")
    else:
        vehicle_manufacturer = [manufacturer]
        result = cur.execute("SELECT AVG(crew) FROM vehicles WHERE manufacturer=?", vehicle_manufacturer)

    res = result.fetchall()
    return res

# Outputs the vehicle with the least crew members from a manufacturer
def least_crewmembers_in_vehicle_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM vehicles WHERE crew=MIN(crew)")
    else:
        vehicle_manufacturer = [manufacturer]
        result = cur.execute("SELECT * FROM vehicles WHERE crew=MIN(crew) AND manufacturer=?", vehicle_manufacturer)

    res = result.fetchall()
    return res

# Outputs the fastest vehicle in a category
def fastest_vehicle(category):
    if category == "all":
        result = cur.execute("SELECT * FROM vehicles WHERE max_speed=MAX(max_speed)")
    else:
        vehicle_category = [category]
        result = cur.execute("SELECT * FROM vehicles WHERE max_speed=MAX(max_speed) AND category=?", vehicle_category)

    res = result.fetchall()
    return res

# Outputs the slowest vehicle in a category
def slowest_vehicle(category):
    if category == "all":
        result = cur.execute("SELECT * FROM vehicles WHERE max_speed=MIN(max_speed)")
    else:
        vehicle_category = [category]
        result = cur.execute("SELECT * FROM vehicles WHERE max_speed=MIN(max_speed) AND category=?", vehicle_category)

    res = result.fetchall()
    return res

# Outputs the fastest vehicle in a category
def fastest_vehicle(category):
    if category == "all":
        result = cur.execute("SELECT * FROM vehicles WHERE max_speed=MAX(max_speed)")
    else:
        vehicle_category = [category]
        result = cur.execute("SELECT * FROM vehicles WHERE max_speed=MAX(max_speed) AND category=?", vehicle_category)

    res = result.fetchall()
    return res

# Outputs the average spaceship speed in a category
def average_vehicle_speed(category):
    if category == "all":
        result = cur.execute("SELECT AVG(speed) FROM vehicles")
    else:
        vehicle_category = [category]
        result = cur.execute("SELECT AVG(speed) FROM vehicles WHERE category=?", vehicle_category)

    res = result.fetchall()
    return res

# Outputs the slowest vehicle in a category
def slowest_vehicle(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships WHERE max_speed=MIN(max_speed)")
    else:
        vehicle_category = [category]
        result = cur.execute("SELECT * FROM vehicles WHERE max_speed=MIN(max_speed) AND category=?", vehicle_category)

    res = result.fetchall()
    return res

# Outputs the fastest vehicle from a manufacturer
def fastest_vehicle_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM vehicles WHERE max_speed=MAX(max_speed)")
    else:
        vehicle_manufacturer = [manufacturer]
        result = cur.execute("SELECT * FROM vehicles WHERE max_speed=MAX(max_speed) AND manufacturer=?", vehicle_manufacturer)

    res = result.fetchall()
    return res

# Outputs the average spaceship speed from a manufacturer
def average_spaceship_speed_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT AVG(max_speed) FROM vehicles")
    else:
        vehicle_manufacturer = [manufacturer]
        result = cur.execute("SELECT AVG(max_speed) FROM vehicles WHERE manufacturer=?", vehicle_manufacturer)

    res = result.fetchall()
    return res

# Outputs the slowest spaceship from a manufacturer
def slowest_spaceship_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM vehicles WHERE max_speed=MIN(max_speed)")
    else:
        vehicle_manufacturer = [manufacturer]
        result = cur.execute("SELECT * FROM vehicles WHERE max_speed=MIN(max_speed) AND manufacturer=?", vehicle_manufacturer)

    res = result.fetchall()
    return res


# Sorting functions

# Sorts vehicles by id in ascending order
def sort_vehicles_by_id_asc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM vehicles ORDER BY id ASC")
    else:
        vehicle_category = [category]
        result = cur.execute("SELECT * FROM vehicles WHERE category=? ORDER BY id ASC", vehicle_category)

    res = result.fetchall()
    return res

# Sorts vehicles by id in descending order
def sort_vehicles_by_id_desc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM vehicles ORDER BY id DESC")
    else:
        vehicle_category = [category]
        result = cur.execute("SELECT * FROM vehicles WHERE category=? ORDER BY id DESC", vehicle_category)

    res = result.fetchall()
    return res

# Sorts vehicles by name in ascending order
def sort_vehicles_by_name_asc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM vehicles ORDER BY name ASC")
    else:
        vehicle_category = [category]
        result = cur.execute("SELECT * FROM vehicles WHERE category=? ORDER BY name ASC", vehicle_category)

    res = result.fetchall()
    return res

# Sorts vehicles by name in descending order
def sort_vehicles_by_name_desc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM vehicles ORDER BY name DESC")
    else:
        vehicle_category = [category]
        result = cur.execute("SELECT * FROM vehicles WHERE category=? ORDER BY name DESC", vehicle_category)

    res = result.fetchall()
    return res

# Sorts vehicles by price in ascending order
def sort_vehicles_by_price_asc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM vehicles ORDER BY price ASC")
    else:
        vehicle_category = [category]
        result = cur.execute("SELECT * FROM vehicles WHERE category=? ORDER BY price ASC", vehicle_category)

    res = result.fetchall()
    return res

# Sorts vehicles by price in descending order
def sort_vehicles_by_price_desc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM vehicles ORDER BY price DESC")
    else:
        vehicle_category = [category]
        result = cur.execute("SELECT * FROM vehicles WHERE category=? ORDER BY price DESC", vehicle_category)

    res = result.fetchall()
    return res

# Sorts vehicles by length in ascending order
def sort_vehicles_by_length_asc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM vehicles ORDER BY length ASC")
    else:
        vehicle_category = [category]
        result = cur.execute("SELECT * FROM vehicles WHERE category=? ORDER BY length ASC", vehicle_category)

    res = result.fetchall()
    return res

# Sorts vehicles by length in descending order
def sort_vehicles_by_length_desc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM vehicles ORDER BY length DESC")
    else:
        vehicle_category = [category]
        result = cur.execute("SELECT * FROM vehicles WHERE category=? ORDER BY length DESC", vehicle_category)

    res = result.fetchall()
    return res

# Sorts vehicles by width in ascending order
def sort_vehicles_by_width_asc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM vehicles ORDER BY width ASC")
    else:
        vehicle_category = [category]
        result = cur.execute("SELECT * FROM vehicles WHERE category=? ORDER BY width ASC", vehicle_category)

    res = result.fetchall()
    return res

# Sorts vehicles by width in descending order
def sort_vehicles_by_width_desc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM vehicles ORDER BY width DESC")
    else:
        vehicle_category = [category]
        result = cur.execute("SELECT * FROM vehicles WHERE category=? ORDER BY width DESC", vehicle_category)

    res = result.fetchall()
    return res

# Sorts vehicles by height in ascending order
def sort_vehicles_by_height_asc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM vehicles ORDER BY height ASC")
    else:
        vehicle_category = [category]
        result = cur.execute("SELECT * FROM vehicles WHERE category=? ORDER BY height ASC", vehicle_category)

    res = result.fetchall()
    return res

# Sorts vehicles by height in descending order
def sort_vehicles_by_height_desc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM vehicles ORDER BY height DESC")
    else:
        vehicle_category = [category]
        result = cur.execute("SELECT * FROM vehicles WHERE category=? ORDER BY height DESC", vehicle_category)

    res = result.fetchall()
    return res

# Sorts vehicles by speed in ascending order
def sort_vehicles_by_speed_asc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM vehicles ORDER BY max_speed ASC")
    else:
        vehicle_category = [category]
        result = cur.execute("SELECT * FROM vehicles WHERE category=? ORDER BY max_speed ASC", vehicle_category)

    res = result.fetchall()
    return res

# Sorts vehicles by speed in descending order
def sort_vehicles_by_speed_desc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM vehicles ORDER BY max_speed DESC")
    else:
        vehicle_category = [category]
        result = cur.execute("SELECT * FROM vehicles WHERE category=? ORDER BY max_speed DESC", vehicle_category)

    res = result.fetchall()
    return res





con.commit()
con.close()
