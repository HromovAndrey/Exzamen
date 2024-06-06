-- CREATE TABLE users (
--     id SERIAL PRIMARY KEY,
--     username VARCHAR(255) NOT NULL,
--     password VARCHAR(255) NOT NULL,
--     email VARCHAR(255) NOT NULL
-- );

--INSERT INTO users (username, password, email) VALUES ('username', 'hashed_password', 'user@example.com');

--SELECT * FROM users WHERE username = 'username' AND password = 'hashed_password';

-- CREATE TABLE pages (
--     id SERIAL PRIMARY KEY,
--     user_id INT NOT NULL,
--     title VARCHAR(255) NOT NULL,
--     content TEXT NOT NULL,
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     FOREIGN KEY (user_id) REFERENCES users(id)
-- );

--INSERT INTO pages (user_id, title, content, created_at) VALUES (user_id, 'Page Title', 'Page Content', 'YYYY-MM-DD HH:MM:SS');

--SELECT * FROM pages WHERE title LIKE '%keyword%' OR content LIKE '%keyword%';
