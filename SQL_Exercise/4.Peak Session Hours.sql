select e.event_id  , count(s.session_id)
from events e
join sessions s on e.event_id = s.event_id  
where time(s.start_time) > '10:00:00' and time(s.end_time) < '12:00:00'  
Group by e.event_id ;