select Name
from (select b.Name as Name, count(*) as reportCount 
      from Employee a join Employee b on a.ManagerId = b.Id group by b.Name) p
where reportCount >= 5
