CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE posts (
    id INTEGER PRIMARY KEY,
    title TEXT,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

INSERT INTO users (id, name)
VALUES (1, 'Saba');

INSERT INTO posts (id, title, user_id)
VALUES
(1, 'My first post', 1),
(2, 'My second post', 1),
(3, 'My third post', 1);

SELECT *
FROM posts
WHERE user_id = 1;
