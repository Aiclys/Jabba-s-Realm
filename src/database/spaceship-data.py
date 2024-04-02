#!/usr/bin/env python3
import sqlite3
import random

con = sqlite3.connect("jabbas-data.db")
cur = con.cursor()

# DO NOT USE anymore, table already created
def create_spaceship_table():
    spaceship_table = """CREATE TABLE if not exists spaceships(
                id INT NOT NULL,
                name TEXT NOT NULL,
                path_to_img TEXT,
                category TEXT NOT NULL,
                manufacturer TEXT,
                price FLOAT NOT NULL,
                length FLOAT,
                width FLOAT,
                height FLOAT,
                crew INT,
                role TEXT,
                max_atmos_speed FLOAT,
                hyperdrive INT,
                shielding TEXT,
                engine TEXT,
                turbolaser INT,
                torpedo INT,
                consumables TEXT
    )"""

    cur.execute(spaceship_table)

# Add spaceships to catalog/database
def add_spaceships():
    spaceship_id = int(input("Spaceship id: "))
    name = input("Spaceship name: ")
    path_to_img = input("Path to image: ")
    category = input("Spaceship category: ")
    manufacturer = input("Spaceship manufacturer: ")
    price = float(input("Spaceship price: "))
    length = float(input("Spaceship length: "))
    width = float(input("Spaceship width: "))
    height = float(input("Spaceship height: "))
    crew = int(input("Spaceship crew: "))
    role = input("Spaceship role: ")
    max_atmos_speed = float(input("Spaceship max atmoshperic speed: "))
    hyperdrive = bool(input("Spaceship hyperdrive(1/0): "))
    shielding = input("Spaceship shielding: ")
    engine = input("Spaceship engine: ")
    turbolaser = int(input("Spaceship turbolaser: "))
    torpedo = int(input("Spaceship torpedo: "))
    consumables = input("Spaceship consumables: ")
    cur.execute(f"""INSERT INTO spaceships VALUES(
        {spaceship_id},
        '{name}',
        '{path_to_img}'
        '{category}',
        '{manufacturer}',
        {price},
        {length},
        {width},
        {height},
        {crew},
        '{role}',
        {max_atmos_speed},
        {hyperdrive},
        '{shielding}',
        '{engine}',
        {turbolaser},
        {torpedo},
        '{consumables}'
        )""")
    con.commit()

# Outputs a random spaceship
def get_random_spaceship(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE category='{category}'")

    res = result.fetchall()
    rand_res = random.choice(res)
    return rand_res

# Outputs a random spaceship from a specific manufacturer
def get_random_spaceship_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM spaceships")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE manufacturer='{manufacturer}'")

    res = result.fetchall()
    rand_res = random.choice(res)
    return rand_res

# Searches spaceships by id
def get_spaceship_by_id(spaceship_id):
    if spaceship_id == "all":
        result = cur.execute("SELECT * FROM spaceships")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE id={spaceship_id}")

    res = result.fetchall()
    return res

# Searches spaceships by name
def get_spaceships_by_name(name):
    if name == "all":
        result = cur.execute("SELECT * FROM spaceships")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE name='{name}'")

    res = result.fetchall()
    return res

# Lists spaceships over a certain price
def get_spaceships_over_price(price):
    result = cur.execute(f"SELECT * FROM spaceships WHERE price>{price}")
    res = result.fetchall()
    return res

# Lists spaceships under a certain price
def get_spaceships_under_price(price):
    result = cur.execute(f"SELECT * FROM spaceships WHERE price<{price}")
    res = result.fetchall()
    return res

# Lists all spaceships in a certain category
def get_spaceships_in_category(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE category='{category}'")

    res = result.fetchall()
    return res

# Lists all spaceships from a specific manufacturer
def get_spaceships_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM spaceships")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE manufacturer='{manufacturer}'")

    res = result.fetchall()
    return res

# Lists all spaceships over a certain length
def get_spaceships_over_length(length):
    result = cur.execute(f"SELECT * FROM spaceships WHERE length>{length}")
    res = result.fetchall()
    return res

# Lists all spaceships under a certain length
def get_spaceships_under_length(length):
    result = cur.execute(f"SELECT * FROM spaceships WHERE length<{length}")
    res = result.fetchall()
    return res

# Lists all spaceships over a certain width
def get_spaceships_over_width(width):
    result = cur.execute(f"SELECT * FROM spaceships WHERE width>{width}")
    res = result.fetchall()
    return res

# Lists all spaceships under a certain width
def get_spaceships_under_width(width):
    result = cur.execute(f"SELECT * FROM spaceships WHERE width<{width}")
    res = result.fetchall()
    return res

# Lists all spaceships over a certain height
def get_spaceships_over_height(height):
    result = cur.execute(f"SELECT * FROM spaceships WHERE height>{height}")
    res = result.fetchall()
    return res

# Lists all spaceships under a certain height
def get_spaceships_under_height(height):
    result = cur.execute(f"SELECT * FROM spaceships WHERE height<{height}")
    res = result.fetchall()
    return res

# Lists all spaceships with more than ... crew members
def get_spaceships_over_crewmembers(crewmembers):
    result = cur.execute(f"SELECT * FROM spaceships WHERE crew>{crewmembers}")
    res = result.fetchall()
    return res

# Lists all spaceships with less than ... crew members
def get_spaceships_under_crewmembers(crewmembers):
    result = cur.execute(f"SELECT * FROM spaceships WHERE crew<{crewmembers}")
    res = result.fetchall()
    return res

# Lists all spaceships with a certain role
def get_spaceships_with_role(role):
    if role == "all":
        result = cur.execute("SELECT * FROM spaceships")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE role='{role}'")

    res = result.fetchall()
    return res

# Lists all spaceships over a certain speed
def get_spaceships_over_speed(speed):
    result = cur.execute(f"SELECT * FROM spaceships WHERE max_atmos_speed>{speed}")
    res = result.fetchall()
    return res

# Lists all spaceships under a certain speed
def get_spaceships_under_speed(speed):
    result = cur.execute(f"SELECT * FROM spaceships WHERE max_atmos_speed<{speed}")
    res = result.fetchall()
    return res

# Lists all spaceships with hyperdrive
def get_spaceships_with_hyperdrive(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships WHERE hyperdrive=1")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE hyperdrive=1 AND category={category}")

    res = result.fetchall()
    return res

# Lists all spaceships without hyperdrive
def get_spaceships_without_hyperdrive(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships WHERE hyperdrive=0")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE hyperdrive=0 AND category={category}")

    res = result.fetchall()
    return res

# Lists all spaceships with a certain shielding
def get_spaceships_with_shielding(shielding):
    if shielding == "all":
        result = cur.execute("SELECT * FROM spaceships")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE shielding = '{shielding}'")

    res = result.fetchall()
    return res

# Lists all spaceships with a specific engine
def get_spaceships_with_engine(engine):
    result = cur.execute(f"SELECT * FROM spaceships WHERE engine='{engine}'")
    res = result.fetchall()
    return res

# Lists all spaceships with a certain amount of turbolasers
def get_spaceships_with_turbolasers(turbolasers):
    result = cur.execute(f"SELECT * FROM spaceships WHERE turbolasers={turbolasers}")
    res = result.fetchall()
    return res

# Lists all spaceships with a certain amount of torpedos
def get_spaceships_with_torpedos(torpedo):
    result = cur.execute(f"SELECT * FROM spaceships WHERE torpedo={torpedo}")
    res = result.fetchall()
    return res

# Lists all spaceships with a certain duration of consumablity
def get_spaceships_with_consumables(consumables):
    result = cur.execute(f"SELECT * FROM spaceships WHERE consumables='{consumables}'")
    res = result.fetchall()
    return res



# TODO later because I'm tired and it's exhausting
def get_spaceships_with_shielding_in_category(shielding, category):
    result = cur.execute(f"SELECT * FROM spaceships WHERE category='{category}' AND shielding='{shielding}'")
    res = result.fetchall()
    return res

# Outputs the longest spaceship in a category
def longest_spaceship(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships WHERE length=MAX(length)")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE length=MAX(length) AND category='{category}'")

    res = result.fetchall()
    return res

# Outputs the average spaceship length in a category
def average_spaceship_length(category):
    if category == "all":
        result = cur.execute("SELECT AVG(length) FROM spaceships")
    else:
        result = cur.execute(f"SELECT AVG(length) FROM spaceships WHERE category='{category}'")

    res = result.fetchall()
    return res

# Outputs the shortest spaceship in a category
def shortest_spaceship(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships WHERE length=MIN(length)")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE length=MIN(length) AND category='{category}'")

    res = result.fetchall()
    return res

# Outputs the longest spaceship from a manufacturer
def longest_spaceship_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM spaceships WHERE length=MAX(length)")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE length=MAX(length) AND manufacturer='{manufacturer}'")

    res = result.fetchall()
    return res

# Outputs the average spaceship length from a manufacturer
def average_spaceship_length_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT AVG(length) FROM spaceships")
    else:
        result = cur.execute(f"SELECT AVG(length) FROM spaceships WHERE manufacturer='{manufacturer}'")

    res = result.fetchall()
    return res

# Outputs the shortest spaceship from a manufacturer
def shortest_spaceship_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM spaceships WHERE length=MIN(length)")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE length=MIN(length) AND manufacturer='{manufacturer}'")

    res = result.fetchall()
    return res

# Outputs the widest spaceship in a category
def widest_spaceship(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships WHERE width=MAX(width)")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE width=MAX(width) AND category='{category}'")

    res = result.fetchall()
    return res

# Outputs the average spaceship width in a category
def average_spaceship_width(category):
    if category == "all":
        result = cur.execute("SELECT AVG(width) FROM spaceships")
    else:
        result = cur.execute(f"SELECT AVG(width) FROM spaceships WHERE category='{category}'")

    res = result.fetchall()
    return res

# Outputs the least wide spaceship in a category
def least_wide_spaceship(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships WHERE width=MIN(width)")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE width=MIN(width) AND category='{category}'")

    res = result.fetchall()
    return res

# Outputs the widest spaceship from a manufacturer
def widest_spaceship_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM spaceships WHERE width=MAX(width)")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE width=MAX(width) AND manufacturer='{manufacturer}'")

    res = result.fetchall()
    return res

# Outputs the average spaceship width from a manufacturer
def average_spaceship_width_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT AVG(width) FROM spaceships")
    else:
        result = cur.execute(f"SELECT AVG(width) FROM spaceships WHERE manufacturer='{manufacturer}'")

    res = result.fetchall()
    return res

# Outputs the least wide spaceship from a manufacturer
def least_wide_spaceship_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM spaceships WHERE width=MIN(width)")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE width=MIN(width) AND manufacturer='{manufacturer}'")

    res = result.fetchall()
    return res

# Outputs the highest spaceship in a category
def highest_spaceship(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships WHERE height=MAX(height)")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE height=MAX(height) AND category='{category}'")

    res = result.fetchall()
    return res

# Outputs the average spaceship height
def average_spaceship_height(category):
    if category == "all":
        result = cur.execute("SELECT AVG(height) FROM spaceships")
    else:
        result = cur.execute(f"SELECT AVG(height) FROM spaceships WHERE category='{category}'")

    res = result.fetchall()
    return res

# Outputs the lowest spaceship in a category
def lowest_spaceship(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships WHERE height=MIN(height)")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE height=MIN(height) AND category='{category}'")

    res = result.fetchall()
    return res

# Outputs the highest spaceship from a manufacturer
def highest_spaceship_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM spaceships WHERE height=MAX(height)")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE height=MAX(height) AND manufacturer='{manufacturer}'")

    res = result.fetchall()
    return res

# Outputs the average spaceship height from a manufacturer
def average_spaceship_height_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT AVG(height) FROM spaceships")
    else:
        result = cur.execute(f"SELECT AVG(height) FROM spaceships WHERE manufacturer='{manufacturer}'")

    res = result.fetchall()
    return res

# Outputs the lowest spaceship from a manufacturer
def lowest_spaceship_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM spaceships WHERE height=MIN(height)")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE height=MIN(height) AND manufacturer='{manufacturer}'")

    res = result.fetchall()
    return res

# Outputs the spaceship with the most crew members in a category
def most_crewmembers_in_spaceship(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships WHERE crew=MAX(crew)")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE crew=MAX(crew) AND category='{category}'")

    res = result.fetchall()
    return res

# Outputs the average amount of crew members in a spaceship in a category
def average_crewmembers_in_spaceship(category):
    if category == "all":
        result = cur.execute("SELECT AVG(crew) FROM spaceships")
    else:
        result = cur.execute(f"SELECT AVG(crew) FROM spaceships WHERE category='{category}'")

    res = result.fetchall()
    return res

# Outputs the spaceship with the least crew members in a category
def least_crewmembers_in_spaceship(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships WHERE crew=MIN(crew)")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE crew=MIN(crew) AND category='{category}'")

    res = result.fetchall()
    return res

# Outputs the spaceship with the most crew members from a manufacturer
def most_crewmembers_in_spaceship_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM spaceships WHERE crew=MAX(crew)")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE crew=MAX(crew) AND manufacturer='{manufacturer}'")

    res = result.fetchall()
    return res

# Outputs the average amount of crew members in a spaceship from a manufcaturer
def average_crewmembers_in_spaceship_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT AVG(crew) FROM spaceships")
    else:
        result = cur.execute(f"SELECT AVG(crew) FROM spaceships WHERE manufacturer='{manufacturer}'")

    res = result.fetchall()
    return res

# Outputs the spaceship with the least crew members from a manufacturer
def least_crewmembers_in_spaceship_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM spaceships WHERE crew=MIN(crew)")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE crew=MIN(crew) AND manufacturer='{manufacturer}'")

    res = result.fetchall()
    return res

# Outputs the most expensive spaceship in a category
def most_expensive_spaceship(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships WHERE price=MAX(price)")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE price=MAX(price) AND category='{category}'")

    res = result.fetchall()
    return res

# Outputs the average spaceship price in a category
def average_spaceship_price(category):
    if category == "all":
        result = cur.execute("SELECT AVG(price) FROM spaceships")
    else:
        result = cur.execute(f"SELECT AVG(price) FROM spaceships WHERE category='{category}'")

    res = result.fetchall()
    return res

# Outputs the cheapest spaceship in a category
def cheapest_spaceship(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships WHERE price=MIN(price)")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE price=MIN(price) AND category='{category}'")

    res = result.fetchall()
    return res

# Outputs the most expensive spaceship from a manufacturer
def most_expensive_spaceship_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM spaceships WHERE price=MAX(price)")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE price=MAX(price) AND manufacturer='{manufacturer}'")

    res = result.fetchall()
    return res

# Outputs the average spaceship price from a manufacturer
def average_spaceship_price_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT AVG(price) FROM spaceships")
    else:
        result = cur.execute(f"SELECT AVG(price) FROM spaceships WHERE manufacturer='{manufacturer}'")

    res = result.fetchall()
    return res

# Outputs the cheapest spaceship from a manufacturer
def cheapest_spaceship_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM spaceships WHERE price=MIN(price)")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE price=MIN(price) AND manufacturer='{manufacturer}'")

    res = result.fetchall()
    return res

# Outputs the most expensive spaceship in a category with a hyperdrive
def most_expensive_spaceship_with_hyperdrive(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships WHERE price=MAX(price) AND hyperdrive=1")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE price=MAX(price) AND category='{category}' AND hyperdrive=1")

    res = result.fetchall()
    return res

# Outputs the average spaceship price in a category with a hyperdrive
def average_spaceship_price_with_hyperdrive(category):
    if category == "all":
        result = cur.execute("SELECT AVG(price) FROM spaceships WHERE hyperdrive=1")
    else:
        result = cur.execute(f"SELECT AVG(price) FROM spaceships WHERE category='{category}' AND hyperdrive=1")

    res = result.fetchall()
    return res

# Outputs the cheapest spaceship in a category with hyperdrive
def cheapest_spaceship_with_hyperdrive(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships WHERE price=MIN(price) AND hyperdrive=1")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE price=MIN(price) AND category='{category}' AND hyperdrive=1")

    res = result.fetchall()
    return res

# Ouputs the most expensive spaceship with a hyperdrive from a manufacturer
def most_expensive_spaceship_with_hyperdrive_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM spaceships WHERE price=MAX(price) AND hyperdrive=1")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE price=MAX(price) AND manufacturer='{manufacturer}' AND hyperdrive=1")

    res = result.fetchall()
    return res

# Outputs the average spaceship price with hyperdrive from a manufacturer
def average_spaceship_price_with_hyperdrive_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT AVG(price) FROM spaceships WHERE hyperdrive=1")
    else:
        result = cur.execute(f"SELECT AVG(price) FROM spaceships WHERE manufacturer='{manufacturer}' AND hyperdrive=1")

    res = result.fetchall()
    return res

# Outputs the cheapest spaceship with hyperdrive from a manufacturer
def cheapest_spaceship_with_hyperdrive_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM spaceships WHERE price=MIN(price) AND hyperdrive=1")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE price=MIN(price) AND manufacturer='{manufacturer}' AND hyperdrive=1")

    res = result.fetchall()
    return res

# Outputs the most expensive spaceship without a hyperdrive
def most_expensive_spaceship_without_hyperdrive(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships WHERE price=MAX(price) AND hyperdrive=0")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE price=MAX(price) AND category='{category}' AND hyperdrive=0")

    res = result.fetchall()
    return res

# Outputs the average spaceship price in a category without a hyperdrive
def average_spaceship_price_without_hyperdrive(category):
    if category == "all":
        result = cur.execute("SELECT AVG(price) FROM spaceships WHERE hyperdrive=0")
    else:
        result = cur.execute(f"SELECT AVG(price) FROM spaceships WHERE category='{category}' AND hyperdrive=0")

    res = result.fetchall()
    return res

# Outputs the cheapest spaceship in a category without hyperdrive
def cheapest_spaceship_without_hyperdrive(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships WHERE price=MIN(price) AND hyperdrive=0")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE price=MIN(price) AND category='{category}' AND hyperdrive=0")

    res = result.fetchall()
    return res

# Outputs the most expensive spaceship without a hyperdrive from a manufacturer
def most_expensive_spaceship_without_hyperdrive_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM spaceships WHERE price=MAX(price) AND hyperdrive=0")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE price=MAX(price) AND manufacturer='{manufacturer}' AND hyperdrive=0")

    res = result.fetchall()
    return res

# Outputs the average price of spaceships without hyperdrive from a manufcaturer
def average_spaceship_price_without_hyperdrive_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT AVG(price) FROM spaceships WHERE hyperdrive=0")
    else:
        result = cur.execute(f"SELECT AVG(price) FROM spaceships WHERE manufacturer='{manufacturer}' AND hyperdrive=0")

    res = result.fetchall()
    return res

# Outputs the cheapest spaceship without hyperdrive from a manufacturer
def cheapest_spaceship_without_hyperdrive_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM spaceships WHERE price=MIN(price) AND hyperdrive=0")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE price=MIN(price) AND manufacturer='{manufacturer}' AND hyperdrive=0")

    res = result.fetchall()
    return res

# Outputs the fastest spaceship in a category
def fastest_spaceship(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships WHERE max_atmos_speed=MAX(max_atmos_speed)")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE max_atmos_speed=MAX(max_atmos_speed) AND category='{category}'")

    res = result.fetchall()
    return res

# Outputs the slowest spaceship in a category
def slowest_spaceship(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships WHERE max_atmos_speed=MIN(max_atmos_speed)")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE max_atmos_speed=MIN(max_atmos_speed) AND category='{category}'")

    res = result.fetchall()
    return res

# Outputs the fastest spaceship in a category
def fastest_spaceship(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships WHERE max_atmos_speed=MAX(max_atmos_speed)")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE max_atmos_speed=MAX(max_atmos_speed) AND category='{category}'")

    res = result.fetchall()
    return res

# Outputs the average spaceship speed in a category
def average_spaceship_speed(category):
    if category == "all":
        result = cur.execute("SELECT AVG(max_atmos_speed) FROM spaceships")
    else:
        result = cur.execute(f"SELECT AVG(max_atmos_speed) FROM spaceships WHERE category='{category}'")

    res = result.fetchall()
    return res

# Outputs the slowest spaceship in a category
def slowest_spaceship(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships WHERE max_atmos_speed=MIN(max_atmos_speed)")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE max_atmos_speed=MIN(max_atmos_speed) AND category='{category}'")

    res = result.fetchall()
    return res

# Outputs the fastest spaceship from a manufacturer
def fastest_spaceship_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM spaceships WHERE max_atmos_speed=MAX(max_atmos_speed)")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE max_atmos_speed=MAX(max_atmos_speed) AND manufacturer='{manufacturer}'")

    res = result.fetchall()
    return res

# Outputs the average spaceship speed from a manufacturer
def average_spaceship_speed_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT AVG(max_atmos_speed) FROM spaceships")
    else:
        result = cur.execute(f"SELECT AVG(max_atmos_speed) FROM spaceships WHERE manufacturer='{manufacturer}'")

    res = result.fetchall()
    return res

# Outputs the slowest spaceship from a manufacturer
def slowest_spaceship_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM spaceships WHERE max_atmos_speed=MIN(max_atmos_speed)")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE max_atmos_speed=MIN(max_atmos_speed) AND manufacturer='{manufacturer}'")

    res = result.fetchall()
    return res



# Sorting functions

# Sorts spaceships in a category by id in ascending order
def sort_spaceships_by_id_asc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships ORDER BY id ASC")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE category='{category}' ORDER BY id ASC")

    res = result.fetchall()
    return res

# Sorts spaceships in a category by id in descending order
def sort_spaceships_by_id_desc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships ORDER BY id DESC")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE category='{category}' ORDER BY id DESC")

    res = result.fetchall()
    return res

# Sorts spaceships in a category by name in ascending order
def sort_spaceships_by_name_asc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships ORDER BY name ASC")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE category='{category}' ORDER BY name ASC")

    res = result.fetchall()
    return res

# Sorts spaceships in a category by name in descending order
def sort_spaceships_by_name_desc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships ORDER BY name DESC")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE category='{category}' ORDER BY name DESC")

    res = result.fetchall()
    return res

# Sorts spaceships in a category by price in ascending order
def sort_spaceships_by_price_asc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships ORDER BY price ASC")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE category='{category}' ORDER BY price ASC")

    res = result.fetchall()
    return res

# Sorts spaceships in a category by price in descending order
def sort_spaceships_by_price_desc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships ORDER BY price DESC")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE category='{category}' ORDER BY price DESC")

    res = result.fetchall()
    return res

# Sorts spaceships in a category by length in ascending order
def sort_spaceships_by_length_asc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships ORDER BY length ASC")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE category='{category}' ORDER BY length ASC")

    res = result.fetchall()
    return res

# Sorts spaceships in a category by length in descending order
def sort_spaceships_by_length_desc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships ORDER BY length DESC")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE category='{category}' ORDER BY length DESC")

    res = result.fetchall()
    return res

# Sorts spaceships in a category by width in ascending order
def sort_spaceships_by_width_asc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships ORDER BY width ASC")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE category='{category}' ORDER BY width ASC")

    res = result.fetchall()
    return res

# Sorts spaceships in a category by height in ascending order
def sort_spaceships_by_width_desc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships ORDER BY width DESC")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE category='{category}' ORDER BY width DESC")

    res = result.fetchall()
    return res

# Sorts spaceships in a category by height in ascending order
def sort_spaceships_by_height_asc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships ORDER BY height ASC")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE category='{category}' ORDER BY height ASC")

    res = result.fetchall()
    return res

# Sorts spaceships in a category by height in descending order
def sort_spaceships_by_height_desc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships ORDER BY height DESC")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE category='{category}' ORDER BY height DESC")

    res = result.fetchall()
    return res

# Sorts spaceships in a category by crew members in ascending order
def sort_spaceships_by_crew_asc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships ORDER BY crew ASC")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE category='{category}' ORDER BY crew ASC")

    res = result.fetchall()
    return res

# Sorts spaceships in a category by crew members in descending order
def sort_spaceships_by_crew_desc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships ORDER BY crew DESC")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE category='{category}' ORDER BY crew DESC")

    res = result.fetchall()
    return res

# Sorts spaceships in a category by speed in ascending order
def sort_spaceships_by_speed_asc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships ORDER BY max_atmos_speed ASC")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE category='{category}' ORDER BY max_atmos_speed ASC")

    res = result.fetchall()
    return res

# Sorts spaceships in a category by speed in descending order
def sort_spaceships_by_speed_desc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships ORDER BY max_atmos_speed DESC")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE category='{category}' ORDER BY max_atmos_speed DESC")

    res = result.fetchall()
    return res

# Sorts spaceships in a category by amount of turbolasers in ascending order
def sort_spaceships_by_turbolaser_asc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships ORDER BY turbolaser ASC")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE category='{category}' ORDER BY turbolaser ASC")

    res = result.fetchall()
    return res

# Sorts spaceships in a category by amount of turbolasers in descending order
def sort_spaceships_by_turbolaser_desc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships ORDER BY turbolaser DESC")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE category='{category}' ORDER BY turbolaser DESC")

    res = result.fetchall()
    return res

# Sorts spaceships in a category by amount of torpedos in ascending order
def sort_spaceships_by_torpedo_asc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships ORDER BY torpedo ASC")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE category='{category}' ORDER BY torpedo ASC")

    res = result.fetchall()
    return res

# Sorts spaceships in a category by amount of torpedos in descending order
def sort_spaceships_by_torpedo_desc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships ORDER BY torpedo DESC")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE category='{category}' ORDER BY torpedo DESC")

    res = result.fetchall()
    return res





# Commit all changes to the database and close the conection
con.commit()
con.close()
