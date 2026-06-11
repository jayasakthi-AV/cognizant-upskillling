select e.event_id ,e.title ,  count(r.user_id) as user_count
from events e
join registrations r on e.event_id  = r.event_id
group by e.event_id
order by user_count desc
limit 3
;