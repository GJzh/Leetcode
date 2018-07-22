SELECT Weather1.Id as Id
FROM Weather Weather1, Weather Weather2
WHERE DATEDIFF(Weather1.Date, Weather2.Date) = 1 AND Weather1.Temperature > Weather2.Temperature
