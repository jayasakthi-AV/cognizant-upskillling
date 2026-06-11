select e.event_id , count(r.resource_id) as resource
from events e
left join resources r on e.event_id = r.event_id 
group by e.event_id;