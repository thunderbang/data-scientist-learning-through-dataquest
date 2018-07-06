## 1. The psql tool ##


psql <<EOF
EOF

## 3. Special PostgreSQL commands ##


psql <<EOF
\l
EOF

## 4. Switching databases ##


psql -d bank_accounts <<EOF
CREATE TABLE deposits (
    id integer PRIMARY KEY,
    name text,
    amount float
);
EOF

## 5. Creating users ##


psql <<EOF
CREATE ROLE sec WITH LOGIN CREATEDB PASSWORD 'test';
EOF