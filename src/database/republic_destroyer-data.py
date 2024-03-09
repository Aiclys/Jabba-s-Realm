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

def sort_users_by_score_asc():
    result = cur.execute("SELECT username FROM rep_dest ORDER BY highscore ASC")
    res = result.fetchall()
    return res

def sort_users_by_score_desc():
    result = cur.execute("SELECT username FROM rep_dest ORDER BY highscore DESC")
    res = result.fetchall()
    return res

def best_user():
    result = cur.execute("SELECT username FROM rep_dest WHERE highscore=MAX(highscore)")
    res = result.fetchall()
    return res

def worst_user():
    result = cur.execute("SELECT username FROM rep_dest WHERE highscore=MIN(highscore)")
    res = result.fethall()
    return res

con.commit()
con.close()
