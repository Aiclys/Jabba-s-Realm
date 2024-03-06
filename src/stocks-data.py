#!/usr/bin/env python3
import sqlite3

con = sqlite3.connect("database/stocks.db")
cur = con.cursor()

# DO NOT USE ANYMORE, table already created
def create_table():
    cur.execute("CREATE TABLE stocks(abbrev, full_name, price, change)")

def add_stocks():
    abbrev = None
    full_name = None
    price = None
    change = None
    while abbrev not in ["exit", "quit", "q"]:
        abbrev = input("Stock abbreviation: ")
        full_name = input("Full name of stock: ")
        price = input("Stock price: ")
        change = input("Stock change in the las t 24 hours: ")
        cur.execute(f"INSERT INTO stocks VALUES({abbrev}, {full_name}, {price}, {change})")
