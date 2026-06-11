with event_session as (
select e.event_id , count(s.session_id) as sessions
from events e
join sessions s on e.event_id = s.event_id
group by e.event_id  
)
select event_id , sessions 
from event_session
where sessions = (select max(sessions) from event_session) ;
;