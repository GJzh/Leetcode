select t.follower, num 
from (select a.follower, count(distinct b.follower) as num 
      from (follow a join follow b on a.follower = b.followee)
      group by a.follower) t
order by t.follower
