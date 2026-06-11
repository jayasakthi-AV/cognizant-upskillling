select e.event_id ,e.title , e.city
from events e
where NOT EXISTS (
select 1 
from resources r
where r.event_id = e.event_id ) ;