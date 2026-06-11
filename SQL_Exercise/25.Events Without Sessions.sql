select *
from events e
where not exists(
select 1
from sessions s
where e.event_id = s.event_id
);