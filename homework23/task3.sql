SELECT users.id, users.first_name, users.last_name, books.title
FROM users
JOIN books
ORDER BY users.id;