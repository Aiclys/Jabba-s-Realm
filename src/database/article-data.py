#!/usr/bin/env python3
import sqlite3

con = sqlite3.connect("jabbas-data.db")
cur = con.cursor()


def create_table():
    cur.execute("CREATE TABLE articles(name, category, manufacturer, price, desc)")


# Add articles until admin inputs "exit"
def add_article():
    article_name = None
    article_category = None
    article_manufacturer = None
    article_price = None
    article_desc = None
    while article_name not in ["exit", "quit", "q"]:
        article_name = input("Name of article (type 'exit' to quit): ")
        article_category = input("Article category: ")
        article_manufacturer = input("Article manufacturer: ")
        article_price = input("Price of article in CRED: ")
        article_desc = input("Article description: ")
        cur.execute(f"INSERT INTO articles VALUES({article_name}, {article_category}, {article_manufacturer}, {article_price}, {article_desc})")

# Lists all articles in a category
def get_articles_in_category(category):
    result = cur.execute(f"SELECT name FROM articles WHERE category='{category}'")
    res = result.fetchall()
    return res

# Lists the most expensive item in a category
def most_expensive_in_category(category):
    if category == "all":
        result = cur.execute(f"SELECT name FROM articles WHERE price=MAX(price)")
    else:
        result = cur.execute(f"SELECT name FROM articles WHERE category='{category}' AND price=MAX(price)")

    res = result.fetchall()
    return res[0][0]

# Outputs the cheapest item in a category
def cheapest_in_category(category):
    if category == "all":
        result = cur.execute(f"SELECT name FROM articles WHERE price=MIN(price)")
    else:
        result = cur.execute(f"SELECT name FROM articles WHERE category='{category}' AND price=MIN(price)")

    res = result.fetchall()
    return res[0][0]

# Lists all articles from a specific manufacturer
def get_articles_from_manufacturer(manufacturer):
    result = cur.execute(f"SELECT name FROM articles WHERE manufacturer='{manufacturer}'")
    res = result.fetchall()
    return res[0][0]

# Ouputs the most expensive article of a given manufacturer
def most_expensive_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute(f"SELECT name FROM articles WHERE price=MAX(price)")
    else:
        result = cur.execute(f"SELECT name FROM articles WHERE price=MAX(price) AND manufacturer='{manufacturer}'")

    res = result.fetchall()
    return res[0][0]

# Outputs the cheapest item of a manufacturer
def cheapest_from_manufacturer(manufacturer):
    if manufacturer == "all":
        result = cur.execute(f"SELECT name FROM articles WHERE price=MIN(price)")
    else:
        result = cur.execute(f"SELECT name FROM articles WHERE price=MIN(price) AND manufacturer='{manufacturer}'")

    res = result.fetchall()
    return res[0][0]

# Lists articles by name in ascending order
def sort_articles_by_name_asc(region):
    if region == "all":
        result = cur.execute(f"SELECT * FROM articles ORDER BY name ASC")
    else:
        result = cur.execute(f"SELECT * FROM articles WHERE region='{region}' ORDER BY name ASC")

    res = result.fetchall()
    return res

# Lists articles by name in descending order
def sort_articles_by_name_desc(region):
    if region == "all":
        result = cur.execute(f"SELECT * FROM articles ORDER BY name DESC")
    else:
        result = cur.execute(f"SELECT * FROM articles WHERE region='{region}' ORDER BY name DESC")

    res = result.fetchall()
    return res

# Lists articles by price in ascending order
def sort_articles_by_price_asc(region):
    if region == "all":
        result = cur.execute(f"SELECT * FROM articles ORDER BY price ASC")
    else:
        result = cur.execute(f"SELECT * FROM articles WHERE region='{region}' ORDER BY price ASC")

    res = result.fetchall()
    return res

# Lists articles by price in descending order
def sort_articles_by_price_desc(region):
    if region == "all":
        result = cur.execute(f"SELECT * FROM articles ORDER BY price DESC")
    else:
        result = cur.execute(f"SELECT * FROM articles WHERE region='{region}' ORDER BY price DESC")

    res = result.fetchall()
    return res


create_table()

con.close()
