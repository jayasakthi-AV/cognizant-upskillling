select user_id , event_id , count(*) as reg_count
from registrations
group by user_id , event_id
having count(*) > 1
;