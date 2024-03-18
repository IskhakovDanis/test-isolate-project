CREATE TABLE IF NOT EXISTS stores (
store_id INTEGER PRIMARY KEY,
store_name VARCHAR(255) NOT NULL,
location VARCHAR(255),
address VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS products (
product_id INTEGER PRIMARY KEY,
product_name VARCHAR(255) NOT NULL,
is_available BOOLEAN NOT NULL,
store_id INTEGER REFERENCES stores(store_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS users (
id SERIAL PRIMARY KEY,
email VARCHAR(255) NOT NULL UNIQUE,
username VARCHAR(255) NOT NULL UNIQUE,
first_name VARCHAR(255),
last_name VARCHAR(255),
hashed_password VARCHAR(255),
is_active BOOLEAN NOT NULL,
role VARCHAR(255)
);

INSERT INTO stores (store_id, store_name, location, address) VALUES (1, 'New Store', 'Spain', 'Avenue 1');
INSERT INTO stores (store_id, store_name, location, address) VALUES (2, 'Big Store', 'France', 'Street 111');