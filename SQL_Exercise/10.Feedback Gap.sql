select e.event_id , e.title
from events e
where e.event_id IN ( select event_id from registrations ) AND 
	e.event_id NOT IN (select event_id from feedback ) ;