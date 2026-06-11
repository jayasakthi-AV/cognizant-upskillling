SELECT *
FROM users u
WHERE u.registration_date >= CURDATE() - INTERVAL 30 DAY
AND NOT EXISTS (
    SELECT 1
    FROM registrations r
    WHERE r.user_id = u.user_id
);