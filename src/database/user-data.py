#!/usr/bin/env python3
import sqlite3

con = sqlite3.connect("jabbas-data.db")
cur = con.cursor()
# DO NOT USE ANYMORE, tables already created
def create_user_table():
    cur.execute("""CREATE TABLE users(
            user_id INT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL,
            region TEXT,
            balance FLOAT,
            cart TEXT
        )""")

create_user_table()

# Add users until admin inputs "exit"
def add_user():
    username = None
    user_region = None
    user_password = None
    user_balance = None
    user_history = None
    def add_userid():
        con = sqlite3.connect("jabbas-data.db")
        cur = con.cursor()

        id_list = []
        all_ids = cur.execute("SELECT id FROM users")
        user_id = random.randint(1, 10000)

        for userid in all_ids:
            id_list.append(user_id[0])

        while True:
            if user_id in id_list:
                user_id = random.randint(1, 10000)
            else:
                break
        return user_id


    while username not in ["exit", "quit", "q"]:
        username = input("Username: ")
        user_id = add_userid()
        user_region = input("User region: ")
        user_password = input("user password: ")
        user_balance = input("User balance: ")
        user_history = input("User history: ")
        user_data = [
            username,
            user_id,
            user_region,
            user_password,
            user_balance,
            user_history
        ]
        cur.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?, ?)", user_data)
        con.commit()

# Lists all users of the selected region
def get_users_in_region(region):
    user_region = [
        region
    ]
    result = cur.execute(f"SELECT username FROM users WHERE region=?", user_region)
    res = result.fetchall()
    return res[0][0]

# Outputs the history of the user
def get_users_history(username):
    user_name = [
        username
    ]
    result = cur.execute(f"SELECT history FROM users WHERE username=?", user_name)
    res = result.fetchall()
    return res

# Outputs the balance of the user
def get_users_balance(username):
    user_name = [
        username
    ]
    result = cur.execute(f"SELECT balance FROM users WHERE username=?", user_name)
    res = result.fetchall()
    return res

# Outputs the average balance in the given region
def average_balance_in_region(region):
    if region == "all":
        result = cur.execute(f"SELECT AVG(balance) FROM users")

    else:
        user_region = [
            region
        ]
        result = cur.execute(f"SELECT AVG(balance) FROM users WHERE region=?", user_region)

    res = result.fetchall()
    return res

# Outputs the richest user in a region
def richest_user(region):
    if region == "all":
        result = cur.execute(f"SELECT MAX(balance) FROM users")
    else:
        user_region = [
            region
        ]
        result = cur.execute(f"SELECT MAX(balance) FROM users WHERE region=?", user_region)

    res = result.fetchall()
    return res

# Outputs the poorest user in a region
def poorest_user(region):
    if region == "all":
        result = cur.execute(f"SELECT MIN(balance) FROM users")
    else:
        user_region = [
            region
        ]
        result = cur.execute(f"SELECT MIN(balance) FROM users WHERE region=?", user_region)

    res = result.fetchall()
    return res

# Lists users in ascending order
def sort_user_asc(region):
    if region == "all":
        result = cur.execute(f"SELECT * FROM users ORDER BY username ASC")
    else:
        user_region = [
            region
        ]
        result = cur.execute("SELECT * FROM users WHERE region=? ORDER BY username ASC", user_region)

    res = result.fetchall()
    return res

# Lists users in descending order
def sort_users_desc(region):
    if region == "all":
        result = cur.execute(f"SELECT * FROM users ORDER BY username DESC")
    else:
        user_region = [
            region
        ]
        result = cur.execute(f"SELECT * FROM users WHERE region=? ORDER BY username DESC", user_region)

    res = result.fetchall()
    return res



con.commit()
con.close()

