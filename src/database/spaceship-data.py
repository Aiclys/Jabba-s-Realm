#!/usr/bin/env python3
import sqlite3

con = sqlite3.connect("jabbas-data.db")
cur = con.cursor()


def create_spaceship_table():
    spaceship_table = """CREATE TABLE if not exists spaceships(
                id INT NOT NULL,
                name TEXT NOT NULL,
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

def add_spaceships():
    spaceship_id = int(input("Spaceship id: "))
    name = input("Spaceship name: ")
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

def get_spaceship_by_id(spaceship_id):
    if spaceship_id == "all":
        result = cur.execute("SELECT * FROM spaceships")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE id={spaceship_id}")

    res = result.fetchall()
    return res

def get_spaceships_by_name(name):
    if name == "all":
        result = cur.execute("SELECT * FROM spaceships")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE name='{name}'")

    res = result.fetchall()
    return res

def get_spaceships_over_price(price):
    result = cur.execute(f"SELECT * FROM spaceships WHERE price>{price}")
    res = result.fetchall()
    return res

def get_spaceships_under_price(price):
    result = cur.execute(f"SELECT * FROM spaceships WHERE price<{price}")
    res = result.fetchall()
    return res

def get_spaceships_in_category(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE category='{category}'")

    res = result.fetchall()
    return res

def get_spaceships_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute("SELECT * FROM spaceships")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE manufacturer='{manufacturer}'")

    res = result.fetchall()
    return res

def get_spaceships_over_length(length):
    result = cur.execute(f"SELECT * FROM spaceships WHERE length>{length}")
    res = result.fetchall()
    return res

def get_spaceships_under_length(length):
    result = cur.execute(f"SELECT * FROM spaceships WHERE length<{length}")
    res = result.fetchall()
    return res

def get_spaceships_over_width(width):
    result = cur.execute(f"SELECT * FROM spaceships WHERE width>{width}")
    res = result.fetchall()
    return res

def get_spaceships_under_width(width):
    result = cur.execute(f"SELECT * FROM spaceships WHERE width<{width}")
    res = result.fetchall()
    return res

def get_spaceships_over_height(height):
    result = cur.execute(f"SELECT * FROM spaceships WHERE height>{height}")
    res = result.fetchall()
    return res

def get_spaceships_under_height(height):
    result = cur.execute(f"SELECT * FROM spaceships WHERE height<{height}")
    res = result.fetchall()
    return res

def get_spaceships_over_crewmembers(crewmembers):
    result = cur.execute(f"SELECT * FROM spaceships WHERE crew>{crewmembers}")
    res = result.fetchall()
    return res

def get_spaceships_under_crewmembers(crewmembers):
    result = cur.execute(f"SELECT * FROM spaceships WHERE crew<{crewmembers}")
    res = result.fetchall()
    return res

def get_spaceships_with_role(role):
    if role == "all":
        result = cur.execute("SELECT * FROM spaceships")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE role='{role}'")

    res = result.fetchall()
    return res

def get_spaceships_over_speed(speed):
    result = cur.execute(f"SELECT * FROM spaceships WHERE max_atmos_speed>{speed}")
    res = result.fetchall()
    return res

def get_spaceships_under_speed(speed):
    result = cur.execute(f"SELECT * FROM spaceships WHERE max_atmos_speed<{speed}")
    res = result.fetchall()
    return res

def get_spaceships_with_hyperdrive(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships WHERE hyperdrive=1")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE hyperdrive=1 AND category={category}")

    res = result.fetchall()
    return res

def get_spaceships_without_hyperdrive(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships WHERE hyperdrive=0")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE hyperdrive=0 AND category={category}")

    res = result.fetchall()
    return res

def get_spaceships_with_shielding(shielding):
    if shielding == "all":
        result = cur.execute("SELECT * FROM spaceships")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE shielding = '{shielding}'")

    res = result.fetchall()
    return res

def get_spaceships_with_engine(engine):
    result = cur.execute(f"SELECT * FROM spaceships WHERE engine='{engine}'")
    res = result.fetchall()
    return res

def get_spaceships_with_turbolasers(turbolasers):
    result = cur.execute(f"SELECT * FROM spaceships WHERE turbolasers={turbolasers}")
    res = result.fetchall()
    return res

def get_spaceships_with_torpedos(torpedo):
    result = cur.execute(f"SELECT * FROM spaceships WHERE torpedo={torpedo}")
    res = result.fetchall()
    return res

def get_spaceships_with_consumables(consumables):
    result = cur.execute(f"SELECT * FROM spaceships WHERE consumables='{consumables}'")
    res = result.fetchall()
    return res



# TODO later because I'm tired and it's exhausting
def get_spaceships_with_shielding_in_category(shielding, category):
    result = cur.execute(f"SELECT * FROM spaceships WHERE category='{category}' AND shielding='{shielding}'")
    res = result.fetchall()
    return res


# Sorting functions

def sort_spaceships_by_id_asc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships ORDER BY id ASC")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE category='{category}' ORDER BY id ASC")

    res = result.fetchall()
    return res

def sort_spaceships_by_id_desc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships ORDER BY id DESC")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE category='{category}' ORDER BY id DESC")

    res = result.fetchall()
    return res

def sort_spaceships_by_name_asc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships ORDER BY name ASC")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE category='{category}' ORDER BY name ASC")

    res = result.fetchall()
    return res

def sort_spaceships_by_name_desc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships ORDER BY name DESC")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE category='{category}' ORDER BY name DESC")

    res = result.fetchall()
    return res

def sort_spaceships_by_price_asc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships ORDER BY price ASC")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE category='{category}' ORDER BY price ASC")

    res = result.fetchall()
    return res

def sort_spaceships_by_price_desc(category):
    if category == "all":
        result = cur.execute("SELECT * FROM spaceships ORDER BY price DESC")
    else:
        result = cur.execute(f"SELECT * FROM spaceships WHERE category='{category}' ORDER BY price DESC")

    res = result.fetchall()
    return res






con.commit()
con.close()
