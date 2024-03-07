#!/usr/bin/env python3
import sqlite3

con = sqlite3.connect("jabbas-data.db")
cur = con.cursor()


def create_starship_table():
    starship_table = """CREATE TABLE if not exists spaceships(
                id INT NOT NULL,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                manufacturer TEXT,
                price FLOAT NOT NULL,
                length FLOAT,
                width FLOAT,
                height FLOAT,
                crew INT,
                passengers INT,
                cargo_cap FLOAT,
                role TEXT,
                max_atmos_speed FLOAT,
                hyperdrive BOOLEAN,
                shielding TEXT,
                power_method TEXT,
                turbolaser INT,
                torpedo INT,
                consumables TEXT
    )"""

    cur.execute(starship_table)

create_starship_table()

con.close()
