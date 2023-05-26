SELECT purchase.id as p_id, purchase.date, users.first_name, users.last_name
FROM purchase
JOIN users;