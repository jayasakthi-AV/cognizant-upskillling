select e.event_id , e.title , u.user_id , u.full_name , e.start_date
from events e
join registrations r on e.event_id = r.event_id
join users u on r.user_id = u.user_id
where
 e.start_date > '2025-05-16'   and
 r.user_id = u.user_id 
 order by e.start_date;

