SELECT Score,
       (SELECT COUNT(DISTINCT Score)+1 FROM Scores WHERE Score > s.Score) as Rank
FROM Scores s
ORDER BY Rank
