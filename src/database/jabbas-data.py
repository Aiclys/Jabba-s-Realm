#!/usr/bin/env python3
import sqlite3


con = sqlite3.connect("jabbas-data.db")
cur = con.cursor()

# Only run once to create tables
def create_table():
    cur.execute("CREATE TABLE articles(name, category, manufacturer, price, desc)")
    cur.execute("CREATE TABLE users(username, region, password, balance, history)")

# Add articles until admin inputs "exit"
def add_article():
    article_name = None
    article_category = None
    article_region = None
    article_price = None
    article_desc = None
    while article_name != "exit":
        article_name = input("Name of article (type 'exit' to quit): ")
        article_category = input("Article category: ")
        article_region = input("Article region: ")
        article_price = input("Price of article in CRED: ")
        article_desc = input("Article description: ")
        cur.execute(f"INSERT INTO articles VALUES({article_name}, {article_category}, {article_region}, {article_price}, {article_desc})")

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

def get_users_in_region(region):
    result = cur.execute(f"SELECT username FROM users WHERE region='{region}'")
    res = result.fetchall()
    return res[0][0]

def get_users_history(username):
    result = cur.execute(f"SELECT history FROM users WHERE username='{username}'")
    res = result.fetchall()
    return res

def get_users_balance(username):
    result = cur.execute(f"SELECT balance FROM users WHERE username='{username}'")

def average_balance_in_region(region):
    if region == "all":
        result = cur.execute(f"SELECT AVG(balance) FROM users")
        res = result.fetchall()
        return res
    else:
        result = cur.execute(f"SELECT AVG(balance) FROM users WHERE region='{region}'")
        res = result.fetchall()
        return res

#def get_articles_in_region(region):
#    result = cur.execute(f"SELECT name FROM articles WHERE region='{region}'")
#    res = result.fetchall()
#    return res[0][0]

def get_articles_in_category(category):
    result = cur.execute(f"SELECT name FROM articles WHERE category='{category}'")
    res = result.fetchall()
    return res




con.close()
