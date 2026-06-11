
with city_rating as (
select e.event_id , f.rating , e.city
from events e
join feedback f on e.event_id = f.event_id
)

select city ,avg (rating)  as avg_rating
from city_rating
group by city

;