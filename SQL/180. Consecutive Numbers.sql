SELECT DISTINCT a.Num as ConsecutiveNums
FROM Logs a, Logs b, Logs c
WHERE a.Num = b.Num AND b.Num = c.Num AND a.Id+1 = b.Id AND b.Id+1 = c.Id
