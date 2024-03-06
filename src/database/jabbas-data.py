#!/usr/bin/env python3
import sqlite3


con = sqlite3.connect("jabbas-data.db")
cur = con.cursor()

# DO NOT USE ANYMORE, tables already created
def create_table():
    cur.execute("CREATE TABLE articles(name, category, manufacturer, price, desc)")
    cur.execute("CREATE TABLE users(username, region, password, balance, history)")


# USERS

# Add users until admin inputs "exit"
def add_user():
    username = None
    user_region = None
    user_password = None
    user_balance = None
    user_history = None
    while username != "exit":
        username = input("Username: ")
        user_region = input("User region: ")
        user_password = input("user password: ")
        user_balance = input("User balance: ")
        user_history = input("User history: ")
        cur.execute(f"INSERT INTO users VALUES({username}, {user_region}, {user_password}, {user_balance}, {user_history})")

# Lists all users of the selected region
def get_users_in_region(region):
    result = cur.execute(f"SELECT username FROM users WHERE region='{region}'")
    res = result.fetchall()
    return res[0][0]

# Outputs the history of the user
def get_users_history(username):
    result = cur.execute(f"SELECT history FROM users WHERE username='{username}'")
    res = result.fetchall()
    return res

# Outputs the balance of the user
def get_users_balance(username):
    result = cur.execute(f"SELECT balance FROM users WHERE username='{username}'")

# Outputs the average balance in the given region
def average_balance_in_region(region):
    if region == "all":
        result = cur.execute(f"SELECT AVG(balance) FROM users")

    else:
        result = cur.execute(f"SELECT AVG(balance) FROM users WHERE region='{region}'")

    res = result.fetchall()
    return res

# Outputs the richest user in a region
def richest_user(region):
    if region == "all":
        result = cur.execute(f"SELECT MAX(balance) FROM users")
    else:
        result = cur.execute(f"SELECT MAX(balance) FROM users WHERE region='{region}'")

    res = result.fetchall()
    return res

# Outputs the poorest user in a region
def poorest_user(region):
    if region == "all":
        result = cur.execute(f"SELECT MIN(balance) FROM users")
    else:
        result = cur.execute(f"SELECT MIN(balance) FROM users WHERE region='{region}'")

    res = result.fetchall()
    return res

# Lists users in ascending order
def sort_user_asc(region):
    if region == "all":
        result = cur.execute(f"SELECT * FROM users ORDER BY username ASC")
    else:
        result = cur.execute(f"SELECT * FROM users WHERE region='{region}' ORDER BY username ASC")

    res = result.fetchall()
    return res

# Lists users in descending order
def sort_users_desc(region):
    if region == "all":
        result = cur.execute(f"SELECT * FROM users ORDER BY username DESC")
    else:
        result = cur.execute(f"SELECT * FROM users WHERE region='{region}' ORDER BY username DESC")

    res = result.fetchall()
    return res





# ARTICLES

# Add articles until admin inputs "exit"
def add_article():
    article_name = None
    article_category = None
    article_manufacturer = None
    article_price = None
    article_desc = None
    while article_name != "exit":
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



con.close()
