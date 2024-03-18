#!/usr/bin/env python3
import sqlite3

con = sqlite3.connect("jabbas-data.db")
cur = con.cursor()

# DO NOT USE ANYMORE, table already created
def create_stock_table():
    stock_table = """CREATE TABLE stocks(
            abbrev TEXT NOT NULL,
            full_name TEXT NOT NULL,
            price FLOAT NOT NULL,
            change FLOAT NOT NULL
    )"""

    cur.execute(stock_table)

def add_stocks():
    abbrev = input("Stock abbreviation: ")
    full_name = input("Full name of stock: ")
    price = input("Stock price: ")
    change = input("Stock change in the las t 24 hours: ")
    stock_data = [
        abbrev,
        full_name,
        price,
        change
    ]
    cur.execute("INSERT INTO stocks VALUES(?, ?, ?, ?)", stock_data)
    con.commit()  # ALWAYS commit after executing INSERT

def get_stock_with_abbrev(abbreviation):
    correct_stock = [abbreviation]
    result = cur.execute("SELECT * FROM stocks WHERE abbrev=?", correct_stock)
    res = result.fetchall()
    return res

def get_stocks_over_price(price):
    stock_price = [price]
    result = cur.execute("SELECT * FROM stocks WHERE price>?", stock_price)
    res = result.fetchall()
    return res

def get_stocks_under_price(price):
    stock_price = [price]
    result = cur.execute("SELECT * FROM stocks WHERE price<?", stock_price)
    res = result.fetchall()
    return res

def get_stocks_over_change(change):
    stock_change = [change]
    result = cur.execute("SELECT * FROM stocks WHERE change>?", stock_change)
    res = result.fetchall()
    return res

def get_stocks_under_change(change):
    stock_change = [change]
    result = cur.execute("SELECT * FROM stocks WHERE change<?", stock_change)
    res = result.fetchall()
    return res

def cheapest_stock():
    result = cur.execute("SELECT * FROM stocks WHERE price=MIN(price)")
    res = result.fetchall()
    return res[0][0]

def most_expensive_stock():
    result = cur.execute("SELECT * FROM stocks WHERE price=MAX(price)")
    res = result.fetchall()
    return res

def highest_stock_change():
    result = cur.execute("SELECT * FROM stocks WHERE change=MAX(change)")
    res = result.fetchall()
    return res

def lowest_stock_change():
    result = cur.execute("SELECT * FROM stocks WHERE change=MIN(change)")
    res = result.fetchall()
    return res

def sort_stocks_by_abbrev_asc():
    result = cur.execute("SELECT * FROM stocks ORDER BY abbrev ASC")
    res = result.fetchall()
    return res

def sort_stocks_by_abbrev_desc():
    result = cur.execute("SELECT * FROM stocks ORDER BY abbrev DESC")
    res = result.fetchall()
    return res

def sort_stocks_by_price_asc():
    result = cur.execute("SELECT * FROM stocks ORDER BY price ASC")
    res = result.fetchall()
    return res

def sort_stocks_by_price_desc():
    result = cur.execute("SELECT * FROM stocks ORDER BY price DESC")
    res = result.fetchall()
    return res


con.commit()
con.close()

