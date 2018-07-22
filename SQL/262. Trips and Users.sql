SELECT Day, ROUND(AVG(Cancellation), 2) as 'Cancellation Rate'
FROM (SELECT Request_at as Day,
             (CASE WHEN Status = 'cancelled_by_client' THEN 1
                   WHEN Status = 'cancelled_by_driver' THEN 1
                   ELSE 0
              END) as Cancellation
      FROM Trips JOIN Users ON Trips.Client_Id = Users.Users_Id
      WHERE Banned = 'NO' AND Request_at BETWEEN '2013-10-01' AND '2013-10-03'
     ) P
GROUP BY Day
