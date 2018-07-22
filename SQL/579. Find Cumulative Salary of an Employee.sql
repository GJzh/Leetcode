select Id, Month, (select sum(Salary) from Employee where Id=t.Id and Month<=t.Month and abs(Month-t.Month)<3) as Salary
from (select * from Employee a where (select count(*) from Employee where a.Id=Id and Month>a.Month)>0) t
order by Id, Month desc
