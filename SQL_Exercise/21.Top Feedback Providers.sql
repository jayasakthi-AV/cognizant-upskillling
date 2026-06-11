select user_id , count(*) as total_feedback
from feedback
group by user_id
order by total_feedback desc
limit 5
;