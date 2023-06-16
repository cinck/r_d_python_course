SELECT age, COUNT(age) as users FROM users
GROUP BY age
ORDER BY users DESC, age;