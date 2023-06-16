SELECT age, COUNT(age) as users FROM users
GROUP BY age
HAVING users > 1
ORDER BY users DESC, age;