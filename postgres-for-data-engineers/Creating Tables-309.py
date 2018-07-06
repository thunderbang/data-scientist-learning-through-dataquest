## 1. Describing a Table ##

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute('SELECT * FROM ign_reviews LIMIT 0')
print(cur.description)

## 2. Adding the id Field ##

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute('CREATE TABLE ign_reviews (id BIGINT PRIMARY KEY)')
conn.commit()

## 3. Finding the Max Length ##

import csv
with open('ign.csv') as f:
    next(f)
    reader = csv.reader(f)
    score = set([len(row[1]) for row in reader])
    max_score = max(score)

## 4. Max String-like Datatypes ##

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
# Add your field and type here.
# Uncomment the following.
cur.execute('drop TABLE ign_reviews')
cur.execute("""
    CREATE TABLE ign_reviews (
        id BIGINT PRIMARY KEY,
        score_phrase VARCHAR(11)
    )
""")
conn.commit()

## 5. Creating the Other String Fields ##

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
# Add your fields and types here.
cur.execute("""
    CREATE TABLE ign_reviews (
        id BIGINT PRIMARY KEY,
        score_phrase VARCHAR(11),
        title TEXT,
        url TEXT,
        platform VARCHAR(20),
        genre TEXT
    )
""")
conn.commit()

## 6. Float-like Types ##

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
# Add your field and type here.
cur.execute("""
    CREATE TABLE ign_reviews (
        id BIGINT PRIMARY KEY,
        score_phrase VARCHAR(11),
        title TEXT,
        url TEXT,
        platform VARCHAR(20),
        genre TEXT,
        score DECIMAL(3, 1)
    )
""")
conn.commit()

## 7. Boolean Types ##

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
# Add your fields and types here.
cur.execute("""
    CREATE TABLE ign_reviews (
        id BIGINT PRIMARY KEY,
        score_phrase VARCHAR(11),
        title TEXT,
        url TEXT,
        platform VARCHAR(20),
        score DECIMAL(3, 1),
        genre TEXT,
        editors_choice BOOLEAN
   )
""")
conn.commit()

## 8. Date Type ##

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
# Add your field here.
#cur.execute("""
#    CREATE TABLE ign_reviews (
#        id BIGINT PRIMARY KEY,
#        score_phrase VARCHAR(11),
#        title TEXT,
#        url TEXT,
#        platform VARCHAR(20),
#        score DECIMAL(3, 1),
#        genre TEXT
#   )
#""")
import csv
from datetime import date
cur.execute("""
    CREATE TABLE ign_reviews (
        id BIGINT PRIMARY KEY,
        score_phrase VARCHAR(11),
        title TEXT,
        url TEXT,
        platform VARCHAR(20),
        score DECIMAL(3, 1),
        genre TEXT,
        editors_choice BOOLEAN,
        release_date DATE
    )
""")

with open('ign.csv', 'r') as f:
    next(f)
    reader = csv.reader(f)
    for row in reader:
        updated_row = row[:8]
        updated_row.append(date(int(row[8]), int(row[9]), int(row[10])))
        cur.execute("INSERT INTO ign_reviews VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", updated_row)
conn.commit()