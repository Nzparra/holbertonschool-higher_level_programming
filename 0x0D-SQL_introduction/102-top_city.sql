-- script that displays the top 3 of cities temperature during July and August
SELECT city, AVG(value) as avg_temp 
FROM temperatures 
WHERE month BETWEEN 7 and 8 
GROUP BY 1 
ORDER BY 2 DESC 
LIMIT 3; 
