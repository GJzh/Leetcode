select Id, t1.Company as Company, Salary
from (select Id, 
             Company, 
             Salary, 
             (select count(Id) from Employee 
              where ((a.Salary>Salary or (a.Salary=Salary and a.Id>=Id) ) and a.Company = Company) ) as rank
     from Employee a) t1
     join
     (select Company, count(*) as CompanySum from Employee group by Company) t2
     using (Company)
where rank between CompanySum/2 and CompanySum/2+1
