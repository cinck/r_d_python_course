
-- Написати запит, який виведе всіх users і назви  всіх книжок, які вони купували, відсортувати дані за user_id.
-- Результат має бути представлений у форматі: users.id, users.first_name, users.last_name, books.title

SELECT users.id, users.first_name, users.last_name, books.title
FROM users
JOIN books
ORDER BY users.id;