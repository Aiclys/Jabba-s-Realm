#!/usr/bin/env python3
import sqlite3


con = sqlite3.connect("jabbas-data.db")
cur = con.cursor()

# DO NOT use this function anymore, database and tables already created
def create_table():
    cur.execute("CREATE TABLE articles(name, category, region, price, desc)")
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

# Add users intol admin inputs "exit"
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

def get_users_for_region(region):
    result = cur.execute(f"SELECT username FROM users WHERE region='{region}'")
    res = result.fetchall()
    return res[0][0]

def get_articles_for_region(region):
    result = cur.execute(f"SELECT name FROM articles WHERE region='{region}'")
    res = result.fetchall()
    return res[0][0]



con.close()
