SELECT
    DATE_FORMAT(registration_date, '%b %Y') AS month,
    COUNT(*) AS registration_count
FROM Registrations
WHERE registration_date >= CURDATE() - INTERVAL 12 MONTH
GROUP BY YEAR(registration_date), MONTH(registration_date)
ORDER BY YEAR(registration_date), MONTH(registration_date);