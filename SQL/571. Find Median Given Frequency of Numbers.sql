set @curFreq=0;
SELECT AVG(Number) AS median 
FROM (
  SELECT Number, Frequency, AccFreq, SumFreq 
  FROM
  (SELECT    Number,
             Frequency, (@curFreq := @curFreq + Frequency) AS AccFreq
   FROM      Numbers 
   ORDER BY  Number) t1,
  (SELECT SUM(Frequency) SumFreq FROM Numbers) t2
) t
WHERE AccFreq BETWEEN SumFreq / 2 AND SumFreq / 2 + Frequency
