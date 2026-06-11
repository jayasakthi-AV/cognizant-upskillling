select e.city  , count(distinct r.user_id) as user_count
from events e
join registrations r on r.event_id = e.event_id  
group by e.city 
order by  count(distinct r.user_id) desc
limit 5 ;