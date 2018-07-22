SELECT Department.Name as Department,
       Employee.Name as Employee, 
       Employee.Salary as Salary
FROM (Employee JOIN Department ON Employee.DepartmentId = Department.Id)
     JOIN (SELECT DepartmentId as Id, MAX(Salary) as Salary
           FROM Employee GROUP BY DepartmentId) q 
     ON Employee.Salary=q.Salary AND Department.Id = q.Id
