SELECT (CASE WHEN Id%2=0 THEN Id-1
             WHEN Id%2=1 AND Id<totalCount THEN Id+1
             ELSE Id
        END) as Id, student
FROM seat, 
     (SELECT COUNT(*) as totalCount FROM seat) as totalCounts
ORDER BY Id
