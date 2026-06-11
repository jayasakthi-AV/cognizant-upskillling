select u.user_id , e.title , f.comments
from users u
join feedback f on u.user_id = f.user_id
join events e on f.event_id = e.event_id
where f.rating < 3 ;