select 
date_format(registration_date , '%Y-%m') as month , 
count(*) as total_registrations
from registrations 
where registration_date >= date_sub(curdate()  , interval 12 month)
group by date_format(registration_date , '%Y-%m')
order by month ;