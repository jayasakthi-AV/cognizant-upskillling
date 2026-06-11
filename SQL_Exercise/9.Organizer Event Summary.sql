select  e.organizer_id , e.status , count(e.event_id ) as no_of_events
from events e
group by e.organizer_id , e.status
;
