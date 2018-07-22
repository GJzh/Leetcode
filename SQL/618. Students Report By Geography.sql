select America.name as America,
       Asia.name as Asia,
       Europe.name as Europe
from (select name, @a := @a+1 as id from student) as Three
     left join
     (select name, @b := @b+1 as id from student where continent = 'America' order by name) as America on Three.id = America.id
     left join
     (select name, @c := @c+1 as id from student where continent = 'Asia' order by name) as Asia on Three.id = Asia.id
     left join
     (select name, @d := @d+1 as id from student where continent = 'Europe' order by name) as Europe on Three.id = Europe.id
where (America.name is not null) or (Asia.name is not null) or (Europe.name is not null)
