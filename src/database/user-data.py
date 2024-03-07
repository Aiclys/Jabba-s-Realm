#!/usr/bin/env python3
import sqlite3


con = sqlite3.connect("jabbas-data.db")
cur = con.cursor()
# DO NOT USE ANYMORE, tables already created
def create_table():
    cur.execute("CREATE TABLE users(username, password, email, region, balance, history)")

# Add users until admin inputs "exit"
def add_user():
    username = None
    user_region = None
    user_password = None
    user_balance = None
    user_history = None
    while username not in ["exit", "quit", "q"]:
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

create_table()

con.close()
