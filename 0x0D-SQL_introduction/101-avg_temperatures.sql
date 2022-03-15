-- order ttemp
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE city IS NOT NULL AND value IS NOT NULL GROUP BY city ORDER BY avg_temp DESC;
