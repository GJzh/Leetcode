select distinct a.id as id, (case when a.p_id is null then 'Root'
                   when b.id is null then 'Leaf'
                   else 'Inner'
              end) as Type
from tree a left join tree b on b.p_id = a.id
