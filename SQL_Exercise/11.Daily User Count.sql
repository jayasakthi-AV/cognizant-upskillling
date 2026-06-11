select registration_date , count(user_id) as new_user
from users 
where registration_date >= current_date() - INTERVAL 7 day
group by registration_date ;