select speaker_name
from sessions 
group by speaker_name
having count(speaker_name) > 1 ;