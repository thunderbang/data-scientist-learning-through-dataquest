## 1. Connection String ##

import psycopg2
conn = psycopg2.connect(dbname='dq', user='postgres', password='abc123')
print(conn)

## 2. Creating a User ##

conn = psycopg2.connect(dbname='dq', user='postgres', password='abc123')
cur = conn.cursor()
cur.execute("CREATE USER data_viewer WITH PASSWORD 'somepassword' NOSUPERUSER")
conn.commit()

## 3. User Privileges ##

conn = psycopg2.connect(dbname="dq", user="dq")
cur = conn.cursor()
cur.execute('REVOKE ALL ON user_accounts FROM data_viewer')
conn.commit()

## 4. Granting Privileges ##

conn = psycopg2.connect(dbname="dq", user="dq")
cur = conn.cursor()
cur.execute('GRANT SELECT ON user_accounts TO data_viewer')
conn.commit()

## 5. Postgres Groups ##

conn = psycopg2.connect(dbname="dq", user="dq")
cur = conn.cursor()
cur.execute('CREATE GROUP readonly NOLOGIN')
cur.execute('REVOKE ALL ON user_accounts FROM readonly')
cur.execute('GRANT SELECT ON user_accounts TO readonly')
cur.execute('GRANT readonly TO data_viewer')
conn.commit()

## 6. Creating a database ##

conn = psycopg2.connect(dbname="dq", user="dq")
# Connection must be set to autocommit.
conn.autocommit = True
cur = conn.cursor()
cur.execute('CREATE DATABASE user_accounts OWNER data_viewer')

## 7. Putting It All Together ##

conn = psycopg2.connect(dbname="dq", user="dq")
conn.autocommit = True
cur = conn.cursor()
cur.execute("CREATE DATABASE top_secret OWNER dq")
conn = psycopg2.connect(dbname="top_secret", user="dq")
cur = conn.cursor()
cur.execute("""
CREATE TABLE documents(id INT, info TEXT);
CREATE GROUP spies NOLOGIN;
REVOKE ALL ON documents FROM spies;
GRANT SELECT, INSERT, UPDATE ON documents TO spies;
CREATE USER double_o_7 WITH CREATEDB PASSWORD 'shakennotstirred' IN GROUP spies;
""")
conn.commit()
conn_007 = psycopg2.connect(dbname='top_secret', user='double_o_7', password='shakennotstirred')