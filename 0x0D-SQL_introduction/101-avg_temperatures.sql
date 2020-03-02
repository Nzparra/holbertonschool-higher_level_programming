-- displays the average temperature (Fahrenheit) by city.
SELECT city, AVG(value) as 'avg_temp' FROM temperatures
GROUP BY 1 ORDER BY 2 DESC;
