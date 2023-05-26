-- запит, який для кожного user порахує суму всіх покупок.
-- Результат має бути представлений у форматі: users.id, users.first_name, users.last_name, total_purchases
SELECT users.id, users.first_name, users.last_name, SUM(books.price) as total_purchases
FROM purchase
JOIN users ON purchase.user_id= users.id
JOIN books ON purchase.book_id = books.id
GROUP BY users.id;

-- запит, який виведе кількість покупок книжок для кожного user.
-- Результат має бути представлений у форматі: user.id, purchases_count
SELECT users.id, COUNT(purchase.user_id) as purchase_count
FROM purchase
JOIN users ON purchase.user_id = users.id
GROUP BY users.id;

-- запит, який виведе кількість покупок книжок для автора Rowling.
-- Результат має бути представлений у форматі: amount
SELECT COUNT(book_id) as amount
FROM purchase
JOIN books ON purchase.book_id = books.id
WHERE author == "Rowling";


-- запит, який виведе загальні суми продажів для кожного автора та кількість покупок.
SELECT books.author, COUNT(books.id) as qty_sold, SUM(books.price) as total_sum
FROM purchase
JOIN books ON purchase.book_id = books.id
GROUP BY books.author;

-- запит, який виведе всі назви книжок із кількістю їх продажів в порядку спадання кількості продажів.
SELECT books.title, count(books.id) as qty_sold
FROM purchase
JOIN books ON purchase.book_id = books.id
GROUP BY books.title
ORDER BY qty_sold DESC, qty_sold;