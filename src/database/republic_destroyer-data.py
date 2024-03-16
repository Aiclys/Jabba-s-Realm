#!/usr/bin/env python3
import sqlite3

con = sqlite3.connect("jabbas-data.db")
cur = con.cursor()


# DO NOT USE ANYMORE, tables already created
def create_rep_dest_table():
    rep_dest_table = """CREATE TABLE rep_dest(
                name TEXT NOT NULL,
                score INT,
                highscore INT
    )"""
    cur.execute(rep_dest_table)

create_rep_dest_table()

# Adds a player
def add_player():
    name = input("Player name: ")
    score = int(input("Score: "))
    highscore = int(input("Highscore: "))
    player_data = [
        name,
        score,
        highscore
    ]
    cur.execute("INSERT INTO rep_dest VALUES(?, ?, ?)", player_data)

# Sorts users by score in ascending order
def sort_users_by_highscore_asc():
    result = cur.execute("SELECT username FROM rep_dest ORDER BY highscore ASC")
    res = result.fetchall()
    return res

# Sorts users by score in descending order
def sort_users_by_highscore_desc():
    result = cur.execute("SELECT username FROM rep_dest ORDER BY highscore DESC")
    res = result.fetchall()
    return res

# Ouputs the best user by highscore
def best_user():
    result = cur.execute("SELECT username, highscore FROM rep_dest WHERE highscore=MAX(highscore)")
    res = result.fetchall()
    return res

# Ouputs the worst user by highscore
def worst_user():
    result = cur.execute("SELECT username, highscore FROM rep_dest WHERE highscore=MIN(highscore)")
    res = result.fethall()
    return res

con.commit()
con.close()
