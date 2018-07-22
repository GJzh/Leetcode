select name, bonus
from Employee left join Bonus using (empId) 
where bonus is null or bonus<1000
