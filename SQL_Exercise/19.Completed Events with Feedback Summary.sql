select e.event_id , 
		e.title , 
		r.total_registration , 
		f.avg_rating
from events e
left join (
select event_id , count(user_id) as total_registration
from registrations 
group by event_id
) r on e.event_id = r.event_id
left join (
select event_id , avg(rating) as avg_rating
from feedback 
group by event_id
) f on e.event_id = f.event_id
where e.status = 'completed'
;