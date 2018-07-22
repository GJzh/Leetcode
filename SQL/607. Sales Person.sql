select name from salesperson
where name not in 
(select DISTINCT salesperson.name as name
from (salesperson left join orders using (sales_id) ) 
      join company using (com_id)
where company.name = 'RED')
