select e.event_id , avg(f.rating) as avg_rating
from events e
join feedback f on f.event_id = e.event_id
group by e.event_id
having count(f.feedback_id) >= 10
order by  AVG(rating) desc;
