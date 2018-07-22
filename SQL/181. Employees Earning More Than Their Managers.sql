SELECT Employee
From ( SELECT EmployeelEFT.Name as Employee , EmployeelEFT.Salary as EmployeeSalary, EmployeeRIGHT.Salary as ManagerSalary
FROM Employee EmployeelEFT
LEFT JOIN Employee EmployeeRIGHT
ON EmployeelEFT.ManagerId = EmployeeRIGHT.Id) as JoinedEmployee
WHERE EmployeeSalary > ManagerSalary
