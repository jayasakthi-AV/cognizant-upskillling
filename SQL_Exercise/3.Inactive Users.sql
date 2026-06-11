select *
from users u
join registrations r on u.user_id = r.user_id
where  u.user_id NOT IN (
				select user_id 
                from registrations 
                where registration_date >= current_date() - INTERVAL 90 day ) ; 



