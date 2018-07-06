## 1. The EXPLAIN Query ##

import pprint as pp
conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()
cur.execute('EXPLAIN SELECT * FROM homeless_by_coc')
pp.pprint(cur.fetchall())

## 2. The Path of a Query ##

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()
cur.execute("EXPLAIN SELECT COUNT(*) FROM homeless_by_coc WHERE year > '2012-01-01'")
pp.pprint(cur.fetchall())

## 3. Additional Output Formats ##

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()
cur.execute("EXPLAIN (format json) SELECT COUNT(*) FROM homeless_by_coc WHERE year > '2012-01-01'")
pp.pprint(cur.fetchall())

## 4. Describing EXPLAIN Output ##

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()
cur.execute("explain (format json) SELECT count FROM homeless_by_coc")
pp.pprint(cur.fetchall())


## 5. Adding the ANALYZE Option ##

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()
cur.execute("EXPLAIN (ANALYZE, format json) SELECT COUNT(*) FROM homeless_by_coc WHERE year > '2012-01-01'")
pp.pprint(cur.fetchall())

## 6. Test and Rollback ##

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()
cur.execute("EXPLAIN (ANALYZE, format json) DELETE FROM state_household_incomes")
conn.rollback()
pp.pprint(cur.fetchall())

## 7. ANALYZE a Join Statement ##

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()
cur.execute("EXPLAIN (ANALYZE, format json) SELECT h.state, h.coc_number, h.coc_name, s.name FROM homeless_by_coc as h, state_info as s WHERE h.state=s.postal")
pp.pprint(cur.fetchall())