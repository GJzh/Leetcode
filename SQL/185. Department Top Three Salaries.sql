SELECT D.Name as Department,
       E.Name as Employee,
       E.Salary as Salary
FROM Department D, Employee E
WHERE (SELECT COUNT(DISTINCT Salary) 
       FROM Employee WHERE Salary > E.Salary AND DepartmentId = E.DepartmentId) < 3
      AND D.Id = E.DepartmentId
ORDER BY D.Id, E.Salary DESC
