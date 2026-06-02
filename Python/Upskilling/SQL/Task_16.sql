SELECT 
u.user_id,
u.full_name 
FROM Users u LEFT JOIN registrations r ON u.user_id = r.user_id where u.registration_date >= CURDATE() - INTERVAL 30 DAY and  r.user_id is null;