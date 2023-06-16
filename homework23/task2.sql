-- Написати запит, який виведе дату покупки і імʼя користувача, що її здійснив.
-- Результат має бути представлений у форматі: purchases.id, purchases.date, user.first_name, user.last_name

SELECT purchase.id as p_id, purchase.date, users.first_name, users.last_name
FROM purchase
JOIN users;