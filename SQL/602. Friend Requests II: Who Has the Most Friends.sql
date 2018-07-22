select id, sum(num) as num
from ((select requester_id as id, count(*) as num from request_accepted group by requester_id)
       union all
      (select accepter_id as id, count(*) as num from request_accepted group by accepter_id)) t
group by id
order by num desc
limit 1
