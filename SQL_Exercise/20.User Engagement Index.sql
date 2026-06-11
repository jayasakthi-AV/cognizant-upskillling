select u.user_id , 
		COALESCE (e.registration , 0) AS total_events_registration ,
        COALESCE (f.total_feedback  , 0) AS total_feedback
from users u
left join (
select user_id , count(event_id) as registration
from registrations 
group by user_id 
) e on u.user_id = e.user_id

left join (
select user_id , count(*) as total_feedback
from feedback
group by user_id
) f on u.user_id = f.user_id
;