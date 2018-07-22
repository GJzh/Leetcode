SELECT DISTINCT a.id, a.date, a.people
FROM stadium a, stadium b, stadium c
WHERE a.people>=100 AND b.people>=100 AND c.people>=100 AND
      ( (a.id+1=b.id AND a.id+2=c.id) OR 
        (a.id-1=b.id AND a.id+1=c.id) OR 
        (a.id-1=b.id AND a.id-2=c.id)) 
ORDER BY a.Id
