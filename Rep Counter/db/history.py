#print sql data here.
import sqlite3 as sql
import os
import csv

db_path = "/home/shripad/Projects/AI-Pose-Estimation/Rep Counter/db/rep.db"
conn =  sql.connect(db_path)

print("\n *--History--*")
print("start_time, end_time, date, left, right, total")
cur = conn.cursor()
cur.execute('''SELECT * FROM rep_counter''')
rows = cur.fetchall()
   
for row in rows:
    print(row)

conn.close()