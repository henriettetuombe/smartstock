-- schema.sql

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(100),
  email VARCHAR(255),
  password VARCHAR(255)
);

CREATE TABLE category (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100)
);

CREATE TABLE item (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  quantity INTEGER,
  price DECIMAL(10, 2),
  status VARCHAR(50),
  category_id INTEGER REFERENCES category(id),
  user_id INTEGER REFERENCES users(id)
);
