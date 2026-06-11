select 
event_id , avg(timestampdiff(minute , start_time , end_time)) as avg_session_duration 
from sessions
group by event_id ;