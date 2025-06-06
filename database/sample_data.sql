-- sample_data.sql

INSERT INTO users (username, email, password) VALUES
('henriette', 'henriette@example.com', 'hashed_password');

INSERT INTO category (name) VALUES
('Food'), ('Clothes'), ('Hygiene');

INSERT INTO item (name, quantity, price, status, category_id, user_id) VALUES
('Rice', 34, 1200.00, 'in_stock', 1, 1),
('Soap', 10, 500.00, 'in_stock', 3, 1);
