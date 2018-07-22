select round(sum(TIV_2016),2) as TIV_2016
from insurance a
where (select count(*) from insurance b where a.TIV_2015=b.TIV_2015)>1 
      and
      (select count(*) from insurance c where a.LAT=c.LAT and a.LON=c.LON)=1
