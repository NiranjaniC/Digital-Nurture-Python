-- User Upcoming Events
-- Show a list of all upcoming events a user is registered for in their city, sorted by date.


SELECT u.full_name,e.title,e.city,e.start_date FROM Users u JOIN registrations r ON u.user_id = r.user_id JOIN events e ON r.event_id=e.event_id WHERE e.status = 'upcoming' AND u.city = e.city ORDER BY e.start_date;